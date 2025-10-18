

from flask import Flask, render_template, request, jsonify
from openai import OpenAI

# 创建 Flask 应用
app = Flask(__name__)

# 初始化 OpenAI 客户端（注意：没有 proxies 参数）
client = OpenAI(
    api_key="sk-laktyimuvruwxaxbwkrjdcooazwsejzbxqjhygrqwyqguhyv",
    base_url="https://api.siliconflow.cn/v1"
)
client = OpenAI(
    api_key="sk-xxxxx",
    base_url="https://api.siliconflow.cn/v1"
)

# 网站首页
@app.route('/')
def index():
    return "<h2>✅ 网站部署成功！<br>请输入 /chat 来与 AI 对话。</h2>"

# 简单聊天接口
@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()
    user_message = data.get("message", "")

    try:
        # 调用 OpenAI Chat 接口
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "你是一个友好的AI助手。"},
                {"role": "user", "content": user_message}
            ]
        )
        reply = response.choices[0].message.content
        return jsonify({"reply": reply})
    except Exception as e:
        return jsonify({"error": str(e)}), 500


# Render 启动入口
if __name__ == '__main__':
    # 在本地运行时使用端口 5000
    app.run(host='0.0.0.0', port=5000)
