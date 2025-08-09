# Backend.py
import vlc

class Backend:
    """
    The `Backend` class for **Catomshik:New.**
    """
    
    def __init__(self):
        self.vlcinst = None
        self.vlcmedia = None
        self.initiated = False
        try:
            self.vlcinst = vlc.Instance()
            self.initiated = True
        except vlc.VLCException as e:
            raise e

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

        else:
            # If libVLC errored out instead of silently shitting itself
            raise RuntimeError("VLC instance not initialized!")
        
    def get_info(self, url:str):
        """
        Gets info from a YouTube URL (ex. `https://www.youtube.com/watch?v=jNQXAC9IVRw`).
        *This function is not implemented yet (Sorry). But contributions for this function are welcome!*
        """
        raise NotImplementedError("getInfo() method not implemented yet, sorz :(")
    
    def get_play_state(self) -> vlc.State:
        """
        Basically get the *state* from `vlc.State`.
        """
        return self.vlcmedia.get_state()


if __name__ == "__main__":
    print("This is a module: it is not meant to be run directly.")
    input("Press Enter to exit.")