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
from geopy.geocoders import Nominatim

df = pd.read_csv(uploaded_file)

geolocator = Nominatim(user_agent="user_agent")
df_updated['addrees'] = df_updated['addrees'] + " " + df_updated['city']
df['lat'] = df['addrees'].apply(lambda x: geolocator.geocode(x).latitude)
df['lng'] = df['addrees'].apply(lambda x: geolocator.geocode(x).longitude)

st.dataframe(df)

st.map(df,
    latitude='lat',
    longitude='lng'
      )


import altair as alt

source = df.groupby("species",as_index=False).size()

base = alt.Chart(source).encode(
    x='size',
    y="species",
    text='size'
).mark_bar()


st.altair_chart(base, use_container_width=True, theme=None)
