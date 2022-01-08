import streamlit as st
from geoanalysis_app import common
from geoanalysis_app import constants as C
from geoanalysis_app.analysis_tools import histograms as hist


@st.cache(allow_output_mutation=True)
def load_data():
    return common.load_data()


def preprocess_data(data, from_day, to_day, day_types, times_of_day):
    # TODO: Apply filetring by from_dat, to_dat
    # I need function without time of the day function!!!

    keep_cols = [
        "Start Time",
        "End Time",
        "Trip Distance",
        "Trip Duration"
    ]

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

    # times_of_day = st.multiselect(
    #     "Wybierz pory dnia:", options=C.TIMES_OF_DAY, default=C.TIMES_OF_DAY
    # )

    if st.button("Wygeneruj analizy"):
        st.markdown(
            """
            ---
            ### Histogram sum przejechanych tras w odstępach godzinowych
            """
        )

        fig = hist.histogram_distance_per_hour(data_df)
        import matplotlib.pyplot as plt
        fig.savefig("sdsd.png", format="png")
        st.pyplot(fig)
