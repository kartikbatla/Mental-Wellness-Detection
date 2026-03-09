import json
import matplotlib.pyplot as plt
from database import fetch_last_n_days

def plot_weekly_emotion_distribution():
    df = fetch_last_n_days(days=7)

    if df.empty:
        print("Not enough data to generate emotion distribution chart.")
        return

    df["emotion_distribution"] = df["emotion_distribution"].apply(json.loads)

    emotion_totals = {}

    for dist in df["emotion_distribution"]:
        for emotion, value in dist.items():
            emotion_totals[emotion] = emotion_totals.get(emotion, 0) + value

    emotions = list(emotion_totals.keys())
    values = [v / len(df) for v in emotion_totals.values()]

    plt.figure()
    plt.bar(emotions, values)
    plt.title("Weekly Emotion Distribution")
    plt.xlabel("Emotion")
    plt.ylabel("Average Intensity")
    plt.tight_layout()
    plt.show()

def plot_wellness_score_trend():
    df = fetch_last_n_days(days=7)

    if df.empty:
        print("Not enough data to generate wellness score chart.")
        return

    plt.figure()
    plt.plot(df["date"], df["wellness_score"])
    plt.title("Wellness Score Trend (Last 7 Days)")
    plt.xlabel("Date")
    plt.ylabel("Wellness Score")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

def plot_stress_level_trend():
    df = fetch_last_n_days(days=7)

    if df.empty:
        print("Not enough data to generate stress level chart.")
        return

    plt.figure()
    plt.plot(df["date"], df["stress_level"])
    plt.title("Stress Level Trend (Last 7 Days)")
    plt.xlabel("Date")
    plt.ylabel("Stress Level")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    plot_weekly_emotion_distribution()
    plot_wellness_score_trend()
    plot_stress_level_trend()
