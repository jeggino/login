import streamlit as st
import credencials

dict = {
    "roberto":'ciao',
    'cosimo':'peccato'
}
dict_keys = dict.keys()


id_input = st.text_input( "Enter some text 👇",value="")
id_input_2 = st.text_input( "Enter some text 👇",type="password")

if id_input in dict_keys:
    
    if dict[id_input] == id_input_2:
        st.write('hi')
        
    else:
        st.write('no')
else:
    st.write("scemo")
