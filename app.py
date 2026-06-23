from flask import Flask, render_template, url_for, request, redirect
import mysql.connector

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
    "Boyz10": {"name": "Boyz (10)", "num": "10", "points": 75},
    "Boyz20": {"name": "Boyz (20)", "num": "20", "points": 150},
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

@app.route("/removeleader/<leader>")
def removeleader(leader):
    leader_data = Leaders[leader]
    if leader in units["leaders"]:
        units["leaders"][leader][1] -= 1
    else:
        units["leaders"][leader] = [leader_data, 1]
    calculate_points()
    return redirect(url_for("builder"))

@app.route("/removebattleline/<battleline>")
def removebattleline(battleline):
    battleline_data = Battleline[battleline]
    if battleline in units["battleline"]:
        units["battleline"][battleline][1] -= 1
    else:
        units["battleline"][battleline] = [battleline_data, 1]
    calculate_points()
    return redirect(url_for("builder"))

@app.route("/removeother/<other>")
def removeother(other):
    other_data = Other[other]
    if other in units["other"]:
        units["other"][other][1] -= 1
    else:
        units["other"][other] = [other_data, 1]
    calculate_points()
    return redirect(url_for("builder"))

@app.route("/addleader/<leader>")
def addleader(leader):
    leader_data = Leaders[leader]
    if leader in units["leaders"]:
        units["leaders"][leader][1] += 1
    else:
        units["leaders"][leader] = [leader_data, 1]
    calculate_points()
    return redirect(url_for("builder"))

@app.route("/addbattleline/<battleline>")
def addbattleline(battleline):
    battleline_data = Battleline[battleline]
    if battleline in units["battleline"]:
        units["battleline"][battleline][1] += 1
    else:
        units["battleline"][battleline] = [battleline_data, 1]
    calculate_points()
    return redirect(url_for("builder"))

@app.route("/addother/<other>")
def addother(other):
    other_data = Other[other]
    if other in units["other"]:
        units["other"][other][1] += 1
    else:
        units["other"][other] = [other_data, 1]
    calculate_points()
    return redirect(url_for("builder"))

@app.route("/builder")
def builder():
    return render_template('builder.html', points=currentpoints)

def calculate_points():
    global totalpoints
    global currentpoints
    total = 0
    for category in units.values():
        for unit_data in category.values():
            unit = unit_data[0]
            count = unit_data[1]
            total += unit['points'] * count
    print(total)
    currentpoints = totalpoints - total
    #as a unit is added, it should be displayed on the right
    #the points cost of all units added should be calculated and display in the 'Points bar'
    #'removeunit' should not work if none of that unit has been added
    #each unit should only be able to be added upto 3 times (6 for battleline)
    #chosen points limit should not be able to be exceeded