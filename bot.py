import telebot
from telebot import types

TOKEN = "8659831278:AAG0YsVDchEtNVFq39YO4DCg9DgMCYGArpM"

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=["start"])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

    markup.row("🎮 FREE FIRE", "💎 Нархҳои алмаз")
    markup.row("🎫 Ваучерҳо", "📋 Фармоишҳои ман")
    markup.row("👨‍💻 Дастгирӣ")

    bot.send_message(
        message.chat.id,
        "🩺 Хуш омадед ба DOKTOR SHOP!\n\n"
        "💎 Free Fire Diamonds\n"
        "⚡ Тез ва боэътимод\n\n"
        "👇 Аз меню интихоб кунед:",
        reply_markup=markup
    )


@bot.message_handler(func=lambda message: True)
def buttons(message):

    if message.text == "🎮 FREE FIRE":
        bot.send_message(
            message.chat.id,
            "🆔 Лутфан ID-и Free Fire-и худро ворид кунед:"
        )

    elif message.text == "💎 Нархҳои алмаз":
        bot.send_message(
            message.chat.id,
            "💎 Нархҳои алмаз:\n\n"
            "💎 110 — 9 сомонӣ\n"
            "💎 341 — 27 сомонӣ\n"
            "💎 572 — 46 сомонӣ\n"
            "💎 1166 — 96 сомонӣ\n"
            "💎 2398 — 192 сомонӣ\n"
            "💎 6160 — 485 сомонӣ"
        )

    elif message.text == "🎫 Ваучерҳо":
        bot.send_message(
            message.chat.id,
            "🎫 Ваучерҳо:\n\n"
            "🎫 Lite Voucher — 7 сомонӣ\n"
            "🎫 Weekly Voucher — 22 сомонӣ\n"
            "🎫 Monthly Voucher — 110 сомонӣ"
        )

    elif message.text == "📋 Фармоишҳои ман":
        bot.send_message(
            message.chat.id,
            "📋 Ҳоло фармоише нест."
        )

    elif message.text == "👨‍💻 Дастгирӣ":
        bot.send_message(
            message.chat.id,
            "👨‍💻 Барои дастгирӣ ба администратор муроҷиат кунед."
        )


print("DOKTOR SHOP BOT STARTED")

bot.infinity_polling()
