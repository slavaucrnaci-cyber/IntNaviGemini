import json
import os

def analyze_roles():
    engine = IntegralAnalyst()
    insights = engine.cross_analyze()
    
    # 1. Считаем роль
    role_scores = {}
    if engine.role_data:
        for ans in engine.role_data:
            scores = ans.get('scores', {})
            for r, score in scores.items():
                role_scores[r] = role_scores.get(r, 0) + score
    
    top_role = max(role_scores, key=role_scores.get) if role_scores else "PIAGET_POSTFORMAL"

    # 2. Добавляем ключ 'moral', чтобы main.py не падал
    # Здесь можно добавить логику оценки (например, если роль Postformal, то мораль Post-conventional)
    moral_level = "Пост-конвенциональная (Интегральная)" 
    
    profile = {
        'role': top_role,
        'moral': moral_level, # ОБЯЗАТЕЛЬНЫЙ КЛЮЧ
        'status': 'Complete'
    }
    
    return profile, insights

class RSS_Analyzer:
    def __init__(self, root_data, shadow_data):
        self.roots = root_data
        self.shadows = shadow_data

    def get_sync_report(self):
        reports = []
        
        # СИНХРОН 1: БЕЗОПАСНОСТЬ -> ТОРМОЖЕНИЕ
        safety_score = self._get_avg('Safety', self.roots)
        brake_score = self._get_avg('Nagoski_SIS_SES', self.shadows)
        if safety_score < 4 and brake_score > 4:
            reports.append("⚠️ [SYNC 0-2y]: Базовая небезопасность блокирует тело. Твой 'тормоз' — это эхо из кроватки.")

        # СИНХРОН 2: ИДЕНТИЧНОСТЬ -> СЦЕНАРИИ
        ident_score = self._get_avg('Identity_Mirroring', self.roots)
        script_score = self._get_avg('Gagnon_Scripts', self.shadows)
        if ident_score > 7 and script_score > 4:
            reports.append("⚠️ [SYNC 3-6y]: Подмена образа в детстве создала 'Актера'. Секс для тебя — театральная постановка.")

        # СИНХРОН 3: ЖЕЛТЫЙ УРОВЕНЬ -> БАЙПАС
        if self._is_yellow() and self._get_avg('Energy_Tantra', self.shadows) > 4:
            reports.append("💡 [INTELLECTUAL BYPASS]: Риск ухода в 'энергии', чтобы не чувствовать реальную боль привязанности.")

        return reports

    def _get_avg(self, cluster, dataset):
        # Вспомогательная функция для расчета среднего по кластеру
        vals = [d['score'] for d in dataset if d.get('cluster') == cluster]
        return sum(vals) / len(vals) if vals else 0

class IntegralAnalyst:
    def __init__(self):
        self.trauma_data = self._load_json('user_answers.json')
        self.role_data = self._load_json('role_answers.json')

    def _load_json(self, path):
        if os.path.exists(path):
            try:
                with open(path, 'r', encoding='utf-8') as f:
                    return json.load(f)
            except Exception:
                return None
        return None

    def cross_analyze(self):
        if not self.trauma_data or not self.role_data:
            return ["❌ Недостаточно данных для кросс-анализа."]

        # Проверка дефицитов (инвертированная логика: score < 4 — это высокая боль)
        trust_issue = any(a.get('score', 10) < 4 for a in self.trauma_data if a.get('cluster') == 'Trust')
        autonomy_issue = any(a.get('score', 10) < 4 for a in self.trauma_data if a.get('period') == '2-4_years')
        
        # Анализ ролей
        role_scores = {}
        for ans in self.role_data:
            for role, score in ans.get('scores', {}).items():
                role_scores[role] = role_scores.get(role, 0) + score
        
        top_role = max(role_scores, key=role_scores.get) if role_scores else "N/A"

        insights = []
        
        # Синтез инсайтов
        if autonomy_issue and (top_role == 'role_lawyer' or top_role == 'PIAGET_POSTFORMAL'):
            insights.append("🚩 КРИТИЧЕСКИЙ РАЗРЫВ: Ваша когнитивная сложность и приверженность структуре — это защита от хаоса, вызванного дефицитом автономии (2-4 года).")
        
        if trust_issue and top_role == 'role_peacekeeper':
            insights.append("🚩 ТЕНЕВОЙ ПАТТЕРН: Миротворец — это не выбор, а стратегия безопасности при базовом недоверии.")

        if not insights:
            insights.append("✅ Конфликты между структурой личности и детским опытом сбалансированы.")

        return insights