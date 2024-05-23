import streamlit as st


st.title('单选框')
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





st.title('多选框')
options = st.multiselect(
    label='请问您喜欢吃什么水果',
    options=('橘子', '苹果', '香蕉', '草莓', '葡萄'),
    default=None,
    format_func=str,
    help='选择您喜欢吃的水果'
)

st.write('您喜欢吃的是', options)

