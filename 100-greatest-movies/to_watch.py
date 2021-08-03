with open("movies.txt", "r") as file:
    movies = file.readlines()

movies_to_watch = []
for movie in movies:
    seen = input(f"Have you seen {movie.strip()}? Type 'y' or 'n': ")
    if seen == 'n':
        movies_to_watch.append(movie.strip())

with open("movies_to_watch.txt", "w") as file:
    for movie in movies_to_watch:
        file.write(f"{movie}\n")