from acoes import (
    abrir_calculadora,
    abrir_bloco_notas,
    abrir_chrome,
    abrir_explorador,
    desligar_computador,
    cancelar_desligamento
)


FERRAMENTAS = {
    "abrir_calculadora": abrir_calculadora,
    "abrir_bloco_notas": abrir_bloco_notas,
    "abrir_chrome": abrir_chrome,
    "abrir_explorador": abrir_explorador,
    "desligar_computador": desligar_computador,
    "cancelar_desligamento": cancelar_desligamento,
}


def executar_ferramenta(nome):
    ferramenta = FERRAMENTAS.get(nome)
    
    if ferramenta is None:
        return f"Ferramenta '{nome}' não encontrado"
    
    
    try:
        return ferramenta()

    except Exception as erro:
        return f"Erro ao executar '{nome}': {erro}"