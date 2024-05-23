import streamlit as st

age = st.slider(label='请输入您的年龄',
                min_value=0,
                max_value=100,
                value=0,
                step=1,
                help="请输入您的年龄"
                )

st.write('您的年龄是', age)