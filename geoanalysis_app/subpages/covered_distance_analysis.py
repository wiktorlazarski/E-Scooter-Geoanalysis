from datetime import datetime

import streamlit as st
from geoanalysis_app import common
from geoanalysis_app import constants as C
from geoanalysis_app.analysis_tools import data_filtering as data_fit
from geoanalysis_app.analysis_tools import histograms as hist


@st.cache(allow_output_mutation=True)
def load_data():
    return common.load_data()


def preprocess_data(data, from_day, to_day, day_types, times_of_day):
    filtered_data = data_fit.filter_data(
        data, day_types, from_day, to_day, times_of_day
    )

    keep_cols = ["Start Time", "End Time", "Trip Distance", "Trip Duration"]

    filtered_data = filtered_data[keep_cols].copy()
    filtered_data.dropna(inplace=True)

    return filtered_data


def render_page() -> None:
    st.markdown(
        """
        # Przebyty dystans
        ---
        """
    )

    data_df = load_data()

    from_day = st.date_input("Analizuj od dnia:", value=datetime(2019, 6, 8))
    to_day = st.date_input("Analizuj do dnia:", value=datetime(2019, 8, 13))

    day_types = st.multiselect(
        "Wybierz typy dni:", options=C.DAY_TYPES, default=C.DAY_TYPES
    )

    times_of_day = st.multiselect(
        "Wybierz pory dnia:", options=C.TIMES_OF_DAY, default=C.TIMES_OF_DAY
    )

    bins_width = st.slider(
        "Wybierz przedział odległości",
        min_value=250,
        max_value=10000,
        value=1000,
        step=250,
    )

    if st.button("Wygeneruj analizy"):
        st.markdown(
            """
            ---
            ### Histogram długości przejechanej drogi w ramach jednego wypożyczenia
            """
        )

        preprocessed_data = preprocess_data(
            data_df,
            from_day,
            to_day,
            day_types,
            times_of_day
        )

        fig = hist.histogram_trip_length(preprocessed_data, bins_width)
        st.pyplot(fig)
