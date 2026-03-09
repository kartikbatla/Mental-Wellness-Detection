import random

emotion_quotes = {
    "sadness": [
        "Even the heaviest rain eventually gives way to sunlight.",
        "It’s okay to feel low. Healing happens quietly.",
        "This moment is not your forever."
    ],
    "fear": [
        "Courage isn’t the absence of fear — it’s moving forward anyway.",
        "You are stronger than your doubts.",
        "Growth begins outside your comfort zone."
    ],
    "anger": [
        "Pause. Breathe. Power is in calm decisions.",
        "Anger is energy — channel it wisely.",
        "Stillness brings clarity."
    ],
    "joy": [
        "Let this happiness expand beyond today.",
        "Your light deserves to shine boldly.",
        "Celebrate even the smallest wins."
    ],
    "neutral": [
        "Every day is a new beginning.",
        "Consistency builds strength.",
        "Small progress is still progress."
    ]
}

def generate_quote(emotion_distribution: dict):
    if not emotion_distribution:
        return random.choice(emotion_quotes["neutral"])

    dominant = max(emotion_distribution, key=emotion_distribution.get)

    if dominant in emotion_quotes:
        return random.choice(emotion_quotes[dominant])

    return random.choice(emotion_quotes["neutral"])
