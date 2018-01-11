import media
import fresh_tomatoes


# interstellar movie : movie title,storyline,poster image,movie trailer

interstellar = media.Movie("Interstellar",
                           "Flim about space",
                           "https://goo.gl/4viv4x",
                           "https://www.youtube.com/watch?v=Lm8p5rlrSkY")

# avatar movie : movie title,story line, poster image,movie trailer

avatar = media.Movie("Avatar",
                     "A Marine on the Planet",
                     "https://goo.gl/myzkaU",
                     "https://www.youtube.com/watch?v=6ziBFh3V1aM")

# internship movie : movie title,story line,poster image,movie title

internship = media.Movie("The Internship",
                         "Internship at Google",
                         "https://goo.gl/CUWEh5",
                         "https://www.youtube.com/watch?v=cdnoqCViqUo")                        
movies = [interstellar, avatar, internship]
fresh_tomatoes.open_movies_page(movies)
print (media.Movie.__doc__)
