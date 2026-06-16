from flask import Flask, render_template, url_for, request, redirect, session

app = Flask(__name__)
app.secret_key = "my_secret_key";

totalpoints = 0;
Unit = {
    "leaders" : "",
    "battleline": "",
    "other":"",
    "totalpoints": 0
}

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

@app.route("/calculate/<int:points>")
def calculate(points):
    global totalpoints
    totalpoints = points
    return redirect(url_for("builder"))

@app.route("/removeunit/<int:points>")
def removeunit(points):
    global totalpoints
    totalpoints = totalpoints - points
    return redirect(url_for("builder"))

@app.route("/addunit/<int:points>")
def addunit(points):
    global totalpoints
    totalpoints = totalpoints + points
    return redirect(url_for("builder"))

@app.route("/builder")
def builder():
    return render_template("builder.html", points=totalpoints)

    # if request.method == "POST":
    #     try:
    #         expression = request.form["display"]
    #         result = eval(expression)
    #     except Exception as e:
    #         result = "error"
    # return render_template('builder.html', result=result)

# @app.route("/calculator", methods=["GET", "POST"])
# def calculator():
#     result = ''
#     if request.method == "POST":
#         try:
#             expression = request.form["display"]
#             result = eval(expression)
#         except Exception as e:
#             result = "error"
#     return render_template('calculator.html', result=result)