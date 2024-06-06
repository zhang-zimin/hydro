from module.floodsim import Reservoir
import streamlit as st
import pandas as pd
import altair as alt
from pathlib import Path


def download():
    # 读取文件路径
    file_path = Path('resources/input.xlsx')

    # 读取文件为字节流
    with open(file_path, 'rb') as f:
        file_bytes = f.read()

    # 使用download_button并提供字节流
    st.download_button(
        label="调洪演算输入文件.xlsx",
        data=file_bytes,
        file_name='template.xlsx',
        mime='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
    )


def get_input_data(_file):
    if uploaded_file.name.endswith('.xlsx') or uploaded_file.name.endswith('.xls'):
        dfs = []
        dfs.append(pd.read_excel(uploaded_file, sheet_name="Flood_Hydrograph", header=0))
        dfs.append(pd.read_excel(uploaded_file, sheet_name="Reservoir_Capacity", header=0))
        dfs.append(pd.read_excel(uploaded_file, sheet_name="Discharge_Curve", header=0))
        dfs.append(pd.read_excel(uploaded_file, sheet_name="Outflow", header=0))
    else:
        st.error("不支持的文件类型")
        dfs = None
    return dfs





def tabshowinputdata(data):
    Flood_Hydrograph = data[0]
    Reservoir_Capacity = data[1]
    Discharge_Curve = data[2]
    Outflow = data[3]

    st.header('输入数据展示')
    tab1, tab2, tab3, tab4 = st.tabs(['洪水过程线', '库容曲线', '下泄曲线', '出库流量'])

    with tab1:
        st.subheader('洪水过程线数据')
        st.dataframe(Flood_Hydrograph, use_container_width=True)
        st.subheader('设计洪水过程线')
        st.line_chart(Flood_Hydrograph, x='t(h)', y='Q(m³)')

    with tab2:
        st.subheader('水位库容数据')
        st.dataframe(Reservoir_Capacity, use_container_width=True)
        st.subheader('水位库容曲线')
        st.line_chart(Reservoir_Capacity, x='水位', y='库容(万m³)')

    with tab3:
        st.subheader('泄洪设施泄流数据')
        st.dataframe(Discharge_Curve, use_container_width=True)
        st.subheader('泄洪设施泄流曲线')
        st.line_chart(Discharge_Curve, x='上游水位(m)', y='总泄量Q(m³/s)')

    with tab4:
        st.subheader('出库流量数据')
        st.dataframe(Outflow, use_container_width=True)
        st.subheader('出库流量线')
        st.line_chart(Outflow, x='t(h)', y='q(m³)')


def water_init_level():
    st.header('计算模块')
    _level = st.number_input('请您输入起调水位',
                             value=None)
    if _level is not None:
        level = float(_level)
        # 根据用户输入进行操作
        if level:
            st.write('您输入的起调水位是', level)
        return level

column_mapping = {
    't': '时间(h)',
    'Discharge': '削峰后出库洪水过程'
}


def calculate(_water_init_level, _input_data):
    if st.button('进行计算'):
        st.subheader("计算结果")
        reservoir = Reservoir(_water_init_level, _input_data)
        _result = reservoir.calculateoutflow()
        _result = _result[['t' , 'Discharge']]
        # 转为中文
        _result.rename(columns=column_mapping, inplace=True)
        # 展示计算结果
        st.dataframe(_result, use_container_width=True)
        return _result


def explain():
    st.markdown("""# 水库调洪演算算法""")


def plot_a_chart(df):
    if df is not None:
        st.subheader("削峰后出库洪水过程")
        st.line_chart(df, x='时间(h)', y='削峰后出库洪水过程')

        # cols = st.multiselect(
        #     "选择您想查看的列", list(df.columns), ["时间", "水库库容"]
        # )
        # if not cols:
        #     st.error("至少选择一列")
        # else:
        #     print(f"df:{df}")
        #     data = df.loc[cols]
        #     chart = (
        #         alt.Chart(data)
        #         .mark_area(opacity=0.3)
        #         .encode(
        #             x="year:T",
        #             y=alt.Y("Gross Agricultural Product ($B):Q", stack=None),
        #         )
        #     )
        #     st.altair_chart(chart, use_container_width=True)


explain()
st.header("上传文件")
uploaded_file = st.file_uploader("请您点下方选择或者拖拽上传输入文件", type=["xlsx"])

with st.expander("下载输入模板文件"):
    # 模板文件下载
    download()

if uploaded_file is not None:
    # 获取输入数据
    input_data = get_input_data(uploaded_file)
    # 展示输入的图表
    tabshowinputdata(input_data)
    # 获取初始起调整水位
    water_init_level = water_init_level()
    # 拿到数据进行计算
    if water_init_level:
        # 计算得到结果
        result = calculate(water_init_level, input_data)
        # 绘制图表
        plot_a_chart(result)
