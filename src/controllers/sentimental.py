from src.app import app
from src.our_db import *
from bson.objectid import ObjectId
from bson.json_util import dumps
import pandas as pd
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from src.controllers.sima  import *
from src.helpers.errorHandler import errorHandler, Error404,APIError
nltk.download("vader_lexicon")


@app.route("/chat/<conversation_id>/sentiment")
@errorHandler
def howufeel(conversation_id):
    """
    Funct returns a dict with average feelings of all the message from one user.
    """
    if db.Conversation.find_one({"_id":ObjectId(conversation_id)}):
        print("Bien")
        cursor_message=db.NEWCHAT.find({"Group":conversation_id},{"_id":0,"Group":0,"by":0})
        mis_mensajes=list(cursor_message)
        print(mis_mensajes)
        print(len(mis_mensajes))
        if mis_mensajes :
            only_sentences=[sentence["Message"] for sentence in mis_mensajes]
            sia = SentimentIntensityAnalyzer()
            ss=[sia.polarity_scores(x) for x in only_sentences]
            return pd.DataFrame(ss).mean().to_json()
    raise Error404("Para estos parametros, no hay match! Prueba con otros.") 



@app.route("/user/<user_id>/recommend")
@errorHandler
def newfriend(user_id):
    """
    Funct returns a new friend similar to a user
    """
    if db.User.find_one({"_id":ObjectId(user_id)})!=None:
            by_id=[ str(x["_id"]) for x in list(db.User.find({},{"username":0}))]
            distances=createsimilars(by_id)
            return dumps(distances[user_id].sort_values(ascending=False)[1:3] )
    raise Error404("Parecce que estos user_id, no hay mensajes encontrados! Prueba con otros.") 