import subprocess
import os


def abrir_calculadora():
    subprocess.Popen("calc.exe")
    return "Calculadora aberta."


def abrir_bloco_notas():
    subprocess.Popen("notepad.exe")
    return "Bloco de notas aberto."


def abrir_chrome():
    caminho = r"C:\Program Files\Google\Chrome\Application\chrome.exe"

    if os.path.exists(caminho):
        subprocess.Popen(caminho)
        return "Google Chrome aberto."

    return "Não encontrei o Google Chrome nesse local."


def abrir_explorador():
    subprocess.Popen("explorer.exe")
    return "Explorador de arquivos aberto."


def desligar_computador():
    os.system("shutdown /s /t 10")
    return "O computador será desligado em 10 segundos."


def cancelar_desligamento():
    os.system("shutdown /a")
    return "Desligamento cancelado."