# FFmpeg Setup Guide (Windows)

This guide will help you set up FFmpeg for the YOUTUBE_DOWNLOADERS project on Windows.

## 1. Download FFmpeg

- Go to the official FFmpeg website: [https://ffmpeg.org/download.html](https://ffmpeg.org/download.html)
- Click on **Windows** and download the latest static build (e.g., from [gyan.dev](https://www.gyan.dev/ffmpeg/builds/)).
- Download the ZIP file (e.g., `ffmpeg-*-essentials_build.zip`).

## 2. Extract FFmpeg

- Extract the downloaded ZIP file to a folder of your choice.
- For this project, you can extract it to the `ffmpeg` folder already present in the project directory.
- After extraction, you should have the following structure:

```
YOUTUBE_DOWNLOADERS/
├── ffmpeg/
│   ├── bin/
│   │   ├── ffmpeg.exe
│   │   ├── ffplay.exe
│   │   └── ffprobe.exe
│   └── ...
```

## 3. Add FFmpeg to System PATH (Recommended)

1. Open the folder where you extracted FFmpeg.
2. Go to the `bin` folder and copy its path (e.g., `E:\Coding World\CURUNT WORKING ON THIS PROJECTS\YOUTUBE_DOWNLOADERS\ffmpeg\bin`).
3. Press `Win + S`, type `Environment Variables`, and open **Edit the system environment variables**.
4. Click on **Environment Variables...**
5. Under **System variables**, find and select the `Path` variable, then click **Edit**.
6. Click **New** and paste the path to the `bin` folder.
7. Click **OK** to save and close all dialogs.

## 4. Verify FFmpeg Installation

- Open a new Command Prompt window and type:

```
ffmpeg -version
```

- You should see FFmpeg version information. If not, make sure you added the correct path and opened a new terminal window.

## 5. Project Usage

- The project uses FFmpeg for audio extraction and conversion.
- No further configuration is needed if FFmpeg is in your PATH or in the `ffmpeg/bin` folder inside the project.

---

**Troubleshooting:**
- If you get errors related to FFmpeg not found, double-check the PATH setup or ensure the `ffmpeg/bin` folder exists and contains `ffmpeg.exe`.
