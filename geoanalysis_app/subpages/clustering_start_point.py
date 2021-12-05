import streamlit as st


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

    st.map()
