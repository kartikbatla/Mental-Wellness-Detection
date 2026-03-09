import pickle
from preprocess import clean_text
import os
import pickle

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

label_map = {
    0: "sadness",
    1: "joy",
    2: "love",
    3: "anger",
    4: "fear",
    5: "surprise"
}

MODEL_PATH = os.path.join(BASE_DIR, "models", "emotion_model.pkl")
Vector_Path = os.path.join(BASE_DIR, "vectorizer", "vectorizer.pkl")
model = pickle.load(open(MODEL_PATH, "rb"))
vectorizer = pickle.load(open(Vector_Path, "rb"))

def predict_emotion_distribution(text):
    cleaned = clean_text(text)
    vec = vectorizer.transform([cleaned])
    probs = model.predict_proba(vec)[0]

    emotion_distribution = {
        label_map[i]: round(float(probs[i]), 2)
        for i in range(len(probs))
    }

    return emotion_distribution
