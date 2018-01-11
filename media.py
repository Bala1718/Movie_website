import webbrowser


class Movie():
    """ This class provides a way to store movie information """
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
        webbrowser.open(self.trailer_youtube_url)
