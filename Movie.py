from Video import Video


class Movie(Video):
    def __init__(self, title, duration, description, video_url=None, movie_poster=None):
        super().__init__(title, duration, description, video_url, 'movie')
        if bool(movie_poster):
            self.moviePoster = movie_poster
            self.poster_image_url = movie_poster
