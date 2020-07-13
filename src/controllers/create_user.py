from src.app import app
from src.our_db import *
from src.helpers.errorHandler import errorHandler, Error404,APIError

@app.route("/user/create/<username>")
@errorHandler
def newuser(username):
    if db.User.find_one({"username":username}) == None:
        db.User.insert({"username":username})
        return str(db.User.find_one({"username":username},{"username":0})["_id"])
    raise APIError("Ese nombre de usuario ya esta ocupado. Prueba con otro :) ! Try again /user/create?username=<username>")