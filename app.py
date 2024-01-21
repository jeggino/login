import streamlit as st
from credencials import dict

placeholder = st.empty()
container =  placeholder.container(height=None, border=True)
id_input = container.text_input( "Enter your user name here",value="")
id_input_2 = container.text_input( "Enter your password here",type="password")

if container.button('Login'):
    if id_input in dict.keys():
        
        if dict[id_input]['password'] == id_input_2:
            placeholder.empty()
            col1,col2 = st.columns(2)
            col1.write(f"Hi {dict[id_input]['name']}")
            if st.button("Logout"):
                col2.rerun()
            
        else:
            container.write('Password incorrect')
            st.stop()
    else:
        container.write("User name incorrect")
        st.stop()
        
    message = st.chat_message("assistant")
    message.write("Hello human")

