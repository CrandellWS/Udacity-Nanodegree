class Movie():
    def __init__(self, movie):
        self.title = movie["title"]
        self.storyline = movie["storyline"]
        self.poster_image_url = movie["poster_image_url"]
        self.trailer_youtube_url = movie["trailer_youtube_url"]



#### The Way it was shown
##
##
##class Movie():
##    def __init__(self, title_, storyline_, poster_image_url_, trailer_youtube_url_):
##        self.title = title_
##        self.storyline = storyline_
##        self.poster_image_url = poster_image_url_
##        self.trailer_youtube_url = trailer_youtube_url_
##
###### What I did is use dict() ie dictionary for reference
