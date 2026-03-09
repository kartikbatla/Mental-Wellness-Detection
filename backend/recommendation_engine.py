def extract_emotion_profile(avg_dist):
    sorted_emotions = sorted(
        avg_dist.items(), key=lambda x: x[1], reverse=True
    )

    primary = sorted_emotions[0][0]
    secondary = sorted_emotions[1][0] if len(sorted_emotions) > 1 else None

    return primary, secondary

def classify_emotional_pattern(esi, stress_level):
    if esi < 0.4 and stress_level > 0.5:
        return "volatile_stress"
    if esi < 0.4:
        return "volatile"
    if stress_level > 0.6:
        return "persistent_stress"
    return "stable"

def generate_personalized_recommendations(
    score,
    avg_dist,
    esi,
    stress_level,
    history_length
):
    recommendations = []

    primary, secondary = extract_emotion_profile(avg_dist)
    pattern = classify_emotional_pattern(esi, stress_level)

    # --- Pattern-based recommendations ---
    if pattern == "volatile_stress":
        recommendations.append(
            "Your emotions show frequent shifts combined with stress. Creating short, predictable routines may help stabilize your mood."
        )

    elif pattern == "volatile":
        recommendations.append(
            "Your emotional state appears unstable. Brief grounding exercises may help you regain balance."
        )

    elif pattern == "persistent_stress":
        recommendations.append(
            "Stress-related emotions have remained high over time. Gradual lifestyle adjustments may be beneficial."
        )

    else:
        recommendations.append(
            "Your emotional patterns appear relatively stable. Maintaining current healthy habits is recommended."
        )

    # --- Emotion-specific personalization ---
    if primary == "anger":
        recommendations.append(
            "Since frustration is prominent, physical activity or controlled breathing may help release built-up tension."
        )

    if primary == "fear":
        recommendations.append(
            "Anxiety appears dominant. Breaking tasks into smaller steps can reduce feelings of overwhelm."
        )

    if primary == "sadness":
        recommendations.append(
            "Low mood seems prevalent. Meaningful social interaction or comforting activities may help."
        )

    if primary == "love":
        recommendations.append(
            "Positive emotional connection is strong. Continue nurturing relationships that provide support."
        )

    if primary == "surprise":
        recommendations.append(
            "Unexpected emotional shifts are noticeable. Reflecting on recent events may help you process these changes."
        )

    # --- Secondary emotion nuance ---
    if secondary:
        recommendations.append(
            f"Alongside {primary}, elements of {secondary} are present. Addressing both may improve emotional balance."
        )

    # --- Severity-based escalation ---
    if score < 40:
        recommendations.append(
            "If emotional distress continues, seeking professional guidance may be helpful."
        )

    # --- Personalization over time ---
    if history_length < 5:
        recommendations.append(
            "As more entries are added, insights will become more personalized and accurate."
        )

    return recommendations
