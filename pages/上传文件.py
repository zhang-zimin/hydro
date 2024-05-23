import streamlit as st

uploaded_file = st.file_uploader("上传文件", type=["csv", "json"])
if uploaded_file:
  st.write(f"你上传的文件是{uploaded_file.name}")