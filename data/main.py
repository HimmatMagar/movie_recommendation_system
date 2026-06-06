import urllib.request as request


class DownloadData:
      
      def __init__(self):
            self.url = "https://github.com/master-temp/movie-rec/raw/refs/heads/main/movies_metadata.csv"
      
      
      def download_data(self):
            filename, header = request.urlretrieve(
                  url = self.url,
                  filename = "movies_data.csv"
            )

            print(f"{filename} downloaded with following info: \n{header}")


if __name__ == "__main__":
      data = DownloadData()
      data.download_data()