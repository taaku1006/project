FROM ollama/ollama

# bashと基本ツールをaptでインストール（Ubuntu/Debianベース用）
RUN apt update && apt install -y bash curl

# モデル定義・エントリースクリプトをコピー
COPY Modelfile /Modelfile
COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

# モデル登録＋Ollama起動のエントリポイントを設定
ENTRYPOINT ["/entrypoint.sh"]
