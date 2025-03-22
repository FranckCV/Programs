
import speech_recognition as sr

archivo = 'audio_leo.wav'

r = sr.Recognizer()

with sr.AudioFile(archivo) as source:
    audio = r.record(source)  

try:
    texto = r.recognize_google(audio, language="es-ES")
    print("Texto transcrito:")
    print(texto)
except sr.UnknownValueError:
    print("No se pudo entender el audio.")
except sr.RequestError as e:
    print("Error del servicio:", e)
