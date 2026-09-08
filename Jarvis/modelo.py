import json
import joblib

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score


with open("dados.json", "r", encoding="utf-8") as arquivo:
    dados = json.load(arquivo)


frases = []
intencoes = []


for intencao in dados["intencoes"]:
    for frase in intencao["frases"]:
        frases.append(frase)
        intencoes.append(intencao["nome"])


X_treino, X_teste, y_treino, y_teste = train_test_split(
    frases,
    intencoes,
    test_size=0.2,
    random_state=42
)


vetorizador = TfidfVectorizer()

X_treino = vetorizador.fit_transform(X_treino)
X_teste = vetorizador.transform(X_teste)


modelo = MultinomialNB()

modelo.fit(X_treino, y_treino)


previsoes = modelo.predict(X_teste)

acuracia = accuracy_score(y_teste, previsoes)

print(f"Acuracia: {acuracia:.2f}")


joblib.dump(modelo, "modelo_jarvis.pkl")
joblib.dump(vetorizador, "vetorizador.pkl")

print("Modelo treinado com sucesso!")