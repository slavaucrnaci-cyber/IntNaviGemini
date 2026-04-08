import json
import os
from collections import defaultdict

def load_user_data(file_path):
    """Универсальный загрузчик данных из JSON."""
    if not os.path.exists(file_path):
        return None
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            return json.load(f)
    except Exception as e:
        print(f"Ошибка при чтении {file_path}: {e}")
        return None

def get_ai_summary():
    """Сводка по Травмам (Модуль 1) для передачи ИИ."""
    data = load_user_data('user_answers.json')
    if not data: 
        return "Нет данных по прошлому (Модуль 1 не пройден)."

    period_stats = defaultdict(list)
    for entry in data:
        score = (11 - entry['score']) if entry.get('inversion') else entry['score']
        period_stats[entry['period']].append(score)

    early_years = period_stats.get("0-2_years", []) + period_stats.get("2-4_years", [])
    avg_early = sum(early_years) / len(early_years) if early_years else 0
    
    amnesia_note = "Память доступна"
    if 0 < avg_early < 2.5:
        amnesia_note = "ОБНАРУЖЕНА АМНЕЗИЯ/ВЫТЕСНЕНИЕ (0-4 года)."
    
    if not period_stats:
        return "Данные опроса пусты."
        
    averages = {p: sum(s)/len(s) for p, s in period_stats.items()}
    worst_p = max(averages, key=averages.get)
    
    summary = f"""
- Карта прошлого: 80 точек сканирования.
- Статус памяти: {amnesia_note}
- Пиковая зона боли: {worst_p} (уровень {averages[worst_p]:.1f}/10).
- Средняя плотность травматизации: {sum(averages.values())/len(averages):.1f}/10.
    """
    return summary.strip()

def analyze_eros_block():
    """Анализ Модуля 3 (Эрос и Тень)."""
    data = load_user_data('eros_answers.json')
    if not data:
        return "Данные по Эросу отсутствуют. Пройдите этап №3."
    
    stats = defaultdict(list)
    for item in data:
        stats[item['cluster']].append(item['score'])
    
    averages = {c: sum(s)/len(s) for c, s in stats.items()}
    
    # Детектор честности
    lie_score = averages.get('Lie_Detector', 0)
    shadow_honesty = "Высокая" if lie_score < 3.5 else "Критически низкая (Вытеснение/Идеализация)"
    
    # Формируем отчет для ИИ
    report = []
    for cluster, avg in averages.items():
        report.append(f"- {cluster}: {avg:.1f}/5")
    
    summary = f"""
{chr(10).join(report)}
---
- Статус честности в Тени: {shadow_honesty}
- Доминирующий вектор: {max(averages, key=averages.get) if averages else 'N/A'}
    """
    return summary.strip()

def analyze_trauma_map():
    """Глубокий технический анализ Модуля 1 с выводом графиков в консоль."""
    data = load_user_data('user_answers.json')
    if not data:
        print("❌ Ошибка: Нет данных для анализа Модуля 1.")
        return

    period_scores = defaultdict(float)
    period_max = defaultdict(float)
    cluster_scores = defaultdict(float)
    cluster_max = defaultdict(float)

    for entry in data:
        p = entry['period']
        c = entry['cluster']
        w = entry.get('weight', 1)
        score = (11 - entry['score']) if entry.get('inversion') else entry['score']
        
        period_scores[p] += score * w
        period_max[p] += 10 * w
        cluster_scores[c] += score * w
        cluster_max[c] += 10 * w

    print_periods(period_scores, period_max)
    print_clusters(cluster_scores, cluster_max)
    
    patterns = detect_patterns(cluster_scores)
    print_patterns(patterns)

def print_periods(scores, max_scores):
    print("\n--- 📊 ГРАФИК ТРАВМАТИЗАЦИИ ПО ПЕРИОДАМ ---")
    ordered = ["0-2_years", "2-4_years", "4-6_years", "7-9_years", "9-12_years", "12-14_years", "14-16_years", "16-18_years"]
    for p in ordered:
        if p in scores and max_scores[p] > 0:
            perc = (scores[p] / max_scores[p]) * 100
            bar = "█" * int(perc / 5)
            print(f"{p:12} | {bar} {perc:.1f}%")

def print_clusters(scores, max_scores):
    print("\n--- 🧠 ТОП-3 БОЛЕВЫХ КЛАСТЕРА ---")
    sorted_c = sorted(scores.items(), key=lambda x: x[1]/max_scores[x[0]] if max_scores[x[0]] > 0 else 0, reverse=True)
    for c, val in sorted_c[:3]:
        perc = (val / max_scores[c]) * 100
        print(f"{c:20} | {perc:.1f}%")

def detect_patterns(cluster_scores):
    patterns = []
    def is_high(c): return cluster_scores.get(c, 0) > 15
    if is_high("Safety") and is_high("Trust"): patterns.append("Базовое недоверие к миру")
    if is_high("Self_Worth") and is_high("Criticism"): patterns.append("Синдром 'я недостаточно хорош'")
    if is_high("Emotions") and is_high("Loneliness"): patterns.append("Эмоциональная изоляция")
    return patterns

def print_patterns(patterns):
    print("\n--- ⚠️ КЛЮЧЕВЫЕ ПАТТЕРНЫ ---")
    for p in patterns: print(f"• {p}")
    if not patterns: print("Явных паттернов не обнаружено.")

if __name__ == "__main__":
    analyze_trauma_map()