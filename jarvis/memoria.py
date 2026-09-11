import json
import os


ARQUIVO_MEMORIA = "memoria.json"
LIMITE_MENSAGENS = 20


class Memoria:

    def __init__(self):
        self.historico = []
        self.carregar()

    def carregar(self):
        if not os.path.exists(ARQUIVO_MEMORIA):
            self.historico = []
            return

        try:
            with open(ARQUIVO_MEMORIA, "r", encoding="utf-8") as arquivo:
                dados = json.load(arquivo)

                if isinstance(dados, list):
                    self.historico = dados
                else:
                    self.historico = []

        except (json.JSONDecodeError, OSError):
            self.historico = []

    def salvar(self):
        try:
            with open(ARQUIVO_MEMORIA, "w", encoding="utf-8") as arquivo:
                json.dump(
                    self.historico,
                    arquivo,
                    ensure_ascii=False,
                    indent=4
                )
        except OSError as erro:
            print(f"Erro ao salvar memória: {erro}")

    def adicionar_usuario(self, mensagem):
        self.historico.append({
            "role": "user",
            "content": mensagem
        })

        self.limitar_historico()
        self.salvar()

    def adicionar_jarvis(self, mensagem):
        self.historico.append({
            "role": "assistant",
            "content": mensagem
        })

        self.limitar_historico()
        self.salvar()

    def limitar_historico(self):
        if len(self.historico) > LIMITE_MENSAGENS:
            self.historico = self.historico[-LIMITE_MENSAGENS:]

    def obter_historico(self):
        return self.historico

    def limpar(self):
        self.historico = []
        self.salvar()

    def exibir(self):
        if not self.historico:
            print("Memória vazia.")
            return

        print("\n===== MEMÓRIA =====")

        for mensagem in self.historico:
            if mensagem["role"] == "user":
                nome = "Você"
            else:
                nome = "Jarvis"

            print(f"{nome}: {mensagem['content']}")

        print("===================")