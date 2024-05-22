from pytube import YouTube
import os

def download_video(url, output_path):
    try:
        yt = YouTube(url)
        video = yt.streams.get_highest_resolution()
        video.download(output_path)
        print("Video descargado exitosamente!")
    except Exception as e:
        print("Error al descargar el video:", str(e))

def download_audio(url, output_path):
    try:
        yt = YouTube(url)
        audio = yt.streams.filter(only_audio=True).first()
        audio.download(output_path)
        print("Audio descargado exitosamente!")
    except Exception as e:
        print("Error al descargar el audio:", str(e))

if __name__ == "__main__":
    url = input("Inserte el enlace de YouTube: ")
    output_path = input("Inserte la ruta de destino para la descarga: ")

    # Crea el directorio de salida si no existe
    if not os.path.exists(output_path):
        os.makedirs(output_path)

    download_video(url, output_path)
    download_audio(url, output_path)