import subprocess
import webbrowser


def abrir_google():
    webbrowser.open("https://www.google.com")


def abrir_youtube():
    webbrowser.open("https://www.youtube.com")


def abrir_calculadora():
    subprocess.Popen("calc.exe")


def abrir_bloco_notas():
    subprocess.Popen("notepad.exe")


def abrir_discord():
    subprocess.Popen("start discord:", shell=True)


def abrir_spotify():
    subprocess.Popen("start spotify:", shell=True)