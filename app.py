import streamlit as st
from credencials import dict

with st.container(height=None, border=True):
    id_input = st.text_input( "Enter some text 👇",value="")
    id_input_2 = st.text_input( "Enter some text 👇",type="password")
    
    if id_input in dict.keys():
        
        if dict[id_input] == id_input_2:
            st.write('hi')
            
        else:
            st.write('no')
    else:
        st.write("scemo")
