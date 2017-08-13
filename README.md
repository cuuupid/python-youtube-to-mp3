# Youtube to mp3 

## Performance

Very low performance library (downloading as mp4, converting to mp3).

Testing speed using `benchmark.py` resolves `9.236s` for `3:03` video with moving visuals.

Converting to mp3 creates overhead --> resolve using opened pipe in stdout. TODO exists for this.

`ffmpeg` accounts for ~4 seconds.

## Dependencies

1. `ffmpeg`
2. `python`
3. `requests` module (`pip install requests`)
4. `pytube` module (`pip install pytube`)

## Usage

```
from youtube_downloader import download_youtube_video

mp3_filepath = download_youtube_video("https://www.youtube.com/watch?v=VIZibp4cQ7E")

os.system('open \"'+mp3_filepath+'\"') # open mp3 in default player for playback
```