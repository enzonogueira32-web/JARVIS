from memoria import Memoria


class Conversa:

    def __init__(self, modelo):
        self.modelo = modelo
        self.memoria = Memoria()

    def obter_historico_gemini(self):
        historico = []

        for mensagem in self.memoria.obter_historico():

            if mensagem["role"] == "user":
                historico.append({
                    "role": "user",
                    "content": mensagem["content"]
                })

            elif mensagem["role"] == "assistant":
                historico.append({
                    "role": "model",
                    "content": mensagem["content"]
                })

        return historico

    def adicionar_usuario(self, mensagem):
        self.memoria.adicionar_usuario(mensagem)

    def adicionar_jarvis(self, resposta):
        self.memoria.adicionar_jarvis(resposta)

    def obter_contexto(self):
        return self.obter_historico_gemini()

    def limpar_memoria(self):
        self.memoria.limpar()

    def mostrar_memoria(self):
        self.memoria.exibir()