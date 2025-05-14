import streamlit as st
from ui.components.chat_history import chat_history
from ui.components.chat_input import chat_input
from ui.components.new_thread_form import new_thread_form
from ui.components.thread_sidebar import thread_sidebar
from backend.services.llm_service import LLMChatService

def chat_page():
    #  LLMサービスをセッション内で初期化
    if "llm_service" not in st.session_state:
        st.session_state.llm_service = LLMChatService()

    col1, col2 = st.columns([1, 3])

    with col1:
        new_thread_form()
        thread_sidebar()

    with col2:
        selected_thread = st.session_state.get("selected_thread_id")
        if selected_thread is None:
            st.markdown("### スレッドを選択してください")
            return

        thread_id, thread_title = selected_thread
        chat_history(thread_id, thread_title)
        st.markdown("---")
        chat_input(thread_id)