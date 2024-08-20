import telebot
from telebot import types


# Create a Telegram bot object
bot = telebot.TeleBot("7215023908:AAGyji867UGYX5J9UBS3w2h86Fsqaym80uc")

# Handle the '/start' command
@bot.message_handler(commands=['start'])
def start_command(message):
    chat_id = message.chat.id
    user_id = message.from_user.id
    bot.send_message(message.from_user.id, 'Здравствуйте, Ваше имя? ')
    bot.register_next_step_handler(message, gender_callback)
@bot.message_handler(content_types=['text'])
def gender_callback(message):
    markup = types.InlineKeyboardMarkup()
    item1 = types.InlineKeyboardButton("Мужчина", callback_data='Male')
    item2 = types.InlineKeyboardButton("Женщина", callback_data='Female')

    markup.add(item1, item2)

    bot.send_message(message.from_user.id, 'Выберите пол', reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data == 'Male' or call.data == 'Female')
def age(call):
    markup = types.InlineKeyboardMarkup()
    item1 = types.InlineKeyboardButton('Младше 18 лет', callback_data='smal')
    item2 = types.InlineKeyboardButton('18-25 лет', callback_data='adult')
    item3 = types.InlineKeyboardButton('26-35 лет', callback_data='adults')
    item4 = types.InlineKeyboardButton('36-45 лет', callback_data='adultse')
    item5 = types.InlineKeyboardButton('46-55 лет', callback_data='adultser')
    item6 = types.InlineKeyboardButton('56-65 лет', callback_data='adultsers')
    item7 = types.InlineKeyboardButton('Старше 65 лет', callback_data='elderly')
    markup.add(item1, item2, item3, item4, item5, item6, item7)
    bot.send_message(call.from_user.id, 'Возраст', reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data == 'smal' or call.data == 'adult' or call.data == 'adults' or call.data == 'adultse' or call.data == 'adultser' or call.data == 'adultsers' or call.data == 'elderly')
def social_media(message):
    markup = types.InlineKeyboardMarkup()

    item1 = types.InlineKeyboardButton("Соц сети", callback_data='social')
    item2 = types.InlineKeyboardButton("Сайт masters", callback_data='site')
    item3 = types.InlineKeyboardButton("Друзья", callback_data='recomend')
    item4 = types.InlineKeyboardButton("Почта", callback_data='email')
    item5 = types.InlineKeyboardButton("Телевидение", callback_data='phone')
    item6 = types.InlineKeyboardButton("Другое", callback_data='walk')
    item7 = types.InlineKeyboardButton("Проходил(а) мимо", callback_data='other')

    markup.add(item1, item2, item3, item4, item5, item6, item7)

    bot.send_message(message.from_user.id, 'Откуда вы узнали о Левашовском хлебозаводе и почему решили прийти?', reply_markup=markup)

@bot.callback_query_handler(func=lambda call: call.data == 'social' or call.data == 'site' or call.data == 'recomend' or call.data == 'email' or call.data == 'phone' or call.data == 'walk' or call.data == 'other')
def museum(call):
    bot.send_message(call.message.chat.id, 'Как часто вы посещаете Левашовский хлебазавод')
    bot.register_next_step_handler(call.message, visitor)



@bot.message_handler(content_types=['text'])
def visitor(message):
    markup = types.InlineKeyboardMarkup()
    item1 = types.InlineKeyboardButton('Один / одна', callback_data='one')
    item2 = types.InlineKeyboardButton('С семьей', callback_data='family')
    item3 = types.InlineKeyboardButton('С ребенком', callback_data='child')
    item4 = types.InlineKeyboardButton('С партнером', callback_data='peer')
    item5 = types.InlineKeyboardButton('С друзьями', callback_data='friends')
    markup.add(item1, item2, item3, item4, item5)
    bot.send_message(message.from_user.id, 'С кем вы посетили сегодня Левашовский хлебозавод?', reply_markup=markup)





@bot.callback_query_handler(func=lambda call: call.data == 'one' or call.data == 'family' or call.data == 'child' or call.data == 'peer' or call.data == 'friends')
def childage(call):
    bot.send_message(call.message.chat.id, 'Если вы были у нас с ребенком/детьми, какого возраста?')
    bot.register_next_step_handler(call.message, occupation)
@bot.message_handler(content_types=['text'])
def occupation(message):
    bot.send_message(message.from_user.id, 'Расскажите, пожалуйста, о вашем роде деятельности?')
    bot.register_next_step_handler(message, museum)

@bot.message_handler(content_types=['text'])
def museum(message):
    bot.send_message(message.from_user.id, 'Как часто вы посещаете выставки/музеи/галереи? ')
    bot.register_next_step_handler(message, gallery)

@bot.message_handler(content_types=['text'])
def gallery(message):
    bot.send_message(message.from_user.id, 'Какие галереи, музеи, выставки в Санкт-Петербурге вы посещали за последний месяц / полгода? Напишите пожалуйста названия.')
    bot.register_next_step_handler(message, sites)
@bot.message_handler(content_types=['text'])
def sites(message):
    bot.send_message(message.from_user.id, 'На какие источники вы чаще всего ориентируетесь, когда планируете досуг? Можно указать конкретные каналы, сообщества, сайты, источники.  ')
    bot.register_next_step_handler(message, social)
@bot.message_handler(content_types=['text'])
def social(message):
    bot.send_message(message.from_user.id,'Какие соцсети вы используете регулярно (минимум раз в неделю)?')
    bot.register_next_step_handler(message, subscribe)

