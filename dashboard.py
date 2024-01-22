import streamlit as st
from log_fun import *

login()

if st.button("Logout"):
        st.cache_resource.clear()
        st.rerun()

"---"

from deta import Deta

data_key = "a0wjgvwqjle_qGyGFkc1ZEkNkjGmRxKnxecr7DfvxonW"

# Connect to Deta Base with your Data Key
deta = Deta(data_key)


db = deta.Base("df_eBird")

"Here's everything stored in the database:"

db_content = db.fetch(limit=None).items
st.dataframe(db_content)
st.write(len(db_content))

"---"
