#Kevin Antonio Caballero Curiel - 17330423
#pip install SpeechRecognition
#pip install pyttsx3

import speech_recognition as sr
import pyttsx3
from pyttsx3 import engine
from pyttsx3.engine import Engine
import os
import subprocess

Engine=pyttsx3.init()

def hablar(text):
    Engine.say(text)
    Engine.runAndWait()

listener = sr.Recognizer()

def main(reload=""):
    try:
        with sr.Microphone () as mic:
            listener.adjust_for_ambient_noise(mic)
            rec = reload
            while rec != "Okay compu adiós":
                if rec == "Okay compu" or rec == "Oye compu" or rec == "Hey compu":
                    hablar("¿En qué puedo ayudarte?")
                    print("¿En qué puedo ayudarte?")
                    print("Escuchando...")
                    voice=listener.listen(mic)
                    rec=listener.recognize_google(voice, language="es-ES")

                    print(rec)

                    if rec == "Abre Spotify":
                        file='"C:\\Program Files\\WindowsApps\\SpotifyAB.SpotifyMusic_1.176.447.0_x86__zpdnekdrzrea0\\Spotify.exe"'
                        os.system(file)
                        hablar("Ok, abriendo Spotify")
                        print("Okay, abriendo Spotify")
                    elif rec == "Abre Word":
                        file='"C:/Program Files/Microsoft Office/root/Office16/WINWORD.EXE"'
                        os.system("start WINWORD.EXE")
                        hablar("Ok, abriendo Word")
                        print("Okay, abriendo Word")
                    elif rec == "Abre Powerpoint":
                        file='"C:/Program Files/Microsoft Office/root/Office16/POWERPNT.EXE"'
                        os.system("start POWERPNT.EXE")
                        hablar("Ok, abriendo Powerpoint")
                        print("Okay, abriendo Powerpoint")
                    elif rec == "Abre Excel":
                        file='"C:/Program Files/Microsoft Office/root/Office16/EXCEL.EXE"'
                        os.system("start EXCEL.EXE")
                        hablar("Ok, abriendo Excel")
                        print("Okay, abriendo Excel")
                    elif rec == "Abre una foto de las y gotita" or rec == "Abre una foto de lassie Gotita":
                        file='"D:/Pictures/Mascotas/IMG-20160828-WA0006.jpg"'
                        os.system(file)
                        hablar("Ok, abriendo la foto de la cigotita")
                        print("Okay, abriendo la foto de la cigotita")
                    elif rec == "abre el navegador" or rec == "Abre Google Chrome":
                        file='"C:/Program Files (x86)/Google/Chrome/Application/chrome.exe"'
                        os.system(file)
                        hablar("Ok, abriendo Google Chrome")
                        print("Okay, abriendo Google Chrome")
                    elif rec == "apaga la computadora":
                        os.system("D:/apagar.lnk")
                        hablar("Ok, la computadora se apagará en 30 segundos")
                        print("Okay, la computadora se apagará en 30 segundos")
                    elif rec == "Cancela el apagado":
                        os.system("D:/cancelar.lnk")
                        hablar("Ok, acción de apagado cancelada")
                        print("Okay, acción de apagado cancelada")
                    elif rec == "Okay compu adiós" or rec == "Okay adiós":
                        rec = "Okay compu adiós"
                        hablar("Ok, adios")
                        print("Okay, adios")
                    else:
                        hablar("No he entendido la acción o no la tengo programada aún, intenta de nuevo.")
                        print("No he entendido la acción o no la tengo programada aún, intenta de nuevo.")
                        rec = "Okay compu"
                else:
                    print("Escuchando...")
                    voice=listener.listen(mic)
                    rec=listener.recognize_google(voice, language="es-ES")
        
    except sr.UnknownValueError:
        hablar("No he entendido la acción o no la tengo programada aún, intenta de nuevo.")
        print("No he entendido la acción o no la tengo programada aún, intenta de nuevo.")
        main("")
    except sr.RequestError as e:
        print("Error: " + e)

main("")