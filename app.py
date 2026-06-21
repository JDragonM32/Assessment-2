from flask import Flask, render_template, url_for, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
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
    result = ''
    if request.method == "POST":
        try:
            expression = request.form["display"]
            result = eval(expression)
        except Exception as e:
            result = "error"
    return render_template('builder.html', result=result)

@app.route("/calculator", methods=["GET", "POST"])
def calculator():
    result = ''
    if request.method == "POST":
        try:
            expression = request.form["display"]
            result = eval(expression)
        except Exception as e:
            result = "error"
    return render_template('calculator.html', result=result)

#units
#Leaders
Warboss = {"name": "Warboss", "num": "1", "points": 75}
Weirdboy = {"name": "Weirdboy", "num": "1", "points": 65}
#Battleline
Boyz10 = {"name": "Boyz", "num": "10", "points": 75}
Boyz20 = {"name": "Boyz", "num": "20", "points": 150}
Gretchin10 = {"name": "Gretchin", "num": "10", "points": 45}
Gretchin20 = {"name": "Gretchin", "num": "20", "points": 80}
#Other
Dakkarig = {"name": "Big Mek Dakkarig", "num": "1", "points": 100}