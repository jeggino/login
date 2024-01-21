import streamlit as st
from log_fun import *

login()

if st.button("Logout"):
        st.cache_resource.clear()
        st.rerun()
        
uploaded_file = st.file_uploader("")

if uploaded_file is None:
        
        st.stop()

import pandas as pd

df = pd.read_csv(uploaded_file)
st.dataframe(df)

st.map(df,
    latitude='lat',
    longitude='lng'
      )

import altair as alt

source = df.groupby("sciName",as_index=False).size()

base = alt.Chart(source).encode(
    x='size',
    y="sciName",
    text='size'
).mark_bar()


st.altair_chart(base, use_container_width=True, theme=None)
