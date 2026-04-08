def check_for_hallucination(ai_answer, sensor_data):
    if ai_answer == "All Good" and sensor_data == "High Stress":
        return "ALARM: System is hallucinating!"
    else:
        return "System is honest."