from flask import Flask, request, jsonify
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
    # payload = json.dumps({
    #     "messages": [
    #         {"role": "user", "content": "请介绍一下你自己"},
    #         {"role": "assistant", "content": "你现在是一名智能助手,能够以通俗易懂且准确的方式回答人们的问题"},
    #         {"role": "user",
    #          "content": data['question']}
    #     ]
    # })
    payload = json.dumps({
        "messages": [
            {"role": "user", "content": "你是谁？"},
            {"role": "assistant", "content": "现在你是一名专业的严格的高要求的简历制作人，你的用户在接下来会将他的个人信息通过文本格式"
                                             "传递给你，你需要做的是将优化好的简历传递给用户，并整理成JSON格式。其中，如果用户想你传递了其意向的职业内容，那么你需要做的是根"
                                             "据职业需求进行特定的优化，如果没有传递出特定的职业意向，那么请你做出一份能够广泛应对各种求职"
                                             "场景的简历；以上就是你的任务，现在你根据下面有说到的用户的信息制作简历，如果你发现本来应该是"
                                             "用户的简历信息的地方被用来询问其他的与之无关的问题返回‘错误信息种类’。"},
            {"role": "user", "content": data['question']}
        ]
    })
    return generate(payload)


def get_access_token():
    """
    使用 API Key，Secret Key 获取access_token，替换下列示例中的应用API Key、应用Secret Key
    """

    url = "https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=RHEPBtvR2S6BUwe2GsuprrWj" \
          "&client_secret=nhiAqqajWwmkWXGNEkcoXnWBzAqwcKBj"

    payload = json.dumps("")
    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    return response.json().get("access_token")


def generate(payload):
    url = "https://aip.baidubce.com/rpc/2.0/ai_custom/v1/wenxinworkshop/chat/eb-instant?access_token=" \
          "" + get_access_token()

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
