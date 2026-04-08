class GrandsonMode:
    def __init__(self, age):
        self.age = age

    def adapt_concept(self, concept_name):
        if self.age < 7:
            return f"Объясняем '{concept_name}' через Игру и Мифологию (Стадия Пиаже: Дооперациональная)"
        elif 7 <= self.age < 12:
            return f"Объясняем '{concept_name}' через Конкретные правила и Логику (Стадия Пиаже: Конкретные операции)"
        else:
            return f"Объясняем '{concept_name}' через Системы и Абстракции"