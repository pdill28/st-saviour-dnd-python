
class Music:
    def __init__(self, title: str, artist: str, album: str, duration: float):
        self.title = title
        self.artist = artist
        self.album = album
        self.duration = duration  # duration in minutes

    def listen(self) -> str:
        return f"Listening to '{self.title}' by {self.artist} from the album '{self.album}'."