import time
from youtube_downloader import download_youtube_video as dyv

cur_time = time.time()
dyv("https://www.youtube.com/watch?v=VIZibp4cQ7E&list=PLO7zq9QHlycrmWom3aheS5oVTdKw3IvCD&index=77")
fin_time = time.time()
print(str(fin_time-cur_time))