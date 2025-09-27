# -*- coding: utf-8 -*-
import os
from flask import Flask, request, jsonify, render_template
from openai import OpenAI

app = Flask(__name__)

# API 配置（建议后续放到 .env 文件中管理）
client = OpenAI(
    api_key="sk-laktyimuvruwxaxbwkrjdcooazwsejzbxqjhygrqwyqguhyv",
    base_url="https://api.siliconflow.cn/v1"
)

# 首页
@app.route("/")
def index():
    return render_template("index.html")

# 聊天页
@app.route("/chat")
def chat():
    return render_template("chat.html")

# AI 回复接口
@app.route("/ask", methods=["POST"])
def ask():
    data = request.json
    user_input = data.get("question", "")

    try:
        response = client.chat.completions.create(
            model="Qwen/QwQ-32B",
            messages=[{"role": "user", "content": user_input}]
        )
        answer = response.choices[0].message.content
    except Exception as e:
        answer = f"出错了: {str(e)}"

    return jsonify({"answer": answer})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)


