from pychromecast import Chromecast
from pychromecast.controllers.media import MediaController

class LuminaShowAPI:
    def __init__(self):
        self.tracks = []
        self.layouts = {}
        self.chromecast = None

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

    def connect_chromecast(self, device_name):
        """Connect to a Chromecast device."""
        self.chromecast = Chromecast(device_name)
        self.chromecast.wait()

    def play_media(self, media_url):
        """Play media via Chromecast."""
        if self.chromecast:
            controller = MediaController()
            self.chromecast.register_handler(controller)
            controller.play_media(media_url, content_type="video/mp4")
            controller.block_until_active()
