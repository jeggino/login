# import yaml
import streamlit as st
# from yaml.loader import SafeLoader
# import streamlit_authenticator as stauth



# # Loading config file
# with open('config.yaml') as file:
#     config = yaml.load(file, Loader=SafeLoader)

# # Creating the authenticator object
# authenticator = stauth.Authenticate(
#     config['preauthorized']
# )

# # creating a login widget
# authenticator.login('', 'sidebar')
# if st.session_state["authentication_status"]:
#     # authenticator.logout('Logout', 'main')
#     st.write(f'Welcome *{st.session_state["name"]}*')
#     st.title('Some content')
# elif st.session_state["authentication_status"] is False:
#     st.error('Username/password is incorrect')
# elif st.session_state["authentication_status"] is None:
#     st.warning('Please enter your username and password')

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
