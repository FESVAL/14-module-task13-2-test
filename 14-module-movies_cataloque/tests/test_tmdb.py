import requests
from flask import Flask, render_template, url_for, request
import tmdb_client
from unittest.mock import Mock

def test_get_poster_url_uses_default_size():
   # Підготовка даних
   poster_api_path = "some-poster-path"
   expected_default_size = 'w342'
   # Виклик коду, який ми тестуємо
   poster_url = tmdb_client.get_poster_url(poster_api_path=poster_api_path)
   # Порівняння результатів
   assert expected_default_size in poster_url
   assert poster_url == "https://image.tmdb.org/t/p/w342/some-poster-path"

def test_get_movies_list(monkeypatch):
   # Список, який поверне прихований "запит до API".
   mock_movies_list = ['Movie 1', 'Movie 2']

   requests_mock = Mock()
   # Результат запиту до API
   response = requests_mock.return_value
   # Ми перевизначаємо результат виклику методу json().
   response.json.return_value = mock_movies_list
   monkeypatch.setattr("tmdb_client.requests.get", requests_mock)

   movies_list = tmdb_client.get_movies_list(list_type="popular")
   assert movies_list == mock_movies_list


def test_get_single_movie(monkeypatch):
   mock_single_movie = ['Movie']
   requests_mock = Mock()
   response = requests_mock.return_value
   response.json.return_value = mock_single_movie
   monkeypatch.setattr("tmdb_client.requests.get", requests_mock)
   single_movie = tmdb_client.get_single_movie(movie_id="")
   assert single_movie == mock_single_movie


def test_get_single_movie_cast(monkeypatch):
   mock_single_movie_cast = ['Actor1', 'Actor2']
   requests_mock = Mock()
   response = requests_mock.return_value
   response.json.return_value = mock_single_movie_cast
   monkeypatch.setattr("tmdb_client.requests.get", requests_mock)
   single_movie_cast = tmdb_client.get_single_movie(movie_id="")
   assert single_movie_cast == mock_single_movie_cast

def test_get_movie_images(monkeypatch):
   mock_movie_images = ['image1', 'image2']
   requests_mock = Mock()
   response = requests_mock.return_value
   response.json.return_value = mock_movie_images
   monkeypatch.setattr("tmdb_client.requests.get", requests_mock)
   movie_images = tmdb_client.get_movie_images(movie_id="")
   assert movie_images == mock_movie_images








#допоміжний матеріал - підказки, видалити!
#def test_get_movies_list_type_popular():
   #movies_list = tmdb_client.get_movies_list(list_type="popular")
   #assert movies_list is not None

#def some_function_to_mock():
   #raise Exception("Original was called")

#def test_mocking(monkeypatch):
   #my_mock = Mock()
   #my_mock.return_value = 2
   #monkeypatch.setattr("tests.test_tmdb.some_function_to_mock", my_mock)
   #result = some_function_to_mock()
   #assert result == 2


#def test_get_single_movie_url():
   # Підготовка даних
   #endpoint = "https://api.themoviedb.org/3/movie/{movie_id}"
   # Виклик коду, який ми тестуємо
   #single_movie_url=tmdb_client.get_single_movie(endpoint=endpoint)
   # Порівняння результатів
   #assert single_movie_url == 