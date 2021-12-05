import streamlit as st

import geoanalysis_app.subpages as sp


def start() -> None:
    st.sidebar.markdown("# 📊 Available Geoanalysis")
    st.sidebar.markdown("---")

    subpages_render_func = {
        "Home": sp.home.render_page,
        "Start points clustering": sp.clustering_start_point.render_page,
        "End points clustering": sp.clustering_end_point.render_page,
        "Covered distance analysis": sp.covered_distance_analysis.render_page,
    }

    chosen_subpage = st.sidebar.radio("Menu", list(subpages_render_func.keys()))
    subpages_render_func[chosen_subpage]()


if __name__ == "__main__":
    start()
