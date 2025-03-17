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
        elif download_type == 'audio':
            stream = yt.streams.filter(only_audio=True).first()
        else:
            return jsonify({'success': False, 'message': 'Invalid download type'})
        
        # Abrir ventana de selección de archivo
        root = Tk()
        root.withdraw()
        root.attributes('-topmost', True)  # Mantener la ventana arriba
        root.filename = filedialog.asksaveasfilename(initialdir=os.path.expanduser("~/Downloads"),
                                                      title="Guardar como",
                                                      defaultextension=stream.extension,
                                                      filetypes=[(f"{stream.extension.upper()} files", f"*.{stream.extension}")])
        if not root.filename:
            return jsonify({'success': False, 'message': 'No se seleccionó ninguna ubicación de descarga'})
        
        # Descargar el archivo en la ubicación seleccionada
        filename = stream.download(output_path=os.path.dirname(root.filename), filename=os.path.basename(root.filename))

        return jsonify({'success': True, 'message': 'Descarga completada', 'filename': filename})
    except Exception as e:
        return jsonify({'success': False, 'message': str(e)})

if __name__ == '__main__':
    app.run(debug=True)

 