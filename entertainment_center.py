import fresh_tomatoes
import media


interstellar = media.Movie("Interstellar",
                           "Flim about space",
                          "https://upload.wikimedia.org/wikipedia/en/b/bc/Interstellar_film_poster.jpg",
                           "https://www.youtube.com/watch?v=Lm8p5rlrSkY")

#print(interstellar.storyline)

avatar = media.Movie("Avatar",
                     "A Marine on the Planet",
                     "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
                     "https://www.youtube.com/watch?v=6ziBFh3V1aM")
avatar.show_trailer()

#print(avatar.storyline)
                           
movies = [interstellar,avatar]
fresh_tomatoes.open_movies_page(movies)
