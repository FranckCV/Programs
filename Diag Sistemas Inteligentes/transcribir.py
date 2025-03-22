# Integrantes: Cortez Villaseca, Franco | Gil Alarcon , Gabriel | Paucar mejia, Fabiana | Perez Davila , Junior



import speech_recognition as sr

def transcribir(recognizer, source):
    try:
        print("Escuchando...")
        audio = recognizer.listen(source)
        texto = recognizer.recognize_google(audio, language="es-ES") 
        return texto
    except sr.UnknownValueError:
        print("No se pudo entender el audio. Inténtalo de nuevo.")
        return None
    except sr.RequestError as e:
        print("Error del servicio:", e)
        return None

r = sr.Recognizer()

with sr.Microphone() as source:
    print("🎤 Habla ahora... (presiona Ctrl+C para salir)")
    r.adjust_for_ambient_noise(source) 

    try:
        while True:
            texto = transcribir(r, source)
            if texto: 
                print("Texto transcrito:", texto)

    except KeyboardInterrupt:
        print("\n🛑 Transcripción detenida por el usuario.")
