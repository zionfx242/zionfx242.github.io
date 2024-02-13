from flask import Flask, render_template, request, send_file
import yt_dlp
import os

app = Flask(__name__)

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

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        url = request.form['url']
        download_type = int(request.form['download_type'])
        download_video_and_audio(url, download_type)
        file_path = os.path.join(os.path.expanduser('~'), 'Downloads')
        # Retrieve the file name from the directory
        file_name = [f for f in os.listdir(file_path) if os.path.isfile(os.path.join(file_path, f))][0]
        # Serve the file as a response
        return send_file(os.path.join(file_path, file_name), as_attachment=True)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
