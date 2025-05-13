from db import SessionLocal
from db.models.message import Message
from backend.utils.logger import get_logger

logger = get_logger(__name__)

#メッセージを送信
def send_message(thread_id: int, content: str, sender_type: str = 'user'):
    with SessionLocal() as session:
        try:
            message = Message(thread_id=thread_id, content=content, sender_type=sender_type)
            session.add(message)
            session.commit()
            logger.info(f"メッセージ送信成功: thread_id={thread_id}, sender_type={sender_type}, content={content}")
        except Exception as e:
            session.rollback()
            logger.error(f"メッセージ送信失敗: {e}")
            raise

# 会話履歴を取得
def get_messages_by_thread(thread_id: int):
    with SessionLocal() as session:
        try:
            messages = (
                session.query(Message)
                .filter(Message.thread_id == thread_id)
                .order_by(Message.id)
                .all()
            )
            logger.info(f"会話履歴取得成功: thread_id={thread_id}, メッセージ数={len(messages)}")
            return messages
        except Exception as e:
            logger.error(f"会話履歴取得失敗: {e}")
            raise

