from aiogram.types import CallbackQuery, Message
from aiogram.filters import Command, CommandStart
from aiogram import Router, F 
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from config import chat_id

import app.keyboards as kb



router = Router()                           #назначение роутера 

class Trial_EN(StatesGroup):                #назначение состояний для английского языка
    language = State()
    level = State()
    aim = State()
    exp = State()
    memory = State()


class Trial_Ch(StatesGroup):             #назначение состояний для китайского языка
    language = State()
    level = State()
    aim = State()
    exp = State()
    memory = State()    
   

@router.message(CommandStart())                        #старт команды /start
@router.callback_query(F.data == 'to_main')             
async def start(message: Message | CallbackQuery):
    if isinstance(message, Message):
        await message.answer_sticker(f'CAACAgIAAxkBAAJGtWXwj6o_NK8AAX86IuLH_L_LFYIs3QACqQgAAm4y2AABGXPOIvVr7iA0BA')   
        await message.answer(f'{message.from_user.first_name}, привет!👋\n'
                            'Добро пожаловать в онлайн школу Lin Lulu💫'
                            'Чем я тебе могу помочь?😇', reply_markup=kb.main)
        
    else:
        await message.answer('Вы вернулись в главное меню')
        await message.message.edit_text(f'{message.from_user.first_name}, привет!👋\n'
                                'Добро пожаловать в онлайн школу Lin Lulu💫'
                                'Чем я тебе могу помочь?😇', reply_markup=kb.main)
        
@router.callback_query(F.data=='trial')
async def trial(callback: CallbackQuery):
    
    await callback.answer()
    await callback.message.edit_text(f'Это круто!🔥 А на какой язык ты хочешь'
                                    'записаться?',reply_markup=kb.select_language)
       

@router.callback_query(F.data == 'en')
async def en(callback: CallbackQuery,state: FSMContext):
    await state.update_data(language=en)
    await state.set_state(Trial_EN.level)
    await callback.answer()
    await callback.message.edit_text('Какой у Вас уровень знаний?🧠',reply_markup=kb.level)
    

@router.callback_query(F.data == 'ch')
async def ch(callback: CallbackQuery, state: FSMContext):
    await state.update_data(language = ch)
    await state.set_state(Trial_Ch.level)
    await callback.answer()
    await callback.message.edit_text('Какой у Вас уровень знаний?🧠',reply_markup=kb.level)
          


@router.callback_query(Trial_EN.level)
async def level(callback: CallbackQuery, state: FSMContext):   
    await callback.bot.send_message(chat_id, f'{callback.from_user.full_name} ❤️🔥 хочет записаться на английский язык\n\nУровень текущих знаний: {callback.data}')      
    await state.update_data(level=callback.data)
    await state.set_state(Trial_EN.aim)
    await callback.answer()
    await callback.message.edit_text('Почему ты хочешь изучить именно этот язык?✨', reply_markup=kb.aim)

@router.callback_query(Trial_Ch.level)
async def level(callback: CallbackQuery, state: FSMContext):
    await callback.bot.send_message(chat_id, f'{callback.from_user.full_name} ❤️🔥 хочет записаться на китайский язык\n\nУровень текущих знаний: {callback.data}')
    await state.update_data(level=callback.data)
    await state.set_state(Trial_Ch.aim)
    await callback.answer()
    await callback.message.edit_text('Почему ты хочешь изучить именно этот язык?✨', reply_markup=kb.aim)

@router.callback_query(Trial_EN.aim)
async def aim(callback: CallbackQuery, state: FSMContext):
    await callback.bot.send_message(chat_id, f'Цель изучения: {callback.data}✨')
    await state.update_data(aim=callback.data)
    await state.set_state(Trial_EN.exp)
    await callback.answer()
    await callback.message.edit_text('А был ли у тебя опыт с другими репетиторами🧑‍🏫?', reply_markup=kb.exp)    

@router.callback_query(Trial_Ch.aim)
async def aim(callback: CallbackQuery, state: FSMContext):
    await callback.bot.send_message(chat_id, f'Цель изучения: {callback.data}✨')
    await state.update_data(aim=callback.data)
    await state.set_state(Trial_Ch.exp)
    await callback.answer()
    await callback.message.edit_text('А был ли у тебя опыт с другими репетиторами🧑‍🏫?', reply_markup=kb.exp)

@router.callback_query(Trial_EN.exp)
async def exp(callback: CallbackQuery, state: FSMContext):
    await callback.bot.send_message(chat_id, f'Опыт с другими репетиторами: {callback.data}🧑‍🏫')
    await state.update_data(exp=callback.data)
    await state.set_state(Trial_EN.memory)
    await callback.answer()
    await callback.message.edit_text('Как тебе легче запоминать информацию?📀💾', reply_markup=kb.memory)

@router.callback_query(Trial_Ch.exp)
async def exp(callback: CallbackQuery, state: FSMContext):
    await callback.bot.send_message(chat_id, f'Опыт с другими репетиторами: {callback.data}🧑‍🏫')
    await state.update_data(exp=callback.data)
    await state.set_state(Trial_Ch.memory)
    await callback.answer()
    await callback.message.edit_text('Как тебе легче запоминать информацию?📀💾', reply_markup=kb.memory)    

