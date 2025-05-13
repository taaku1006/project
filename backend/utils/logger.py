import logging
import sys

def get_logger(name: str = "app", level: int = logging.INFO) -> logging.Logger:
    """
    ロガーを生成して返す。StreamHandler付き。再生成は防ぐ。

    :param name: ロガー名（デフォルト: "app"）
    :param level: ログレベル（デフォルト: logging.INFO）
    :return: logging.Logger インスタンス
    """
    logger = logging.getLogger(name)

    if logger.hasHandlers():
        return logger

    logger.setLevel(level)

    handler = logging.StreamHandler(sys.stdout)
    formatter = logging.Formatter("[%(levelname)s] %(asctime)s - %(name)s - %(message)s")
    handler.setFormatter(formatter)

    logger.addHandler(handler)

    return logger
