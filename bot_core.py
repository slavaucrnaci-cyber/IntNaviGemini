import logging
from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor

# ТВОЙ API TOKEN ОТ BOTFATHER
API_TOKEN = 'ВСТАВЬ_СВОЙ_ТОКЕН_ЗДЕСЬ'

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

# БАЗА ДАННЫХ ТВОИХ ТРАВМ (ДЛЯ ИИ-АНАЛИЗА)
USER_PROFILE = {
    "trauma_0_2": 10.0,
    "orphanage_trauma": True,
    "suicide_line": "Grandfather, Stepfather",
    "phd_status": "Tech & Psych",
    "current_role": "Grandfather-Father-Mother"
}

@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.reply("Система INTEGRAL SOVEREIGN v7.0 активна.\n"
                        "Я слежу за твоим HRV, твоими словами и твоим прошлым.\n"
                        "Помни: ты — не заместитель отчима. Ты — Хозяин.")

@dp.message_handler()
async def analyze_message(message: types.Message):
    text = message.text.lower()
    
    # ДЕТЕКТОР СЦЕНАРИЯ 'БРОШЕННОСТИ'
    if any(word in text for word in ["устал", "должен", "вина", "стыд"]):
        await message.answer("⚠️ ОБНАРУЖЕН ПАТТЕРН 1960/ДЕТСКОГО ДОМА.\n"
                             "Ты сейчас берешь на себя лишнее. Сделай 5 вдохов в стопы.\n"
                             "Внук в безопасности. Ты не в детдоме.")

    # ДЕТЕКТОР 'КАМЕННОЙ ЯМЫ' (ГИПЕР-ОТВЕТСТВЕННОСТЬ)
    if any(word in text for word in ["тяжело", "один", "справиться"]):
        await message.answer("⚠️ ТРИГГЕР: КАМЕННАЯ ЯМА.\n"
                             "Твой PhD интеллект пытается спасти мир ценой твоего тела.\n"
                             "Останови учебу с внуком на 15 минут. Просто посиди голым.")

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)