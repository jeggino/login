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
df['operator'] = f"{dict[id_input]['name']}"
st.dataframe(df)

