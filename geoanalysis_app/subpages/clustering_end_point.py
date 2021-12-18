import streamlit as st
from geoanalysis_app import common
from geoanalysis_app import constants as C
from geoanalysis_app.analysis_tools import cluster_map as cm
from streamlit_folium import folium_static


@st.cache(allow_output_mutation=True)
def load_data():
    return common.load_data()


def preprocess_data(data, from_day, to_day, day_types, times_of_day):
    # TODO: Apply filetring by from_dat, to_dat, times_of_day

    keep_cols = [
        "end_centroid_latitude",
        "end_centroid_longitude",
    ]

    data = data[keep_cols].copy()
    data.dropna(inplace=True)

    end_loc = data[["end_centroid_latitude", "end_centroid_longitude"]]
    end_loc = end_loc.to_numpy()

    return end_loc


def render_page() -> None:
    st.markdown(
        """
        # Grupowanie punktów końcowych
        ---
        """
    )

    data_df = common.load_data()

    from_day = st.date_input("Analizuj od dnia:")
    to_day = st.date_input("Analizuj do dnia:")

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
            ### Wizualizacja rejonów ze względu na największą ilość zwrotów.
            """
        )

        preprocessed_data = preprocess_data(
            data_df, from_day, to_day, day_types, times_of_day
        )

        cluster_map = cm.create_cluster_map(preprocessed_data)
        folium_static(cluster_map)
