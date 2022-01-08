import matplotlib.pyplot as plt
import streamlit as st
from geoanalysis_app import common
from geoanalysis_app import constants as C
from geoanalysis_app.analysis_tools import histograms as hist


@st.cache(allow_output_mutation=True)
def load_data():
    return common.load_data()


def preprocess_data(data, from_day, to_day, day_types, times_of_day):
    # TODO: Apply filetring by from_dat, to_dat, times_of_day

    keep_cols = ["Start Time", "End Time", "Trip Distance", "Trip Duration"]

    data = data[keep_cols].copy()
    data.dropna(inplace=True)

    return data


def render_page() -> None:
    st.markdown(
        """
        # Przebyty dystans
        ---
        """
    )

    data_df = load_data()

    from_day = st.date_input("Analizuj od dnia:")
    to_day = st.date_input("Analizuj do dnia:")

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

        # tu to bins_width musisz zrobić
        fig = hist.histogram_trip_length(data_df, bins_width)
        st.pyplot(fig)
