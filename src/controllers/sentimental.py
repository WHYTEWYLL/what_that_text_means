from src.app import app
from src.our_db import *
from bson.objectid import ObjectId
from bson.json_util import dumps
import pandas as pd
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from src.controllers.sima  import *
nltk.download("vader_lexicon")


@app.route("/chat/<conversation_id>/sentiment")
def howufeel(conversation_id):
    if db.Conversation.find_one({"_id":ObjectId(conversation_id)}) :
        cursor_message=db.NEWCHAT.find({"Group":conversation_id},{"_id":0,"Group":0,"by":0})
        only_sentences=[sentence["Message"] for sentence in cursor_message]
        sia = SentimentIntensityAnalyzer()
        ss=[sia.polarity_scores(x) for x in only_sentences]
        return pd.DataFrame(ss).mean().to_json()


@app.route("/user/<user_id>/recommend")
def newfriend(user_id):
    if db.User.find_one({"_id":ObjectId(user_id)}):
            by_id=[ str(x["_id"]) for x in list(db.User.find({},{"username":0}))]
            distances=createsimilars(by_id)
            return dumps(distances[user_id].sort_values(ascending=False)[1:3] )
    return "Este usuario no existe, prueba con otro."