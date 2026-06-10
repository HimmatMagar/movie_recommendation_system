from fastapi import FastAPI, HTTPException
import pandas as pd
import pickle
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI(title='Movie Recommendation API')

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

movies = pickle.load(open("api/movies.pkl", "rb"))
similarity = pickle.load(open("api/similarity.pkl", "rb"))

def recommend(movie):
      movie_index = movies[movies['title'] == movie].index[0]
      
      distances = similarity[movie_index]
      movie_list = sorted(
            list(enumerate(distances)),
            reverse=True,
            key=lambda x: x[1]
      )[1:6]
      
      for i in movie_list:
            return movies.iloc[i[0]].title
      

@app.get("/")
def root():
      return {"message": "Movie Recommendation system API"}

@app.get("/health")
def check_health():
      return {"status": 'Ok'}

@app.get("/recommend/{movie_name}")
def recommend_movie(movie_name: str):
      result = recommend(movie = movie_name)
      
      if result is None:
            raise HTTPException(
                  status_code=404,
                  detail="Movie not found"
            )
      
      return {
            "movie": movie_name,
            "recommendation": result
      }