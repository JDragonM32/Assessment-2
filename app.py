from flask import Flask, render_template, url_for, request, redirect
import sqlite3
conn = sqlite3.connect('database.db')
cursor = conn.cursor

cursor.execute('''CREATE TABLE leader
               (num INTEGER, name TEXT, points INTEGER)''')
conn.commit()

cursor.execute('''CREATE TABLE battleline
               (num INTEGER, name TEXT, points INTEGER)''')
conn.commit()

cursor.execute('''CREATE TABLE other
               (num INTEGER, name TEXT, points INTEGER)''')
conn.commit()

cursor.execute("INSERT INTO leader (num, name, points) VALUES (?, ?, ?)",
               (1, 'Warboss', 75),
               (1, 'Weirdboy, 65'))
conn.commit()

cursor.execute("INSERT INTO battleline (num, name, points) VALUES (?, ?, ?)",
               (10, 'Boyz', 75),
               (20, 'Boyz', 150),
               (10, 'Gretchin', 45),
               (20, 'Gretchin', 80))
conn.commit()

cursor.execute("INSERT INTO other (num, name, points) VALUES (?, ?, ?)",
               (1, 'Big Mek Dakkarig', 100))
conn.commit()

app = Flask(__name__)

totalpoints = 0
currentpoints =0

units = {
    "leader":{},
    "battleline":{},
    "other":{}
}
Leader = {
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
        "leader": {},
        "battleline": {},
        "other": {}
    }
    return redirect(url_for("builder"))

@app.route("/removeleader/<leader>")
def removeleader(leader):
    if leader in units["leader"]:
        units["leader"][leader][1] -= 1
        if(units["leader"][leader][1] <=0):
            units["leader"].pop(leader)
    calculate_points()
    return redirect(url_for("builder"))

@app.route("/removebattleline/<battleline>")
def removebattleline(battleline):
    if battleline in units["battleline"]:
        units["battleline"][battleline][1] -= 1
        if(units["battleline"][battleline][1] <=0):
            units["battleline"].pop(battleline)
    calculate_points()
    return redirect(url_for("builder"))

@app.route("/removeother/<other>")
def removeother(other):
    if other in units["other"]:
        units["other"][other][1] -= 1
        if(units["other"][other][1] <=0):
            units["other"].pop(other)
    calculate_points()
    return redirect(url_for("builder"))

@app.route("/addleader/<leader>")
def addleader(leader):
    leader_data = Leader[leader]
    if(check_points(leader_data["points"])):
        if leader in units["leader"]:
            units["leader"][leader][1] += 1
        else:
            units["leader"][leader] = [leader_data, 1]
    calculate_points()
    return redirect(url_for("builder"))

@app.route("/addbattleline/<battleline>")
def addbattleline(battleline):
    battleline_data = Battleline[battleline]
    if(check_points(battleline_data["points"])):
        if battleline in units["battleline"]:
            units["battleline"][battleline][1] += 1
        else:
            units["battleline"][battleline] = [battleline_data, 1]
    calculate_points()
    return redirect(url_for("builder"))

@app.route("/addother/<other>")
def addother(other):
    other_data = Other[other]
    if(check_points(other_data["points"])):
        if other in units["other"]:
            units["other"][other][1] += 1
        else:
            units["other"][other] = [other_data, 1]
    calculate_points()
    return redirect(url_for("builder"))

@app.route("/builder")
def builder():
    return render_template('builder.html', points=currentpoints, leader_list=units["leader"], battleline_list=units["battleline"], other_list=units["other"])

def check_points(points_to_add):
    global currentpoints
    return currentpoints>points_to_add

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