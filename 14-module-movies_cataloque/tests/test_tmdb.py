import pytest
import requests
from flask import Flask, render_template, url_for, request
import tmdb_client
import app, types
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

#def test_homepage(monkeypatch):
   #api_mock = Mock(return_value={'results': []})
   #monkeypatch.setattr("tmdb_client.call_tmdb_api", api_mock)
   #with app.test_client() as client:
      #response = client.get('/')
      #api_mock.assert_called_once_with('movie/popular')

@pytest.mark.parametrize('list_type', (
   ('popular'),
   ('top_rated'),
   ('now_playing'),
   ('upcoming')
))

def test_homepage_list_types(monkeypatch, list_type):
    api_mock = Mock(return_value={'results': []})
    monkeypatch.setattr("tmdb_client.call_tmdb_api", api_mock)
    with app.test_client() as client:
      response = client.get('/')
      #(f"/?list_type={list_type}")
      assert response.status_code == 200
        #api_mock.assert_called_once_with('movie'/{list_type})
      api_mock.assert_called_once_with('movie/{list_type}')

#@pytest.mark.parametrize("list_type", types)
#def test_homepage_list_types(monkeypatch, list_type):
    #api_mock = Mock(return_value={'results': []})
    #monkeypatch.setattr("tmdb_client.call_tmdb_api", api_mock)
    #with app.test_client() as client:
        #response = client.get(f'/list_type={list_type}')
        #assert response.status_code == 200
        #api_mock.assert_called_once_with(f'movie/{list_type}')



