import streamlit as st
import pickle
import pandas as pd
import numpy as np
import requests


def fetch_poster(movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key=07f211e99d167974df097a5666350356&language=en-US"
    response = requests.get(url)
    data = response.json()

    poster_path = data.get('poster_path')
    return "https://image.tmdb.org/t/p/w500" + poster_path if poster_path else None

def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies = []
    recommended_movies_posters = []
    for i in movies_list:
        movies_id = movies.iloc[i[0]].movie_id

        recommended_movies.append(movies.iloc[i[0]].title)
        #fetch poster from api
        recommended_movies_posters.append(fetch_poster(movies_id))

    return recommended_movies ,recommended_movies_posters


movies_dict = pickle.load(open('movies_dict.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)


import gzip
import pickle

with gzip.open("similarity.gz", "rb") as file:
    similarity = pickle.load(file)



st.title('Movie Recommender System')

selected_movies_name = st.selectbox(
    'Select a movie to get recommendations:',
    movies['title'].values
)

if st.button('Recommend'):
    names,posters = recommend(selected_movies_name)

    # Old code (deprecated)
    # col1, col2, col3 = st.beta_columns(5)

    # Fixed code
    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        st.header(names[0])
        st.image(posters[0])
    with col2:
        st.header(names[1])
        st.image(posters[1])
    with col3:
        st.header(names[2])
        st.image(posters[2])
    with col4:
        st.header(names[3])
        st.image(posters[3])
    with col5:
        st.header(names[4])
        st.image(posters[4])


