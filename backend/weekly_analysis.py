import json
from database import fetch_last_n_days

def get_weekly_data():
    df = fetch_last_n_days(days=7)

    if df.empty:
        return None

    # Convert emotion_distribution from JSON string to dict
    df["emotion_distribution"] = df["emotion_distribution"].apply(json.loads)

    return df
def weekly_emotion_distribution(df):
    emotion_totals = {}

    for dist in df["emotion_distribution"]:
        for emotion, value in dist.items():
            emotion_totals[emotion] = emotion_totals.get(emotion, 0) + value

    total_entries = len(df)

    return {
        emotion: round(total / total_entries, 2)
        for emotion, total in emotion_totals.items()
    }
def weekly_wellness_metrics(df):
    avg_score = round(df["wellness_score"].mean(), 1)
    avg_esi = round(df["esi"].mean(), 2)
    avg_stress = round(df["stress_level"].mean(), 2)

    return avg_score, avg_esi, avg_stress
def detect_weekly_trend(df):
    midpoint = len(df) // 2

    first_half = df.iloc[:midpoint]
    second_half = df.iloc[midpoint:]

    stress_change = (
        second_half["stress_level"].mean()
        - first_half["stress_level"].mean()
    )

    score_change = (
        second_half["wellness_score"].mean()
        - first_half["wellness_score"].mean()
    )

    return round(score_change, 2), round(stress_change, 2)
def generate_weekly_insights(
    emotion_dist,
    avg_score,
    avg_esi,
    stress_trend,
    score_trend
):
    insights = []

    dominant_emotion = max(emotion_dist, key=emotion_dist.get)

    insights.append(
        f"This week, {dominant_emotion} was the most prominent emotion."
    )

    if score_trend > 0:
        insights.append(
            "Your overall mental wellness showed improvement as the week progressed."
        )
    elif score_trend < 0:
        insights.append(
            "Mental wellness declined slightly toward the end of the week."
        )
    else:
        insights.append(
            "Mental wellness levels remained relatively consistent throughout the week."
        )

    if stress_trend > 0:
        insights.append(
            "Stress-related emotions increased during the latter part of the week."
        )
    else:
        insights.append(
            "Stress levels remained stable or decreased during the week."
        )

    if avg_esi < 0.4:
        insights.append(
            "Emotional stability was low this week, indicating frequent mood shifts."
        )
    elif avg_esi < 0.7:
        insights.append(
            "Some emotional fluctuations were observed this week."
        )
    else:
        insights.append(
            "Your emotions remained relatively stable throughout the week."
        )

    return insights
