import streamlit as st


def render_page() -> None:
    st.markdown(
        """
        # 🛴 Geoanaliza wyporzyczeń hulajnóg elektrycznych 🌎
        ---
        ## Przedmiot: _(SPDB) Przestrzenne Bazy Danych_

        #### Autorzy: Wiktor Łazarski, Ula Tworzydło, Zosia Matyjewska
        """,
    )


if __name__ == '__main__':
    render_page()
