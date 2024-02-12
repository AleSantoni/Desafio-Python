import pyttsx3
import speech_recognition as sr


def grabar_audio():
    # Configuramos el motor de texto a voz
    engine = pyttsx3.init()

    # Configuramos el reconocedor de voz
    recognizer = sr.Recognizer()

    # Configuramos la duración de la grabación
    duracion = 5  # Duración en segundos

    # Grabamos audio desde el micrófono utilizando speech_recognition
    try:
        engine.say("Escuchando...")
        engine.runAndWait()

        with sr.Microphone() as mic:
            print("Grabando audio...")
            audio = recognizer.listen(mic, timeout=duracion)

        # Utilizamos Google Speech Recognition para convertir el audio en texto
        pedido = recognizer.recognize_google(audio, language="es-ar")

        # Imprimimos en pantalla lo que se dijo
        print("Usted dice:", pedido)

        # Devolvemos el pedido
        return pedido

    # En caso de que no comprenda el audio
    except sr.UnknownValueError:
        print("No se ha entendido el audio")
        return "No entendí, sigo esperando"

    # En caso de error al procesar el pedido
    except sr.RequestError:
        print("Error al procesar la solicitud de audio")
        return "No entendí, sigo esperando"



# Llamamos a la función para iniciar el proceso de transformación de audio en texto
resultado = grabar_audio()
print(resultado)