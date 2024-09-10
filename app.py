import pandas as pd
import streamlit as st
import pickle
from tmdbv3api import TMDb, Movie

tmdb = TMDb()
tmdb.api_key = 'bf49392cc5a7db79873193791c6c5701'

def fetch_poster(movie_title):
    movie = Movie()
    search = movie.search(movie_title)
    if search:
        poster_path = search[0].poster_path
        return f"https://image.tmdb.org/t/p/w500{poster_path}"
    return None

def recommend(movie):
    movie_lower = movie.strip().lower()
    movies['orig_title_lower'] = movies['orig_title'].str.strip().str.lower()

    if movie_lower not in movies['orig_title_lower'].values:
        st.write(f"Movie '{movie}' not found in the DataFrame.")
        return []

    movie_idx = movies[movies['orig_title_lower'] == movie_lower].index[0]
    movies_list = sorted(list(enumerate(similarity[movie_idx])), reverse=True, key=lambda x: x[1])[1:11]

    recommended_movies = []
    recommended_posters = []
    for i in movies_list:
        recommended_movies.append(movies.iloc[i[0]]['orig_title'])  # Use original title case
        poster_url = fetch_poster(movies.iloc[i[0]]['orig_title'])
        recommended_posters.append(poster_url)

    return recommended_movies, recommended_posters

try:
    movies = pickle.load(open('movies.pkl', 'rb'))
    similarity = pickle.load(open('similarity.pkl', 'rb'))
    movies = pd.DataFrame(movies)
except Exception as e:
    st.write("Error loading data: ", e)

if 'orig_title' not in movies.columns:
    st.write("Error: 'orig_title' column not found in the dataset.")
else:
    st.title("Movie Recommendation System")
    option = st.selectbox('Choose a movie for recommendations:', movies['orig_title'])
    st.write(f"You selected: {option}")

    if st.button('Recommend'):
        recommendations, posters = recommend(option)
        if recommendations:
            st.write(f"Top 10 movie recommendations:")

            cols1 = st.columns(5)
            for idx, (movie, poster) in enumerate(zip(recommendations[:5], posters[:5])):
                with cols1[idx]:
                    if poster:
                        st.markdown(f"""
                        <div style="text-align: center;">
                            <img src="{poster}" width="150" style="display: block; margin: 0 auto;"/>
                            <div style="margin-top: 10px; font-weight: bold;">{movie}</div>
                        </div>
                        """, unsafe_allow_html=True)

            cols2 = st.columns(5)
            for idx, (movie, poster) in enumerate(zip(recommendations[5:], posters[5:])):
                with cols2[idx]:
                    if poster:
                        st.markdown(f"""
                        <div style="text-align: center;">
                            <img src="{poster}" width="150" style="display: block; margin: 0 auto;"/>
                            <div style="margin-top: 10px; font-weight: bold;">{movie}</div>
                        </div>
                        """, unsafe_allow_html=True)
        else:
            st.write("No recommendations available for the selected movie.")
