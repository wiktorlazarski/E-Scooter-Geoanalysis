from datetime import datetime

import streamlit as st
from geoanalysis_app import common
from geoanalysis_app import constants as C
from geoanalysis_app.analysis_tools import cluster_map as cm
from geoanalysis_app.analysis_tools import data_filtering as data_fit
from streamlit_folium import folium_static


@st.cache(allow_output_mutation=True)
def load_data():
    return common.load_data()


def preprocess_data(data, from_day, to_day, day_types, times_of_day):
    filtered_data = data_fit.filter_data(
        data, day_types, from_day, to_day, times_of_day
    )

    keep_cols = [
        "Start Centroid Latitude",
        "Start Centroid Longitude",
    ]

    filtered_data = filtered_data[keep_cols].copy()
    filtered_data.dropna(inplace=True)

    start_loc = filtered_data[["Start Centroid Latitude", "Start Centroid Longitude"]]
    start_loc = start_loc.to_numpy()

    return start_loc


def render_page() -> None:
    st.markdown(
        """
        # Grupowanie punktów startowych
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

    if st.button("Wygeneruj analizy"):
        st.markdown(
            """
            ---
            ### Wizualizacja rejonów ze względu na największą ilość wypożyczeń.
            """
        )

        preprocessed_data = preprocess_data(
            data_df, from_day, to_day, day_types, times_of_day
        )

        cluster_map = cm.create_cluster_map(preprocessed_data)
        folium_static(cluster_map)
