# functions/single_video.py

import yt_dlp

def download_single_video(url):
    ydl_opts = {
        'format': 'bestvideo[height<=720]+bestaudio/best[height<=720]',
        'outtmpl': '%(title)s.%(ext)s',
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        print("Video download completed!")
    except Exception as e:
        print(f"Error occurred: {e}")
