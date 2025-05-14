import streamlit as st
from backend.services.thread_service import ThreadService

thread_service = ThreadService()

def thread_sidebar():
    st.markdown("### スレッド履歴一覧")
    threads = thread_service.get_all_threads()
    for thread in threads:
        if st.button(f" [{thread.id}] {thread.title}", key=f"thread_{thread.id}"):
            st.session_state["selected_thread_id"] = (thread.id, thread.title)