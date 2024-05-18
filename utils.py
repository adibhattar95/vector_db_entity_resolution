#Import libraries
import streamlit as st

class Frontend:

    def clear_session_state():
        st.session_state.clear()
        st.write("Session state cleared successfully!")

    def displayMessages():
        for message in st.session_state.messages:
            if message["role"]=="1":
                with st.chat_message("assistant"):
                    st.write(message["title1"])
                    st.write(message["master_attr"])
                    st.write(message["title2"])
                    st.write(message["veer_rslt"])
            elif message["role"]=="2":
                with st.chat_message("assistant"):
                    st.write(message["content"])