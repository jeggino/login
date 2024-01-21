import streamlit as st
from log_fun import *

login()
        

genre = st.radio("What's your favorite movie genre",
                 [":rainbow[Comedy]", "***Drama***", "Documentary :movie_camera:"],
                 captions = ["Laugh out loud.", "Get the popcorn.", "Never stop learning."])


st.write(f'You selected {genre}.')
