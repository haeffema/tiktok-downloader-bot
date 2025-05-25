import requests
import os


def download_tiktok(url):
    api_url = "https://api.tikmate.app/api/lookup"
    params = {"url": url}

    response = requests.post(api_url, data=params)

    if response.status_code == 200:
        data = response.json()
        download_url = f"https://tikmate.app/download/{data['token']}/{data['id']}.mp4"

        video_response = requests.get(download_url, stream=True)

        if video_response.status_code == 200:
            try:
                os.remove("tiktok.mp4")
            except OSError:
                pass
            with open("tiktok.mp4", "wb") as f:
                for chunk in video_response.iter_content(1024):
                    f.write(chunk)
