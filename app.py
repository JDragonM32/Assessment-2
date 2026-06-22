from flask import Flask, render_template, url_for, request, redirect
import sqlite3
conn = sqlite3.connect('database.db')
cursor = conn.cursor()

app = Flask(__name__)

totalpoints = 0
currentpoints =0

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
    "Boyz10": {"name": "Boyz", "num": "10", "points": 75},
    "Boyz20": {"name": "Boyz", "num": "20", "points": 150},
    "Gretchin10": {"name": "Gretchin", "num": "10", "points": 45},
    "Gretchin20": {"name": "Gretchin", "num": "20", "points": 80}
}
Other = {
    "Dakkarig": {"name": "Big Mek Dakkarig", "num": "1", "points": 100}
}

@app.route("/", methods=["GET", "POST"])
@app.route("/index")
def index():
    return render_template('index.html')

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

@app.route("/removeunit/<battleline>")
def removeunit(battleline):
    global totalpoints
    leader_data = Battleline[battleline]
    units["battleline"] = battleline_data
    totalpoints = totalpoints + units["battleline"]["points"]
    return redirect(url_for("builder"))

@app.route("/removeunit/<other>")
def removeunit(other):
    global totalpoints
    leader_data = Other[other]
    units["other"] = other_data
    totalpoints = totalpoints + units["other"]["points"]
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

@app.route("/addunit/<battleline>")
def addunit(battleline):
    battleline_data = Battleline[battleline]
    if battleline in units["battleline"]:
        units["battleline"][battleline][1] += 1
    else:
        units["battleline"][battleline] = [battleline_data, 1]
    calculate_points()
    return redirect(url_for("builder"))

@app.route("/addunit/<other>")
def addunit(other):
    other_data = Other[other]
    if other in units["other"]:
        units["other"][other][1] += 1
    else:
        units["other"][other] = [other_data, 1]
    calculate_points()
    return redirect(url_for("builder"))

@app.route("/builder")
def builder():
    result = ''
    if request.method == "POST":
        try:
            expression = request.form["display"]
            result = eval(expression)
        except Exception as e:
            result = "error"
    return render_template('builder.html', points=currentpoints)

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