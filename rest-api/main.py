import datetime
import string
from flask import Flask, config, render_template, request, make_response, jsonify
import flask
from markupsafe import escape
import logging

app = Flask(__name__)

# Create and configure logger
logging.basicConfig(filename="logs/"+datetime.datetime.now().__str__()+".log", format="%(asctime)s %(message)s", filemode="w")
# Creating an object
logger = logging.getLogger()
# Setting the threshold of logger to DEBUG
logger.setLevel(logging.DEBUG)


DEFAULT_ALPH = "abcdefghijklmnopqrstuvwxyz"


def getBooleanResult(s, alphabet):
    for letter in alphabet:
        if letter not in s.lower():
            return False
    return True


@app.route("/")
def root():
    res = make_response("API (version: 1.0.0)", 200)
    return res


@app.route("/api/v1")
@app.route("/api/v1/")
def main():
    res = make_response(
        "[STATUS PAGE] [CURRENT STATUS: ONLINE] ["
        + datetime.datetime.now().__str__()
        + "]",
        200,
    )
    res.headers["Content-Type"] = "text/html"
    res.headers["Access-Control-Allow-Origin"] = "*"
    return res


@app.route("/api/v1/ispangram/<string:input>", methods=["GET"])
def isPangram_url(input):
    if input:
        res = make_response(
            "[ " + getBooleanResult(input, DEFAULT_ALPH).__str__() + " ]", 200
        )
    res.headers["Content-Type"] = "text/html"
    res.headers["Access-Control-Allow-Origin"] = "*"
    res.headers["Language"] = "en-us"
    return res


@app.route("/api/v1/ispangram", methods=["POST"])
def isPangram_json():
    dataset = request.get_json()
    if request.content_type.lower() != "application/json":
        logger.info("-->/405IPJ/"+datetime.datetime.now().__str__())
        res = make_response(
            jsonify(
                {
                    "ERROR_CODE": "405IPJ",
                    "ERROR_MSG": "INVALID HEADER",
                    "TIMESTAMP": datetime.datetime.now().__str__(),
                }
            ),
            405,
        )
        return res
    if dataset:
        if dataset["input"]:
            res = make_response(
                jsonify(
                    {
                        "result": getBooleanResult(dataset["input"], DEFAULT_ALPH),
                        "input": dataset["input"],
                        "alphabet": DEFAULT_ALPH,
                        "timestamp": datetime.datetime.now().__str__(),
                    }
                ),
                200,
            )
        else:
            logger.info("-->/204IPJ/"+datetime.datetime.now().__str__())
            res = make_response(
                jsonify(
                    {
                        "ERROR_CODE": "204IPJ",
                        "ERROR_MSG": "INVALID INPUT STRING",
                        "TIMESTAMP": datetime.datetime.now().__str__(),
                    }
                ),
                202,
            )
    res.headers["Language"] = "en-us"
    res.headers["Content-Type"] = "application/json"
    res.headers["Access-Control-Allow-Origin"] = "*"
    return res


@app.route("/demo/user")
def sample():
    return {"user": "Tom", "time": datetime.datetime.now(), "isSample": True}


@app.errorhandler(404)
def not_found(error):
    res = make_response(render_template("error.html"), 404)
    res.headers["X-Something"] = "A value"
    return res


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080, debug=True)
