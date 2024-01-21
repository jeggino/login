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
    x='sciName',
    y="size",
    text='size'
)

base.mark_bar() + base.mark_text(align='left', dx=2)

