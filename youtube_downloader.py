import yt_dlp
import os

url = input("Enter YouTube video URL: ")

# Create downloads folder
download_folder = "downloads"
os.makedirs(download_folder, exist_ok=True)

ydl_opts = {
    'format': 'best',
    'outtmpl': f'{download_folder}/%(title)s.%(ext)s'
}

with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download([url])

print("Download completed!")
