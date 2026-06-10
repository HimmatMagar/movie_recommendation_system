from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
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

movies = pickle.load(open("artifact/movies.pkl", "rb"))
similarity = pickle.load(open("artifact/similarity.pkl", "rb"))

def recommend(movie):
      matches = movies[movies['title'].str.lower() == movie.lower()]
      if matches.empty:
            return None
            
      movie_index = matches.index[0]
      distances = similarity[movie_index]
      movie_list = sorted(
            list(enumerate(distances)),
            reverse=True,
            key=lambda x: x[1]
      )[1:6]
      
      return [movies.iloc[i[0]].title for i in movie_list]
      
      

class MovieRequest(BaseModel):
    movie_name: str


@app.get("/")
def root():
      return {"message": "Movie Recommendation system API"}

@app.get("/health")
def check_health():
      return {"status": 'Ok'}

@app.post("/recommend")
def recommend_movie(request: MovieRequest):
      result = recommend(movie = request.movie_name)
      
      if result is None:
            raise HTTPException(
                  status_code=404,
                  detail="Movie not found"
            )
      
      return {
            "movie": request.movie_name,
            "recommendation": result
      }