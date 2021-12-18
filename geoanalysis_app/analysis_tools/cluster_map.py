import folium
import folium.plugins
from geoanalysis_app import constants as C


def create_cluster_map(data):
    map_object = folium.Map(location=C.CHICAGO_COORDINATES, zoom_start=11)

    marker_clusters = folium.plugins.MarkerCluster(data)
    map_object.add_child(marker_clusters)

    return map_object
