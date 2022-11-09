from app import app
from flask import make_response
import time
import os
import datetime
from recommendation_model import model_process
from functools import lru_cache

#This route serves the user recommendations
@app.route("/recommend/<userid>")
@lru_cache
def recommend(userid):
    myList=list(model_process.gettop20movies(userid, app.algo, app.df_new))
    moviesID=[]
    for x in myList:
        for k in x['Movie']:
            raw_string = x['Movie'][k]
            moviesID.append(raw_string.split('/rate/')[1].split('=')[0])
    print(moviesID)
    response = make_response(",".join(moviesID), 200)
    response.mimetype = "text/plain"
    return response


@app.errorhandler(404)
def error(error):
    return "This page does not exist :("