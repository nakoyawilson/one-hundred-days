with open("movies_to_watch.txt", "r") as file:
    movies = file.readlines()

remove_movies = True
while remove_movies:
    remove_a_movie = input("Would you like to remove a movie from the to watch list? Type 'y' or 'n': ")
    if remove_a_movie == "y":
        movie = input("Which movie would you like to remove? ").title()
        for movie_title in movies:
            if movie in movie_title:
                movies.remove(movie_title)
    else:
        remove_movies = False

with open("movies_to_watch.txt", "w") as file:
    for movie in movies:
        file.write(f"{movie}")