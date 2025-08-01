from functions.output_manager import get_output_path
import yt_dlp

def download_playlist(url, download_type):
    try:
        # Fetch info first to get playlist title
        with yt_dlp.YoutubeDL({'quiet': True}) as ydl:
            info = ydl.extract_info(url, download=False)
            playlist_title = info.get("title", "Unknown_Playlist")

        mode = "playlist_video" if download_type == 'video' else "playlist_audio"
        ydl_opts = {
            'format': 'bestvideo[height<=720]+bestaudio/best[height<=720]' if download_type == 'video' else 'bestaudio/best',
            'outtmpl': get_output_path(mode, playlist_title),
        }

        if download_type == 'audio':
            ydl_opts['postprocessors'] = [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }]

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])

        print(f"Playlist {download_type} download completed!")

    except Exception as e:
        print(f"Error occurred: {e}")
