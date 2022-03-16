import flask
from kWords import get_stats

app = flask.Flask(__name__)

@app.route("/")
def hello_world():
    return flask.render_template("index.html")

@app.route("/api/processtext", methods=["POST"])
def string_to_stats():

    print(flask.request.json["text"])
    # return request

    text = flask.request.json['text']

    return get_stats(text)


    # curl -X POST -d '{"text": "형태소는 언어학에서 일정한 의미가 있는 가장 작은 말의 단위로 발화체 내에서 따로 떼어낼 수 있는 것을 말합니다."}' http://127.0.0.1:5000/api/processtext
