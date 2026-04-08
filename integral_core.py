import json

class IntegralCore:
    def __init__(self, trauma_path='user_answers.json', role_path='role_answers.json'):
        self.trauma = self._load(trauma_path)
        self.roles = self._load(role_path)

    def _load(self, path):
        try:
            with open(path, 'r', encoding='utf-8') as f: return json.load(f)
        except: return None

    def get_summary_for_ai(self):
        # 1. Считаем среднюю боль по периодам
        # 2. Находим пиковую роль и моральный уровень
        # 3. Формируем "Конфликтный пакет"
        
        summary = {
            "critical_trauma_period": "4-6_years", # Пример расчета
            "dominant_role": "Strategist",
            "moral_level": "Law and Order",
            "cognitive_complexity": "High",
            "detected_gap": "Strategy vs Rules" 
        }
        return summary

# Теперь этот summary отправляется в LLM (Gemini/GPT)
