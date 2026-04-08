import json
import os
import analytics  # Твой обновленный файл с расчетами

class IntegralAgent:
    def __init__(self):
        self.user_data_path = 'user_answers.json'
        self.role_data_path = 'role_results.json'
        self.report_path = 'analysis_report.json'

    def load_json(self, path):
        if os.path.exists(path):
            with open(path, 'r', encoding='utf-8') as f:
                return json.load(f)
        return None

    def cross_calculate(self):
        """Связывает данные о травмах и текущих ролях."""
        trauma_data = self.load_json(self.user_data_path)
        role_data = self.load_json(self.role_data_path)

        if not trauma_data or not role_data:
            return None

        # Базовая логика извлечения данных
        role = role_data.get('dominant_role', 'YELLOW')
        moral = role_data.get('moral_level', 'UNIVERSAL')
        # Пример расчета разрыва (можно усложнить)
        gap = 2.5 

        return {
            "top_role": role,
            "moral_level": moral,
            "gap_value": gap,
            "cognitive_stage": "Postformal"
        }

    def generate_final_mirror(self):
        """Формирует финальный пакет данных для копирования в чат ИИ."""
        analysis = self.cross_calculate()
        
        if not analysis:
            print("❌ Ошибка: Недостаточно данных. Пройдите Модуль 1 и Модуль 2.")
            return

        # 1. Получаем краткий отчет по 80 вопросам из analytics.py
        trauma_brief = analytics.get_ai_summary()
        
        # 2. Пытаемся достать выявленные паттерны из отчета
        report = self.load_json(self.report_path)
        patterns = ", ".join(report.get('patterns', ["Требуется глубокий анализ"])) if report else "Анализ не запущен"

        # 3. Печать блока для копирования
        print("\n" + "="*60)
        print("✅ ИНТЕГРАЛЬНЫЙ ПАКЕТ СФОРМИРОВАН")
        print("--- СКОПИРУЙ ТЕКСТ НИЖЕ И ВСТАВЬ В ЧАТ С ИИ ---")
        print("="*60)
        
        prompt = f"""
[ADVANCED INTEGRAL SCAN]
1. HARD DATA (Python Output):
   - Roles: {analysis['top_role']}
   - Moral: {analysis['moral_level']}
   - Cognitive Gap: {analysis['gap_value']}
   
2. TRAUMA MAP (Module 1 - 80 points):
{trauma_brief}
   - Dominant Pattern: {patterns}
   
3. AI TASK (Thin Diagnosis):
   - ИИ, проанализируй связку между Ролью {analysis['top_role']} и выявленными зонами боли.
   - Учти фактор амнезии, если он указан в 'Статусе памяти'.
   - Вскрой компенсацию и ЗАДАЙ 1 ПАРАДОКСАЛЬНЫЙ ВОПРОС, который пробьет систему защиты.
        """
        print(prompt)
        print("="*60)

    def show_menu(self):
        while True:
            print("\n--- 🧠 INTEGRAL ANALYST SYSTEM V.9.2 ---")
            print("1. Пройти Модуль 1 (Травмы 0-18 лет / 80 вопросов)")
            print("2. Пройти Модуль 2 (Роли и Мораль)")
            print("3. Сформировать Интегральное Зеркало (Пакет для ИИ)")
            print("4. Выход")
            
            choice = input("\nВыберите действие: ")
            
            if choice == '1':
                # Здесь должен быть твой вызов опросника Модуля 1
                print("Запуск Модуля 1...") 
                # analytics.analyze_trauma_map() - вызываем после прохождения
            elif choice == '2':
                print("Запуск Модуля 2...")
            elif choice == '3':
                # Сначала обновляем аналитику по 80 вопросам
                analytics.analyze_trauma_map()
                # Затем генерируем зеркало
                self.generate_final_mirror()
            elif choice == '4':
                break
            else:
                print("Неверный выбор.")

if __name__ == "__main__":
    agent = IntegralAgent()
    agent.show_menu()