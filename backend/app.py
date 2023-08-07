from flask import Flask, render_template, request, jsonify
import requests
import json
from flask_cors import CORS, cross_origin

app = Flask(__name__)
CORS(app)


@app.route('/')
def hello_world():  # put application's code here
    # return render_template("sample.html")
    payload = json.dumps({
        "messages": [
            {"role": "user", "content": "请介绍一下你自己"},
            {"role": "assistant", "content": "你现在是一名智能助手,能够以通俗易懂且准确的方式回答人们的问题"},
            {"role": "user",
             "content": "请列举一些关于健身的英文单词，比如说心肺能力Cardiopulmonary capacity，有氧运动	Aerobics 之类的  "}
        ]
    })
    return generate(payload)


@app.route('/submit', methods=['POST'])
@cross_origin()
def submit_question():
    data = request.json
    if data is None:
        return jsonify({'error': 'No JSON data provided'}), 400
    print(data)
    # 在这里进行数据处理或其他逻辑操作
    # 这只是一个简单的示例，实际上你可以根据需要做更多的事情
    payload = json.dumps({
        "messages": [
            {"role": "user", "content": "请介绍一下你自己"},
            {"role": "assistant", "content": "你现在是一名智能助手,能够以通俗易懂且准确的方式回答人们的问题"},
            {"role": "user",
             "content": data['question']}
        ]
    })
    return generate(payload)


def get_access_token():
    """
    使用 API Key，Secret Key 获取access_token，替换下列示例中的应用API Key、应用Secret Key
    """

    url = "https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=RHEPBtvR2S6BUwe2GsuprrWj&client_secret=nhiAqqajWwmkWXGNEkcoXnWBzAqwcKBj"

    payload = json.dumps("")
    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    return response.json().get("access_token")


def generate(payload):
    url = "https://aip.baidubce.com/rpc/2.0/ai_custom/v1/wenxinworkshop/chat/eb-instant?access_token=" + get_access_token()

    # payload = json.dumps({
    #     "messages": [
    #         {"role": "user", "content": "请介绍一下你自己"},
    #         {"role": "assistant", "content": "你现在是一名智能助手,能够以通俗易懂且准确的方式回答人们的问题"},
    #         {"role": "user",
    #          "content": "请列举一些关于健身的英文单词，比如说心肺能力Cardiopulmonary capacity，有氧运动	Aerobics 之类的  "}
    #     ]
    # })
    headers = {
        'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    file_path = ".\\WENXIN.JSON"
    with open(file_path, "w") as file:
        file.write(response.text)
    print(response.text)
    return response.text


if __name__ == '__main__':
    app.run()
