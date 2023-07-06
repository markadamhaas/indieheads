from flask import Flask, render_template, request
import sqlite3
# import mysql.connector


app = Flask(__name__)


# mydb = mysql.connector.connect(
#   host="localhost",
#   user="yourusername",
#   password="yourpassword"
# )


@app.route("/")
def index_page():
    return render_template("index.html")


@app.route("/create-db")
def create_db():

    connection_obj = sqlite3.connect('project.db')
    cursor_obj = connection_obj.cursor()

    cursor_obj.execute("DROP TABLE IF EXISTS users")

    table = """ CREATE TABLE users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name CHAR(32) NOT NULL
    ); """
    cursor_obj.execute(table)

    table = """ CREATE TABLE classes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        code CHAR(32) NOT NULL
    ); """
    cursor_obj.execute(table)

    table = """ CREATE TABLE user_class_reln (
        user_id INTEGER,
        class_id INTEGER,
        FOREIGN KEY (user_id) REFERENCES users(id)
        FOREIGN KEY (class_id) REFERENCES classes(id)
    ); """
    cursor_obj.execute(table)

    connection_obj.close()

    return "DB is fresh and ready"


@app.route("/get-users")
def get_users():

    connection_obj = sqlite3.connect('project.db')
    cursor_obj = connection_obj.cursor()
    
    cursor_obj.execute("SELECT * FROM users ORDER BY id DESC LIMIT 1000000")
    output = cursor_obj.fetchall()

    connection_obj.close()

    return render_template("get-users.html", users = output)


@app.route("/create-user")
def creat_user():

    name = str(request.args.get("name")).strip()
    if name == '':
        return "Name cannot be empty"

    connection_obj = sqlite3.connect('project.db')
    cursor_obj = connection_obj.cursor()
    
    cursor_obj.execute(f"INSERT INTO users (name) VALUES ('{name}')")
    connection_obj.commit()

    connection_obj.close()

    return "Created a new user"


@app.route("/get-classes")
def get_classes():

    connection_obj = sqlite3.connect('project.db')
    cursor_obj = connection_obj.cursor()
    
    cursor_obj.execute("SELECT * FROM classes ORDER BY id DESC LIMIT 1000000")
    output = cursor_obj.fetchall()

    connection_obj.close()

    return render_template("get-classes.html", classes = output)


@app.route("/create-class")
def creat_class():

    code = str(request.args.get("code")).strip()
    if code == '':
        return "Code cannot be empty"

    connection_obj = sqlite3.connect('project.db')
    cursor_obj = connection_obj.cursor()
    
    cursor_obj.execute(f"INSERT INTO classes (code) VALUES ('{code}')")
    connection_obj.commit()

    connection_obj.close()

    return "Created a new class"


@app.route("/class/<int:id>")
def class_(id):

    connection_obj = sqlite3.connect('project.db')
    cursor_obj = connection_obj.cursor()
    
    cursor_obj.execute(f"SELECT * FROM classes WHERE id = {id} LIMIT 1")
    cls_info = cursor_obj.fetchone()

    if cls_info is None:
        return "No class found"

    cursor_obj.execute(f"SELECT * FROM users WHERE id IN ( SELECT user_id FROM user_class_reln WHERE class_id = {cls_info[0]} )")
    users = cursor_obj.fetchall()

    connection_obj.close()

    return render_template("class.html", cls_info = cls_info, users = users)


@app.route("/user/<int:id>")
def user(id):

    connection_obj = sqlite3.connect('project.db')
    cursor_obj = connection_obj.cursor()
    
    cursor_obj.execute(f"SELECT * FROM users WHERE id = {id} LIMIT 1")
    usr_info = cursor_obj.fetchone()

    if usr_info is None:
        return "No user found"

    cursor_obj.execute(f"SELECT * FROM classes WHERE id IN ( SELECT class_id FROM user_class_reln WHERE user_id = {usr_info[0]} )")
    classes = cursor_obj.fetchall()

    connection_obj.close()

    return render_template("user.html", usr_info = usr_info, classes = classes)


@app.route("/connect")
def connect():

    class_id = int(request.args.get("class_id"))
    user_id = int(request.args.get("user_id"))

    connection_obj = sqlite3.connect('project.db')
    cursor_obj = connection_obj.cursor()

    cursor_obj.execute(f"SELECT * FROM user_class_reln WHERE class_id = {class_id} AND user_id = {user_id} LIMIT 1")
    exist = cursor_obj.fetchone()

    if exist is not None:
        return "Connection already exists"

    try:
        cursor_obj.execute(f"INSERT INTO user_class_reln (class_id, user_id) VALUES ( {class_id}, {user_id} )")
        connection_obj.commit()
    except:
        return "Either user_id or class_id doens't exist"
    
    return "Done!"


if __name__ == '__main__':
    app.run(debug=True)

