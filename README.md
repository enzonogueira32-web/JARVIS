# JARVIS

observação: este projeto teve que ser descontinuado, pois o programador atualmente não possui a idade necessária para criar uma chave api gratuita

Assistente pessoal para computador desenvolvido em Python, utilizando Machine Learning para entender comandos em linguagem natural e executar ações no computador.

O projeto foi criado como uma forma de estudar e aplicar conceitos de **Machine Learning, processamento de texto e automação em Python**.

## Sobre o projeto

O JARVIS recebe um comando digitado pelo usuário, utiliza um modelo de Machine Learning para identificar a intenção do comando e, depois, executa a ação correspondente.

Exemplo:

```text
Usuário: abre o Google

JARVIS:
Intenção: abrir_google
Confiança: 38.07%
Abrindo o Google.
```

O funcionamento básico é:

```text
Comando do usuário
       ↓
TF-IDF
       ↓
Modelo de Machine Learning
       ↓
Identificação da intenção
       ↓
Ação correspondente
       ↓
Resposta do JARVIS
```

## Funcionalidades atuais

O JARVIS atualmente consegue:

* Identificar saudações
* Informar a hora
* Informar a data
* Responder agradecimentos
* Responder elogios
* Contar piadas
* Mostrar curiosidades
* Conversar de forma simples
* Abrir o Google
* Abrir o YouTube
* Abrir a Calculadora
* Abrir o Bloco de Notas
* Abrir o Discord
* Abrir o Spotify
* Reconhecer comandos de pesquisa
* Reconhecer comandos de cálculo
* Identificar comandos de confirmação e negação
* Encerrar o programa

## Machine Learning

O JARVIS utiliza:

* **TF-IDF** para transformar frases em dados numéricos
* **Multinomial Naive Bayes** para classificar as intenções
* **Scikit-learn** para treinamento e avaliação do modelo
* **Joblib** para salvar o modelo e o vetorizador

As frases utilizadas no treinamento ficam no arquivo:

```text
dados.json
```

Cada intenção possui várias frases diferentes para que o modelo consiga reconhecer maneiras diferentes de fazer o mesmo pedido.

Por exemplo:

```json
{
    "nome": "abrir_calculadora",
    "frases": [
        "abra a calculadora",
        "abre a calculadora",
        "abrir calculadora",
        "quero abrir a calculadora"
    ]
}
```

## Estrutura do projeto

```text
Jarvis/
│
├── dados.json
├── modelo.py
├── modelo_jarvis.pkl
├── vetorizador.pkl
├── jarvis.py
└── acoes.py
```

### `dados.json`

Contém as frases utilizadas para treinar o modelo e suas respectivas intenções.

### `modelo.py`

Responsável por:

* Carregar os dados
* Separar treinamento e teste
* Criar o TF-IDF
* Treinar o Naive Bayes
* Avaliar a acurácia
* Salvar o modelo
* Salvar o vetorizador

### `modelo_jarvis.pkl`

Modelo de Machine Learning treinado.

### `vetorizador.pkl`

TF-IDF treinado utilizado para transformar novos comandos em vetores.

### `jarvis.py`

É o programa principal.

Ele:

1. Recebe o comando do usuário
2. Processa o texto
3. Identifica a intenção
4. Verifica a confiança
5. Executa a ação
6. Retorna uma resposta

### `acoes.py`

Contém as funções responsáveis por executar ações no computador.

Exemplo:

```python
def abrir_calculadora():
    subprocess.Popen(["calc.exe"])
```

## Tecnologias utilizadas

* Python
* Scikit-learn
* TF-IDF
* Multinomial Naive Bayes
* Joblib
* JSON
* Subprocess
* Webbrowser

## Como executar

### 1. Instalar as dependências

No terminal:

```powershell
pip install scikit-learn joblib
```

Caso `pip` não funcione:

```powershell
python -m pip install scikit-learn joblib
```

### 2. Treinar o modelo

Depois de modificar o `dados.json`, execute:

```powershell
python modelo.py
```

O modelo será treinado e os arquivos:

```text
modelo_jarvis.pkl
vetorizador.pkl
```

serão atualizados.

### 3. Executar o JARVIS

Depois:

```powershell
python jarvis.py
```

O programa será iniciado:

```text
Digite 'sair' para encerrar.

Voce:
```

Agora basta digitar um comando.

Exemplo:

```text
Voce: abre o google

Intencao: abrir_google
Confianca: 38.07%
Jarvis: Abrindo o Google.
```

## Exemplos de comandos

```text
abre o google
abre o youtube
abre a calculadora
abre o bloco de notas
abre o discord
abre o spotify

que horas sao
que dia e hoje

conte uma piada
me conte uma curiosidade

quero conversar
me ajuda
```

## Próximos passos

O projeto ainda está em desenvolvimento. Algumas funcionalidades planejadas são:

### JARVIS 2.0

* Reconhecimento de voz
* Respostas por voz
* Ativação por palavra-chave
* Comandos mais naturais

Exemplo:

```text
"Jarvis, abra o Google."
```

### JARVIS 3.0

* Pesquisa na internet
* Controle de aplicativos
* Controle de volume
* Controle de música
* Abertura de arquivos
* Execução de programas
* Automação de tarefas
* Sistema de memória
* Comandos com parâmetros

Um dos objetivos é fazer o JARVIS entender comandos mais complexos, como:

```text
"Jarvis, abre o Google e pesquisa cursos de Python."
```

Nesse estágio, o sistema não precisará apenas identificar a intenção `pesquisar`, mas também extrair o que deve ser pesquisado.

## Objetivo do projeto

O objetivo principal do projeto é estudar, na prática, como combinar **Machine Learning com automação de computadores**.

A ideia é evoluir o JARVIS gradualmente, começando com comandos simples e chegando a um assistente capaz de interpretar comandos mais complexos e realizar tarefas no computador.

## Status

**Em desenvolvimento.**

A primeira versão do sistema de classificação de intenções e execução de ações já está funcionando.

O projeto continuará recebendo novas funcionalidades conforme o desenvolvimento avançar.
