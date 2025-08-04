import streamlit as st

st.set_page_config(layout="wide")
st.title("🧊 Refrigerator Base Appliance Configuration")

params = [
    ("待机功耗", "standby", "number"),
    ("E_aux", "e_aux", "number"),
    ("箱体 KA", "ka", "number"),
    ("压缩机型号", "compressor_model", "selectbox")
]

for label, key, typ in params:
    col1, col2 = st.columns([1.5, 2])
    with col1:
        st.markdown(label)
    with col2:
        if typ == "number":
            st.number_input("", key=key, label_visibility="collapsed")
        else:
            st.selectbox(
                "",
                ["VESH11C", "VESH7C", "VESG9C", "VEMH8C", "VESH9G", "VESH6C", "VESF7C"],
                key=key,
                label_visibility="collapsed"
            )

