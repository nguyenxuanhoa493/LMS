import sys
from os.path import join, dirname
from pytube import Playlist

sys.path.append(join(dirname(__file__), "..", ""))
from API import lms
from API.until import get_tittle_youtube
from API.syllabus import add_video_youtube, update_content_syllabus


school = lms.New(type_dmn="bgg", dmn="ve", user_code="sbg", password="Sbg@2024")
iid_syllabus = 57113318
url_playlist = (
    "https://www.youtube.com/playlist?list=PLDly2FSuA2aN9O7ZVhZi7HTKXRsz2gQYD"
)


pls = Playlist(url_playlist)
videos = []
for item in pls:
    videos.append({"name": get_tittle_youtube(item), "id": item})


content = []
for v in videos:
    content.append(add_video_youtube(school, iid_syllabus, v))
update_content_syllabus(school, iid_syllabus, content)
