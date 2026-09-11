from ferramentas import executar_ferramenta


class Cerebro:

    def __init__(self, cliente=None):
        self.cliente = cliente

    def responder(self, mensagem, contexto):
        """
        Recebe a mensagem do usuário e o histórico da conversa.

        Quando o Gemini estiver conectado, esta função será
        responsável por enviar tudo para ele.
        """

        if self.cliente is None:
            return self.resposta_teste(mensagem)

        return self.cliente.responder(
            mensagem,
            contexto
        )

    def executar_ferramenta(self, nome):
        """
        Executa uma ferramenta disponível no Jarvis.
        """

        return executar_ferramenta(nome)

    def resposta_teste(self, mensagem):

        mensagem = mensagem.lower()

        if "calculadora" in mensagem:
            return self.executar_ferramenta(
                "abrir_calculadora"
            )

        if "bloco de notas" in mensagem:
            return self.executar_ferramenta(
                "abrir_bloco_notas"
            )

        if "chrome" in mensagem:
            return self.executar_ferramenta(
                "abrir_chrome"
            )

        if "explorador" in mensagem:
            return self.executar_ferramenta(
                "abrir_explorador"
            )

        return (
            "Ainda estou no modo de teste. "
            "O Gemini será conectado posteriormente."
        )