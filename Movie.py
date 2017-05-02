from Video import Video


class Movie(Video):
    """
    The Movie class is used to generate the data structure for a Movie.
    Example: 
        Movie(
            'Rocky',
            '2h 2m',
            'A down on his luck low-level boxer fights the champion for the title',
            'https://youtu.be/3VUblDwa648',
            'http://imagecache5d.allposters.com/watermarker/56-5698-2SSUG00Z.jpg',
            'movie'
        )
    """
    def __init__(self, title, duration, description, video_url=None, movie_poster=None):
        """
        Args: 
            title (str): The title for the movie
            duration (str): The total duration of the movie (hr, min)
            description (str): The description for the movie
            video_url (str, optional): An optional video url that can be clicked to open.
                Defaults to None.
       """
        super(Movie, self).__init__(title, duration, description, video_url, 'movie')
        if bool(movie_poster):
            self.moviePoster = movie_poster
            self.poster_image_url = movie_poster
