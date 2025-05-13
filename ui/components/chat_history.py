import streamlit as st
from backend.services.message_service import get_messages_by_thread

def chat_history(thread_id: int, thread_title: str):
    st.markdown(f"### スレッド [{thread_id}] {thread_title} の会話履歴")
    messages = get_messages_by_thread(thread_id)

    for msg in messages:
        if msg.sender_type == "user":
            st.markdown(f"🧑: {msg.content}")
        else:
            st.markdown(f"🤖: {msg.content}")

