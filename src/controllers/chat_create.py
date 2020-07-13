from src.app import app
from src.our_db import *
from flask import request
from bson.objectid import ObjectId
from bson.json_util import dumps

@app.route("/chat/create")
def createchat():
    team = request.args.getlist('Participants')
    groupname=request.args.get('groupname')
    if db.Conversation.find_one({"name":groupname}) == None:
        db.Conversation.insert({"Participants": team , "name":groupname})
        return str(db.Conversation.find_one({"name":groupname},{"Participants":0,"name":0})["_id"])
    return "Este grupo ya existe. Prueba con otro :) !"

@app.route("/chat/<conversation_id>/adduser")
def add_more_tochat(conversation_id):
    if db.Conversation.find_one({"_id":ObjectId(conversation_id)}) :
        new_one=request.args.getlist('add_user_id')
        db.Conversation.update_one({"_id":ObjectId(conversation_id)},{"$push":{"Participants":{"$each": new_one}}})
        return str(db.Conversation.find_one({"_id":ObjectId(conversation_id)},{"Participants":1,"_id":0})["Participants"])
    return "Esa conversacion. No existe!"

@app.route("/chat/<conversation_id>/addmessage/<user_id>",methods = ['POST'])
def addmessage(conversation_id,user_id):
    texto = request.args.get('text')
    print(texto)
    if db.Conversation.find_one({"_id":ObjectId(conversation_id),"Participants":user_id}) :
        db.NEWCHAT.insert({"Message":texto,"by":user_id,"Group":conversation_id})
        return "Mensaje enviado"

@app.route("/chat/<conversation_id>/list")
def showme(conversation_id):
    mensajes=db.NEWCHAT.find({"Group":conversation_id})
    print(mensajes)
    return dumps(mensajes)