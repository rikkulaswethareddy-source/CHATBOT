import streamlit as st
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# ----------------------------
# Sample Movie Dataset
# ----------------------------
data = {
    'movie_title': [
        'Inception', 'Interstellar', 'The Dark Knight',
        'Avengers', 'Iron Man', 'Thor',
        'Titanic', 'The Notebook', 'La La Land',
        'Joker', 'Batman Begins', 'Doctor Strange'
    ],
    'genres': [
        'Sci-Fi Thriller', 'Sci-Fi Drama', 'Action Crime',
        'Action Superhero', 'Action Superhero', 'Action Fantasy',
        'Romance Drama', 'Romance Drama', 'Romance Musical',
        'Crime Drama', 'Action Crime', 'Fantasy Superhero'
    ]
}

df = pd.DataFrame(data)

# ----------------------------
# Vectorization and Similarity
# ----------------------------
cv = CountVectorizer()
count_matrix = cv.fit_transform(df['genres'])
similarity = cosine_similarity(count_matrix)

# ----------------------------
# Recommendation Function
# ----------------------------
def recommend(movie):
    movie_index = df[df['movie_title'] == movie].index[0]
    distances = similarity[movie_index]
    movie_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])

    recommended_movies = []
    for i in movie_list[1:6]:
        recommended_movies.append(df.iloc[i[0]].movie_title)
    return recommended_movies

# ----------------------------
# Streamlit UI
# ----------------------------
st.title("🎬 Movie Recommendation System")

selected_movie = st.selectbox(
    "Select a movie you like:",
    df['movie_title'].values
)

if st.button("Recommend"):
    recommendations = recommend(selected_movie)
    st.write("### Recommended Movies:")
    for movie in recommendations:
        st.write(movie)