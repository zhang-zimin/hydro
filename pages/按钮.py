import streamlit as st

if st.button('点我'):
    st.write('今天是个好日子！')


cb = st.checkbox('确认', value=False)

if cb:
    st.write('确认成功')
else:
    st.write('没有确认')
