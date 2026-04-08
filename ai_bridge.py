import json

def compose_ai_request():
    # 1. Загружаем данные из обоих тестов
    try:
        with open('analysis_report.json', 'r', encoding='utf-8') as f:
            report = json.load(f)
        with open('role_report.json', 'r', encoding='utf-8') as f:
            role_info = json.load(f)
    except FileNotFoundError:
        return "Ошибка: Не все тесты пройдены."

    # 2. Формируем "Контекстный пакет" для ИИ
    user_context = f"""
    ДАННЫЕ ПОЛЬЗОВАТЕЛЯ:
    - Пиковая травма: {report['worst_period']} (Энергопотеря: {report['energy_drain']}%).
    - Текущая Роль: {role_info['dominant_role']}.
    - Моральный уровень: {role_info['moral_level']}.
    - Когнитивный стиль: {role_info['piaget_level']}.
    - Выявленный конфликт: {report.get('root_cause_conflict', 'Скрытый дефицит')}.
    """

    # 3. Соединяем с Системным Промптом
    final_prompt = f"Действуй как Интегральный Аналитик. Проанализируй данные: {user_context}"
    
    return final_prompt