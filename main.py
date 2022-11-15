class Song:
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


class Album:
    """ Class to represent an album, using its track title

    Attributes:
        album_name (str): The name of the album.
        year (init): The year was album released.
        artist (artist): The artist responsible for the album. if not specified,
        the artist will default to an artist with the name "various artists".
        tracks (list[song]): A list of the songs on the album.

    Methods:
        add_song: used to add a new song to the album's track list."""

    def __init__(self, name, year, artist=None):
        self.name = name
        self.year = year
        if artist is None:
            self.artist = Artist("Various Artist")
        else:
            self.artist = artist

        self.tracks = []

    def add_song(self, song, position=None):
        """ Adds a song to the track list

        Args:
            song(song): a song to add
            position (optional): if specified, the song will be added to that position
            in the track list - inserting it between other songs if necessary.
            otherwise, the song will be added to the end of the list.
        """
        if position is None:
            self.tracks.append(song)
        else:
            self.tracks.insert(position, song)


