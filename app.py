import pickle
import streamlit as st
import requests
import math

def fetch_poster(movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key=65c260ea9d577fa60ff54d40ccf54137&language=en-US"
    data = requests.get(url).json()
    poster_path = data.get('poster_path')
    if poster_path:
        return f"https://image.tmdb.org/t/p/w500{poster_path}"
    return None

def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    recommended_movies = []
    for i in distances[1:21]:  # Changed to get 20 recommendations
        movie_id = movies.iloc[i[0]].movie_id
        title = movies.iloc[i[0]].title
        poster = fetch_poster(movie_id)
        recommended_movies.append((title, poster))
    return recommended_movies

st.set_page_config(page_title="Movie Recommender System", layout="wide")
st.header('Movie Recommender System')

@st.cache_resource
def load_data():
    movies = pickle.load(open('movie_list.pkl', 'rb'))
    similarity = pickle.load(open('similarity.pkl', 'rb'))
    return movies, similarity

movies, similarity = load_data()

movie_list = movies['title'].values
selected_movie = st.selectbox(
    "Type or select a movie from the dropdown",
    movie_list
)

if st.button('Show Recommendation'):
    recommended_movies = recommend(selected_movie)
    
    # Calculate the number of rows needed (4 movies per row)
    num_rows = math.ceil(len(recommended_movies) / 4)
    
    for row in range(num_rows):
        cols = st.columns(4)
        for col in range(4):
            idx = row * 4 + col
            if idx < len(recommended_movies):
                title, poster = recommended_movies[idx]
                with cols[col]:
                    st.subheader(title)
                    if poster:
                        st.image(poster)
                    else:
                        st.write("No poster available")
                    st.write("---")  # Add a separator between movies

