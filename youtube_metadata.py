import requests
from dotenv import load_dotenv
import os


def get_youtube_metadata(video_id):
    load_dotenv()
    rapidapi_key = os.getenv("RAPIDAPI_KEY")

    url = "https://youtube-video-information1.p.rapidapi.com/api/youtube"

    querystring = {"video_id":video_id}
    headers = {
        "x-rapidapi-key": f"{rapidapi_key}",
        "x-rapidapi-host": "youtube-video-information1.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring)
    data = response.json()
    print(data)
    video_name = data['title']
    video_name = video_name[0:25]
    image_url = data['thumbnail']

    print(video_name, image_url)
    return video_name, image_url

get_youtube_metadata("A1vEZhwH8y8")
