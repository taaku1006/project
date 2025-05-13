from db import SessionLocal
from db.models.thread import Thread
from backend.utils.logger import get_logger

logger = get_logger(__name__)

# スレッド一覧の取得
def get_all_threads():
    with SessionLocal() as session:
        return session.query(Thread).all()

# スレッドの新規作成
def create_thread(title: str):
    with SessionLocal() as session:
        try:
            new_thread = Thread(title=title)
            session.add(new_thread)
            session.commit()
            logger.info(f"スレッド登録成功: title={title}")
        except Exception as e:
            session.rollback()
            logger.error(f"スレッド登録失敗: {e}")
            raise