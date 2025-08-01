# functions/playlist_download.py

import yt_dlp

def download_playlist(url, download_type):
    if download_type == 'video':
        ydl_opts = {
            'format': 'bestvideo[height<=720]+bestaudio/best[height<=720]',
            'outtmpl': '%(playlist_title)s/%(playlist_index)s - %(title)s.%(ext)s',
        }
    elif download_type == 'audio':
        ydl_opts = {
            'format': 'bestaudio/best',
            'outtmpl': '%(playlist_title)s/%(playlist_index)s - %(title)s.%(ext)s',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
        }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        print(f"Playlist {download_type} download completed!")
    except Exception as e:
        print(f"Error occurred: {e}")
