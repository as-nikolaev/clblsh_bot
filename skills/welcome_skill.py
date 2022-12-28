import random

trigger_words = (
    'привет',
    'здарова',
    'дарова',
    'салют',
    'здарова-корова',
    'хай',
    'hi',
)

answers = (
    'Привет',
    'Привет-привет',
    'Ну здарова',
    'Дарова',
    'Салют',
    'О! Нарисовался...',
    'Гля-гля кто припёрся!',
    'Здарова-корова',
)

def gen_answer():
    return random.choice(answers)

def has_trigger(trigger):
    if trigger in trigger_words: return 1
