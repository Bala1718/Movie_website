import fresh_tomatoes
import media


interstellar = media.Movie("Interstellar",
                           "Flim about space",
                           "http://www.imdb.com/title/tt0816692/mediaviewer/rm1728576256",
                           "https://www.youtube.com/watch?v=Lm8p5rlrSkY")

#print(interstellar.storyline)

avatar = media.Movie("Avatar",
                     "A Marine on the Planet",
                     "http://avatar.wikia.com/wiki/Category:Avatar_State_images?file=Aang_creates_an_air_pocket.png",
                     "https://www.youtube.com/watch?v=6ziBFh3V1aM")
avatar.show_trailer()
                           
movies = [interstellar,avatar]
fresh_tomatoes.open_movies_page(movies)
