import streamlit as st

st.set_page_config(layout="wide")
st.title("🧊 Refrigerator Base Appliance vs New Appliance Configuration")

params = [
    "高压侧温度", "低压侧温度", "E_steady", "化霜增量", "Es"
]

# 横向两列：左边base，右边new
col_base, col_new = st.columns(2)

def appliance_input_area(area_name, key_prefix):
    st.markdown(f"### {area_name}")

    # 参数名和两个温度列标题
    col_name, col_16, col_32 = st.columns([1.5, 1, 1])
    with col_name:
        st.markdown("**参数名称**")
    with col_16:
        st.markdown("**16°C**")
    with col_32:
        st.markdown("**32°C**")

    results = {}

    # 参数输入
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

    st.markdown("#### 单值参数")

    # 单值参数输入
    single_params = [
        ("待机功耗", f"{key_prefix}_standby", "number"),
        ("E_aux", f"{key_prefix}_e_aux", "number"),
        ("箱体 KA", f"{key_prefix}_ka", "number"),
        ("压缩机型号", f"{key_prefix}_compressor", "selectbox"),
    ]

    for label, key, typ in single_params:
        col1, col2 = st.columns([1.5, 1])
        with col1:
            st.markdown(label)
        with col2:
            if typ == "number":
                results[key] = st.number_input("", key=key, label_visibility="collapsed")
            else:
                results[key] = st.selectbox(
                    "", 
                    ["VESH11C", "VESH7C", "VESG9C", "VEMH8C", "VESH9G", "VESH6C", "VESF7C"],
                    key=key,
                    label_visibility="collapsed"
                )
    return results


with col_base:
    base_results = appliance_input_area("Base Appliance", "base")

with col_new:
    new_results = appliance_input_area("New Appliance", "new")

st.divider()

if st.button("打印所有输入"):
    st.subheader("Base Appliance 输入")
    st.write(base_results)
    st.subheader("New Appliance 输入")
    st.write(new_results)
