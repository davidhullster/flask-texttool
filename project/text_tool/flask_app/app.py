from flask import Flask, render_template, flash, request, make_response
from flask_wtf import FlaskForm
from wtforms import TextField, TextAreaField, StringField, SubmitField
from wtforms.validators import DataRequired
from datetime import datetime, timezone
import uuid
import random

# App config.
DEBUG = True
app = Flask(__name__)
app.config.from_object(__name__)
app.config["SECRET_KEY"] = str(uuid.uuid4())
# CORS Config
origin_list = [
    "https://accounts.google.com",
    "https://texttool.davidhull.click",
    "https://amazon.com",
]


class TextTransformer(FlaskForm):
    text_entry = StringField("Enter Text Below:", validators=[DataRequired()])
    submit = SubmitField("Enter Text to Transform")

    @app.route("/", methods=["GET", "POST", "OPTIONS"])
    @app.route("/index", methods=["GET", "POST", "OPTIONS"])
    def index():
        time_output = datetime.utcnow()
        form = TextTransformer(request.form)
        text_entry = None
        print(form.errors)
        if request.method == "POST":
            time_output = datetime.utcnow()
            text_entry = request.form["text_entry"]
            print(text_entry.swapcase())
        resp = make_response(
            render_template(
                "index.html",
                form=form,
                time_output=time_output,
                text_entry=text_entry.swapcase(),
            )
        )
        resp.headers["Access-Control-Allow-Origin"] = origin_list
        resp.headers["Access-Control-Allow-Credentials"] = "true"
        resp.headers["Access-Control-Allow-Methods"] = "GET, POST, OPTIONS, PUT, DELETE"
        return resp


if __name__ == "__main__":
    app.run()
