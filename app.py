from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template('index.html')

@app.route("/user")
def user():
    return render_template('user.html')

@app.route("/reference")
def reference():
    return render_template('reference.html')

@app.route("/builder")
def builder():
    return render_template('builder.html')