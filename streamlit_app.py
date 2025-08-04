import streamlit as st

st.set_page_config(layout="wide")
st.title("Refrigerator Base Appliance Configuration")

st.header("📋 Base Appliance Inputs")

# 使用三列来模拟“参数名 + 16°C + 32°C”的表格布局
col_name, col_16, col_32 = st.columns([2, 1, 1])

# 表头
with col_name:
    st.markdown("**参数名称**")
with col_16:
    st.markdown("**16°C**")
with col_32:
    st.markdown("**32°C**")

# 双温度参数
with col_name:
    st.write("高压侧温度")
with col_16:
    high_16 = st.number_input("", key="high_16")
with col_32:
    high_32 = st.number_input("", key="high_32")

with col_name:
    st.write("低压侧温度")
with col_16:
    low_16 = st.number_input("", key="low_16")
with col_32:
    low_32 = st.number_input("", key="low_32")

with col_name:
    st.write("E_steady")
with col_16:
    esteady_16 = st.number_input("", key="esteady_16")
with col_32:
    esteady_32 = st.number_input("", key="esteady_32")

with col_name:
    st.write("化霜增量")
with col_16:
    defrost_16 = st.number_input("", key="defrost_16")
with col_32:
    defrost_32 = st.number_input("", key="defrost_32")

with col_name:
    st.write("Es")
with col_16:
    Es_16 = st.number_input("", key="es_16")
with col_32:
    Es_32 = st.number_input("", key="es_32")

# 单列参数
col_name2, col_input = st.columns([2, 2])

with col_name2:
    st.write("待机功耗")
with col_input:
    standby_power = st.number_input("", key="standby_power")

with col_name2:
    st.write("E_aux")
with col_input:
    E_aux = st.number_input("", key="e_aux")

with col_name2:
    st.write("箱体 KA")
with col_input:
    KA = st.number_input("", key="KA")

with col_name2:
    st.write("压缩机型号")
with col_input:
    compressor = st.selectbox("", ["型号A", "型号B", "型号C"], key="compressor")

# 输出区
st.divider()
st.header("🧾 输入汇总")
if st.button("打印所有输入值"):
    st.write({
        "压缩机型号": compressor,
        "箱体 KA": KA,
        "高压侧温度": {"16°C": high_16, "32°C": high_32},
        "低压侧温度": {"16°C": low_16, "32°C": low_32},
        "E_steady": {"16°C": esteady_16, "32°C": esteady_32},
        "化霜增量": {"16°C": defrost_16, "32°C": defrost_32},
        "Es": {"16°C": Es_16, "32°C": Es_32},
        "待机功耗": standby_power,
        "E_aux": E_aux
    })
