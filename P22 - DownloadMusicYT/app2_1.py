from flask import Flask, render_template, request, jsonify
from pytube import YouTube
from tkinter import Tk, filedialog
import os

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
            # Abrir ventana de selección de archivo
            root = Tk()
            root.withdraw()
            root.attributes('-topmost', True)  # Mantener la ventana arriba
            download_path = filedialog.askdirectory(initialdir=os.path.expanduser("~/Downloads"))
            filename = stream.download(download_path)
        elif download_type == 'audio':
            stream = yt.streams.filter(only_audio=True).first()
            # Abrir ventana de selección de archivo
            root = Tk()
            root.withdraw()
            root.attributes('-topmost', True)  # Mantener la ventana arriba
            download_path = filedialog.askdirectory(initialdir=os.path.expanduser("~/Downloads"))
            filename = stream.download(download_path)
            # Cambiar la extensión del archivo descargado a .mp3
            mp3_filename = filename.split('.')[0] + '.mp3'
            os.rename(filename, mp3_filename)
            filename = mp3_filename
        else:
            return jsonify({'success': False, 'message': 'Invalid download type'})

        return jsonify({'success': True, 'message': 'Download completed', 'filename': filename})
    except Exception as e:
        return jsonify({'success': False, 'message': str(e)})

if __name__ == '__main__':
    app.run(debug=True)


 