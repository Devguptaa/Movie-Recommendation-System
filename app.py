import streamlit as st
import pandas as pd
import pickle
import requests
import numpy
movie_dict = pickle.load(open('movie_dict.pkl', 'rb'))
movies = pd.DataFrame(movie_dict)
similarity=pickle.load(open('similarity.pkl', 'rb'))
st.title('Movie Recommender System')

def fetch_poster(movie_id):
    response=requests.get("https://api.themoviedb.org/3/movie/{}?api_key=b01304f5e93e7a6a171089e7866c96c9".format(movie_id))
    data=response.json()
    poster_path = data['poster_path']
    return "https://image.tmdb.org/t/p/w500/" + poster_path



def recommend(movie):
    movie_index=movies[movies['title']==movie].index[0]
    distances=similarity[movie_index]
    recommended_movie_poster=[]
    recommended_movie=[]
    movies_list=sorted(list(enumerate(distances)),reverse=True,key=lambda x:x[1])[1:6]
    for i in movies_list:
        movie_id=movies.iloc[i[0]].movie_id
        recommended_movie.append(movies.iloc[i[0]].title)
        recommended_movie_poster.append(fetch_poster(movie_id))
    return recommended_movie,recommended_movie_poster


selected_movie_name= st.selectbox(
    'How would you like to be contacted?',
    movies['title'].values)
if st.button('Recommend'):
    names,posters=recommend(selected_movie_name)
    print(names,posters)
    print(type(posters))
    # col1, col2, col3, col4, col5 = st.beta_columns((1,2,3,4,5))
    col1, col2, col3, col4, col5 = st.beta_columns(5)

    with col1:
        # Add chart #1
        st.text(names[0])
        st.image(posters[0])
    with col2:
        st.text(names[1])
        st.image(posters[1])
    ...
    with col3:
        st.text(names[2])
        st.image(posters[2])
    with col4:
        st.text(names[3])
        st.image(posters[3])
    with col5:
        # Add chart #4
        st.text(names[4])
        st.image(posters[4])

# Add bottom chart
    # for i in recommendation:
    #     st.write(i)

