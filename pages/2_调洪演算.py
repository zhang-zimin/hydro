from module.floodsim import Reservoir
import streamlit as st
import pandas as pd
import altair as alt

uploaded_file = st.file_uploader("上传调洪演算输入文件", type=["csv", "xlsx", "json"])


def get_input_data(_file):
    if uploaded_file.name.endswith('.xlsx') or uploaded_file.name.endswith('.xls'):
        _df = pd.read_excel(uploaded_file)
    elif _file.name.endswith('.json'):
        _df = _file
    else:
        st.error("不支持的文件类型")
        _df = None
    return _df


if uploaded_file is not None:
    # st.write(f"你上传的文件是{uploaded_file.name}")
    input_data = get_input_data(uploaded_file)
    print(input_data)
    # reservoir = Reservoir(500,input_data)
    # data = reservoir.calculateoutflow()
    # print(data)
    # edited_df = st.data_editor(data)


def tabs():
    st.title('输入数据展示')
    tab1, tab2, tab3 = st.tabs(['洪水过程线', '下泄曲线', 'imageio'])

    with tab1:
        '''
        ```python
        import cv2
        image = cv2.imread('image.png')
        ```
        '''

    with tab2:
        '''
        ```python
        from PIL import Image
        image = Image.open('image.png')
        ```
        '''

    with tab3:
        '''
        ```python
        import imageio
        image = imageio.imread('image.png')
        ```
        '''