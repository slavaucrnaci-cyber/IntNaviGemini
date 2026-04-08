import json
import os

class SurveyEngine:
    def __init__(self):
        self.user_data_path = 'user_answers.json'

    def load_questions(self, file_path):
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                return json.load(f)
        except FileNotFoundError:
            print(f"❌ Ошибка: Файл {file_path} не найден.")
            return []

    def print_scale(self):
        """Выводит визуальную подсказку шкалы для Модуля 1."""
        print("   [ 1 --- 2 --- 3 --- 4 --- 5 --- 6 --- 7 --- 8 --- 9 --- 10 ]")
        print("     НЕТ (Совсем не так) <----------------------> ДА (Именно так)")
        print("     (Макс. дискомфорт)                          (Полный комфорт)")

    def run_survey(self, questions_file='module1_trauma.json', save_file='user_answers.json'):
        questions = self.load_questions(questions_file)
        if not questions:
            return

        answers = []
        option_letters = ["A", "B", "C", "D", "E"]

        for q in questions:
            print("\n" + "="*70)
            print(f"[{q.get('id', '??')}] ПЕРИОД: {q.get('period', 'N/A')} | КЛАСТЕР: {q.get('cluster', 'N/A')}")
            if q.get('scenario'): print(f"🎬 СЦЕНАРИЙ: {q['scenario']}")
            print(f"❓ {q.get('question', 'Нет текста вопроса')}")
            print("-" * 70)

            # ЛОГИКА 1: Если есть варианты ответов (Модуль 2 / Кейсы)
            if 'options' in q:
                for i, option in enumerate(q['options']):
                    opt_text = option['text'] if isinstance(option, dict) else option
                    print(f"  {i+1}. {opt_text}")

                while True:
                    choice = input("\n📝 Ваш выбор (номер): ").strip()
                    if choice.isdigit() and 1 <= int(choice) <= len(q['options']):
                        idx = int(choice) - 1
                        selected = q['options'][idx]
                        
                        answer_data = {
                            "id": q.get('id'),
                            "selected_option": option_letters[idx] if idx < len(option_letters) else str(idx + 1),
                            "period": q.get('period'),
                            "cluster": q.get('cluster'),
                            "question": q['question'],
                            "weight": q.get('weight', 1)
                        }

                        if isinstance(selected, dict):
                            answer_data["score"] = selected.get('score')
                            answer_data["scores"] = selected.get('scores')
                        else:
                            answer_data["score"] = idx + 1
                            
                        answers.append(answer_data)
                        break
                    print(f"❌ Ошибка! Выберите число от 1 до {len(q['options'])}")

            # ЛОГИКА 2: Шкала 1-10 (Модуль 1 / 80 вопросов)
            else:
                self.print_scale() # ВЫВОДИМ ПОДСКАЗКУ
                while True:
                    choice = input("\n📝 Ваша оценка (1-10): ").strip()
                    if choice.isdigit() and 1 <= int(choice) <= 10:
                        score = int(choice)
                        answers.append({
                            "id": q.get('id'),
                            "period": q.get('period'),
                            "cluster": q.get('cluster'),
                            "score": score,
                            "weight": q.get('weight', 1),
                            "inversion": q.get('inversion', False),
                            "question": q['question']
                        })
                        break
                    print("❌ Ошибка! Введите целое число от 1 до 10.")

        # Сохранение
        with open(save_file, 'w', encoding='utf-8') as f:
            json.dump(answers, f, ensure_ascii=False, indent=2)
        
        print(f"\n✅ Модуль завершен. Данные сохранены в {save_file}")

if __name__ == "__main__":
    engine = SurveyEngine()
    engine.run_survey()