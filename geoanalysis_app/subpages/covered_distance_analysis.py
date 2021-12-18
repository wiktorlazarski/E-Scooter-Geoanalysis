import matplotlib.pyplot as plt
import streamlit as st
from geoanalysis_app import common
from geoanalysis_app import constants as C


@st.cache(allow_output_mutation=True)
def load_data():
    return common.load_data()


def render_page() -> None:
    st.markdown(
        """
        # Przebyty dystans
        ---
        """
    )

    from_day = st.date_input("Analizuj od dnia:")
    to_day = st.date_input("Analizuj do dnia:")

    times_of_day = st.multiselect(
        "Wybierz pory dnia:", options=C.TIMES_OF_DAY, default=C.TIMES_OF_DAY
    )

    if st.button("Wygeneruj analizy"):
        st.markdown(
            """
            ---
            ### Histogram długości przejechanej drogi w ramach jednego wypożyczenia
            """
        )

        fig = plt.figure()
        plt.hist([1, 1, 1, 1, 2, 2, 3, 3, 3])
        st.pyplot(fig)
