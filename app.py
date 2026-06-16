from flask import Flask, render_template, url_for

app = Flask(__name__)

totalpoints = 0;


@app.route("/")
@app.route("/index")
def index():
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

@app.route("/calculator/<int:points>")
def calculator(points):
    totalpoints = points
    return render_template("builder.html", points=totalpoints)