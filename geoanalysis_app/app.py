import streamlit as st

import geoanalysis_app.subpages as sp


def start() -> None:
    st.sidebar.markdown("# 📊 Dostępne geoanalizy")
    st.sidebar.markdown("---")

    subpages_render_func = {
        "Home": sp.home.render_page,
        "Grupowanie punktów startowych": sp.clustering_start_point.render_page,
        "Grupowanie punktów końcowych": sp.clustering_end_point.render_page,
        "Przebyty dystans w ramach jednego przejazdu": sp.covered_distance_analysis.render_page,
        "Sumy przejechanych dystansów w przedziałach godzinowych": sp.distances_during_hour.render_page
    }

    chosen_subpage = st.sidebar.radio("Menu", list(subpages_render_func.keys()))
    subpages_render_func[chosen_subpage]()


if __name__ == "__main__":
    start()
