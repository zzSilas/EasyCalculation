import streamlit as st

st.set_page_config(layout="wide")
st.title("Refrigerator Base Appliance Configuration")

# 使用列布局
col1, col2 = st.columns([1, 2])

with col1:
    st.header("Base Appliance Inputs")

    compressor = st.selectbox("压缩机型号", ["型号A", "型号B", "型号C"])
    KA = st.number_input("箱体 KA 值", min_value=0.0, step=0.1)

    st.subheader("高压侧温度")
    high_temp_16 = st.number_input("16°C", key="high_16")
    high_temp_32 = st.number_input("32°C", key="high_32")

    st.subheader("低压侧温度")
    low_temp_16 = st.number_input("16°C", key="low_16")
    low_temp_32 = st.number_input("32°C", key="low_32")

    standby_power = st.number_input("待机功耗", min_value=0.0, step=0.1)

    st.subheader("E_steady")
    E_steady_16 = st.number_input("16°C", key="esteady_16")
    E_steady_32 = st.number_input("32°C", key="esteady_32")

    st.subheader("化霜增量")
    defrost_16 = st.number_input("16°C", key="defrost_16")
    defrost_32 = st.number_input("32°C", key="defrost_32")

    E_aux = st.number_input("E_aux", min_value=0.0, step=0.1)

    st.subheader("Es")
    Es_16 = st.number_input("16°C", key="es_16")
    Es_32 = st.number_input("32°C", key="es_32")

with col2:
    st.header("输出结果区域（可扩展）")
    st.write("你可以在这里显示计算结果、图表或者导出按钮等内容。")

    if st.button("打印所有输入值"):
        st.write("压缩机型号:", compressor)
        st.write("箱体 KA:", KA)
        st.write("高压侧温度:", {"16°C": high_temp_16, "32°C": high_temp_32})
        st.write("低压侧温度:", {"16°C": low_temp_16, "32°C": low_temp_32})
        st.write("待机功耗:", standby_power)
        st.write("Es:", {"16°C": Es_16, "32°C": Es_32})
