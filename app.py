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
df['Adres'] = df['Adres'] + " " + df['Stad']
df['lat'] = df['Adres'].apply(lambda x: geolocator.geocode(x).latitude)
df['lng'] = df['Adres'].apply(lambda x: geolocator.geocode(x).longitude)

st.dataframe(df)

data_key = "a0ekeqcbs2m_kN32hbBkXeAfgHAGKsNj6fPoKTvbY7xf"



