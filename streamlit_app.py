import streamlit as st

st.set_page_config(layout="wide")
st.title("🧊 Refrigerator Calculation 🧊")

params = [
    "高压侧温度", "低压侧温度", "E_steady", "化霜增量", "Es"
]

# 三列布局：左栏、中间分割栏（窄），右栏
col_base, col_divider, col_new = st.columns([4, 0.1, 4])

def appliance_input_area(area_name, key_prefix):
    st.markdown(f"### {area_name}")

    col_name, col_16, col_32 = st.columns([1.5, 1, 1])
    with col_name:
        st.markdown("**参数名称**")
    with col_16:
        st.markdown("**16°C**")
    with col_32:
        st.markdown("**32°C**")

    results = {}

    for param in params:
        col_name, col_16, col_32 = st.columns([1.5, 1, 1])
        with col_name:
            st.markdown(param)
        with col_16:
            results[f"{param}_16"] = st.number_input(
                "", key=f"{key_prefix}_{param}_16", label_visibility="collapsed")
        with col_32:
            results[f"{param}_32"] = st.number_input(
                "", key=f"{key_prefix}_{param}_32", label_visibility="collapsed")


    # 替代原来的 single_params，改成逐项输入
    col1, col2 = st.columns([1.5, 1])
    with col1:
        st.markdown("待机功耗")
    with col2:
        results[f"{key_prefix}_standby"] = st.number_input("", key=f"{key_prefix}_standby", label_visibility="collapsed")

    col1, col2 = st.columns([1.5, 1])
    with col1:
        st.markdown("E_aux")
    with col2:
        results[f"{key_prefix}_e_aux"] = st.number_input("", key=f"{key_prefix}_e_aux", label_visibility="collapsed")

    col1, col2 = st.columns([1.5, 1])
    with col1:
        st.markdown("压缩机型号")
    with col2:
        results[f"{key_prefix}_compressor"] = st.selectbox(
            "", 
            ["VESH11C", "VESH7C", "VESG9C", "VEMH8C", "VESH9G", "VESH6C", "VESF7C"],
            key=f"{key_prefix}_compressor",
            label_visibility="collapsed"
        )

    # 箱体 KA 和 特征温度输入（RC, VF, CC, FC）
    st.markdown("<h4 style='text-align: center;'>箱体 KA 与特征温度设置</h4>", unsafe_allow_html=True)
    room_labels = ["RC", "VF", "CC", "FC"]

    # 第一行：标签
    col_name, *ka_cols = st.columns([1.5] + [1]*4)
    with col_name:
        st.markdown("**参数项**")
    for i, room in enumerate(room_labels):
        with ka_cols[i]:
            st.markdown(f"**{room}**")

    # 第二行：KA 值
    col_name, *ka_input_cols = st.columns([1.5] + [1]*4)
    with col_name:
        st.markdown("KA 值")
    for i, room in enumerate(room_labels):
        with ka_input_cols[i]:
            results[f"{key_prefix}_ka_{room}"] = st.number_input(
                "", key=f"{key_prefix}_ka_{room}", label_visibility="collapsed"
            )

    # 第三行：特征温度
    col_name, *temp_input_cols = st.columns([1.5] + [1]*4)
    with col_name:
        st.markdown("特征温度 (°C)")
    for i, room in enumerate(room_labels):
        with temp_input_cols[i]:
            results[f"{key_prefix}_temp_{room}"] = st.number_input(
                "", key=f"{key_prefix}_temp_{room}", label_visibility="collapsed"
            )


with col_base:
    base_results = appliance_input_area("Base Appliance", "base")

with col_divider:
    st.markdown("<div style='border-left:2px solid #aaa; height: 100%; margin: 0 10px;'></div>", unsafe_allow_html=True)

with col_new:
    new_results = appliance_input_area("New Appliance", "new")

st.divider()

if st.button("打印所有输入"):
    st.subheader("Base Appliance 输入")
    st.write(base_results)
    st.subheader("New Appliance 输入")
    st.write(new_results)
