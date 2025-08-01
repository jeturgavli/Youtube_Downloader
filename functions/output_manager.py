# functions/output_manager.py

import os

def get_output_path(mode: str, playlist_title: str = None):
    """
    Returns a formatted output path string depending on the mode.
    
    Parameters:
        mode (str): One of ['single_video', 'audio', 'playlist_video', 'playlist_audio']
        playlist_title (str, optional): Used to create a subfolder for each playlist
    
    Returns:
        str: Output path template string for yt_dlp's 'outtmpl'
    """
    base_folder = "output"

    # Ensure the base output folder exists
    os.makedirs(base_folder, exist_ok=True)

    if mode == "single_video":
        path = os.path.join(base_folder, "single_video", "%(title)s.%(ext)s")

    elif mode == "audio":
        path = os.path.join(base_folder, "Mp3_audio", "%(title)s.%(ext)s")

    elif mode in ["playlist_video", "playlist_audio"]:
        if playlist_title:
            # Sanitize playlist title to avoid path errors
            safe_title = "".join(c for c in playlist_title if c.isalnum() or c in " _-").rstrip()
            path = os.path.join(base_folder, "playlist_video" if mode == "playlist_video" else "Mp3_audio", safe_title, "%(playlist_index)s - %(title)s.%(ext)s")
        else:
            # Fallback path
            path = os.path.join(base_folder, "playlist_video", "%(playlist_index)s - %(title)s.%(ext)s")
    
    return path
