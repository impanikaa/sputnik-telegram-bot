import telebot
from telebot import types
from config import TOKEN

bot = telebot.TeleBot(TOKEN)

users = {}


@bot.message_handler(commands=['start'])
def welcome(message):
    chat_id = message.chat.id
    keyboard = telebot.types.ReplyKeyboardMarkup()
    button_1 = telebot.types.InlineKeyboardButton(text="🤓 Экспериментальное задание №17")
    button_2 = telebot.types.InlineKeyboardButton(text="📖 Ресурсы для подготовки")
    button_3 = telebot.types.InlineKeyboardButton(text="✍️ О проекте")
    keyboard.add(button_1, button_2, button_3)
    bot.send_message(chat_id, 'Добро пожаловать в бот Спутник', reply_markup=keyboard)


@bot.message_handler(
    func=lambda message: message.text == '🤓 Экспериментальное задание №17')
def experimental_task_17(message):
    chat_id = message.chat.id
    keyboard = telebot.types.ReplyKeyboardMarkup()
    button_1 = telebot.types.InlineKeyboardButton(text="О задании")
    button_2 = telebot.types.InlineKeyboardButton(text="Решения 19 типов этого задания")
    button_3 = telebot.types.InlineKeyboardButton(text="Вернуться в главное меню")
    keyboard.add(button_1, button_2, button_3)
    bot.send_message(chat_id, 'Что Вас интересует?', reply_markup=keyboard)


@bot.message_handler(func=lambda message: message.text == "О задании")
def about_task(message):
    bot.send_message(message.chat.id, "Описание задания")


@bot.message_handler(
    func=lambda message: message.text == "Решения 19 типов этого задания")
def choose_set(message):
    chat_id = message.chat.id
    keyboard = telebot.types.InlineKeyboardMarkup()
    button_first = telebot.types.InlineKeyboardButton(text="1", callback_data='first_s')
    button_second = telebot.types.InlineKeyboardButton(text="2", callback_data='second_s')
    button_third = telebot.types.InlineKeyboardButton(text="3", callback_data='third_s')
    button_fourth = telebot.types.InlineKeyboardButton(text="4", callback_data='fourth_s')
    button_fifth = telebot.types.InlineKeyboardButton(text="6", callback_data='sixth_s')
    keyboard.add(button_first, button_second, button_third, button_fourth, button_fifth)

    bot.send_message(chat_id, f'Выберите комплект', reply_markup=keyboard)


@bot.callback_query_handler(func=lambda call: call.data == 'first_s')
def first_set(call):
    message = call.message
    chat_id = message.chat.id
    message_id = message.message_id
    keyboard = telebot.types.InlineKeyboardMarkup()
    button_first = telebot.types.InlineKeyboardButton(text="1", callback_data='first_t')
    button_second = telebot.types.InlineKeyboardButton(text="2", callback_data='second_t')
    button_third = telebot.types.InlineKeyboardButton(text="3", callback_data='third_t')
    button_fourth = telebot.types.InlineKeyboardButton(text="4", callback_data='fourth_t')
    button_fifth = telebot.types.InlineKeyboardButton(text="5", callback_data='fifth_t')
    button_back = telebot.types.InlineKeyboardButton(text="Назад", callback_data='back')
    keyboard.add(button_first, button_second, button_third, button_fourth, button_fifth, button_back)

    bot.edit_message_text(chat_id=chat_id, message_id=message_id, text="Первый комплект, выберите задание",
                          reply_markup=keyboard)


@bot.callback_query_handler(func=lambda call: call.data == 'second_s')
def second_set(call):
    message = call.message
    chat_id = message.chat.id
    message_id = message.message_id
    keyboard = telebot.types.InlineKeyboardMarkup()
    button_first = telebot.types.InlineKeyboardButton(text="6", callback_data='sixth_t')
    button_second = telebot.types.InlineKeyboardButton(text="7", callback_data='seventh_t')
    button_third = telebot.types.InlineKeyboardButton(text="8", callback_data='eighth_t')
    button_back = telebot.types.InlineKeyboardButton(text="Назад", callback_data='back')
    keyboard.add(button_first, button_second, button_third, button_back)

    bot.edit_message_text(chat_id=chat_id, message_id=message_id, text="Второй комплект, выберите задание",
                          reply_markup=keyboard)


