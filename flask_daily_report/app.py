from flask import Flask, render_template,session, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime


app = Flask(__name__)

app.config['SECRET_KEY'] = 'this is very secret'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


@app.route('/')
def index():
    row = Report.query.all()
    return render_template("index.html",row=row,title='details')


if __name__ == "__main__":
    app.run(debug=True)