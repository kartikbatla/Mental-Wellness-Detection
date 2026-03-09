import pickle
from preprocess import clean_text

label_map = {
    0: "sadness",
    1: "joy",
    2: "love",
    3: "anger",
    4: "fear",
    5: "surprise"
}

model = pickle.load(open("C:\\Users\\batla\\OneDrive\\Desktop\\coding\\mental wellness\\models\\emotion_model.pkl", "rb"))
vectorizer = pickle.load(open("C:\\Users\\batla\\OneDrive\\Desktop\\coding\\mental wellness\\models\\vectorizer.pkl", "rb"))

def predict_emotion_distribution(text):
    cleaned = clean_text(text)
    vec = vectorizer.transform([cleaned])
    probs = model.predict_proba(vec)[0]

    emotion_distribution = {
        label_map[i]: round(float(probs[i]), 2)
        for i in range(len(probs))
    }

    return emotion_distribution
