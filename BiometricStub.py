import json
import biometric_bridge  # Это наша "рация", которую мы сделали в Шаге 1

import os

def get_pulse():
    if os.path.exists('biomarkers_log.json'):
        with open('biomarkers_log.json', 'r') as f:
            data = json.load(f)
            return data.get('heart_rate', 0)
    return 0

def get_my_heart_now():
    # Робот спрашивает у рации: "Эй, какой там пульс в облаке?"
    real_pulse = biometric_bridge.get_latest_heart_rate()
    
    if real_pulse:
        print(f"Робот услышал сердце: {real_pulse}")
        return real_pulse
    else:
        print("Связи нет, беру старое число 70")
        return 70

# Сохраняем это в твою "тетрадку" (файл biomarkers_log.json)
def save_to_log(pulse):
    data = {"pulse": pulse, "time": "сейчас"}
    with open('biomarkers_log.json', 'w') as f:
        json.dump(data, f)