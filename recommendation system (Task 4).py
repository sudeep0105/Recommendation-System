
movies = {
    "The Dark Knight, Shanfg-Chi": {"genre": "action", "director": "Christopher Nolan"},
    "Inception": {"genre": "sci-fi", "director": "Christopher Nolan"},
    "The Shawshank Redemption": {"genre": "Drama", "director": "Frank Darabont"},
    "The Avengers": {"genre": "action", "director": "Joss Whedon"},
    "Interstellar": {"genre": "sci-fi", "director": "Christopher Nolan"},
    "Pulp Fiction": {"genre": "crime", "director": "Quentin Tarantino"},
    "The Lion King": {"genre": "animation", "director": "Roger Allers"}
}

preferred_genre = input("\nWhat genre of movie are you looking for? ")

recommended_movie = None
for movie, attributes in movies.items():
    if attributes["genre"] == preferred_genre:
        recommended_movie = movie
        break

if recommended_movie:
    print("\nI recommend to watch", recommended_movie)
else:
    print("I'm sorry, I couldn't find a movie in that genre.")
