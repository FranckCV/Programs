
# import speech_recognition as sr
# from pydub import AudioSegment
# import os

# def convertir_a_wav(archivo):
#     if archivo.lower().endswith('.mp3'):
#         archivo_wav = archivo.replace('.mp3', '.wav')
#         try:
#             audio = AudioSegment.from_file(archivo, format="mp3")  # Carga MP3
#             audio.export(archivo_wav, format="wav")  # Convierte a WAV
#             return archivo_wav
#         except Exception as e:
#             print(f"Error al convertir MP3 a WAV: {e}")
#             return None
#     return archivo  # Si ya es WAV, devuelve el mismo archivo

# archivo = "aaa.wav"  # Puede ser MP3 o WAV
# archivo_wav = convertir_a_wav(archivo)

# if archivo_wav:  # Verifica que la conversión fue exitosa
#     r = sr.Recognizer()

#     with sr.AudioFile(archivo_wav) as source:
#         audio = r.record(source)

#     try:
#         texto = r.recognize_google(audio, language="es-ES")
#         print("Texto transcrito:")
#         print(texto)
#     except sr.UnknownValueError:
#         print("No se pudo entender el audio.")
#     except sr.RequestError as e:
#         print("Error del servicio:", e)

#     # Opcional: Eliminar el archivo WAV temporal si se convirtió de MP3
#     if archivo_wav != archivo:
#         os.remove(archivo_wav)






import speech_recognition as sr

r = sr.Recognizer()


with sr.Microphone() as source:
    print("🎤 Habla ahora... (presiona Ctrl+C para salir)")
    r.adjust_for_ambient_noise(source)  # Ajusta el ruido de fondo

    try:
        while True:
            print("Escuchando...")
            audio = r.listen(source)  # Captura el audio en tiempo real
            texto = r.recognize_google(audio, language="es-ES")  # Transcribe
            print("Texto transcrito:", texto)
    
    except sr.UnknownValueError:
        print("No se pudo entender el audio.")
    except sr.RequestError as e:
        print("Error del servicio:", e)
    except KeyboardInterrupt:
        print("\n🛑 Transcripción detenida por el usuario.")
