import yt_dlp
import os

def download_video_and_audio(url, download_type):
    download_path = os.path.join(os.path.expanduser('~'), 'Downloads', '%(title)s.%(ext)s')

    video_opts = {
        'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/bestvideo+bestaudio',
        'outtmpl': download_path,
        'postprocessors': [{
            'key': 'FFmpegVideoConvertor',
            'preferedformat': 'mp4',
        }],
    }
    audio_opts = {
        'format': 'bestaudio/best',
        'outtmpl': download_path,
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'wav',
            'preferredquality': '320',
        }],
    }

    if download_type == 1 or download_type == 3:
        with yt_dlp.YoutubeDL(video_opts) as ydl:
            ydl.download([url])

    if download_type == 2 or download_type == 3:
        with yt_dlp.YoutubeDL(audio_opts) as ydl:
            ydl.download([url])

# Ask user what they want to download
print("Which Would You Like To Download?")
print("Video - 1")
print("Audio - 2")
print("Both - 3")

choice = int(input("Enter your choice: "))

# Example usage
download_video_and_audio('https://youtu.be/O3tnOVideSo?si=kDlm9pdV8zETphi4', choice)