@bot.callback_query_handler(func=lambda call: call.data == 'third_s')
def third_set(call):
    message = call.message
    chat_id = message.chat.id
    message_id = message.message_id
    keyboard = telebot.types.InlineKeyboardMarkup()
    button_first = telebot.types.InlineKeyboardButton(text="9", callback_data='ninth_t')
    button_second = telebot.types.InlineKeyboardButton(text="10", callback_data='tenth_t')
    button_third = telebot.types.InlineKeyboardButton(text="11", callback_data='eleventh_t')
    button_fourth = telebot.types.InlineKeyboardButton(text="12", callback_data='twelfth_t')
    button_back = telebot.types.InlineKeyboardButton(text="Назад", callback_data='back')
    keyboard.add(button_first, button_second, button_third, button_fourth, button_back)

    bot.edit_message_text(chat_id=chat_id, message_id=message_id, text="Третий комплект, выберите задание",
                          reply_markup=keyboard)


@bot.callback_query_handler(func=lambda call: call.data == 'fourth_s')
def fourth_set(call):
    message = call.message
    chat_id = message.chat.id
    message_id = message.message_id
    keyboard = telebot.types.InlineKeyboardMarkup()
    button_first = telebot.types.InlineKeyboardButton(text="13", callback_data='thirteenth_t')
    button_second = telebot.types.InlineKeyboardButton(text="14", callback_data='fourteenth_t')
    button_third = telebot.types.InlineKeyboardButton(text="15", callback_data='fifteenth_t')
    button_fourth = telebot.types.InlineKeyboardButton(text="16", callback_data='sixteenth_t')
    button_back = telebot.types.InlineKeyboardButton(text="Назад", callback_data='back')
    keyboard.add(button_first, button_second, button_third, button_fourth, button_back)

    bot.edit_message_text(chat_id=chat_id, message_id=message_id, text="Четвёртый комплект, выберите задание",
                          reply_markup=keyboard)


@bot.callback_query_handler(func=lambda call: call.data == 'sixth_s')
def sixth_set(call):
    message = call.message
    chat_id = message.chat.id
    message_id = message.message_id
    keyboard = telebot.types.InlineKeyboardMarkup()
    button_first = telebot.types.InlineKeyboardButton(text="17", callback_data='seventeenth_t')
    button_second = telebot.types.InlineKeyboardButton(text="18", callback_data='eighteenth_t')
    button_third = telebot.types.InlineKeyboardButton(text="19", callback_data='nineteenth_t')
    button_back = telebot.types.InlineKeyboardButton(text="Назад", callback_data='back')
    keyboard.add(button_first, button_second, button_third, button_back)

    bot.edit_message_text(chat_id=chat_id, message_id=message_id, text="Шестой комплект, выберите задание",
                          reply_markup=keyboard)


@bot.callback_query_handler(func=lambda call: call.data == 'back')
def choose_set(call):
    message = call.message
    chat_id = message.chat.id
    message_id = message.message_id
    keyboard = telebot.types.InlineKeyboardMarkup()
    button_first = telebot.types.InlineKeyboardButton(text="1", callback_data='first_s')
    button_second = telebot.types.InlineKeyboardButton(text="2", callback_data='second_s')
    button_third = telebot.types.InlineKeyboardButton(text="3", callback_data='third_s')
    button_fourth = telebot.types.InlineKeyboardButton(text="4", callback_data='fourth_s')
    button_fifth = telebot.types.InlineKeyboardButton(text="6", callback_data='sixth_s')
    keyboard.add(button_first, button_second, button_third, button_fourth, button_fifth)

    bot.edit_message_text(chat_id=chat_id, message_id=message_id, text="Выберите комплект", reply_markup=keyboard)


@bot.message_handler(
    func=lambda message: message.text == "Вернуться в главное меню")
def welcome(message):
    chat_id = message.chat.id
    keyboard = telebot.types.ReplyKeyboardMarkup()
    button_1 = telebot.types.InlineKeyboardButton(text="🤓 Экспериментальное задание №17")
    button_2 = telebot.types.InlineKeyboardButton(text="📖 Ресурсы для подготовки")
    button_3 = telebot.types.InlineKeyboardButton(text="✍️ О проекте")
    keyboard.add(button_1, button_2, button_3)
    bot.send_message(chat_id, 'Добро пожаловать в бота сбора обратной связи', reply_markup=keyboard)


if __name__ == '__main__':
    print('Бот запущен!')
    bot.infinity_polling()
