from conversa import Conversa
from cerebro import Cerebro
from gemini import Gemini


gemini = Gemini()

cerebro = Cerebro(gemini)

conversa = Conversa(cerebro)


print("================================")
print("            JARVIS")
print("================================")
print("Sistema iniciado.")
print()
print("Comandos:")
print("  /memoria  -> mostra o histórico")
print("  /limpar   -> apaga o histórico")
print("  sair      -> encerra o Jarvis")


while True:

    mensagem = input("\nVocê: ").strip()

    if mensagem.lower() == "sair":
        print("Jarvis: Até mais.")
        break

    if mensagem.lower() == "/memoria":
        conversa.mostrar_memoria()
        continue

    if mensagem.lower() == "/limpar":
        conversa.limpar_memoria()
        print("Jarvis: Memória apagada.")
        continue

    if not mensagem:
        continue

    conversa.adicionar_usuario(mensagem)

    contexto = conversa.obter_contexto()

    resposta = cerebro.responder(
        mensagem,
        contexto
    )

    conversa.adicionar_jarvis(resposta)

    print("Jarvis:", resposta)