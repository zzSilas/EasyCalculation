import streamlit as st

st.set_page_config(layout="wide")
st.title("🧊 Refrigerator Base Appliance Configuration")

# 三列布局：参数名称、16°C、32°C
col_name, col_16, col_32 = st.columns([1.5, 1, 1])
with col_name:
    st.markdown("**参数名称**")
with col_16:
    st.markdown("**16°C**")
with col_32:
    st.markdown("**32°C**")

params = [
    "高压侧温度", "低压侧温度", "E_steady", "化霜增量", "Es"
]
results = {}

for param in params:
    col_name, col_16, col_32 = st.columns([1.5, 1, 1])
    with col_name:
        st.markdown(param)
    with col_16:
        results[f"{param}_16"] = st.number_input(
            "", key=f"{param}_16", label_visibility="collapsed")
    with col_32:
        results[f"{param}_32"] = st.number_input(
            "", key=f"{param}_32", label_visibility="collapsed")

# 单值参数部分
col1, col2 = st.columns([1.5, 2])
with col1:
    st.markdown("待机功耗")
with col2:
    standby = st.number_input("", key="standby", label_visibility="collapsed")

with col1:
    st.markdown("E_aux")
with col2:
    e_aux = st.number_input("", key="e_aux", label_visibility="collapsed")

with col1:
    st.markdown("箱体 KA")
with col2:
    ka = st.number_input("", key="ka", label_visibility="collapsed")

with col1:
    st.markdown("压缩机型号")
with col2:
    compressor = st.selectbox("", ["型号A", "型号B", "型号C"], label_visibility="collapsed")

# 可选：输入结果展示
st.divider()
if st.button("打印所有输入"):
    st.subheader("输入值汇总")
    st.write("压缩机型号：", compressor)
    st.write("箱体 KA：", ka)
    st.write("待机功耗：", standby)
    st.write("E_aux：", e_aux)
    for param in params:
        st.write(f"{param}：", {"16°C": results[f"{param}_16"], "32°C": results[f"{param}_32"]})
