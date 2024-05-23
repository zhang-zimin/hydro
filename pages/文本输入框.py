import streamlit as st

name = st.text_input('请输入用户名', max_chars=100, help='最大长度为100字符')

# 根据用户输入进行操作
st.write('您的用户名是', name)