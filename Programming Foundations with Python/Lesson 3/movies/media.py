import webbrowser

class Video():
    """ This Class provides a way to store Video related information

    Recieves dictionary style information of a Video.

    Args:
    video["title"]: The video title
    video["duration"]: The video play time

    Returns:
    A dict mapping keys to the corresponding Args
    """
    def __init__(self, video):
        """ Create a video object"""
        self.title = video["title"]
        self.duration = video["duration"]

class Movie(Video):
    """ This Class provides a way to store movie related information

    Recieves dictionary style information of a movie.

    Args:
        video["title"]: The video title
        video["duration"]: The video play time
        movie["storyline"]: A short movie storyline summary (1-2 sentences)
        movie["poster_image_url"] A web address to the movie poster image
        movie["trailer_youtube_url"] A YouTube url to the movie trailer

    Returns:
        A dict mapping keys to the corresponding Args
    """
    VALID_RATINGS = ["G", "PG", "PG-13", "R"]

    def __init__(self, movie):
        """ Create a movie object"""
        # self.title = movie["title"]
        # self.duration = movie["duration"]
        Video.__init__(self, movie)
        self.storyline = movie["storyline"]
        self.poster_image_url = movie["poster_image_url"]
        self.trailer_youtube_url = movie["trailer_youtube_url"]

    def show_trailer(self):
        """ open a youtube based trailer """
        webbrowser.open(self.trailer_youtube_url)


class TvShow(Video):
    """ This Class provides a way to store movie related information

    Recieves dictionary style information of a tvshow.

    Args:
        video["title"]: The video title
        video["duration"]: The video play time
        tvshow["season"]: The tvshow season number
        tvshow["episode"]: The tvshow episode number
        tvshow["tv_station"]: The tv_station name
        tvshow["storyline"]: A short tvshow storyline summary (1-2 sentences)

    Returns:
        A dict mapping keys to the corresponding Args
    """
    def __init__(self, video, tvshow):
        """ Create a tvshow object"""
        self.title = video["title"]
        self.duration = video["duration"]
        self.season = tvshow["season"]
        self.episode = tvshow["episode"]
        self.tv_station = tvshow["tv_station"]

    def get_local_listing():
        """ Create a tvshow object"""
