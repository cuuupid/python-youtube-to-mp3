import sys, os, requests
from pytube import YouTube as Youtube_Video
import re

def download_youtube_video(video_url):
    ''' Takes in a video URL to a youtube video, outputs the relative path to the downloaded video '''
    vid = Youtube_Video(video_url)
    vid.set_filename(re.sub('[^a-zA-Z]','',vid.filename).lower())
    saved_to = vid.filename
    if os.path.exists('static/'+saved_to+'.mp4'):
        print("[=] Video exists...")
        return 'static/'+saved_to+'.mp4'
    mp4_vids = vid.filter('mp4')
    if not len(mp4_vids)>0:
        return -1
    vid = mp4_vids[0] #who gives a fuck about resolution
    ### UNCOMMENT BELOW FOR PROGRESS
    # vid.download('static/',on_progress=lambda x,y: print(int(x/y*100)))
    vid.download('static/')
    mp4 = 'static/'+saved_to+'.mp4'
    mp3 = 'static/'+saved_to+'.mp3'
    cmd = "ffmpeg -i \"" + mp4 + "\" -vn -ar 44100 -ac 2 -ab 192k -f mp3 \"" + mp3 + "\""
    os.system(cmd)
    try:
        os.remove(mp4)
    except Exception as e:
        print(e)
        print("-"*60)
        print("\nFailed to remove "+mp4)
    return 'static/'+saved_to+'.mp3'