# functions/single_video.py

import yt_dlp
from functions.output_manager import get_output_path

def download_single_video(url):
    ydl_opts = {
        'format': 'bestvideo[height<=720]+bestaudio/best[height<=720]',
        'outtmpl': get_output_path("single_video"),
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        print("Video download completed!")
    except Exception as e:
        print(f"Error occurred: {e}")
