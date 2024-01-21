import streamlit as st
from log_fun import *

login()

if st.button("Logout"):
        st.cache_resource.clear()
        st.rerun()
with st.container(height=120):
        st.image("https://terschelling-cdn.travelbase.nl/image-transforms/logo/500x500/f30402d250ee0d24b57be8e69299e1f9.png")
        
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

