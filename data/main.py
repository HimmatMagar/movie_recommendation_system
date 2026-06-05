import urllib.request as request

def download_data():
      filename, header = request.urlretrieve(
            url="https://github.com/master-temp/movie-rec/raw/refs/heads/main/movies_metadata.csv",
            filename="movies.csv"
      )

download_data()