# import yaml
# import streamlit as st
# from yaml.loader import SafeLoader
# import streamlit_authenticator as stauth



# # Loading config file
# with open('config.yaml') as file:
#     config = yaml.load(file, Loader=SafeLoader)

# # Creating the authenticator object
# authenticator = stauth.Authenticate(
#     config['credentials'],
#     config['cookie']['name'], 
#     config['cookie']['key'], 
#     config['cookie']['expiry_days'],
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

import streamlit as st
from streamlit_login_auth_ui.widgets import __login__

__login__obj = __login__(auth_token = "courier_auth_token", 
                    company_name = "Shims",
                    width = 200, height = 250, 
                    logout_button_name = 'Logout', hide_menu_bool = False, 
                    hide_footer_bool = False, 
                    lottie_url = 'https://assets2.lottiefiles.com/packages/lf20_jcikwtux.json')

LOGGED_IN = __login__obj.build_login_ui()

if LOGGED_IN == True:

    st.markown("Your Streamlit Application Begins here!")

   
