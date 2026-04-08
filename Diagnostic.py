import json
from collections import Counter

class IntegralDiagnostic:
    def __init__(self, matrix_path, profile_path):
        with open(matrix_path, 'r') as f:
            self.matrix = json.load(f)
        # profile_path пока используем как структуру, куда будем записывать итог
        self.profile_path = profile_path

    def process_answers(self, user_answers):
        # user_answers ожидается в формате: {"CASE_1_HEINZ": "A", "CASE_2_PROJECT": "C", ...}
        results = []
        try:
            for case_id, option_id in user_answers.items():
                case_data = next((item for item in self.matrix if item["id"] == case_id), None)
                if case_data:
                    option = next((opt for opt in case_data["options"] if opt["id"] == option_id), None)
                    if option:
                        results.append(option["impact"])
        except Exception as e:
            print(f"❌ Ошибка при обработке ответов: {e}")
            
        return self.calculate_profile(results)

    def calculate_profile(self, raw_results):
        if not raw_results:
            return {"error": "Нет данных для анализа"}

        # Веса для числового анализа разрывов (GAP)
        weights = {
            "BEIGE": 1, "PURPLE": 2, "RED": 3, "BLUE": 4, "ORANGE": 5, "GREEN": 6, "YELLOW": 7, "TURQUOISE": 8,
            "PRE_OP": 2, "CONCRETE": 4, "FORMAL": 6, "POST_FORMAL": 8,
            "INSTRUMENTAL": 3, "LAW_ORDER": 4, "SOCIAL_CONTRACT": 6, "POST_CONV": 7, "UNIVERSAL": 8
        }

        # Собираем доминирующие стадии по каждой линии
        lines = ["graves", "piaget", "kohlberg", "levinger", "gebser"]
        summary = {}
        scores = {}

        for line in lines:
            line_data = [res[line] for res in raw_results if line in res]
            if line_data:
                most_common = Counter(line_data).most_common(1)[0][0]
                summary[f"dominant_{line}"] = most_common
                # Считаем средний балл для расчета GAP
                scores[f"{line}_score"] = sum(weights.get(val, 5) for val in line_data) / len(line_data)

        # Формируем итоговый отчет
        report = {
            "dominant_graves": summary.get("dominant_graves", "N/A"),
            "dominant_piaget": summary.get("dominant_piaget", "N/A"),
            "dominant_kohlberg": summary.get("dominant_kohlberg", "N/A"),
            "piaget_score": scores.get("piaget_score", 0),
            "kohlberg_score": scores.get("kohlberg_score", 0),
            "raw_stats": summary
        }

        # Сохраняем результат в SubjectModel.json (опционально)
        self.save_profile(report)
        
        return report

    def save_profile(self, report):
        with open(self.profile_path, 'w', encoding='utf-8') as f:
            json.dump(report, f, ensure_ascii=False, indent=4)