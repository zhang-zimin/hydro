import streamlit as st
import pandas as  pd


df = pd.DataFrame({'rating':[1],"command":[2]})
edited_df = st.data_editor(df)
favorite_command = edited_df.loc[edited_df["rating"].idxmax()]["command"]
st.markdown(f"双击单元进行修改")