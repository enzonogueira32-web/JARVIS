from google import genai

from gemini_ferramentas import FERRAMENTAS_GEMINI
from ferramentas import executar_ferramenta


class Gemini:

    def __init__(self):
        self.cliente = None
        self.modelo = "gemini-3.8-flash"

    def configurar(self):
        """
        Cria o cliente do Gemini.

        A API Key será configurada posteriormente.
        """

        self.cliente = genai.Client()

    def responder(self, mensagem, contexto):

        if self.cliente is None:
            return (
                "O Gemini ainda não está configurado."
            )

        interaction = self.cliente.interactions.create(
            model=self.modelo,
            input=mensagem,
            tools=FERRAMENTAS_GEMINI,
        )

        for step in interaction.steps:

            if step.type == "function_call":

                nome = step.name
                argumentos = step.arguments

                print(
                    f"[Ferramenta] {nome}"
                )

                print(
                    f"[Argumentos] {argumentos}"
                )

                resultado = executar_ferramenta(
                    nome
                )

                resultado_interacao = (
                    self.cliente.interactions.create(
                        model=self.modelo,
                        input=[
                            {
                                "type": "function_result",
                                "name": nome,
                                "call_id": step.id,
                                "result": [
                                    {
                                        "type": "text",
                                        "text": resultado
                                    }
                                ],
                            }
                        ],
                        tools=FERRAMENTAS_GEMINI,
                        previous_interaction_id=interaction.id,
                    )
                )

                return resultado_interacao.output_text

        return interaction.output_text