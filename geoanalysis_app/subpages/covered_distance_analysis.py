import matplotlib.pyplot as plt
import streamlit as st


def render_page() -> None:
    st.markdown(
        """
        # Covered distance analysis
        ---
        """
    )

    from_day = st.date_input("Analyze starting from day:")
    to_day = st.date_input("Analyze to day:")

    st.markdown(
        """
        ---
        ### Histogram długości przejechanej drogi w ramach jednego wypożyczenia
        """
    )

    fig = plt.figure()
    plt.hist([1, 1, 1, 1, 2, 2, 3, 3, 3])
    st.pyplot(fig)
