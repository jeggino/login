import streamlit as st
import streamlit_authenticator as stauth

import yaml
from yaml.loader import SafeLoader

with open('config.yaml') as file:
    config = yaml.load(file, Loader=SafeLoader)

authenticator = stauth.Authenticate(
    config['credentials'],
    config['cookie']['name'],
    config['cookie']['key'],
    config['cookie']['expiry_days'],
    config['preauthorized']
)

authenticator.login()



        
if st.session_state["authentication_status"] is False:
    st.error('Username/password is incorrect')
elif st.session_state["authentication_status"] is None:
    st.warning('Please enter your username and password')
elif st.session_state["authentication_status"]:
    with open('config.yaml', 'w') as file:
        yaml.dump(config, file, default_flow_style=False)
    st.write(f'Welcome *{st.session_state["name"]}*')
    agree = st.checkbox('I agree')

    if agree:
        st.write('Great!')

    option = st.selectbox(
       "How would you like to be contacted?",
       ("Email", "Home phone", "Mobile phone"),
       index=None,
       placeholder="Select contact method...",
    )

    st.write('You selected:', option)



