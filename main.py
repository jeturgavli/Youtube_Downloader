from functions.single_video import download_single_video
from functions.single_audio import download_single_audio
from functions.playlist_download import download_playlist

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
            download_single_video(url)
        elif choice == '2':
            download_single_audio(url)
        elif choice == '3':
            download_playlist(url, 'video')
        elif choice == '4':
            download_playlist(url, 'audio')
        else:
            print("Invalid choice. Please select again.")

if __name__ == "__main__":
    main()