@bot.message_handler(content_types=['text'])
def subscribe(message):
    bot.send_message(message.from_user.id,'Подписаны ли вы на соцсети Левашовского хлебозавода, посещали ли наш сайт?')
    bot.register_next_step_handler(message, yusuf)

@bot.message_handler(content_types=['text'])
def yusuf(message):
    bot.send_message(message.from_user.id,'Если да, то расскажите, пожалуйста, насколько удобно вам было пользоваться сайтом.')
    bot.register_next_step_handler(message, holiday)

@bot.message_handler(content_types=['text'])
def holiday(message):
    bot.send_message(message.from_user.id,'Какие выставки и события вам хочется видеть чаще на Левашовском хлебозаводе?')
    bot.register_next_step_handler(message, thank)
@bot.message_handler(content_types=['text'])
def thank(message):
    bot.send_message(message.from_user.id, "Спасибо!")


# Start the bot
bot.polling()










# @bot.callback_query_handler(func=lambda call: call.data == 'Male' or call.data == 'Female')
# def social_callback(call):
#     markup = types.InlineKeyboardMarkup()
#
#     item1 = types.InlineKeyboardButton("Первый раз", callback_data='first')
#     item2 = types.InlineKeyboardButton("Уже бывал(а)", callback_data='been')
#
#     markup.add(item1, item2)
#
#     bot.send_message(call.from_user.id,
#                          'Вы пришли на Левашовский хлебозавод первый раз или уже бывали у нас раньше?',
#                          reply_markup=markup)
#
#
# @bot.message_handler(content_types=['text'])
# def social_media(message):
#     markup = types.InlineKeyboardMarkup()
#
#     item1 = types.InlineKeyboardButton("Социальные сети", callback_data='Social Media')
#     item2 = types.InlineKeyboardButton("Сайт masters/Левашовского Хлебозавода", callback_data='Site masters')
#     item3 = types.InlineKeyboardButton("Рекомендации друзей или коллег", callback_data='recomendation of friends or colleges')
#     item4 = types.InlineKeyboardButton("Почтовая рассылка", callback_data='email requiries')
#     item5 = types.InlineKeyboardButton("Телевидение или новостные каналы", callback_data='television or news channel')
#     item6 = types.InlineKeyboardButton("Просто проходил(а) мимо / живу недалеко и решил(а) зайти", callback_data='just walking around')
#     item7 = types.InlineKeyboardButton("Другой источник", callback_data='Other')
# #
# #     markup.add(item1, item2, item3, item4, item5, item6, item7)
# #
# #     bot.send_message(message.from_user.id, 'Откуда вы узнали о Левашовском хлебозаводе и почему решили прийти?', reply_markup=markup)
# #
# #
#
#
#
# @bot.callback_query_handler(func=lambda call: call.data == 'Social Media')
# def social_callback(call):
#
#     markup = types.InlineKeyboardMarkup()
#
#     item1 = types.InlineKeyboardButton("Telegram", callback_data='tg')
#     item2 = types.InlineKeyboardButton("Instagram", callback_data='insta')
#
#     markup.add(item1, item2)
#
#     bot.send_message(call.from_user.id, 'Выберите социальную сеть', reply_markup=markup)
# # Handle the inline button callback
# @bot.callback_query_handler(func=lambda call: call.data == 'tg' or call.data == 'insta')
# def social_callback(call):
#     markup = types.InlineKeyboardMarkup()
#
#     item1 = types.InlineKeyboardButton("Первый раз", callback_data='first')
#     item2 = types.InlineKeyboardButton("Уже бывал(а)", callback_data='been')
#
#     markup.add(item1, item2)
#
#     bot.send_message(call.from_user.id, 'Вы пришли на Левашовский хлебозавод первый раз или уже бывали у нас раньше?', reply_markup=markup)
#
#
#
#
# # ---------------------------------------------------------------------------------------------------------
# @bot.callback_query_handler(func=lambda call: call.data == 'Site masters' or call.data == 'recomendation of friends or colleges' or call.data == 'email requiries' or call.data == 'television or news channel' or call.data == 'just walking around')
# def social_callback(call):
#     markup = types.InlineKeyboardMarkup()
#
#     item1 = types.InlineKeyboardButton("Первый раз", callback_data='first')
#     item2 = types.InlineKeyboardButton("Уже бывал(а)", callback_data='been')
#
#     markup.add(item1, item2)
#
#     bot.send_message(call.from_user.id, 'Вы пришли на Левашовский хлебозавод первый раз или уже бывали у нас раньше?', reply_markup=markup)


# ----------------------------------------------------------------------------------------------







# @bot.callback_query_handler(func=lambda call: call.data == 'Other')
# def other_callback(call):
#     bot.send_message(call.from_user.id, "Введите другой источник")

# @bot.callback_query_handler(func=lambda call:call.data == 'Other')
# def other_source_handler(message):
#     # Add code to retrieve the user's input from the database
#     # Send the next question to the user
#     markup = types.InlineKeyboardMarkup()
#
#     item1 = types.InlineKeyboardButton("Первый раз", callback_data='first')
#     item2 = types.InlineKeyboardButton("Уже бывал(а)", callback_data='been')
#
#     markup.add(item1, item2)
#
#     bot.send_message(message.from_user.id, 'Вы пришли на Левашовский хлебозавод первый раз или уже бывали у нас раньше?', reply_markup=markup)
#




