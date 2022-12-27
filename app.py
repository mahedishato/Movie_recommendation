import streamlit as st
import pandas as pd
import pickle
import requests


def poster(movie_id):
    respons= requests.get("https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US".format(movie_id))
    data= respons.json()
    poster_path = data['poster_path']
    full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
    return full_path

def recommend(movie):
    movie_index =movies[movies['title']== movie].index[0]
    distence= similarity[movie_index]
    movie_list = sorted(list(enumerate(distence)), reverse=True, key=lambda x:x[1])[1:6]
    
    recommended_movie= []
    recommended_movie_poster_path = []
    for i in movie_list:
        movie_id= movies.iloc[i[0]].id	
        recommended_movie.append(movies.iloc[i[0]].title)
        recommended_movie_poster_path.append(movie_id)
       # print(i[0])
    return recommended_movie, recommended_movie_poster_path


 



movie_list = pickle.load(open('tmdb_5000_movies.csv\movie.pkl', 'rb'))

movies= pd.DataFrame(movie_list)


similarity=pickle.load(open('tmdb_5000_movies.csv\similarity.pkl','rb'))

st.title('Movie Recommender System')


option= st.selectbox('WHAT DO YOU WANT', movies['title'])


if st.button('Recommend'):
    recommended_movie, recommended_movie_poster_path = recommend(option)
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(recommended_movie[0])
        st.image(recommended_movie_poster_path[0])
    with col2:
        st.text(recommended_movie[1])
        st.image(recommended_movie_poster_path[1])

    with col3:
        st.text(recommended_movie[2])
        st.image(recommended_movie_poster_path[2])
    with col4:
        st.text(recommended_movie[3])
        st.image(recommended_movie_poster_path[3])
    with col5:
        st.text(recommended_movie[4])
        st.image(recommended_movie_poster_path[4])