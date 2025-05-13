# ベースイメージ
FROM python:3.11

# 作業ディレクトリを /app に設定
WORKDIR /app

# Poetryのインストール
RUN pip install --upgrade pip && \
    pip install poetry

# Poetryの仮想環境を無効化（グローバルに依存をインストール）
RUN poetry config virtualenvs.create false

# Poetry依存ファイルを先にコピー（キャッシュ効率化）
COPY pyproject.toml poetry.lock* /app/

# 依存関係のインストール
RUN poetry install --no-root

# ルートディレクトリ全体をコピーする
COPY . /app

ENV PYTHONPATH="${PYTHONPATH}:/app"

# Streamlitアプリの起動
CMD ["streamlit", "run", "main.py", "--server.port=8501", "--server.address=0.0.0.0"]
