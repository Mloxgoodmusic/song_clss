class song:
    """class to represent a song"""
    '''attribute:
            title (str): the tittle of the song
            artist (artist): an artist object representing the songs creator
            duration (int): the duration of the song in seconds. may be zero
            '''

    def __init__(self, title, artist, duration=0):
        """ song init method

        args:
             title (str): initialise the 'title' attribute
             artist(artist): an artist object representing the song creator
             duration (optional): initial value for the 'duration' attribute.
            will default to zero if not specified.
        """
        self.title = title
        self.artist = artist
        self.duration = duration

