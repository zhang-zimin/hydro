import pandas as pd
import numpy as np
import altair as alt
import streamlit as st



st.title('互动表格')
random_data = np.random.rand(100, 10)
df = pd.DataFrame(random_data, columns=[f'Col{i}' for i in range(1, 11)])


st.dataframe(df)

##绘图
st.title('点云图')


df = pd.DataFrame(
    np.random.randn(200, 3),
    columns=['a', 'b', 'c'])

c = alt.Chart(df).mark_circle().encode(
    x='a', y='b', size='c', color='c', tooltip=['a', 'b', 'c'])

st.write(c)


st.title('折线图')



col1, col2 = st.columns([3, 1])
data = np.random.randn(10, 1)

col1.subheader("A wide column with a chart")
st.divider()
col1.line_chart(data)
