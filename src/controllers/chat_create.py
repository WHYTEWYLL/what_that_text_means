from src.app import app
from src.our_db import *
from flask import request
from bson.objectid import ObjectId
from bson.json_util import dumps
from src.helpers.errorHandler import errorHandler, Error404,APIError

@app.route("/chat/create")
@errorHandler
def createchat():
    """    
    Funct creates a chat base of the Participants param, with a groupname.
    """
    team = request.args.getlist('Participants')
    groupname=request.args.get('groupname')
    if db.Conversation.find_one({"name":groupname}) == None:
        db.Conversation.insert({"Participants": team , "name":groupname})
        return str(db.Conversation.find_one({"name":groupname},{"Participants":0,"name":0})["_id"])
    raise APIError("Ese nombre de groupname ya esta ocupado. Prueba con otro :) ! ")

@app.route("/chat/<conversation_id>/adduser")
@errorHandler
def add_more_tochat(conversation_id):
    """    
    Funct adds a existing user to a conversation.
    """
    if db.Conversation.find_one({"_id":ObjectId(conversation_id)}) :
        new_one=request.args.getlist('add_user_id')
        db.Conversation.update_one({"_id":ObjectId(conversation_id)},{"$push":{"Participants":{"$each": new_one}}})
        return str(db.Conversation.find_one({"_id":ObjectId(conversation_id)},{"Participants":1,"_id":0})["Participants"])
    raise Error404("Esa conversacion. No existe!") 

@app.route("/chat/<conversation_id>/addmessage/<user_id>",methods = ['POST'])
@errorHandler
def addmessage(conversation_id,user_id):
    """
    Funct add a message to a conversation by the user_id.
    """
    texto = request.args.get('text')
    print(texto)
    if db.Conversation.find_one({"_id":ObjectId(conversation_id),"Participants":user_id}) :
        db.NEWCHAT.insert({"Message":texto,"by":user_id,"Group":conversation_id})
        return "Mensaje enviado"
    raise Error404("Para estos parametros, no hay match! Prueba con otros.") 

@app.route("/chat/<conversation_id>/list")
@errorHandler 
def showme(conversation_id):
    """
    Funct shows all messages from a conversation.
    """
    cursor_mensajes=db.NEWCHAT.find({"Group":conversation_id})
    mensajes=dumps(cursor_mensajes)
    print(type(mensajes))
    if mensajes != "[]" :
        return mensajes
    raise Error404("Para estos parametros, no hay match! Prueba con otros.") 