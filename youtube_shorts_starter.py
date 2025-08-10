# fetch_shorts.py
from googleapiclient.discovery import build
import os
from dotenv import load_dotenv

# Load API key from .env
load_dotenv()
API_KEY = os.getenv("YOUTUBE_API_KEY")

# Initialize YouTube API
youtube = build("youtube", "v3", developerKey=API_KEY)

def fetch_shorts_video_ids(query, max_results=50):
    """
    Search YouTube for short videos (<4 mins, we'll filter later for <= 60 sec)
    """
    request = youtube.search().list(
        q=query,
        part="id",
        type="video",
        videoDuration="short",
        maxResults=max_results,
        order="date"
    )
    response = request.execute()

    video_ids = []
    for item in response.get("items", []):
        vid_id = item["id"].get("videoId")
        if vid_id:
            video_ids.append(vid_id)

    return video_ids

if __name__ == "__main__":
    ids = fetch_shorts_video_ids("#shorts", 10)
    print(f"Fetched {len(ids)} IDs")
    print(ids)
