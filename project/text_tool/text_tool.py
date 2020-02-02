from flask import Flask, render_template, flash, request
from flask_wtf import FlaskForm
from wtforms import TextField, TextAreaField, validators, StringField, SubmitField
from datetime import datetime, timezone

# App config.
DEBUG = True
app = Flask(__name__)
app.config.from_object(__name__)
app.config['SECRET_KEY'] = '7d441f27d441f27567d441f2b6176a'

class TextTransformer(FlaskForm):
    text_entry = StringField('Enter Text Below:', validators=[validators.data_required])
    submit = SubmitField('Enter Text to Transform')
    
    @app.route("/", methods=['GET', 'POST'])
    @app.route("/index", methods=['GET', 'POST'])
    def index():
        time_output = datetime.utcnow()
        form = TextTransformer(request.form)
        text_entry=None
        print(form.errors)
        if request.method == 'POST':
            time_output = datetime.utcnow()
            text_entry=request.form['text_entry']
            print(text_entry)
    
        return render_template('index.html', form=form, time_output=time_output, text_entry=text_entry)

if __name__ == "__main__":
    app.run()