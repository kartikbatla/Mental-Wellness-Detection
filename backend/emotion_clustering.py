import numpy as np
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

def build_feature_vector(avg_dist, esi, stress_level):
    return [
        avg_dist.get("anger", 0),
        avg_dist.get("sadness", 0),
        avg_dist.get("fear", 0),
        avg_dist.get("joy", 0),
        avg_dist.get("love", 0),
        avg_dist.get("surprise", 0),
        esi,
        stress_level
    ]
class EmotionClusterModel:
    def __init__(self, n_clusters=4):
        self.scaler = StandardScaler()
        self.model = KMeans(n_clusters=n_clusters, random_state=42)
        self.fitted = False
        self.data = []

    def add_sample(self, feature_vector):
        self.data.append(feature_vector)

    def fit(self):
        X = np.array(self.data)
        X_scaled = self.scaler.fit_transform(X)
        self.model.fit(X_scaled)
        self.fitted = True

    def predict_cluster(self, feature_vector):
        if not self.fitted:
            return None
        fv_scaled = self.scaler.transform([feature_vector])
        return int(self.model.predict(fv_scaled)[0])
CLUSTER_LABELS = {
    0: "Stable-Positive",
    1: "Emotionally Volatile",
    2: "Stress-Dominant",
    3: "Low-Expressive"
}

def interpret_cluster(cluster_id):
    return CLUSTER_LABELS.get(cluster_id, "Unclassified")

def cluster_based_guidance(cluster_name):
    if cluster_name == "Stress-Dominant":
        return [
            "Stress-related emotions appear consistently high. Structured rest and workload management may help.",
            "Consider prioritizing recovery-oriented activities."
        ]

    if cluster_name == "Emotionally Volatile":
        return [
            "Emotional fluctuations are frequent. Establishing predictable routines may increase stability.",
            "Short grounding practices can help during emotional transitions."
        ]

    if cluster_name == "Stable-Positive":
        return [
            "Your emotional patterns are balanced. Continue maintaining habits that support well-being."
        ]

    if cluster_name == "Low-Expressive":
        return [
            "Emotional expression appears subdued. Reflective journaling may help increase emotional awareness."
        ]

    return []
