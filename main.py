import streamlit as st
from langchain_aws import ChatBedrock

llm = ChatBedrock(
    model_id = "us.amazon.nova-micro-v1:0"
)

st.title("猴版startai")

prompt = st.chat_input("Insert contents")

if prompt:
    usr_msg = st.chat_message("human")
    usr_msg.write(prompt)

    ai_msg = st.chat_message("ai")
    ai_rply = llm.invoke(prompt)
    ai_msg.write(ai_rply)