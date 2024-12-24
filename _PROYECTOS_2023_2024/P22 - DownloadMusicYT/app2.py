from flask import Flask, render_template, request, jsonify
from pytube import YouTube

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/download', methods=['POST'])
def download():
    url = request.form['url']
    download_type = request.form['type']
    
    try:
        yt = YouTube(url)
        if download_type == 'video':
            stream = yt.streams.get_highest_resolution()
            filename = stream.download()
        elif download_type == 'audio':
            # Filtrar solo los flujos de audio
            audio_stream = yt.streams.filter(only_audio=True).first()
            # Descargar el flujo de audio
            filename = audio_stream.download()
            # Cambiar la extensión del archivo descargado a .mp3
            mp3_filename = filename.split('.')[0] + '.mp3'
            import os
            os.rename(filename, mp3_filename)
            filename = mp3_filename
        else:
            return jsonify({'success': False, 'message': 'Invalid download type'})

        return jsonify({'success': True, 'message': 'Download completed', 'filename': filename})
    except Exception as e:
        return jsonify({'success': False, 'message': str(e)})

if __name__ == '__main__':
    app.run(debug=True)


 