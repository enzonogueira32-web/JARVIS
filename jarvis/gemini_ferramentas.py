FERRAMENTAS_GEMINI = [

    {
        "type": "function",
        "name": "abrir_calculadora",
        "description": (
            "Abre a calculadora do Windows. "
            "Use quando o usuário pedir para abrir "
            "ou iniciar a calculadora."
        ),
        "parameters": {
            "type": "object",
            "properties": {},
        },
    },

    {
        "type": "function",
        "name": "abrir_bloco_notas",
        "description": (
            "Abre o Bloco de Notas do Windows. "
            "Use quando o usuário pedir para abrir "
            "ou iniciar o bloco de notas."
        ),
        "parameters": {
            "type": "object",
            "properties": {},
        },
    },

    {
        "type": "function",
        "name": "abrir_chrome",
        "description": (
            "Abre o Google Chrome. "
            "Use quando o usuário pedir para abrir "
            "ou iniciar o navegador."
        ),
        "parameters": {
            "type": "object",
            "properties": {},
        },
    },

    {
        "type": "function",
        "name": "abrir_explorador",
        "description": (
            "Abre o Explorador de Arquivos do Windows."
        ),
        "parameters": {
            "type": "object",
            "properties": {},
        },
    },

    {
        "type": "function",
        "name": "desligar_computador",
        "description": (
            "Desliga o computador. "
            "Só use quando o usuário pedir claramente "
            "para desligar o computador."
        ),
        "parameters": {
            "type": "object",
            "properties": {},
        },
    },

    {
        "type": "function",
        "name": "cancelar_desligamento",
        "description": (
            "Cancela um desligamento do computador "
            "que tenha sido agendado."
        ),
        "parameters": {
            "type": "object",
            "properties": {},
        },
    },
]