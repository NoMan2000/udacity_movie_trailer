import webbrowser


class Video(object):
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

