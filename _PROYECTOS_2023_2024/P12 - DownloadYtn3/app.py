from flask import Flask, render_template, request, send_file
from pytube import YouTube
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/download', methods=['POST'])
def download():
    url = request.form['url']
    format = request.form['format']
    try:
        yt = YouTube(url)
        if format == 'video':
            stream = yt.streams.filter(progressive=True, file_extension='mp4').first()
            filename = f"{yt.title}.mp4"
        else:
            stream = yt.streams.filter(only_audio=True).first()
            filename = f"{yt.title}.mp3"

        filepath = os.path.join(app.root_path, 'downloads', filename)
        stream.download(output_path=os.path.join(app.root_path, 'downloads'), filename=filename)

        return send_file(filepath, as_attachment=True)
    except Exception as e:
        message = f'Error al descargar: {str(e)}'
        return render_template('index.html', message=message)

if __name__ == '__main__':
    app.run(debug=True)



# from flask import Flask, render_template, request, send_file
# import yt_dlp as youtube_dl
# import os

# app = Flask(__name__)

# @app.route('/')
# def index():
#     return render_template('index.html')

# @app.route('/download', methods=['POST'])
# def download():
#     url = request.form['url']
#     format = request.form['format']
#     try:
#         ydl_opts = {}
#         if format == 'video':
#             ydl_opts = {
#                 'format': 'bestvideo+bestaudio/best',
#                 'outtmpl': os.path.join(app.root_path, 'downloads', '%(title)s.%(ext)s')
#             }
#         else:
#             ydl_opts = {
#                 'format': 'bestaudio/best',
#                 'postprocessors': [{
#                     'key': 'FFmpegExtractAudio',
#                     'preferredcodec': 'mp3',
#                     'preferredquality': '192',
#                 }],
#                 'outtmpl': os.path.join(app.root_path, 'downloads', '%(title)s.%(ext)s')
#             }

#         with youtube_dl.YoutubeDL(ydl_opts) as ydl:
#             result = ydl.extract_info(url, download=True)
#             filename = ydl.prepare_filename(result)
#             if format == 'audio':
#                 filename = filename.replace('.webm', '.mp3')

#         return send_file(filename, as_attachment=True)
#     except Exception as e:
#         message = f'Error al descargar: {str(e)}'
#         return render_template('index.html', message=message)

# if __name__ == '__main__':
#     if not os.path.exists(os.path.join(app.root_path, 'downloads')):
#         os.makedirs(os.path.join(app.root_path, 'downloads'))
#     app.run(debug=True)
