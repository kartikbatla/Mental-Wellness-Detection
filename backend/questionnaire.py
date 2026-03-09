QUESTIONS = [
    "I feel mentally exhausted by the end of the day.",
    "I feel emotionally supported by people around me.",
    "I find it hard to control my emotions.",
    "I feel calm and relaxed most of the time.",
    "I feel anxious about my future.",
    "I am able to focus on tasks without feeling overwhelmed.",
    "I feel satisfied with my daily routine.",
    "I often feel stressed without knowing why."
]
def conduct_questionnaire():
    print("\n📝 Mental Wellness Questionnaire")
    print("Answer from 1 (Strongly Disagree) to 5 (Strongly Agree)\n")

    responses = []

    for q in QUESTIONS:
        while True:
            try:
                ans = int(input(f"{q}\nYour response (1-5): "))
                if 1 <= ans <= 5:
                    responses.append(ans)
                    break
            except:
                pass
            print("Please enter a number between 1 and 5.")

    return responses
def questionnaire_score(responses):
    """
    Higher score = better mental wellness
    """
    # Reverse score for negative questions
    negative_indices = [0, 2, 4, 7]  # positions of negatively framed questions

    adjusted = []
    for i, r in enumerate(responses):
        if i in negative_indices:
            adjusted.append(6 - r)  # reverse scale
        else:
            adjusted.append(r)

    avg = sum(adjusted) / len(adjusted)

    # Normalize to 0–100
    return round((avg - 1) / 4 * 100)
