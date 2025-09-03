# functions/urls_file_downloader.py
from functions.single_video import download_single_video

def download_from_file(file_path="urls_file.txt"):
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            urls = [line.strip() for line in f if line.strip()]
        
        if not urls:
            print("⚠️ urls_file.txt is empty.")
            return

        print(f"\n📂 Found {len(urls)} URLs in {file_path}")
        for i, url in enumerate(urls, start=1):
            print(f"\n[{i}/{len(urls)}] Downloading: {url}")
            try:
                download_single_video(url)
            except Exception as e:
                print(f"❌ Failed: {url} | Error: {e}")
    except FileNotFoundError:
        print("⚠️ urls_file.txt not found. Please create the file and add URLs.")
