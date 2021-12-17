import folium
import folium.plugins
import streamlit as st
from geoanalysis_app import common
from geoanalysis_app import constants as C
from streamlit_folium import folium_static


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
    keep_cols = [
        "start_centroid_latitude",
        "start_centroid_longitude",
        "end_centroid_latitude",
        "end_centroid_longitude",
    ]

    data_df = data_df[keep_cols]
    data_df.dropna(inplace=True)

    start_loc = data_df[["start_centroid_latitude", "start_centroid_longitude"]]
    start_loc = start_loc.to_numpy()

    map_object = folium.Map(
        location=C.CHICAGO_COORDINATES, zoom_start=11
    )

    marker_clusters = folium.plugins.MarkerCluster(start_loc)
    map_object.add_child(marker_clusters)

    folium_static(map_object)
