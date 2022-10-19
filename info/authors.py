import streamlit as st
def authors():
    with st.expander("ℹ️ - Acerca de Nosotros", expanded=True):
        col1, col2, col3 = st.columns([1,2,1])
        col1.image("https://avatars.githubusercontent.com/u/58157906?v=4", caption=None, width=50, use_column_width=None, clamp=False, channels="RGB", output_format="auto")
        col2.write("[Fuhrerh-Lemon](https://github.com/Fuhrerh-Lemon), Ing. Sistemas Computacionles")
        st.write(
            """     
                -   [HewelFo](https://github.com/HewelFo), Ing. Sistemas Computacionles
                -   [notdesby](https://github.com/notdesby), Ing. Sistemas Computacionles
                -   [ModestoDiaz](https://github.com/ModestoDiaz), Ing. Sistemas Computaciones
            """
        )