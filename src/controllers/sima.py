import pandas as pd
import nltk
from src.our_db import *
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from scipy.spatial.distance import pdist, squareform





def quemelohagauna(id):
        cursor_message=db.NEWCHAT.find({"by":id},{"_id":0,"Group":0,"by":0})
        only_sentences=[sentence["Message"] for sentence in cursor_message]
        sia = SentimentIntensityAnalyzer()
        ss=[sia.polarity_scores(x) for x in only_sentences]
        return pd.DataFrame(ss).mean()

def createsimilars(by_id):
    
    trya={tio:quemelohagauna(tio) for tio in by_id}
    trya=pd.DataFrame(trya)
    distances = pd.DataFrame(1/(1 + squareform(pdist(trya.T, 'euclidean'))), 
                         index=trya.columns, columns=trya.columns)
    return distances