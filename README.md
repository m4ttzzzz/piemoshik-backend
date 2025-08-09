# piemoshik-backend
The backend module for the upcoming PieMoshik program.

----
**DEVELOPMENT IS NOT DONE YET, SOME OF THE METHODS ARE NOT IMPLEMENTED YET AND WILL RAISE AN ERROR!!**

`piemoshik-backend` is the backend for PieMoshik, serving as the handler for VLC.

# Dependencies:
- `python-vlc`

```
pip install python-vlc
```

- An installation of VLC

----

# How To Use
To use this module, you have to import the `Backend` class, as the example here:

```
from Modules.System.Backend import Backend
```

After that, you can create the class:

```
backend = Backend()
```

And, voila! You can call `play_stream_url` to play a file or a web stream. Like this example:

```
backend.play_stream_url("/path/to/file")
```

*More documentation is available at the Wiki.*
