import streamlit as st
from backend.services.thread_service import create_thread

def new_thread_form():
    if st.button("新規スレッド作成"):
        st.session_state["create_thread"] = True

    # スレッド作成モード
    if st.session_state.get("create_thread", False):

        title = st.text_input("スレッドタイトルを入力してください", key="new_thread_title")

        if st.button("作成する"):
            if title.strip():
                create_thread(title)
                st.success(f"スレッド '{title}' を作成しました")
                # 状態をリセット
                st.session_state["create_thread"] = False
                if "new_thread_title" in st.session_state:
                    del st.session_state["new_thread_title"]
                # UIを反映
                st.rerun()
            else:
                st.warning("タイトルを入力してください")

