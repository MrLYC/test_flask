#!/usr/bin/env python
# encoding: utf-8

import math

from flask import Flask, request
from flask import render_template

from ycyc.base.calctools import safecalc
from ycyc.base.funcutils import iter_attrs

app = Flask(__name__)

Calc_Func = {
    n: f
    for n, f in iter_attrs(math, exclude_methods=False)
}


@app.route("/", methods=["GET"])
def index():
    return render_template("index.html", init_lines=(
        u"Welcome",
    ))


@app.route("/calc", methods=["POST"])
def calc():
    expr = request.form.get("expr")
    if not expr:
        return ""
    try:
        return str(safecalc(expr, Calc_Func))
    except Exception as err:
        return "Error: %s" % err


def main():
    app.run(host="0.0.0.0", debug=True)


if __name__ == '__main__':
    main()
