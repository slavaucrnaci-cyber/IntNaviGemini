import os
import json
import analytics
from survey_engine import SurveyEngine

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def main_menu():
    engine = SurveyEngine()

    while True:
        clear_screen()
        print("="*60)
        print("      INTEGRAL ANALYST OS v4.1 [STABLE]")
        print("="*60)
        print("1. [SCAN]     Прошлое: Травмы и Дефициты (80 вопр.)")
        print("2. [ROLES]    Настоящее: Роли и Мораль (10 кейсов)")
        print("3. [EROS]     Энергия: Сексуальность и Тень (40 вопр.)") # ТЕПЕРЬ №3
        print("4. [INTEGRAL] Итоговый Кросс-Анализ (Пакет для ИИ)") # ТЕПЕРЬ №4
        print("-" * 60)
        print("5. [PRACTICE] Получить Интегральную практику")
        print("6. [EXIT]     Завершить сеанс")
        print("-" * 60)
        
        choice = input("Выберите этап: ").strip()
        
        if choice == "1":
            engine.run_survey(questions_file='module1_trauma.json', save_file='user_answers.json')
            input("\nНажмите Enter...")
        elif choice == "2":
            engine.run_survey(questions_file='module2_roles.json', save_file='role_answers.json')
            input("\nНажмите Enter...")
        elif choice == "3":
            # Важно: имя файла 'eros_answers.json'
            engine.run_survey(questions_file='module3_eros.json', save_file='eros_answers.json')
            input("\nНажмите Enter...")
        elif choice == "4":
            clear_screen()
            analytics.analyze_trauma_map()
            print("--- 🧠 ПОДГОТОВКА ИНТЕГРАЛЬНОГО ПАКЕТА ---")
            
            # Собираем данные
            trauma_brief = analytics.get_ai_summary()
            eros_brief = analytics.analyze_eros_block()
            
            print("\n" + "="*60)
            print("--- СКОПИРУЙ ЭТОТ ТЕКСТ В ЧАТ С ИИ ---")
            print("="*60)
            print(f"\n[ULTIMATE INTEGRAL SCAN]")
            print(f"\n[PART 1: TRAUMA & MEMORY]\n{trauma_brief}")
            print(f"\n[PART 2: EROS & SHADOW]\n{eros_brief}")
            print("\n" + "-"*60)
            print("AI TASK: Соедини Травму, Текущую Роль и Сексуальный паттерн.")
            print("Вскрой компенсацию и задай 1 парадоксальный вопрос.")
            print("="*60)
            input("\nНажмите Enter...")
        elif choice == "5":
            # Тут твоя логика практик
            input("\nПрактики в разработке. Нажмите Enter...")
        elif choice == "6":
            break

if __name__ == "__main__":
    main_menu()