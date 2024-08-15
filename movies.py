import streamlit as st
import pickle
import pandas as pd

# Loading the movie dictionary and similarity matrix from the pickle files
movies_dict = pickle.load(open('movies_dict.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)
similarity = pickle.load(open('similarity.pkl', 'rb'))

# Defineing a function to recommend movies based on the input movie
def recommend(movie):
    # Geting the index of the movie that matches the title
    movie_index = movies[movies['title'] == movie].index[0]
    
    # Geting the list of similarity scores for that movie
    distances = similarity[movie_index]
    
    # Sorting the movies based on similarity scores in descending order and get the top 10
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:11]
    
    # Extracting the titles of the recommended movies
    recommended_movies = []
    for i in movies_list:
        recommended_movies.append(movies.iloc[i[0]].title)
    
    return recommended_movies

# Setting the title of the Streamlit app
st.title('Movie Recommender System')

# Creating a select box for the user to choose a movie from the list of titles
selected_movie_name = st.selectbox(
    'Select a movie to get recommendations:',
    movies['title'].values
)

# When the 'Recommend' button is clicked, displaying the recommended movies
if st.button('Recommend'):
    recommendations = recommend(selected_movie_name)
    for i in recommendations:
        st.write(i)
