# CUDA対応ベースイメージ（GPU使用のため）
FROM nvidia/cuda:12.6.0-base-ubuntu22.04

# Python3.11と基本ツールをインストール
RUN apt update && apt install -y \
    python3.11 python3.11-venv python3.11-dev python3-pip \
    curl git build-essential

# python3 のデフォルトを 3.11 に設定
RUN update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.11 1

# Poetryインストール
RUN curl -sSL https://install.python-poetry.org | python3 -

# Poetryのパスを有効に
ENV PATH="/root/.local/bin:$PATH"

# 作業ディレクトリ
WORKDIR /app

# Poetryの仮想環境を無効化（グローバルにインストール）
RUN poetry config virtualenvs.create false

# 依存ファイルのみ先にコピー（キャッシュ効率化）
COPY pyproject.toml poetry.lock* /app/

# 依存ライブラリのインストール
RUN poetry install --no-root

# アプリ全体をコピー
COPY . /app

# PYTHONPATHを設定
ENV PYTHONPATH="${PYTHONPATH}:/app"

# Streamlitアプリの起動
CMD ["streamlit", "run", "main.py", "--server.port=8501", "--server.address=0.0.0.0"]
