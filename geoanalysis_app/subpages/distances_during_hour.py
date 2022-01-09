from datetime import datetime

import streamlit as st
from geoanalysis_app import common
from geoanalysis_app import constants as C
from geoanalysis_app.analysis_tools import data_filtering as data_fit
from geoanalysis_app.analysis_tools import histograms as hist


@st.cache(allow_output_mutation=True)
def load_data():
    return common.load_data()


def preprocess_data(data, from_day, to_day, day_types):
    filtered_data = data_fit.filter_data(
        data, day_types, from_day, to_day, ["RANO", "POŁUDNIE", "WIECZÓR", "NOC"]
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

    if st.button("Wygeneruj analizy"):
        st.markdown(
            """
            ---
            ### Histogram sum przejechanych tras w odstępach godzinowych
            """
        )

        preprocessed_data = preprocess_data(
            data_df,
            from_day,
            to_day,
            day_types,
        )

        fig = hist.histogram_distance_per_hour(preprocessed_data)
        st.pyplot(fig)
