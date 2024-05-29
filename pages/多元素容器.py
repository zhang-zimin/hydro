import streamlit as st
import numpy as np

with st.container():
   st.write("这是容器内的内容")

   # 您可以调用任何 Streamlit 命令，包括自定义组件：
   st.bar_chart(np.random.randn(50, 3))

st.write("这是容器外的内容")
