import streamlit as st
from backend.services.message_service import send_message

def chat_input(thread_id: int):
    with st.form("chat_form"):
        user_input = st.text_input("ユーザー入力", key="chat_input")
        submitted = st.form_submit_button("送信")

        if submitted and user_input.strip():
            st.session_state.setdefault("messages", [])
            st.session_state["messages"].append({"sender": "user", "text": user_input})
            send_message(thread_id, content=user_input, sender_type='user')

            # LangChainサービスでLLM呼び出し
            bot_response = st.session_state.llm_service.chat(user_input)

            # LLMからの応答も履歴に追加＆DB保存
            st.session_state["messages"].append({"sender": "ai", "text": bot_response})
            send_message(thread_id, content=bot_response, sender_type='ai')

            # UIを反映
            st.rerun()

            del st.session_state["chat_input"]



