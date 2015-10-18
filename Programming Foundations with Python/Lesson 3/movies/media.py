import webbrowser

class Movie():
    """ This Class provides a way to store movie related information

    Recieves dictionary style information of a movie.

    Args:
        movie["title"]: The movie title
        movie["storyline"]: A short movie storyline summary (1-2 sentences)
        movie["poster_image_url"] A web address to the movie poster image
        movie["trailer_youtube_url"] A YouTube url to the movie trailer

    Returns:
        A dict mapping keys to the corresponding Args
    """
    VALID_RATINGS = ["G", "PG", "PG-13", "R"]

    def __init__(self, movie):
        self.title = movie["title"]
        self.storyline = movie["storyline"]
        self.poster_image_url = movie["poster_image_url"]
        self.trailer_youtube_url = movie["trailer_youtube_url"]

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
