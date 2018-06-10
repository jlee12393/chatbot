from flask import Flask
from flask import request
from flask import jsonify
from flask import json

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "이글스 챗봇에 놀러오신걸 환영합니다~"


@app.route('/keyboard')
def Keyboard():
    
    dataSend = {
        "type" : "buttons",
        "buttons" : ["시작하기", "도움말"]
    }
    
    return jsonify(dataSend)



@app.route('/message', methods=['POST'])
def Message():
    
    dataReceive = request.get_json()
    content = dataReceive['content']
    
    if content == u"시작하기":
        dataSend = {
            "message": {
                "text": "아직 개발중이라 대답을 잘 못해도 이해해줘^^;"
        }
    }
    elif content == u"도움말":
        dataSend = {
            "message": {
                "text": "이제 곧 정식 버전이 출시될거야. 조금만 기다려~~~"
            }
        }
    elif u"안녕" in content:
        dataSend = {
            "message": {
                "text": "안녕~~ 반가워 ㅎㅎ"
            }
        }
    else:
        dataSend = {
            "message": {
                "text": "나랑 놀자 ㅋㅋㅋ"
            }
        }
    return jsonify(dataSend)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
