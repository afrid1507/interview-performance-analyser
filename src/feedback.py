def generate_feedback(confidence, clarity, emotion):
    strengths = []
    weaknesses = []

    if confidence > 6:
        strengths.append("Good speaking confidence")
    else:
        weaknesses.append("Low confidence")

    if clarity > 6:
        strengths.append("Clear communication")
    else:
        weaknesses.append("Needs structured answers")

    if emotion == "Confident":
        strengths.append("Positive body language")
    else:
        weaknesses.append("Visible nervousness")

    suggestions = [
        "Practice mock interviews",
        "Use STAR method",
        "Maintain eye contact",
        "Slow down speech"
    ]

    return strengths, weaknesses, suggestions
