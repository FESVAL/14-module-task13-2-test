import requests

API_TOKEN = "eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJjNTQ1ZjMwMTBmMjEwM2RiYTY0ZjMwMGYxNGQ4MmE4ZSIsInN1YiI6IjYzZmEyMjc1MzQ0YThlMDA4ZWM1NGY3OCIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.Ma0KfWmd04R2hKopfjxY4sg9x44rPcT77BJ7Tw0BI8I"

def get_popular_movies():
    endpoint = "https://api.themoviedb.org/3/movie/popular"
    headers = {
        "Authorization": f"Bearer {API_TOKEN}"
    }
    response = requests.get(endpoint, headers=headers)
    #print (response)
    return response.json()

def get_poster_url(poster_api_path, size="w342"):
    base_url = "https://image.tmdb.org/t/p/"
    return f"{base_url}{size}/{poster_api_path}"

def call_tmdb_api(endpoint):
   full_url = f"https://api.themoviedb.org/3/{endpoint}"
   headers = {
       "Authorization": f"Bearer {API_TOKEN}"
   }
   response = requests.get(full_url, headers=headers)
   response.raise_for_status()
   return response.json()

def get_movies_list(list_type):
   return call_tmdb_api(f"movie/{list_type}")

def get_single_movie(movie_id):
    return call_tmdb_api(f"movie/{movie_id}")

def get_single_movie_cast(movie_id):
    return call_tmdb_api(f"movie/{movie_id}/credits")

def get_movie_images(movie_id):
    return call_tmdb_api(f"movie/{movie_id}/images")

   