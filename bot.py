import logging
import os
import random
from telegram import Update, ReplyKeyboardMarkup, KeyboardButton
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters

logging.basicConfig(
    format='%(asctime)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

TOKEN = os.getenv("BOT_TOKEN")  # Токен нужно задать через переменную окружения на PythonAnywhere

CARDS = {
    "Влюбленные": {
        "text": (
            "*Влюбленные*\n\n"
            "_«Больше нету стен, между нами нет запретных тем»_ 🔮\n\n"
            "Любовь, выбор сердца и гармония — твой союз с миром начинается сегодня."
        ),
        "sticker": "CAACAgIAAxkBAANNaIeS9tyjbeUjm0T4whBVt6asa1UAAid6AAJlKEFI-GWfehzR0r42BA"
    },
    "Шут": {
        "text": (
            "*Шут*\n\n"
            "_«Я так хочу увидеть, что еще не видел!»_ 🌠\n\n"
            "Свобода и новые начала — смело шагай навстречу приключениям, без страха и сомнений."
        ),
        "sticker": "CAACAgIAAxkBAANPaIeTOIUYnErq4zVJlGAe1r2Cn0kAAix7AAIe5DhIGxPWIGTiTUk2BA"
    },
    "Маг": {
        "text": (
            "*Маг*\n\n"
            "_«Как плотно и тонко наша Вселенная соткана»_ ✨\n\n"
            "Ты владеешь всеми инструментами — создай свою реальность силой намерения."
        ),
        "sticker": "CAACAgIAAxkBAANRaIeTQmnY6Gr8dOov6inH9vNPC0oAAst9AAJVW0FIiRPKDiMyWFA2BA"
    },
    "Императрица": {
        "text": (
            "*Императрица*\n\n"
            "_«Среди морей лесов или четырех стен…пусть тебе будет легко!»_ 🌌\n\n"
            "Творчество и изобилие растут вокруг тебя — время дать мечтам форму."
        ),
        "sticker": "CAACAgIAAxkBAANTaIeTUgxSf7hIrcHhSCV2rpyp2L8AAo5_AALcmUBICHXd-o6GXh02BA"
    },
    "Колесница": {
        "text": (
            "*Колесница*\n\n"
            "_«Ты как ночная дорога\nТысячи поворотов»_ 🌑\n\n"
            "Воля и решимость ведут тебя к победе — держи курс и не сбивайся."
        ),
        "sticker": "CAACAgIAAxkBAANVaIeTX2sJfP1N_r8BnoQ92PDXymgAAnB7AAJaLThI-9Vmw4EvUSw2BA"
    },
    "Звезда": {
        "text": (
            "*Звезда*\n\n"
            "_«Я же видела\nКак ты можешь\nИз обломков наугад — складывать созвездия»_ 💫\n\n"
            "Надежда и вдохновение светят в темноте — верь в чудеса и мечты."
        ),
        "sticker": "CAACAgIAAxkBAANXaIeTdjfNtSET3DQTG9TYOG2Gy0wAAnJ0AAL3-zhINYfvz723GWw2BA"
    },
    "Луна": {
        "text": (
            "*Луна*\n\n"
            "_«Ты понимаешь, — наверху за нас давно всё налажено»_ 🌙\n\n"
            "Ваша луна в ударе! Интуиция и тайны манят — доверься внутреннему свету и своей мудрости."
        ),
        "sticker": "CAACAgIAAxkBAANZaIeTieDALfMQY27i3sbXH55HwrYAAvx2AAK9bEBIis746TplUnc2BA"
    },
    "Солнце": {
        "text": (
            "*Солнце*\n\n"
            "_«Ты как солнце — весь мир обнимаешь!\nТы все меняешь вокруг меня»_ 🌅\n\n"
            "Радость, успех и энергия — сияй ярко, твой свет озаряет путь."
        ),
        "sticker": "CAACAgIAAxkBAANbaIeTkz8ma8HcIagCq_TbyLk8uHsAAvmCAAI130FIfSTIYXLaZRU2BA"
    },
    "Вселенная": {
        "text": (
            "*Вселенная*\n\n"
            "_«Распахнув широкие на нас смотрит вся Вселенная»_ 👁️\n\n"
            "Циклы завершаются, новый этап начинается — ты часть великого и прекрасного."
        ),
        "sticker": "CAACAgIAAxkBAANdaIeToMvA9zR38mj4cXKPP0ZIRlgAAsuOAAJQgDlIzmcrRkhENiU2BA"
    },
}

MAIN_MENU = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton("🌕 Карта дня от Mesch!")],
        [KeyboardButton("🔮 Пресейв “Луна в ударе”")],
        [KeyboardButton("🎫 Купить билет на концерт")],
        [KeyboardButton("💌 Поддержать проект")]
    ],
    resize_keyboard=True
)

AFTER_CARD_MENU = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton("🌝 Хочу ещё знак")],
        [KeyboardButton("🌠 Давай прямо к звёздам")]
    ],
    resize_keyboard=True
)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Выбери, что тебе интересно сегодня 🌙",
        reply_markup=MAIN_MENU
    )

async def send_card(update: Update, context: ContextTypes.DEFAULT_TYPE):
    card = random.choice(list(CARDS.values()))
    await update.message.reply_sticker(card["sticker"])
    await update.message.reply_text(
        card["text"],
        parse_mode="Markdown",
        reply_markup=AFTER_CARD_MENU
    )

async def send_final_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    with open("/home/nastyamesch/luna_bot/images/afisha.jpeg", "rb") as photo:
        await update.message.reply_photo(
            photo=photo,
            caption=(
                "Оставайся на волне Mesch!\n"
                "Приходи на концерт-презентацию альбома 25 сентября в POWERHOUSE MOSCOW\n\n"
                "<b>SAVE THE DATE</b>\n"
                "Билеты скоро в продаже\n\n"
                '<a href="https://vk.com/mesch.music">Группа в VK</a>\n'
                '<a href="https://band.link/meschband">Слушать</a>\n'
                '<a href="https://t.me/meschband">Наш Telegram</a>'
            ),
            parse_mode="HTML",
            reply_markup=MAIN_MENU
        )

async def pre_save(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🔮 Пресейв «Луна в ударе»:\nhttps://band.link/mesch_sailormoon/pre-save"
    )

async def buy_ticket(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🎫 Скоро здесь будет прямая ссылка. Следи за анонсами тут:\nhttps://vk.com/mesch.music"
    )

async def support(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "💌 Поддержать проект:\nhttps://tips.yandex.ru/guest/payment/6568930?wl=yandex_music/support"
    )

async def message_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text.lower()
    if "карта дня" in text or "ещё знак" in text:
        await send_card(update, context)
    elif "звёздам" in text:
        await send_final_message(update, context)
    elif "пресейв" in text:
        await pre_save(update, context)
    elif "купить билет" in text:
        await buy_ticket(update, context)
    elif "поддержать" in text:
        await support(update, context)

def main():
    logging.info("Запуск скрипта...")
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, message_handler))
    logging.info("Бот запущен!")
    app.run_polling()

if __name__ == "__main__":
    main()