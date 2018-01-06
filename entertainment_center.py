import media
import fresh_tomatoes

#interstellar movie : movie title,storyline,poster image,movie trailer
interstellar = media.Movie("Interstellar",
                           "Flim about space",
                           "https://upload.wikimedia.org/wikipedia/en/b/bc/Interstellar_film_poster.jpg",
                           "https://www.youtube.com/watch?v=Lm8p5rlrSkY")
#avatar movie : movie title,story line, poster image,movie trailer

avatar = media.Movie("Avatar",
                     "A Marine on the Planet",
                     "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
                     "https://www.youtube.com/watch?v=6ziBFh3V1aM")

#internship movie : movie title,story line,poster image,movie title

internship = media.Movie("The Internship",
                             "Internship at Google",
                             "https://upload.wikimedia.org/wikipedia/en/e/ed/The-internship-poster.jpg",
                             "https://www.youtube.com/watch?v=cdnoqCViqUo")


                           
movies = [interstellar,avatar,internship]
fresh_tomatoes.open_movies_page(movies)
print (media.Movie.__doc__)
