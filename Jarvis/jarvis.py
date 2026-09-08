import joblib
from datetime import datetime

from acoes import (
    abrir_google,
    abrir_youtube,
    abrir_calculadora,
    abrir_bloco_notas,
    abrir_discord,
    abrir_spotify
)


modelo = joblib.load("modelo_jarvis.pkl")
vetorizador = joblib.load("vetorizador.pkl")


def responder(comando):

    comando = comando.lower().strip()

    texto = vetorizador.transform([comando])

    intencao = modelo.predict(texto)[0]

    probabilidades = modelo.predict_proba(texto)[0]

    confianca = max(probabilidades)

    confianca_porcentagem = confianca * 100

    print(f"\nIntencao: {intencao}")
    print(f"Confianca: {confianca_porcentagem:.2f}%")

    if confianca < 0.20:
        return "Nao tenho certeza do que voce quis dizer."

    if intencao == "saudacao":
        return "Ola! Como posso ajudar?"

    elif intencao == "hora":
        hora = datetime.now().strftime("%H:%M")
        return f"Agora sao {hora}."

    elif intencao == "data":
        data = datetime.now().strftime("%d/%m/%Y")
        return f"Hoje e dia {data}."

    elif intencao == "despedida":
        return "Ate mais!"

    elif intencao == "agradecimento":
        return "Por nada!"

    elif intencao == "elogio":
        return "Obrigado! Estou evoluindo."

    elif intencao == "como_estou":
        return "Voce parece estar bem."

    elif intencao == "como_voce_esta":
        return "Estou funcionando perfeitamente."

    elif intencao == "ajuda":
        return "Posso informar a hora e a data, abrir aplicativos, abrir sites e executar outras tarefas que estamos adicionando."

    elif intencao == "conversa":
        return "Claro. Sobre o que voce quer conversar?"

    elif intencao == "curiosidade":
        return "Os polvos possuem tres coracoes."

    elif intencao == "contar_piada":
        return "Por que o computador foi ao medico? Porque ele estava com um virus."

    elif intencao == "confirmacao":
        return "Beleza!"

    elif intencao == "negacao":
        return "Tudo bem."

    elif intencao == "insulto":
        return "Calma ai, estou aprendendo."

    elif intencao == "abrir_google":
        abrir_google()
        return "Abrindo o Google."

    elif intencao == "abrir_youtube":
        abrir_youtube()
        return "Abrindo o YouTube."

    elif intencao == "abrir_calculadora":
        abrir_calculadora()
        return "Abrindo a calculadora."

    elif intencao == "abrir_notepad":
        abrir_bloco_notas()
        return "Abrindo o bloco de notas."

    elif intencao == "abrir_discord":
        abrir_discord()
        return "Abrindo o Discord."

    elif intencao == "abrir_spotify":
        abrir_spotify()
        return "Abrindo o Spotify."

    else:
        return "Ainda nao sei fazer isso."



print("Digite 'sair' para encerrar.")



while True:

    comando = input("Voce: ")

    if comando.lower().strip() in ["sair", "encerrar", "fechar", "desligar"]:
        print("Jarvis: Ate mais!")
        break

    resposta = responder(comando)

    print(f"Jarvis: {resposta}")