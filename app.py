from flask import Flask, render_template, url_for, request, redirect

app = Flask(__name__)

totalpoints = 0
currentpoints = 0

units = {
    "leaders":{},
    "battleline":{},
    "other":{}
}

Leaders = {
    "Warboss": {"name": "Warboss", "num": "1", "points": 75},
    "Weirdboy": {"name": "Weirdboy", "num": "1", "points": 65}
}

Battleline = {
    "Boyz10": {"name": "Boyz", "num": "10", "points": 80},
    "Boyz20": {"name": "Boyz", "num": "20", "points": 170},
    "Gretchin10": {"name": "Gretchin", "num": "10", "points": 40},
    "Gretchin20": {"name": "Gretchin", "num": "20", "points": 80}
}
Other = {
    "Dakkarig": {"name": "Big Mek Dakkarig", "num": "1", "points": 120}
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

@app.route("/setpoints/<int:points>")
def calculate(points):
    global totalpoints
    global currentpoints
    totalpoints = points
    currentpoints = totalpoints
    global units
    units = {
        "leaders": {},
        "battleline": {},
        "other": {}
    }
    return redirect(url_for("builder"))

@app.route("/removeunit/<leader>")
def removeunit(leader):
    global totalpoints
    leader_data = Leaders[leader]
    units["leaders"] = leader_data
    totalpoints = totalpoints + units["leaders"]["points"]
    return redirect(url_for("builder"))

@app.route("/addunit/<leader>")
def addunit(leader):
    leader_data = Leaders[leader]
    
    if leader in units["leaders"]:
        units["leaders"][leader][1] += 1
    else:
        units["leaders"][leader] = [leader_data, 1]

    calculate_points()

    return redirect(url_for("builder"))

@app.route("/builder")
def builder():
    return render_template("builder.html", points=currentpoints)

def calculate_points():
    global totalpoints
    global currentpoints
    
    battlelinepoints = 0
    otherpoints = 0
    leaderpoints = 0

    for unit in units:
        for category, (data, count) in units[unit].items():
            print(count)
            leaderpoints = data["points"] * count
            print(leaderpoints)

    currentpoints = totalpoints - (leaderpoints + battlelinepoints + otherpoints)





# @app.route("/builder")
# def builder():
#     result = ''
#     if request.method == "POST":
#         try:
#             expression = request.form["display"]
#             result = eval(expression)
#         except Exception as e:
#             result = "error"
#     return render_template('builder.html', result=result)

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

