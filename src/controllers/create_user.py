from src.app import app
from src.our_db import *

@app.route("/user/create/<username>")
def newuser(username):
    if db.User.find_one({"username":username}) == None:
        db.User.insert({"username":username})
        return str(db.User.find_one({"username":username},{"username":0})["_id"])
    return "Ese nombre de usuario ya esta ocupado. Prueba con otro :) !"