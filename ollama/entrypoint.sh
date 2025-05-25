#!/bin/bash

# Ollamaバックグラウンド起動
ollama serve &

# 起動安定待ち（2秒）
sleep 2

# モデル登録（すでに存在すればスキップ）
if ! ollama list | grep -q "elyza3"; then
  echo "elyza3 モデルを作成中..."
  ollama create -f /Modelfile elyza3
  echo "elyza3 モデルの作成が完了しました。"
else
  echo "elyza3 モデルはすでに存在します。スキップします。"
fi

# 無限ループで待機（コンテナ維持用）
tail -f /dev/null
