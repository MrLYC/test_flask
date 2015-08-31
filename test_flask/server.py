#!/usr/bin/env python
# encoding: utf-8

from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route("/", methods=["GET"])
def index():
    return render_template("index.html", init_lines=(
        u"Welcome",
    ))


def main():
    app.run(host="0.0.0.0", debug=True)


if __name__ == '__main__':
    main()
