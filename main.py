import telebot

import config
import keyboards as kb

bot = telebot.TeleBot(config.BOT_TIKEN)

a = ['Легко знакомишься с людьми', 'Охотоно и подолгу могу что-нибудь мастерить', 'Люблю ходить в музеи, театры',
     'Охотно и постоянно ухаживаю за расстениями,животным', 'Охотно и подолгу могу что-нибудь вычислять,чертить',
     'С удовольствием общаюсь со сверстниками или малышами', 'С удовольствием ухаживаю за растениями и животными',
     'Обычно делаю мало ошибок в письменных работах', 'Мои изделия обычно вызывают интерес у товарищей, старших',
     'Люди считают, что у меня есть художественные способности', 'Охотно читаю о растениях,жиовтных',
     'Принимаю участие в спектаклях, концертах', 'Люблю читать об устройстве муханизмов, приборов,машин',
     'Подолгу могу разгадывать головоломки,задачи,ребусы', 'Легко улаживаю разногласия между людьми',
     'СЧитаю, что у меня есть способности к работе с техникой', 'Людям нравится мое художественное творчество',
     'У меня есть способности к работе с растениями и живтоным', 'Я могу ясно излагать',
     'Я почти никогда ни с кем не сорюсь', 'Результаты моего технического творчества одобряют даже незнакомы люди',
     'Без особного труда усваиваю инстранные языки', 'Мне часто случается помогать даже незнакомым людям',
     'Подолгу могу заниматься музыкой,рисованием,читать книги и т.д.', 'Могу влиять на ход развитиярастений и живтных',
     'Люблю разбираться в устройстве механизмов, приборов', 'Мне обычно удается убедить людей в своей правоте',
     'Охотно наблюдаю за растениями или животными',
     'Охотно читаю научно-популярную, критическую литературу,публицистику',
     'Стараюсь понять секреты мастерства и пробую свои силы в живописи,музыке и т.п.']
answers = {}


@bot.message_handler(commands=['start'])
def start_mes(message):
    chat_id = message.chat.id

    res = bot.send_message(chat_id, 'Сейчас тут будут вопросы',
                           reply_markup=kb.START_TEST)
    bot.delete_message(chat_id, res.id - 1)


@bot.callback_query_handler(func=lambda call: call.data == 'Пройти тест')
def some_funk(call):
    chat_id = call.message.chat.id
    mes_id = call.message.id
    answers[chat_id] = ''
    bot.edit_message_text(message_id=mes_id, chat_id=chat_id, text=a[0])
    bot.edit_message_reply_markup(chat_id=chat_id, message_id=mes_id,
                                  reply_markup=kb.PLUS_MINUS)


@bot.callback_query_handler(func=lambda call: call.data.startswith('ans_'))
def quiz(call):
    cl_d = call.data.replace('ans_', '')
    chat_id, mes_id = call.message.chat.id, call.message.id
    answers[chat_id] += cl_d
    if len(answers[chat_id]) < len(a):
        bot.edit_message_text(a[len(answers[chat_id])], chat_id, mes_id, reply_markup=kb.PLUS_MINUS)

    else:
        bot.edit_message_reply_markup(chat_id, mes_id, reply_markup=None)
        bot.edit_message_text(quiz_analizer(answers[chat_id]), chat_id, mes_id)
        answers[chat_id] = ''


def quiz_analizer(answers: str) -> str:
    chelovek_chelovek = []
    chelovek_technika = []
    chelovek_priroda = []
    chelovek_izo = []
    chelovek_zs = []
    a = list(answers)
    # s = list(a)
    # s = sum([list(i) for i in a], [])
    # print(s)
    # print(s[4])
    print(a)
    if a[0] == '+': chelovek_chelovek.append(1)
    if a[3] == '+': chelovek_priroda.append(1)
    if a[4] == '+': chelovek_zs.append(1)
    if a[2] == '+': chelovek_izo.append(1)
    if a[1] == '+': chelovek_technika.append(1)
    if a[5] == '+': chelovek_chelovek.append(1)
    if a[6] == '+': chelovek_priroda.append(1)
    if a[7] == '+': chelovek_zs.append(1)
    if a[11] == '+': chelovek_izo.append(1)
    if a[12] == '+': chelovek_technika.append(1)
    if a[19] == '+': chelovek_chelovek.append(1)
    if a[10] == '+': chelovek_priroda.append(1)
    if a[21] == '+': chelovek_zs.append(1)
    if a[23] == '+': chelovek_izo.append(1)
    if a[20] == '+': chelovek_technika.append(1)
    if a[26] == '+': chelovek_chelovek.append(1)
    if a[27] == '+': chelovek_priroda.append(1)
    if a[28] == '+': chelovek_zs.append(1)
    if a[29] == '+': chelovek_izo.append(1)
    if a[25] == '+': chelovek_technika.append(1)
    if a[14] == '+': chelovek_chelovek.append(2)
    if a[24] == '+': chelovek_priroda.append(2)
    if a[18] == '+': chelovek_zs.append(2)
    if a[16] == '+': chelovek_izo.append(2)
    if a[15] == '+': chelovek_technika.append(2)
    if a[22] == '+': chelovek_chelovek.append(2)
    if a[17] == '+': chelovek_priroda.append(2)
    if a[13] == '+': chelovek_zs.append(2)
    if a[9] == '+': chelovek_izo.append(2)
    if a[8] == '+': chelovek_technika.append(2)
    b1 = sum(chelovek_zs)
    b2 = sum(chelovek_technika)
    b3 = sum(chelovek_priroda)
    b4 = sum(chelovek_chelovek)
    b5 = sum(chelovek_izo)
    m = max(b1, b2, b3, b4, b5)
    v=[]
    if m==b1:v.append(1)
    if m==b2:v.append(1)
    if m==b3:v.append(1)
    if m==b4:v.append(1)
    if m==b5:v.append(1)
    if len(v) >= 2:
        print('Вам подходит несколько направлений, выбирите одно из них:')
        if m==b1:print('человек знакаовая система')
        if m==b2:print('человек техника')
        if m==b3:print('человек природа')
        if m==b4:print('человек человек')
        if m==b5:print('человек изо')
    else:
        if m==b1:print('Ты человек знакаовая система')
        elif m==b2:print('Ты человек техника')
        elif m==b3:print('Ты человек природа')
        elif m==b4:print('Ты человек человек')
        elif m==b5:print('Ты человек изо')
    a.clear()
    return 'Вы прошли тест'


if __name__ == '__main__':
    bot.infinity_polling()
