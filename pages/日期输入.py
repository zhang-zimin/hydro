import datetime
import streamlit as st

birthday = st.date_input(label='请输入您的出生年月',
                         value=None,
                         min_value=None,
                         max_value=datetime.date.today(),
                         help='请输入您的出生年月')

st.write('您的生日是：', birthday)