from module.floodsim import Reservoir
import streamlit as st
import pandas as pd
import altair as alt

uploaded_file = st.file_uploader("上传调洪演算输入文件", type=["csv", "xlsx", "json"])


def get_input_data(_file):
    if uploaded_file.name.endswith('.xlsx') or uploaded_file.name.endswith('.xls'):
        dfs = []
        dfs.append(pd.read_excel(uploaded_file, sheet_name="Flood_Hydrograph"))
        dfs.append(pd.read_excel(uploaded_file, sheet_name="Reservoir_Capacity"))
        dfs.append(pd.read_excel(uploaded_file, sheet_name="Discharge_Curve"))
        dfs.append(pd.read_excel(uploaded_file, sheet_name="Outflow"))
    # elif _file.name.endswith('.json'):
    #     _df = _file
    else:
        st.error("不支持的文件类型")
        dfs = None
    return dfs


def tabs(data):
    Flood_Hydrograph = data[0]
    Reservoir_Capacity = data[1]
    Discharge_Curve = data[2]
    Outflow = data[3]

    st.title('输入数据展示')
    tab1, tab2, tab3, tab4 = st.tabs(['洪水过程线', '库容曲线', '下泄曲线', '出库流量'])

    with tab1:
        st.dataframe(Flood_Hydrograph)

    with tab2:
        st.dataframe(Reservoir_Capacity)

    with tab3:
        st.dataframe(Discharge_Curve)

    with tab4:
        st.dataframe(Outflow)


if uploaded_file is not None:
    # st.write(f"你上传的文件是{uploaded_file.name}")
    input_data = get_input_data(uploaded_file)
    tabs(input_data)
    print(input_data)
    # reservoir = Reservoir(500,input_data)
    # data = reservoir.calculateoutflow()
    # print(data)
    # edited_df = st.data_editor(data)
