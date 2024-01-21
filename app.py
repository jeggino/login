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
            
            st.title(f"HI :blue[{dict[id_input]['name']}]")
            if st.button("Logout"):
                st.rerun()
            
        else:
            container.write('Password incorrect')
            st.stop()
    else:
        container.write("User name incorrect")
        st.stop()
        
    if st.button("Home"):
        st.switch_page("app.py")
    if st.button("Page 1"):
        st.switch_page("pages/page_1.py")
    if st.button("Page 2"):
        st.switch_page("pages/page_2.py")

