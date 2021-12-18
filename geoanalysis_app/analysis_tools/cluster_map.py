import folium
import folium.plugins
from geoanalysis_app import constants as C


def create_cluster_map(data):
    map_object = folium.Map(location=C.CHICAGO_COORDINATES, zoom_start=11)

    marker_clusters = folium.plugins.MarkerCluster(data, name="Rents clusters")
    map_object.add_child(marker_clusters)

    folium.plugins.HeatMap(data, name="Rents heatmap").add_to(map_object)

    folium.TileLayer("Stamen Toner").add_to(map_object)
    folium.TileLayer("Stamen Terrain").add_to(map_object)

    folium.LayerControl().add_to(map_object)

    return map_object
