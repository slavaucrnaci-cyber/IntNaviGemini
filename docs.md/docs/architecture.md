# Architecture Overview

The system is designed with a **Fractal Modular Core**, allowing for seamless updates without breaking global logic.

## 1. Interaction Layer
* `bot_sovereign.py`: The primary agent interface. Handles tone, persona, and intent recognition.
* `GuestMirror.py`: Specialized module for rapid diagnostic of third-party users.

## 2. Processing Layer (The Engine)
* `integral_engine.py`: Processes semantic inputs through the lens of Integral Theory (AQAL).
* `DevelopmentPath.py`: Maps the user's trajectory across cognitive and ego stages.

## 3. Somatic/Biometric Bridge
* `biometric_bridge.py`: Connects real-time physiological markers to the cognitive analysis.
* `body_map.json`: A digital twin of the user's somatic tensions and "trauma nodes."

## 4. Knowledge Base (JSON Modules)
* `module1_trauma.json`: The "Johnson Protocol" for deconstructing core developmental wounds.
* `module3_eros.json`: Psycho-sexual energy and maturity mapping.

# Архитектура Системы v10.2

Система построена по модульному принципу, что позволяет тиражировать ядро, адаптируя только «слой данных» под конкретного пользователя.

### Основные компоненты (Core):
* **bot_sovereign.py:** Главный оркестратор смыслов и ролевых моделей.
* **integral_engine.py:** Вычислительное ядро, сопоставляющее ответы пользователя с картами развития (Грейвз, Кеган).
* **biometric_bridge.py:** Интерфейс взаимодействия с физическими маркерами (HRV, темпо-ритм речи).
* **ai_bridge.py:** Логика взаимодействия с LLM (Large Language Models) для глубокого семантического анализа.

### База знаний (JSON-модули):
* `module1_trauma.json`: Сетка деконструкции по Джонсону (v10.2).
* `module2_levels.json`: Матрица вертикального развития.
* `module3_eros.json`: Психосексуальные стадии и энергетические блоки.
* `module6_evolution.json`: Сценарии бесконечного становления.

### Пайплайн обработки:
`Входной сигнал (Аудио/Текст) -> Биометрический фильтр -> Семантическое зеркало -> Интегральный вывод -> Override-инструкция`.