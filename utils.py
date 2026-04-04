import pandas as pd


def load_sample_data():
    """
    Returns the sample movie dataset as a DataFrame.
    You can later replace this with CSV loading.
    """
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
    return pd.DataFrame(data)


def clean_text(text):
    """
    Basic text cleaning for genres/features.
    """
    return str(text).lower().strip()


def validate_movie(df, movie_name):
    """
    Checks whether the selected movie exists in dataset.
    """
    return movie_name in df['movie_title'].values