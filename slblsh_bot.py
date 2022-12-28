#!/usr/bin/python

import telebot, re
import settings
from debug import print_debug

from skills import welcome_skill, switch_skill


bot = telebot.TeleBot(settings.TG_TOKEN)

print_debug(settings.TG_TOKEN)

def skill_support(msg_txt):
    if msg_txt.lower() in welcome_skill.trigger_words:
        return 1

def gen_answer(msg_txt):
    if msg_txt.lower() in welcome_skill.trigger_words:
        return welcome_skill.gen_answer(msg_txt)
    pass

@bot.message_handler(content_types=["text"])
def handle_text(message):
    if skill_support(message.text):
        bot.send_message(message.chat.id, gen_answer(message.text))

bot.polling(none_stop=True, interval=0)




