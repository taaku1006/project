# CUDA対応のUbuntuベース（NVIDIA GPU対応）
FROM nvidia/cuda:12.6.0-base-ubuntu22.04

# 基本ツールのインストール（Python3.11含む）
RUN apt update && apt install -y \
    python3.11 python3.11-venv python3.11-dev python3.11-distutils \
    curl git build-essential libgl1 wget

# Python3のデフォルトを3.11に設定
RUN update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.11 1

# pipをインストール
RUN wget https://bootstrap.pypa.io/get-pip.py && python3.11 get-pip.py && rm get-pip.py

# Poetryのインストール（公式スクリプト使用）
RUN curl -sSL https://install.python-poetry.org | python3 -

# Poetryのパスを追加
ENV PATH="/root/.local/bin:$PATH"

# 作業ディレクトリ
WORKDIR /app

# Poetryの仮想環境を無効化（グローバルインストール）
RUN poetry config virtualenvs.create false

# 依存定義ファイルのみ先にコピー（キャッシュを効かせる）
COPY pyproject.toml poetry.lock* /app/

# 依存パッケージをインストール（--no-rootで自身のパッケージ除外）
RUN poetry install --no-root

# アプリケーションコードをコピー
COPY . /app

# Pythonモジュールパスの設定
ENV PYTHONPATH="${PYTHONPATH}:/app"

# Streamlitアプリの起動コマンド（headlessモード）
CMD ["streamlit", "run", "main.py", "--server.port=8501", "--server.address=0.0.0.0", "--server.headless=true"]
