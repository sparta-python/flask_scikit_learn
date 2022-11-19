from flask import Flask
from flask import render_template
from flask import request

import model

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/", methods=["GET", "POST"])
def predict():
    number = int(request.form["number"])
    predict = model.model(number)
    return render_template("index.html", predict=predict)


if __name__ == "__main__":
    app.run(debug=True)
