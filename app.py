import json
import flask
import requests
from kWords import get_stats

app = flask.Flask(__name__)

@app.route("/")
def hello_world():
    return flask.render_template("index.html")

# @app.route("/login")
# def do_auth_stuff():

#     # auth_url = "https://github.com/login/oauth/authorize" + ""

#     params = {}
#     params['client_id'] = "c4f84261adc0b84a57f7"
#     # params['redirect_uri'] = "http://127.0.0.1:5000/callback"

#     return requests.get("https://github.com/login/oauth/authorize", params=params).content


# @app.route("/session", methods=["POST"])
# def process_tokens():

#     thingy = json.load(flask.request.json)

#     test_code = flask.request.json['code']

#     client_id = "c4f84261adc0b84a57f7"

#     client_secret = "559ec0c0c2baeb47b17b4a58724a2f77a706e80a"

#     print(test_code)

#     params = {}
#     params['client_id'] = client_id
#     params['client_secret'] = client_secret
#     params['code'] = test_code
#     # params['redirect_uri'] = 

#     requests.post("https://github.com/login/oauth/access_token", params=params)

#     return flask.redirect("google.com")

#     # return flask.redirect(flask.url_for('hello_world'))


@app.route("/api/processtext", methods=["POST"])
def string_to_stats():

    print(flask.request.json["text"])
    # return request

    text = flask.request.json['text']

    return get_stats(text)

    # curl -X POST -d '{"text": "형태소는 언어학에서 일정한 의미가 있는 가장 작은 말의 단위로 발화체 내에서 따로 떼어낼 수 있는 것을 말합니다."}' http://127.0.0.1:5000/api/processtext
