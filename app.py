import streamlit as st
# import streamlit_authenticator as stauth



# 设置全局属性
st.set_page_config(
    page_title='水文平台',
    page_icon=' ',
    layout='wide',
)
def login_in():
    # 正文
    st.title('欢迎来到水文数字设计平台')
    # empty = st.empty()
    # with empty:
    #     with open('config.yaml') as file:
    #         config = yaml.load(file, Loader=SafeLoader)
    #
    #     authenticator = stauth.Authenticate(
    #         config['credentials'],
    #         config['cookie']['name'],
    #         config['cookie']['key'],
    #         config['cookie']['expiry_days'],
    #         config['pre-authorized']
    #     )
    #
    #     authenticator.login()
    #
    #     if st.session_state["authentication_status"]:
    #         authenticator.logout()
    #         st.write(f'Welcome *{st.session_state["name"]}*')
    #         st.title('Some content')
    #     elif st.session_state["authentication_status"] is False:
    #         st.error('Username/password is incorrect')
    #     elif st.session_state["authentication_status"] is None:
    #         st.warning('Please enter your username and password')


login_in()