import streamlit as st
import pickle
import pandas as pd
import requests

# Function to get base64 representation of a binary file

def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies = []
    for i in movies_list:
        recommended_movies.append(movies.iloc[i[0]].title)
    return recommended_movies


movies_dict = pickle.load(open('movies_dict.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)

similarity = pickle.load(open('similarity.pkl', 'rb'))
# Add custom CSS styles for the title
st.markdown(
    """
    <style>
        .title-text {
            font-size: 48px;
            font-weight: bold;
            text-align: center;
            color: #FF5733; /* Change the color code here */
            text-shadow: 2px 2px 4px #000000;
            margin-bottom: 30px;
        }
        
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown('<h1 class="title-text">Movie Recommender System</h1>', unsafe_allow_html=True)

#st.title('Movie Recommender System')#

selected_movie_name = st.selectbox(
'Life is short, watch more movies',
movies['title'].values)

if st.button('Recommend'):
    recommendations = recommend(selected_movie_name)
    # Create a centered column layout for posters
    columns = st.columns(5)

    for i, col in zip(recommendations, columns):
        # Fetch movie details from TMDb API
        response = requests.get(f'https://api.themoviedb.org/3/search/movie',
                                params={'api_key': 'ac4c16c1748cea6bb2bb8aed42fde5a2', 'query': i})
        if response.status_code == 200:
            data = response.json()
            if data['results']:
                # Get the poster path and movie title from the API response
                poster_path = data['results'][0]['poster_path']
                movie_title = data['results'][0]['original_title']
                if poster_path:
                    # Construct the medium-sized poster URL
                    poster_url = f'https://image.tmdb.org/t/p/w342{poster_path}'
                    # Use CSS to center the poster image and display the movie title
                    col.markdown(
                        f'<p style="text-align:center;"><img src="{poster_url}" alt="{i}" width="200"/><br>{movie_title}</p>',
                        unsafe_allow_html=True)


