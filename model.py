import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity


class MovieRecommender:
    def __init__(self):
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

        self.df = pd.DataFrame(data)

        # ----------------------------
        # Vectorization
        # ----------------------------
        self.cv = CountVectorizer()
        self.count_matrix = self.cv.fit_transform(self.df['genres'])

        # ----------------------------
        # Similarity Matrix
        # ----------------------------
        self.similarity = cosine_similarity(self.count_matrix)

    # ----------------------------
    # Get all movie names
    # ----------------------------
    def get_movies(self):
        return self.df['movie_title'].values

    # ----------------------------
    # Recommendation Function
    # ----------------------------
    def recommend(self, movie, n=5):
        movie_index = self.df[self.df['movie_title'] == movie].index[0]
        distances = self.similarity[movie_index]
        movie_list = sorted(
            list(enumerate(distances)),
            reverse=True,
            key=lambda x: x[1]
        )

        recommended_movies = []
        for i in movie_list[1:n+1]:
            recommended_movies.append(self.df.iloc[i[0]].movie_title)

        return recommended_movies