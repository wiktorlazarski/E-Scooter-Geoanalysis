import streamlit as st
from geoanalysis_app import common
from geoanalysis_app.analysis_tools import cluster_map as cm
from streamlit_folium import folium_static


@st.cache(allow_output_mutation=True)
def load_data():
    return common.load_data()


def preprocess_data(data, from_day, to_day, time_of_day):
    keep_cols = [
        "start_centroid_latitude",
        "start_centroid_longitude",
    ]

    data = data[keep_cols]
    data.dropna(inplace=True)

    start_loc = data[["start_centroid_latitude", "start_centroid_longitude"]]
    start_loc = start_loc.to_numpy()

    return start_loc


def render_page() -> None:
    st.markdown(
        """
        # Starting points' clusters
        ---
        """
    )

    from_day = st.date_input("Analyze starting from day:")
    to_day = st.date_input("Analyze to day:")

    st.markdown(
        """
        ---
        ### Wizualizacja rejonów ze względu na największą ilość wypożyczeń.
        """
    )

    data_df = common.load_data()
    preprocessed_data = preprocess_data(data_df, from_day, to_day, None)

    cluster_map = cm.create_cluster_map(preprocessed_data)
    folium_static(cluster_map)
