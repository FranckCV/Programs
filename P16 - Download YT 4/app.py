from flask import Flask, render_template, request, send_file
from pytube import YouTube
import os
import wget

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

        # Ruta de descarga personalizada
        download_path = os.path.join(app.root_path, 'downloads', filename)
        stream_url = stream.url

        # Descargar el archivo utilizando wget
        wget.download(stream_url, download_path)

        # Devolver el archivo descargado como un archivo adjunto
        return send_file(download_path, as_attachment=True)
    except Exception as e:
        message = f'Error al descargar: {str(e)}'
        return render_template('index.html', message=message)

if __name__ == '__main__':
    app.run(debug=True)
