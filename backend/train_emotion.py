import pandas as pd
import pickle
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report, confusion_matrix
import seaborn as sns
import matplotlib.pyplot as plt


from preprocess import clean_text

# Load dataset
data = pd.read_csv("C:\\Users\\batla\\OneDrive\\Desktop\\coding\\mental wellness\\data\\emotions.csv")

# Clean text
data["clean_text"] = data["text"].apply(clean_text)

X = data["clean_text"]
y = data["label"]

print("Class distribution:")
print(data["label"].value_counts())


# Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

# Vectorization
vectorizer = TfidfVectorizer(max_features=6000)
X_train_vec = vectorizer.fit_transform(X_train)
X_test_vec = vectorizer.transform(X_test)

# Model
model = LogisticRegression(
    max_iter=1500,
    multi_class="multinomial",
    solver="lbfgs",
    class_weight="balanced"
)

model.fit(X_train_vec, y_train)

# Evaluation
preds = model.predict(X_test_vec)
print("Accuracy:", accuracy_score(y_test, preds))

# Save model
pickle.dump(model, open("C:\\Users\\batla\\OneDrive\\Desktop\\coding\\mental wellness\\models\\emotion_model.pkl", "wb"))
pickle.dump(vectorizer, open("C:\\Users\\batla\\OneDrive\\Desktop\\coding\\mental wellness\\models\\vectorizer.pkl", "wb"))

print(classification_report(y_test, preds))

cm = confusion_matrix(y_test, preds)
sns.heatmap(cm, annot=True, fmt="d")
plt.show()
