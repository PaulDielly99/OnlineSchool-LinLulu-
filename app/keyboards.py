from aiogram.types import (InlineKeyboardButton, KeyboardButton,
                           InlineKeyboardMarkup,ReplyKeyboardMarkup)
from aiogram.utils.keyboard import InlineKeyboardBuilder


main = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text = 'Записаться на урок📝',callback_data = 'trial'),
        InlineKeyboardButton(text = 'Узнать об обучении❓', callback_data = 'present')
    ],
    [
        InlineKeyboardButton(text = 'Контакты👥', callback_data = 'contact'),
        InlineKeyboardButton(text = 'Обо мне👩', callback_data = 'about_me')
    
    ],
    [
        InlineKeyboardButton(text = 'Мировые экзамены📄',callback_data = 'exzm')
    ]
])

CH_HSK = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text = 'Записаться на HSK', callback_data = 'ch'),
    ]])

select_language = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text = 'Английский 🇺🇸', callback_data= 'en'),    
        InlineKeyboardButton(text = 'Китайский 🇨🇳', callback_data= 'ch')
    ],
    [
        InlineKeyboardButton(text = 'Назад🔙', callback_data= 'to_main')
    ]])

exzm_language = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text = 'Английский 🇺🇸', callback_data= 'exzm_en'),    
        InlineKeyboardButton(text = 'Китайский 🇨🇳', callback_data= 'exzm_ch')
    ],
    [
        InlineKeyboardButton(text = 'Назад🔙', callback_data= 'to_main')
    ]])
    





level = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text = 'Начальный🧍🏻', callback_data= 'beginner')],
    [
        InlineKeyboardButton(text = 'Средний🚶🏻', callback_data= 'middle')],
    [
        InlineKeyboardButton(text = 'Профи🏃🏻', callback_data= 'professional')
    ]])


aim = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text = 'Оценки5️⃣', callback_data= 'for_result'),
        InlineKeyboardButton(text = 'Экзамен✒️', callback_data= 'for_test')
    ],
    [
        InlineKeyboardButton(text = 'Путешествия✈️', callback_data= 'for_adventure'),
        InlineKeyboardButton(text = 'Работа👨', callback_data= 'for_work')
    ],
    [
        InlineKeyboardButton(text = 'Другое', callback_data= 'for_other')
    ]])

exp = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text = 'Да✅', callback_data= 'yes'),
        InlineKeyboardButton(text = 'Нет❌', callback_data= 'no')
    ]])

memory = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text = 'Глазами👀', callback_data= 'eyes'),
        InlineKeyboardButton(text = 'Ушами🦻', callback_data= 'ears')
    ]])

to_main = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text = 'Назад🔙', callback_data= 'to_main')
    ]])


exzm_en_list = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text = 'Назад🔙', callback_data= 'to_main')
    ]])

exzm_ch_list = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text = 'Подготовка к HSK', callback_data= 'HSK')
    ]])    


