from db import SessionLocal
from db.models.thread import Thread
from backend.utils.logger import get_logger

logger = get_logger(__name__)

class ThreadService:
    def __init__(self):
        self.logger = logger

    #スレッド一覧を取得
    def get_all_threads(self):
        with SessionLocal() as session:
            try:
                threads = session.query(Thread).all()
                self.logger.info(f"スレッド一覧取得成功: 件数={len(threads)}")
                return threads
            except Exception as e:
                self.logger.error(f"スレッド一覧取得失敗: {e}")
                raise

    #新しいスレッドを作成
    def create_thread(self, title: str):
        with SessionLocal() as session:
            try:
                new_thread = Thread(title=title)
                session.add(new_thread)
                session.commit()
                self.logger.info(f"スレッド登録成功: title={title}")
                return new_thread
            except Exception as e:
                session.rollback()
                self.logger.error(f"スレッド登録失敗: {e}")
                raise
