import streamlit as st
from backend.services.message_service import MessageService

message_service = MessageService()

def chat_input(thread_id: int):
    with st.form(f"chat_form_{thread_id}"):  # スレッド単位でフォームも分離（安全）
        user_input = st.text_input("ユーザー入力", key=f"chat_input_{thread_id}")
        submitted = st.form_submit_button("送信")

        if submitted and user_input.strip():
            # LangChainサービスでLLM呼び出し
            bot_response = st.session_state.llm_service.chat(user_input)

            # メッセージDB保存
            message_service.send_message(thread_id, content=user_input, sender_type='user')
            message_service.send_message(thread_id, content=bot_response, sender_type='ai')

            # UI用メッセージキャッシュキー（スレッド単位）
            cache_key = f"messages_{thread_id}"

            # キャッシュに保存
            if cache_key in st.session_state:
                st.session_state[cache_key].append({"sender_type": "user", "content": user_input})
                st.session_state[cache_key].append({"sender_type": "ai", "content": bot_response})
            else:
                st.session_state[cache_key] = [
                    {"sender_type": "user", "content": user_input},
                    {"sender_type": "ai", "content": bot_response},
                ]

            # UIリロード
            st.rerun()
