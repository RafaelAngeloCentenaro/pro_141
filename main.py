from flask import Flask,jsonify,request
import pandas as pd
moviedata=pd.read_csv("movies.csv")
app=Flask(__name__)

all_movies=moviedata[["original_title","poster_link","release_date","run_time","weighted_rating"]]
liked_movies=[]
not_liked_movies=[]
did_not_watch=[]
def assign_val():
    m_data={
        "original_title":all_movies.iloc[0,0],
        "poster_link":all_movies.iloc[0,1],
        "release_date":all_movies.iloc[0,2] or "n/a",
        "duration":all_movies.iloc[0,3],
        "rating":all_movies.iloc[0,4]/2
    }
@app.route("/movies")
def get_movie():
    moviedata=assign_val()
    return jsonify({
        "data":moviedata,
        "status":"success"
    })
@app.route("/like")
def liked_movie():
    global all_movies
    moviedata=assign_val()
    liked_movies.append(moviedata)
    all_movies.drop([0],inplace=True)
    all_movies=all_movies.reset_index(drop=True)
    return jsonify({
        "status":"success"
    })
@app.route("/dislike")
def unlike_movie():
    global all_movies
    moviedata=assign_val()
    not_liked_movies.append(moviedata)
    all_movies.drop([0],inplace=True)
    all_movies=all_movies.reset_index(drop=True)
    return jsonify({
        "status":"success"
    })
@app.route("/did_not_watch")
def did_not_watch_view():
    global all_movies
    moviedata=assign_val()
    did_not_watch.append(moviedata)
    all_movies.drop([0],inplace=True)
    all_movies=all_movies.reset_index(drop=True)
    return jsonify({
        "status":"success"
    })
if __name__=="__main__":
    app.run()