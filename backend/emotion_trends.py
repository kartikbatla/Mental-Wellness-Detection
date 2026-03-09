import pandas as pd
from datetime import datetime

# ===============================
# CONFIG
# ===============================

STRESS_EMOTIONS = ["sadness", "fear", "anger"]

STABILITY_MULTIPLIER = 15

EMOTION_WEIGHTS = {
    "joy": +8,
    "love": +10,
    "surprise": +2,
    "neutral": 0,
    "sadness": -8,
    "fear": -10,
    "anger": -6
}

# ===============================
# EMOTION HISTORY (DYNAMIC)
# ===============================

emotion_log = []

def add_emotion(emotion_distribution):
    emotion_log.append({
        "date": datetime.now(),
        "emotion_distribution": emotion_distribution
    })


def get_emotion_df():
    return pd.DataFrame(emotion_log)

# ===============================
# ANALYSIS FUNCTIONS
# ===============================

def emotion_distribution(df):
    """
    Returns average emotion distribution over time
    """
    emotion_totals = {}

    for dist in df["emotion_distribution"]:
        for emotion, prob in dist.items():
            emotion_totals[emotion] = emotion_totals.get(emotion, 0) + prob

    total_entries = len(df)

    averaged = {
        emotion: round(total / total_entries, 2)
        for emotion, total in emotion_totals.items()
    }

    return averaged


def emotional_stability_index(df):
    if len(df) < 2:
        return 1.0

    changes = []

    for i in range(1, len(df)):
        prev = df.iloc[i-1]["emotion_distribution"]
        curr = df.iloc[i]["emotion_distribution"]

        diff = sum(abs(curr[e] - prev.get(e, 0)) for e in curr)
        changes.append(diff)

    avg_change = sum(changes) / len(changes)

    # Normalize to 0–1 (higher = more stable)
    esi = max(0, 1 - avg_change)

    return round(esi, 2)



def early_stress_detection(df):
    avg_dist = emotion_distribution(df)
    esi = emotional_stability_index(df)

    stress_level = sum(avg_dist.get(e, 0) for e in STRESS_EMOTIONS)

    return {
        "early_stress_detected": stress_level >= 0.6 or esi < 0.5,
        "stress_level": round(stress_level, 2),
        "esi": esi
    }


def mental_wellness_score(df):
    avg_dist = emotion_distribution(df)
    esi = emotional_stability_index(df)

    score = 70  # base

    for emotion, ratio in avg_dist.items():
        score += EMOTION_WEIGHTS.get(emotion, 0) * ratio

    score += esi * STABILITY_MULTIPLIER

    score = max(0, min(100, round(score)))

    return score, esi, avg_dist


def wellness_label(score):
    if score >= 80:
        return "Emotionally Stable"
    elif score >= 60:
        return "Mild Emotional Stress"
    elif score >= 40:
        return "Moderate Stress"
    else:
        return "High Emotional Stress"
    
def combined_wellness_score(emotion_score, questionnaire_score):
    # Emotion is dynamic, questionnaire is stabilizing
    return round(0.6 * emotion_score + 0.4 * questionnaire_score)
