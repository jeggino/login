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
import pydeck as pdk

# Define a layer to display on a map
layer = pdk.Layer(
    "ScatterplotLayer",
    db_content,
    pickable=True,
    opacity=0.8,
    stroked=True,
    filled=True,
    radius_scale=50,
    line_width_min_pixels=1,
    get_position=["lng","lat"],
    get_fill_color=[255, 140, 0],
    get_line_color=[0, 0, 0],
)

# Set the viewport location
view_state = pdk.ViewState(latitude=db_content["lat"].mean(), longitude=db_content["lng"].mean(), zoom=9, bearing=0, pitch=0)

# Render
r = pdk.Deck(layers=[layer], 
             initial_view_state=view_state, 
             # tooltip={"text": "{name}\n{address}"}
            )

st.pydeck_chart(pydeck_obj=r, use_container_width=True)
