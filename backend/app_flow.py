import pandas as pd
from datetime import datetime

from database import create_tables, insert_journal_entry
from questionnaire import questionnaire_score
from recommendation_engine import generate_personalized_recommendations
from predict_emotion import predict_emotion_distribution

from emotion_trends import (
    add_emotion,
    get_emotion_df,
    early_stress_detection,
    mental_wellness_score,
    wellness_label,
    combined_wellness_score
)

from weekly_analysis import (
    get_weekly_data,
    weekly_emotion_distribution,
    weekly_wellness_metrics,
    detect_weekly_trend,
    generate_weekly_insights
)


def run_app_flow(user_text: str, questionnaire_answers: list):
    
    # 1️⃣ Ensure database exists
    create_tables()

    # 2️⃣ Emotion prediction (SYSTEM CONTROLLED)
    emotion = predict_emotion_distribution(user_text)

    # 3️⃣ Store emotion snapshot
    add_emotion(emotion)

    # 4️⃣ Fetch emotion history
    df = get_emotion_df()

    # 5️⃣ If not enough data, return minimal response
    if len(df) < 1:
        return {
            "message": "Not enough data to generate full wellness report yet.",
            "emotion_distribution": emotion
        }

    # 6️⃣ Core wellness calculations
    score, esi, dist = mental_wellness_score(df)
    stress = early_stress_detection(df)

    # 7️⃣ Store journal entry
    insert_journal_entry(
        journal_text=user_text,
        emotion_distribution=dist,
        wellness_score=score,
        esi=esi,
        stress_level=stress["stress_level"]
    )

    # 8️⃣ Generate personalized recommendations
    recommendations = generate_personalized_recommendations(
        score=score,
        avg_dist=dist,
        esi=esi,
        stress_level=stress["stress_level"],
        history_length=len(df)
    )

    # 9️⃣ Questionnaire integration (existing logic)

    q_score = questionnaire_score(questionnaire_answers)

    # 🔟 Final combined score
    final_score = combined_wellness_score(score, q_score)

    # ✅ RETURN STRUCTURED REPORT (FOR FRONTEND)
    return {
        "emotion_distribution": dist,
        "emotion_based_score": score,
        "questionnaire_score": q_score,
        "final_wellness_score": final_score,
        "status": wellness_label(final_score),
        "emotional_stability_index": esi,
        "stress_detected": stress["early_stress_detected"],
        "stress_level": stress["stress_level"],
        "recommendations": recommendations
    }
