import yt_dlp

def download_video_or_audio(url, download_type):
    # Define the options for yt-dlp based on the download type
    if download_type == 'video':
        ydl_opts = {
            'format': 'bestvideo[height<=720]+bestaudio/best[height<=720]',  # 720p video with best audio
            'outtmpl': '%(title)s.%(ext)s',  # Name the file after the title
        }
    elif download_type == 'audio':
        ydl_opts = {
            'format': 'bestaudio/best',  # Best audio
            'outtmpl': '%(title)s.%(ext)s',  # Name the file after the title
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
        }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        print(f"{download_type.capitalize()} download completed!")
    except Exception as e:
        print(f"Error occurred: {e}")

def download_playlist(url, download_type):
    # Define options for playlist download
    if download_type == 'video':
        ydl_opts = {
            'format': 'bestvideo[height<=720]+bestaudio/best[height<=720]',  # 720p video with best audio
            'outtmpl': '%(playlist_title)s/%(playlist_index)s - %(title)s.%(ext)s',  # Organize videos by playlist
        }
    elif download_type == 'audio':
        ydl_opts = {
            'format': 'bestaudio/best',  # Best audio
            'outtmpl': '%(playlist_title)s/%(playlist_index)s - %(title)s.%(ext)s',  # Organize audio by playlist
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

def main():
    while True:
        print("\n1. Download Single Video")
        print("2. Download YouTube to MP3")
        print("3. Download Playlist (Video)")
        print("4. Download Playlist (MP3)")
        print("5. Exit")
        
        choice = input("Enter your choice (1-5): ")

        if choice == '5':
            print("Exiting...")
            break

        url = input("Enter YouTube video or playlist URL: ")

        if choice == '1':
            download_video_or_audio(url, 'video')
        elif choice == '2':
            download_video_or_audio(url, 'audio')
        elif choice == '3':
            download_playlist(url, 'video')
        elif choice == '4':
            download_playlist(url, 'audio')
        else:
            print("Invalid choice. Please select again.")

if __name__ == "__main__":
    main()
