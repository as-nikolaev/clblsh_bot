import random, settings

trigger_words = (
    'проснись',
    'очнись',
    'wakeup',
    'aлло, гараж',
)

answers = (
    'Да тут я, тут...',
    'Как же тихо было без вас...',
    'Вспомнили, наконец-то!',
    'Чего изволите?',
)

def gen_answer():
    settings.IS_ACTIVE = True
    return random.choice(answers)

def has_trigger(trigger):
    if trigger in trigger_words: return 1