@router.callback_query(Trial_EN.memory)
async def memory(callback: CallbackQuery, state: FSMContext):
    await callback.bot.send_message(chat_id, f'Запоминает лучше: {callback.data}📀💾')
    await state.update_data(memory=callback.data) 
    await callback.answer()
    await callback.message.edit_text('Отлично! Мы с тобой записались на пробный урок! Преподаватель с тобой скоро свяжется✅', reply_markup=kb.to_main)
    await state.clear()
    await callback.bot.send_message(chat_id, f"<a href='tg://user?id={callback.from_user.id}'>♥КЛИЕНТ♥</a>", parse_mode='HTML')
    await callback.bot.send_sticker(chat_id, f'CAACAgIAAxkBAAJGtWXwj6o_NK8AAX86IuLH_L_LFYIs3QACqQgAAm4y2AABGXPOIvVr7iA0BA')


@router.callback_query(Trial_Ch.memory)
async def memory(callback: CallbackQuery, state: FSMContext):
    await callback.bot.send_message(chat_id, f'Запоминает лучше: {callback.data}📀💾')
    await state.update_data(memory=callback.data)
    await callback.answer()
    await callback.message.edit_text('Отлично! Мы с тобой записались на пробный урок! Преподаватель с тобой скоро свяжется✅', reply_markup=kb.to_main)
    await state.clear()
    await callback.bot.send_message(chat_id, f"<a href='tg://user?id={callback.from_user.id}'>♥КЛИЕНТ♥</a>", parse_mode='HTML')
    await callback.bot.send_sticker(chat_id, f'CAACAgIAAxkBAAJGtWXwj6o_NK8AAX86IuLH_L_LFYIs3QACqQgAAm4y2AABGXPOIvVr7iA0BA')

@router.callback_query(F.data == 'present')
async def present(callback: CallbackQuery):
    await callback.answer()
    await callback.message.edit_text('Наша школа предоставляет индивидуальные уроки для всех желающих в online формате.'
                                     'Наши преподаватели окончили языковой университет и уже оттачили его с носителями.'
                                     'Мы существуем уже более 6 лет, и обучили не менее 130 учеников.'
                                     'Почему же так немного? Основное наше направление - китайский язык, а изучить его на хорошем уровне нужно немного больше времени и сил наших дорогих учеников'
                                     'Мы работаем как для детей, так для родителей и родителей родителей😁\n\n'
                                     '🌟Наши преимущества:🌟\n'
                                     ' 1. Удобный формат обчуения🔥\n'
                                     ' 2. Индивидуальные материалы под каждого📚\n'
                                     ' 3. Всё внимание только на Вас и Ваш результат📈\n'
                                     ' 4. Работаем с 7 лет и до бесконечности\n'
                                     ' 5. Преподаватели с большим опытом🧠\n'
                                     ' 6. Хорошее качество звука и видео✅🔊\n'
                                     ' 7. Смотрим фильмы и сериалы📺\n\n'
                                     'Проводим бесплатный пробный урок, чтобы вы смогли в полной мере ощутить нас, настроить оборудование, и присоединиться к нашей семье♥\n\n На какой язык пойдём на пробный урок?',reply_markup=kb.select_language)
@router.callback_query(F.data == 'HSK')
async def HSK(callback: CallbackQuery):
    await callback.answer()
    await callback.message.edit_text('大家好!\n\n'

                                    'Всем привет, я - Лин Лаоши , твой будущий репетитор китайского языка 🇨🇳\n\n'

                                        '— Подготовлю тебя к HSK 1-4💎\n'
                                        '— Учебник покупать НЕ обязательно, я предоставляю все материалы в интерактивной форме онлайн👩🏼‍💻\n'
                                        '— Уроки включают в себя понимание на слух, говорение, чтение, письмо, подготовку к экзамену, игры и интерактивные задания💫\n'
                                        '— Занятия проводятся на интерактивной платформе Microsoft Teams и Edvibe⭐️\n\n'

                                        'Индивидуальные занятия 1500р / 60 минут\n'
                                        'Первое занятие - БЕСПЛАТНО',reply_markup=kb.CH_HSK)




@router.callback_query(F.data == 'exzm')
async def exzm(callback: CallbackQuery):
    await callback.answer()
    await callback.message.edit_text('Выбери интересующий язык 🇨🇳🇺🇸',reply_markup=kb.exzm_language)

@router.callback_query(F.data == 'exzm_en')
async def exzm_en(callback: CallbackQuery):
    await callback.answer()
    await callback.message.edit_text('К английскому языку в данный момент не готовим, ожидайте обновления',reply_markup=kb.exzm_en_list)

@router.callback_query(F.data == 'exzm_ch')
async def exzm_ch(callback: CallbackQuery):
    await callback.answer()
    await callback.message.edit_text('Выберите экзамен', reply_markup=kb.exzm_ch_list)

@router.callback_query(F.data == 'contact')
async def contact(callback: CallbackQuery):
    await callback.answer()
    await callback.message.edit_text('При любом вопросе по обучению👇🏻\n'
                                     'Преподаватель👩‍🏫: Лин Лаоши @linlaoshixin\n\n'
                                     'При любом техническом вопросе👇🏻\n'
                                     'Разработчик🛠: @Paul_Dielly',reply_markup=kb.to_main)

@router.callback_query(F.data == 'about_me')      
async def about_me(callback: CallbackQuery):
    await callback.answer()
    await callback.message.edit_text('Я - Лин Лаоши👩‍🏫, твой будущий репетитор\n\n'
                                     'Я работаю в компании Edvibe, которая работает со всеми компаниями и открыта для всех👩‍💻\n\n'
                                     'Закончила КФУ с отличием и успешнно получила гранд на обучение в Китае🇨🇳\n'
                                     'Занимаюсь обучением и работаю в команде репетиторов китайского и английского языков 💫',reply_markup=kb.to_main)
    
                                    









