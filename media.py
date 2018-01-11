import webbrowser


class Movie():
    
    """ This class provides a way to store movie information 
    Attributes:
        - movie_title(str):     Title of the Movie
        - movie_storyline(str): Main Theme of the Movie
        - poster_image(str):      Url of the video poster image
        - trailer:   Url of the youtube trailer 
    """
    
    # "self" is the object or instance being created
    def __init__(self, 
                 movie_title, 
                 movie_storyline, 
                 poster_image, trailer):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer
    # instance method
    
    def show_trailer(self):
        """ Open the user's web browser for show the youtube movie trailer """
        webbrowser.open(self.trailer_youtube_url)
