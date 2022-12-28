#!/usr/bin/python

import telebot, re
import settings
from debug import print_debug

from skills import welcome_skill, activity_on_skill, activity_off_skill

bot = telebot.TeleBot(settings.TG_TOKEN)

print_debug(settings.TG_TOKEN)

def skill_support(msg_txt):
    if settings.IS_ACTIVE:
        for skill in [welcome_skill, activity_off_skill]:
            if skill.has_trigger(msg_txt): return 1
    else:
        if activity_on_skill.has_trigger(msg_txt): return 1
    return 0

def gen_answer(msg_txt):
    if settings.IS_ACTIVE:
        for skill in [welcome_skill, activity_off_skill]:
            if skill.has_trigger(msg_txt): return skill.gen_answer()
    else:
        if activity_on_skill.has_trigger(msg_txt): return activity_on_skill.gen_answer()
    pass

@bot.message_handler(content_types=["text"])

def handle_text(message):
    message_text = message.text.lower()

    if skill_support(message_text):
        bot.send_message(message.chat.id, gen_answer(message_text))

bot.polling(none_stop=True, interval=0)