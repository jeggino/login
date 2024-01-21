import streamlit as st
from credencials import dict

container =  st.container(height=None, border=True)
id_input = container.text_input( "Enter your user name here",value="")
id_input_2 = container.text_input( "Enter your password here",type="password")

if container.button('Login'):
    if id_input in dict.keys():
        
        if dict[id_input]['password'] == id_input_2:
            st.write(f"Hi {dict[id_input]['name']}")
            
        else:
            container.write('Password incorrect')
    else:
        container.write("User name incorrect")
