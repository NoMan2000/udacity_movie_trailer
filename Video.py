import webbrowser


class Video(object):
    """
    The Video class is used to generate the data structure for a Video.
    Example: 
        Video(
            'Rocky',
            '2h 2m',
            'A down on his luck low-level boxer fights the champion for the title',
            'https://youtu.be/3VUblDwa648',
            'http://imagecache5d.allposters.com/watermarker/56-5698-2SSUG00Z.jpg',
            'movie'
        )
    """
    video_types = [
        None,
        'commercial',
        'amateur',
        'videoblog',
        'movie',
        'tv_show'
    ]

    def __init__(
            self,
            title,
            duration,
            description,
            video_url=None,
            video_type=None
    ):
        """
        Args: 
            title (str): The title for the movie
            duration (str): The total duration of the movie (hr, min)
            description (str): The description for the movie
            video_url (str, optional): An optional video url that can be clicked to open.
                Defaults to None.
            video_type (str, optional): An optional video_type specification.  Defaults to None.
            
        Raises:
            Exception: If a video type is not in the list
       """
        self.title = str(title)
        self.duration = str(duration)
        self.description = str(description)
        self.trailer_youtube_url = str(video_url)
        if video_type in self.video_types:
            self.videoType = video_type
        else:
            raise Exception(str(video_type) + " is not a valid videoType")

    def open_video_url(self):
        if bool(self.trailer_youtube_url):
            return webbrowser.open(self.trailer_youtube_url)

    # Call before initializing the parent/super if a custom video type is needed
    def add_video_type(self, video_type):
        if bool(video_type):
            self.video_types.append(video_type)
