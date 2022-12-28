import random, settings

trigger_words = (
    'заглохни',
    'заткнись',
    'задолбал',
    'да сколько можно',
    'если у тебя есть фонтан - заткни его, дай и фонтану отдохнуть',
)

answers = (
    'Встретимся ещё',
    'Я это запомню',
    'Молчу',
    'Как же вы задолбали... Подай-принеси, отойди не мешай',
)

def gen_answer():
    settings.IS_ACTIVE = False
    return random.choice(answers)

def has_trigger(trigger):
    if trigger in trigger_words: return 1
