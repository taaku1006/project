import streamlit as st
from backend.services.message_service import MessageService

message_service = MessageService()

def chat_history(thread_id: int, thread_title: str):
    st.markdown(f"### スレッド [{thread_id}] {thread_title} の会話履歴")

    cache_key = f"messages_{thread_id}"

    # メッセージ取得
    messages = st.session_state.get(cache_key)
    if messages is None:
        # DBから取得
        messages = message_service.get_messages_by_thread(thread_id)
        # キャッシュに保存
        st.session_state[cache_key] = messages

    # LLMサービスのメモリに復元
    st.session_state.llm_service.load_history_from_records(messages)

    # メッセージを表示
    for msg in messages:
        if msg["sender_type"] == "user":
            st.markdown(f"User: {msg['content']}")
        else:
            st.markdown(f"AI: {msg['content']}")


