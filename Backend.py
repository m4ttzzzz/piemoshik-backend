# Backend.py
import vlc
from yt_dlp import YoutubeDL

class Backend:
    """
    The `Backend` class for **PieMoshik.**
    """
    
    def __init__(self):
        self.vlcinst = None
        self.vlcmedia = None
        self.initiated = False
        try:
            self.vlcinst = vlc.Instance()
            self.initiated = True
        except vlc.VLCException as e:
            raise Warning(f"VLC exception occured! {e}")

    def play_stream_url(self, url:str):
        """
        Plays a file *(preferably, audio)* from an **URL or a file path.**
        """
        if self.initiated:
            # Assuming libVLC initialized properly instead of shitting itself
            if not isinstance(url, str):
                raise ValueError(f"URL is expected to be str, but got {type(url).__name__}")
            
            media = self.vlcinst.media_new(url)

            if self.vlcmedia is None:
                self.vlcmedia = self.vlcinst.media_player_new()

            self.vlcmedia.set_media(media)
            self.vlcmedia.play()

            while True:
                if self.get_play_state() in (vlc.State.Error, vlc.State.Ended, vlc.State.Stopped):
                    self.vlcmedia.stop()
                    break
            self.vlcmedia.release()
            self.vlcmedia = None
        else:
            # If libVLC errored out instead of silently shitting itself
            raise RuntimeError("VLC instance not initialized!")
        
    def get_info(self, url:str):
        """
        Gets info from a YouTube URL (ex. `https://www.youtube.com/watch?v=jNQXAC9IVRw`).
        """
        # This implementation is not well tested.
        opts = {
            "format": "bestaudio",
            "skip_download": True
        }

        with YoutubeDL(opts) as ytdl:
            info = ytdl.extract_info(url)
        return info
        
    def get_play_state(self) -> vlc.State:
        """
        Basically get the *state* from `vlc.State`.
        """
        return self.vlcmedia.get_state()
    
    def pause(self) -> None:
        if self.initiated:
            self.vlcmedia.pause()


if __name__ == "__main__":
    print("This is a module: it is not meant to be run directly.")
    input("Press Enter to exit.")
