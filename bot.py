import telebot

import config
from utils import parse_message
import logic

API_TOKEN = config.TELEGRAM_BOT_TOKEN

bot = telebot.TeleBot(API_TOKEN)


@bot.message_handler(commands=["help", "start"])
def send_welcome(message):
    bot.reply_to(
        message,
        """\
        Hi there, I am EchoBot for testing.\
        e.g\
        /pwr 2,5\
        /exp 1        
""",
    )


@bot.message_handler(func=lambda message: message.text.startswith("/pwr"))
def do_pwr(message):
    a, b = parse_message(message.text[4:])
    c = logic.do_power(a, b)
    bot.send_message(
        message.chat.id, text=f"Число {a} возведенное в стпень {b} равно {c}"
    )


@bot.message_handler(func=lambda message: message.text.startswith("/exp"))
def do_pwr(message):
    a, _ = parse_message(message.text[4:])
    c = logic.do_exp(a)
    bot.send_message(message.chat.id, text=f"Экспонента в степени {a} равно {c}")


@bot.message_handler(func=lambda message: message.text.startswith("/add"))
def do_pwr(message):
    a, b = parse_message(message.text[4:])
    c = logic.do_add2(a, b)
    bot.send_message(message.chat.id, text=f"Сумма {a} и {b} равно {c}")


@bot.message_handler(func=lambda message: message.text.startswith("/sub"))
def do_pwr(message):
    a, b = parse_message(message.text[4:])
    c = logic.do_sub2(a, b)
    bot.send_message(message.chat.id, text=f"Разность {a} и {b} равно {c}")


@bot.message_handler(func=lambda message: message.text.startswith("/mul"))
def do_pwr(message):
    a, b = parse_message(message.text[4:])
    c = logic.do_mul2(a, b)
    bot.send_message(message.chat.id, text=f"Произведение {a} и {b} равно {c}")


@bot.message_handler(func=lambda message: message.text.startswith("/div"))
def do_pwr(message):
    a, b = parse_message(message.text[4:])
    c = logic.do_div2(a, b)
    bot.send_message(message.chat.id, text=f"Частное {a} и {b} равно {c}")


bot.infinity_polling()
