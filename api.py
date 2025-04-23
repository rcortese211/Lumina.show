class LuminaShowAPI:
    def __init__(self):
        self.tracks = []
        self.layouts = {}
        self.media_url = None

    def add_track(self, track_data):
        """Add a new track to the timeline."""
        self.tracks.append(track_data)

    def get_tracks(self):
        """Retrieve all timeline tracks."""
        return self.tracks

    def create_layout(self, layout_name, grid):
        """Create a new layout."""
        self.layouts[layout_name] = grid

    def get_layouts(self):
        """Retrieve all layouts."""
        return self.layouts

    def play_media(self, media_url):
        """Play media via Chromecast."""
        self.media_url = media_url
        # Implement casting logic using pychromecast or similar library
