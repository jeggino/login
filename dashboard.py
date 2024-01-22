import streamlit as st
from log_fun import *

login()

if st.button("Logout"):
        st.cache_resource.clear()
        st.rerun()

"---"

from deta import Deta

data_key = "a0eengonb7b_UCVkWd6CJS5ccGoKFzNCYj6UnMeRcF5Y"

# Connect to Deta Base with your Data Key
deta = Deta(data_key)


db = deta.Base("elskenecologie_2024-db")

"Here's everything stored in the database:"

db_content = db.fetch(limit=None).items
st.dataframe(db_content)

"---"
