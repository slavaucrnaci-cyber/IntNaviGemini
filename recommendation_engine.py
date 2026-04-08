import json

def suggest_practice():
    try:
        with open('analysis_report.json', 'r', encoding='utf-8') as f:
            analysis = json.load(f)
        worst_period = analysis['worst_period']
    except FileNotFoundError:
        print("❌ Сначала запустите Анализ (пункт 2)!")
        return

    try:
        with open('module5_practices.json', 'r', encoding='utf-8') as f:
            practices = json.load(f)
    except FileNotFoundError:
        print("❌ Файл практик не найден!")
        return

    print(f"\n--- 🏥 РЕКОМЕНДАЦИЯ НА ОСНОВЕ ПАТТЕРНОВ ---")
    print(f"Целевой период для проработки: {worst_period}")
    
    found = False
    for p in practices:
        if p.get('target_age') == worst_period:
            print(f"\nРЕКОМЕНДУЕМАЯ ПРАКТИКА: ⭐ {p['name']} ⭐")
            print(f"ОПИСАНИЕ: {p['description']}")
            found = True
            break
    
    if not found:
        print("\nДля данного периода специфическая практика еще не добавлена.")
        print("Рекомендуется общая практика: 'Длинный выдох'.")

if __name__ == "__main__":
    suggest_practice()