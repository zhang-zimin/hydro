import streamlit as st

# 设置全局属性
st.set_page_config(
    page_title='我是标题',
    page_icon=' ',
    layout='wide'
)

# 正文
st.title('hello world')
st.markdown('> Streamlit 支持通过 st.markdown 直接渲染 markdown11111')
st.columns([1, 2, 3])



with st.sidebar:
    st.title('欢迎来到我的应用')
    st.markdown('---')
    st.markdown('这是它的特性：\n- feature 1\n- feature 2\n- feature 3')



st.title('Python 不同的库实现图像读入成 numpy 数组')
tab1, tab2, tab3 = st.tabs(['opencv', 'pillow', 'imageio'])

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


data = {
    'latitude': [37.7749, 34.0522, 40.7128],
    'longitude': [-122.4194, -118.2437, -74.0060],
    'name': ['San Francisco', 'Los Angeles', 'New York']
}

st.map(data, zoom=4, use_container_width=True)


sex = st.selectbox(
    label='请输入您的性别',
    options=('男', '女', '保密'),
    index=2,
    format_func=str,
    help='如果您不想透露，可以选择保密'
)

if sex == '男':
    st.write('男士您好!')
elif sex == '女':
    st.write('女士您好!')
else:
    st.write('您好!')


options = st.multiselect(
    label='请问您喜欢吃什么水果',
    options=('橘子', '苹果', '香蕉', '草莓', '葡萄'),
    default=None,
    format_func=str,
    help='选择您喜欢吃的水果'
)

st.write('您喜欢吃的是', options)

import streamlit as st

age = st.slider(label='请输入您的年龄',
                min_value=0,
                max_value=100,
                value=0,
                step=1,
                help="请输入您的年龄"
                )

st.write('您的年龄是', age)

import datetime

birthday = st.date_input(label='请输入您的出生年月',
                         value=None,
                         min_value=None,
                         max_value=datetime.date.today(),
                         help='请输入您的出生年月')

st.write('您的生日是：', birthday)


if st.button('点我'):
    st.write('今天是个好日子！')


cb = st.checkbox('确认', value=False)

if cb:
    st.write('确认成功')
else:
    st.write('没有确认')


name = st.text_input('请输入用户名', max_chars=100, help='最大长度为100字符')

# 根据用户输入进行操作
st.write('您的用户名是', name)

import pandas as pd
import numpy as np

random_data = np.random.rand(100, 10)
df = pd.DataFrame(random_data, columns=[f'Col{i}' for i in range(1, 11)])

st.dataframe(df)
st.table(df)

import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 10, 100)
y1 = np.sin(x)
y2 = np.cos(x)

plt.plot(x, y1, label='sin(x)')
plt.plot(x, y2, label='cos(x)')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
st.pyplot()
