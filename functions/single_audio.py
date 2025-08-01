# functions/single_audio.py

import yt_dlp
from functions.output_manager import get_output_path

def download_single_audio(url):
    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': get_output_path("audio"),
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        print("Audio (MP3) download completed!")
    except Exception as e:
        print(f"Error occurred: {e}")
