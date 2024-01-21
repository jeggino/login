import streamlit as st
from log_fun import *

login()

if st.button("Logout"):
        st.cache_resource.clear()
        st.rerun()

"---"
          
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




#--------------
from deta import Deta

data_key = "a0ekeqcbs2m_kN32hbBkXeAfgHAGKsNj6fPoKTvbY7xf"

# Data to be written to Deta Base
with st.form("form"):
    st.dataframe(df)
    submitted = st.form_submit_button("Store in database")


# Connect to Deta Base with your Data Key
deta = Deta(data_key)

# Create a new database "example-db"
# If you need a new database, just use another name.
db = deta.Base("elskenecologie_2024-db")

# If the user clicked the submit button,
# write the data from the form to the database.
# You can store any data you want here. Just modify that dictionary below (the entries between the {}).
if submitted:
        for row in df.to_dict('records'):
                db.put(row)

"---"
"Here's everything stored in the database:"
# This reads all items from the database and displays them to your app.
# db_content is a list of dictionaries. You can do everything you want with it.
db_content = db.fetch().items
st.dataframe(db_content)





