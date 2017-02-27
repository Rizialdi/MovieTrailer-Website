# define a class for our each instance of a Movie object
class Movie():
    # the constructor for each instance of our object

    def __init__(self, title, poster_image_url, trailer_youtube_id):
        self.title = title
        self.poster_image_url = poster_image_url
        self.trailer_youtube_url = trailer_youtube_id

