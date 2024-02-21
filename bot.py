# ags_infobot
# Importing required libraries
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from IPython.display import Markdown
from telegram.constants import ParseMode
import logging
from db import Database
from dotenv import load_dotenv

logging.basicConfig(level=logging.INFO)

load_dotenv()

# Put the token that you received from BotFather in the quotes
bot = Bot(token='6433643074:AAHD4UBaaNWumOmmRSG6ltI_S8wnZnLrmuE')

# Initializing the dispatcher object
dp = Dispatcher(bot)
db = Database('database.db')

# Defining and adding buttons
# Initial buttons: high/elem
highSchool = InlineKeyboardButton(
    text="Старшая школа", callback_data="highSchool")
elemSchool = InlineKeyboardButton(
    text="Младшая школа", callback_data="elemSchool")

# Inline keyboard high/elem
highElemKeyboard = InlineKeyboardMarkup().add(highSchool, elemSchool)

# -------------------------- HIGH SCHOOL --------------------------
# high school buttons
schedule = InlineKeyboardButton(
    text="Расписание", callback_data="schedule")
chats = InlineKeyboardButton(
    text="Чаты", callback_data="chats")
curators = InlineKeyboardButton(
    text="Кураторы", callback_data="curators")
rules = InlineKeyboardButton(
    text="Внутришкольные правила", callback_data="rules")
website = InlineKeyboardButton(
    text="Сайт школы", callback_data="website")
itInfo = InlineKeyboardButton(
    text="IT info", callback_data="itInfo")
politics = InlineKeyboardButton(
    text="Политики", callback_data="politics")
staffMembers = InlineKeyboardButton(
    text="Список сотрудников", callback_data="staffMembers")
resources = InlineKeyboardButton(
    text="Полезные ресурсы", callback_data="resources")
development = InlineKeyboardButton(
    text="Развитие", callback_data="development")
faq = InlineKeyboardButton(
    text="FAQ", callback_data="faq")
back = InlineKeyboardButton(
    text="Назад", callback_data="back")
bback = InlineKeyboardButton(
    text="Назад", callback_data="bback")
room_booking = InlineKeyboardButton(
    text="Бронь аудитории", callback_data="room_booking")

# Inline keyboard - high school
highKeyboard = InlineKeyboardMarkup(row_width=1).add(schedule, chats, curators, rules,
                                                     website, itInfo, politics, staffMembers, room_booking, resources, development, faq, back)


# chatsKeyboard
academTeam = InlineKeyboardButton(
    text="Академическая команда", callback_data="academTeam")
it_support_chat = InlineKeyboardButton(
    text="IT Support", callback_data="it_support_chat")
cleaning = InlineKeyboardButton(
    text="Cleaning", callback_data="cleaning")
sklad = InlineKeyboardButton(
    text="Выдача канцтоваров", callback_data="sklad")
zayavki = InlineKeyboardButton(
    text="Заявки: разное", callback_data="zayavki")

chatsKeyboard = InlineKeyboardMarkup(row_width=1).add(
    academTeam, it_support_chat, cleaning, sklad, zayavki, bback)

# rscKeyboard
olympiads = InlineKeyboardButton(
    text="Канал олимпиад AGS", callback_data="olympiads")
collegeCounceling = InlineKeyboardButton(
    text="Канал College Counselilng AGS", callback_data="collegeCounseling")
classroomManagement = InlineKeyboardButton(
    text="AGS Teacher Resources", callback_data="classroomManagement")

rscKeyboard = InlineKeyboardMarkup(row_width=1).add(
    olympiads, collegeCounceling, classroomManagement, bback)

# curatorsKeyboard

class_5A = InlineKeyboardButton(
    text="5A - Асхат Айсаев", callback_data="class_5A")
class_5B = InlineKeyboardButton(
    text="5B - Макпал Мауленкулова", callback_data="class_5B")
class_5C = InlineKeyboardButton(
    text="5C - Аделина Жангиреева", callback_data="class_5C")
class_5D = InlineKeyboardButton(
    text="5D - Жулдыз Байбатырова", callback_data="class_5D")

class_6A_6C = InlineKeyboardButton(
    text="6A, 6C - Айгерим Жалелханова", callback_data="class_6A_6C")
class_6B_6E = InlineKeyboardButton(
    text="6B, 6E - Айнур Айтжанова", callback_data="class_6B_6E")
class_6D_7A = InlineKeyboardButton(
    text="6D, 7A - Алена Шиянюк", callback_data="class_6D_7A")

class_7B = InlineKeyboardButton(
    text="7B - Дидар Ерназарова", callback_data="class_7B")

class_8A_8D = InlineKeyboardButton(
    text="8A, 8D - Куаныш Айтжанов", callback_data="class_8A_8D")
class_8B_8C_9B = InlineKeyboardButton(
    text="8B, 8C, 9B - Камила Сайынкызы", callback_data="class_8B_8C_9B")

class_9A_9C_9D = InlineKeyboardButton(
    text="9A, 9C, 9D - Нургуль Алкеева", callback_data="class_9A_9C_9D")

class_10A_10B_7C = InlineKeyboardButton(
    text="10A, 10B, 7C - Айгерим Хамитова", callback_data="class_10A_10B_7C")
class_10C = InlineKeyboardButton(
    text="10C - Азат Дюсембаев", callback_data="class_10C")

class_11A_11B = InlineKeyboardButton(
    text="11A, 11B - Артур Арутюнян", callback_data="class_11A_11B")

curatorsKeyboard = InlineKeyboardMarkup(row_width=1).add(
    class_5A, class_5B, class_5C, class_5D, class_6A_6C, class_6B_6E, class_6D_7A, class_7B, class_8A_8D, class_8B_8C_9B, class_9A_9C_9D, class_10A_10B_7C, class_10C, class_11A_11B, bback)

# developmentKeyboard
contests = InlineKeyboardButton(
    text="Конкурсы профессионального мастерства для педагогов", callback_data="contests")
conferences = InlineKeyboardButton(
    text="Конференции", callback_data="conferences")
devKeyboard = InlineKeyboardMarkup(
    row_width=1).add(contests, conferences, bback)

backKeyboard = InlineKeyboardMarkup(
    row_width=1).add(back)

bbackKeyboard = InlineKeyboardMarkup(
    row_width=1).add(bback)
# --------------------------END HIGH SCHOOL --------------------------

# -------------------------- ELEM SCHOOL --------------------------
# elem school buttons
elem_it = InlineKeyboardButton(
    text="IT support", callback_data="elem_it")
elem_cleaning = InlineKeyboardButton(
    text="Cleaning", callback_data="elem_cleaning")
elem_axo = InlineKeyboardButton(
    text="Выдача канцтоваров", callback_data="elem_axo")
elem_rules = InlineKeyboardButton(
    text="Внутришкольные правила", callback_data="elem_rules")
elem_staff = InlineKeyboardButton(
    text="Список сотрудников по младшей школе", callback_data="elem_staff")
toddle = InlineKeyboardButton(
    text="Работа в Toddle", callback_data="toddle")

# Inline keyboard - elem school
elemKeyboard = InlineKeyboardMarkup(row_width=1).add(
    elem_it, elem_cleaning, elem_axo, website, elem_staff, elem_rules, toddle)


# --------------------------END ELEM SCHOOL --------------------------


# Message handler for the /highSchool command


@dp.message_handler(commands=['start'])
# async def check(message: types.Message):
async def start(message: types.Message):
    if message.chat.type == 'private':
        if not db.user_exists(message.from_user.id):
            db.add_user(message.from_user.id)
            db.set_active(message.from_user.id, 1)
        # await message.reply("Здравствуй! Я инфо-бот AGS. Выбери старшую/младшую школу:", reply_markup=highElemKeyboard)
        await bot.send_message(message.from_user.id, "Здравствуй! Я инфо-бот AGS. Выбери старшую/младшую школу:", reply_markup=highElemKeyboard)

# Callback query handler for the inline keyboard buttons


@dp.callback_query_handler(text=["highSchool", "elemSchool"])
async def check_button(call: types.CallbackQuery):

    # Checking which button is pressed and respond accordingly
    if call.data == "highSchool":
        await call.message.answer("Вы выбрали старшую школу. Выберите вкладку из списка ниже:", reply_markup=highKeyboard)
    elif call.data == "elemSchool":
        await call.message.answer("Вы выбрали младшую школу. Выберите вкладку из списка ниже:", reply_markup=elemKeyboard)
    # Notify the Telegram server that the callback query is answered successfully
    await call.answer()

# -------------------------- HIGH SCHOOL QUERY HANDLER --------------------------

# Callback query handler for the high school buttons


@dp.callback_query_handler(text=["schedule", "chats", "curators", "rules",
                                 "website", "itInfo", "politics", "staffMembers", "room_booking", "development", "resources", "faq", "back", "bback"])
async def check_button(call: types.CallbackQuery):

    # Checking which button is pressed and respond accordingly
    if call.data == "schedule":
        await call.message.answer("Расписания уроков по классам:")
        await bot.send_document(call.message.chat.id, open(r'23_24_for_classes_from_29_01.pdf', 'rb'))
        await call.message.answer("Расписания уроков по учителям:")
        await bot.send_document(call.message.chat.id, open(r'23_24_for_teachers_from_29_01.pdf', 'rb'), reply_markup=bbackKeyboard)
    elif call.data == "chats":
        await call.message.answer("Выберите чат из списка ниже:", reply_markup=chatsKeyboard)
    elif call.data == "curators":
        await call.message.answer("Выберите класс:", reply_markup=curatorsKeyboard)
    elif call.data == "rules":
        await call.message.answer("Внутришкольные правила: https://sway.office.com/9LE9T6EdxzSOdHyS?ref=Link", reply_markup=backKeyboard)
    elif call.data == "website":
        await call.message.answer("Школьный сайт: https://ags.edu.kz", reply_markup=backKeyboard)
    elif call.data == "itInfo":
        await call.message.answer("Информация по IT: https://shorturl.at/gqwDG", reply_markup=bbackKeyboard)
    elif call.data == "politics":
        await call.message.answer("Политика:")
        await bot.send_document(call.message.chat.id, open(r'politics/Academic honesty policy of high school.pdf', 'rb'))
        await bot.send_document(call.message.chat.id, open(r'politics/Assessment policy of high school.pdf', 'rb'))
        await bot.send_document(call.message.chat.id, open(r'politics/Language policy of high school.pdf', 'rb'))
        await bot.send_document(call.message.chat.id, open(r'politics/Special educational needs policy of high school.pdf', 'rb'))
        await bot.send_document(call.message.chat.id, open(r'politics/Дисциплинарная политика старшей школы.pdf', 'rb'))
        await bot.send_document(call.message.chat.id, open(r'politics/Жоғары мектептің тіл саясаты.pdf', 'rb'))
        await bot.send_document(call.message.chat.id, open(r'politics/Положение о методическом совете старшей школы.pdf', 'rb'))
        await bot.send_document(call.message.chat.id, open(r'politics/Программа превенции буллинга старшей школы.pdf', 'rb'))
        await bot.send_document(call.message.chat.id, open(r'politics/Языковая политика старшей школы.pdf', 'rb'))
        await bot.send_document(call.message.chat.id, open(r'politics/Ответственность сторон в процессе поступления в ВУЗы старшей школы.pdf', 'rb'), reply_markup=bbackKeyboard)
    elif call.data == "staffMembers":
        await call.message.answer("Список сотрудников:")
        await bot.send_document(call.message.chat.id, open(r'staff_list.xlsx', 'rb'), reply_markup=bbackKeyboard)
    elif call.data == "room_booking":
        await call.message.answer("Инструкция по букингу аудитории/кабинета: https://shorturl.at/hACP0", reply_markup=bbackKeyboard)
    elif call.data == "development":
        await call.message.answer("Выберите опцию по развитию:", reply_markup=devKeyboard)
    elif call.data == "resources":
        await call.message.answer("Полезные ресурсы и каналы:", reply_markup=rscKeyboard)
    elif call.data == "faq":
        await call.message.answer("Часто задаваемые вопросы:", reply_markup=bbackKeyboard)
    elif call.data == "back":
        await call.message.answer("Выберите школу:", reply_markup=highElemKeyboard)
    elif call.data == "bback":
        await call.message.answer("Выберите опцию ниже:", reply_markup=highKeyboard)
    # Notify the Telegram server that the callback query is answered successfully
    await call.answer()

contest_list = [
    "1. [Республиканский и областной конкурс 'Лучший педагог'](https://adilet.zan.kz/rus/docs/P1200000394)",
    "2. [Республиканский конкурс 'Лучший педагог' реабилитационного центра и кабинета психолого-педагогической коррекции'](https://special-edu.kz/uploads/files/docposition/%D0%9F%D0%BE%D0%BB%D0%BE%D0%B6%D0%B5%D0%BD%D0%B8%D0%B5%D0%A0%D0%A6,%D0%9A%D0%9F%D0%9F%D0%9A.pdf)",
    "3. [Республиканский конкурс 'Лучший педагог психолого-медико-педагогической консультации'](https://astana-modern.edu.kz/wp-content/uploads/2022/05/%D0%9B%D1%83%D1%87%D1%88%D0%B8%D0%B9-%D1%81%D0%BF%D0%B5%D1%86%D0%B8%D0%B0%D0%BB%D0%B8%D1%81%D1%82-%D0%BF%D1%81%D0%B8%D1%85%D0%BE%D0%BB%D0%BE%D0%B3%D0%BE-%D0%BC%D0%B5%D0%B4%D0%B8%D0%BA%D0%BE-%D0%BF%D0%B5%D0%B4%D0%B0%D0%B3%D0%BE%D0%B3%D0%B8%D1%87%D0%B5%D1%81%D0%BA%D0%BE%D0%B9-%D0%BA%D0%BE%D0%BD%D1%81%D1%83%D0%BB%D1%8C%D1%82%D0%B0%D1%86%D0%B8%D0%B8.pdf)",
    "4. [Республиканский конкурс 'Лучший психолог года'](https://docs.google.com/document/d/11d96GeI7QbrFlujD_x4S0iZpkQtyfpn8/edit)",
    "5. [Республиканский конкурс 'Лучшая авторская программа'](https://docs.google.com/document/d/1fp51aaZAfZd5b5sG-AdciHTyTFtO1gnc/edit)",
    "6. [Республиканский конкурс 'Фестиваль педагогических идей'](https://daryn.kz/blog/2023/11/14/%D0%B8%D0%BD%D1%84%D0%BE%D1%80%D0%BC%D0%B0%D1%86%D0%B8%D0%BE%D0%BD%D0%BD%D0%BE%D0%B5-%D0%BF%D0%B8%D1%81%D1%8C%D0%BC%D0%BE-%D0%BE-%D0%BF%D1%80%D0%BE%D0%B2%D0%B5%D0%B4%D0%B5%D0%BD%D0%B8%D0%B8-%D1%80-6/)",
    "7. [Республиканская олимпиада для учителей математики 'Математическая регата'](https://daryn.kz/wp-content/uploads/2020/10/2-%D0%9C%D0%B0%D1%82%D0%B5%D0%BC%D0%B0%D1%82%D0%B8%D1%87%D0%B5%D1%81%D0%BA%D0%B0%D1%8F-%D1%80%D0%B5%D0%B3%D0%B0%D1%82%D0%B0-%D0%BF%D1%80%D0%B0%D0%B2%D0%B8%D0%BB%D0%B0-%D1%80%D1%83%D1%81.docx)",
    "8. [Республиканская олимпиада для молодых педагогов 'Талантливый учитель-одаренным детям'](https://daryn.kz/wp-content/uploads/2020/10/2-%D0%A2%D0%B0%D0%BB%D0%B0%D0%BD%D1%82%D0%BB%D0%B8%D0%B2%D1%8B%D0%B9-%D1%83%D1%87%D0%B8%D1%82%D0%B5%D0%BB%D1%8C-%D0%BE%D0%B4%D0%B0%D1%80%D0%B5%D0%BD%D0%BD%D1%8B%D0%BC-%D0%B4%D0%B5%D1%82%D1%8F%D0%BC-%D0%9F%D1%80%D0%B0%D0%B2%D0%B8%D0%BB%D0%B0-%D1%80%D1%83%D1%81.docx)",
    "9. [Республиканская олимпиада по предметам для учителей 'ПедСтарт'](https://daryn.kz/pedstart-ru/)",
    "10. [Республиканский конкурс для учителей начальных классов 'Алтын тұғыр'](https://daryn.kz/wp-content/uploads/2020/12/%D0%90%D0%BB%D1%82%D1%8B%D0%BD-%D1%82%D2%B1%D2%93%D1%8B%D1%80-%D0%95%D1%80%D0%B5%D0%B6%D0%B5%D1%81%D1%96-2021.doc)",
    "11. [Республиканский конкурс видео-уроков и видео-лекций для организаций дошкольного, среднего, дополнительного, технического и профессионального, послесреднего, высшего образования 'Панорама педагогических идей'](https://ppi.orleu-edu.kz/?page_id=18444&lang=ru)",
    "12. [Республиканский конкурс молодых педагогов 'Новой школе – современный учитель'](https://baldauren.kz/news/zhas-pedagogter-bayk-auy.html)"
]

conference_list = [
    "1. [KIMEP International Research Conference](https://www.kimep.kz/bang-college-of-business/en/kimep-international-research-conference/#panely0)",
    "2. [Central Asia Language and Education Conference](https://www.kimep.kz/college-humanities-education/en/che-conference/)",
    "4. [LCOY Kazakhstan 2023](https://nu.edu.kz/ru/events/lcoy-kazakhstan-2023-2)",
    "5. [7-я ежегодная конференция ВШГП НУ «Сдвиг границ в глобальном и местном управлении»](https://nu.edu.kz/ru/events/7-ya-ezhegodnaya-konferentsiya-vshgp-nu-sdvig-granits-v-global-nom-i-mestnom-upravlenii)"
]

contests_python_text = "\n".join(contest_list)

conferences_python_text = "\n".join(conference_list)


@dp.callback_query_handler(text=["contests", "conferences"])
async def check_button(call: types.CallbackQuery):

    # Checking which button is pressed and respond accordingly
    if call.data == "contests":
        await call.message.answer("Конкурсы профессионального мастерства для педагогов: \n")
        await call.message.answer(contests_python_text, parse_mode=ParseMode.MARKDOWN, reply_markup=bbackKeyboard)
    elif call.data == "conferences":
        await call.message.answer("Конференции:")
        await call.message.answer(conferences_python_text, parse_mode=ParseMode.MARKDOWN, reply_markup=bbackKeyboard)

    # Notify the Telegram server that the callback query is answered successfully
    await call.answer()

# curators' telegram accounts


@dp.callback_query_handler(text=["class_5A", "class_5B", "class_5C", "class_5D", "class_6A_6C", "class_6B_6E", "class_6D_7A", "class_7A_7C", "class_7B", "class_7D", "class_8A_8D", "class_8B_8C_9B", "class_9A_9C_9D", "class_10A_10B_7C", "class_10C", "class_11A_11B"])
async def check_button(call: types.CallbackQuery):

    # Checking which button is pressed and respond accordingly
    if call.data == "class_5A":
        # await call.message.answer("Конкурсы профессионального мастерства для педагогов:", reply_markup=bbackKeyboard)
        await call.message.answer("https://t.me/Jaqsy_adam", reply_markup=bbackKeyboard)
    elif call.data == "class_5B":
        await call.message.answer("https://t.me/makpalmaulenkulova", reply_markup=bbackKeyboard)
    elif call.data == "class_5C":
        await call.message.answer("https://t.me/adelina_z", reply_markup=bbackKeyboard)
    elif call.data == "class_5D":
        await call.message.answer("https://t.me/baibatyrova", reply_markup=bbackKeyboard)
    elif call.data == "class_6A_6C":
        await call.message.answer("https://t.me/igerim17", reply_markup=bbackKeyboard)
    elif call.data == "class_6B_6E":
        await call.message.answer("https://t.me/Ainura_2708", reply_markup=bbackKeyboard)
    elif call.data == "class_6D_7A":
        await call.message.answer("https://t.me/Shyianiuk_Alona", reply_markup=bbackKeyboard)
    elif call.data == "class_7B":
        await call.message.answer("https://t.me/ydidarra", reply_markup=bbackKeyboard)
    elif call.data == "class_8A_8D":
        await call.message.answer("https://t.me/Kuanysh_Aitzhanov", reply_markup=bbackKeyboard)
    elif call.data == "class_8B_8C_9B":
        await call.message.answer("https://t.me/KamilaSain", reply_markup=bbackKeyboard)
    elif call.data == "class_9A_9C_9D":
        await call.message.answer("https://t.me/nurgulags", reply_markup=bbackKeyboard)
    elif call.data == "class_10A_10B_7C":
        await call.message.answer("https://t.me/Aigerim2710", reply_markup=bbackKeyboard)
    elif call.data == "class_10C":
        await call.message.answer("https://t.me/AzatAgs", reply_markup=bbackKeyboard)
    elif call.data == "class_11A_11B":
        await call.message.answer("https://t.me/Arthur_Arutyunyan", reply_markup=bbackKeyboard)

    # Notify the Telegram server that the callback query is answered successfully
    await call.answer()

# School telegram chats


@dp.callback_query_handler(text=["academTeam", "it_support_chat", "cleaning", "sklad", "zayavki", "olympiads", "collegeCounseling", "classroomManagement"])
async def check_button(call: types.CallbackQuery):

    # Checking which button is pressed and respond accordingly
    if call.data == "academTeam":
        await call.message.answer("https://t.me/+V0qM8HoO4q9rUqCL", reply_markup=bbackKeyboard)
    elif call.data == "it_support_chat":
        await call.message.answer("https://t.me/+ywpD7ThjJnI2ZDEy", reply_markup=backKeyboard)
    elif call.data == "cleaning":
        await call.message.answer("https://t.me/+3qoxmjz7gN1jMzgy", reply_markup=backKeyboard)
    elif call.data == "sklad":
        await call.message.answer("https://t.me/+iEqA_0BAXuwyNzRi", reply_markup=backKeyboard)
    elif call.data == "zayavki":
        await call.message.answer("https://t.me/+WU-PKkqVlLtlMzdi", reply_markup=bbackKeyboard)
    elif call.data == "olympiads":
        await call.message.answer("https://t.me/+UNH9cPs6_wzjY1mn", reply_markup=bbackKeyboard)
    elif call.data == "collegeCounseling":
        await call.message.answer("https://t.me/+bJRlA5cN9PMxOGIy", reply_markup=bbackKeyboard)
    elif call.data == "classroomManagement":
        await call.message.answer("https://gardenschoolastana-my.sharepoint.com/:o:/g/personal/a_yesdauletkyzy_ags_edu_kz/EiQoQCpFI1RBnSqlB7KgJZkBysfNO1yZq4bEerxJEvqCdA?e=Qe4ubm", reply_markup=bbackKeyboard)

    # Notify the Telegram server that the callback query is answered successfully
    await call.answer()

# -------------------------- END HIGH SCHOOL QUERY HANDLER --------------------------


# -------------------------- ELEM SCHOOL QUERY HANDLER ------------------------------
# -------------------------- END ELEM SCHOOL QUERY HANDLER --------------------------

# Рассылка сообщений
@dp.message_handler(commands=['sendall'])
async def sendall(message: types.Message):
    if message.chat.type == 'private':
        if message.from_user.id == 437628023 or message.from_user.id == 495531330:
            text = message.text[9:]
            users = db.get_users()
            print(users)
            for row in users:
                print("пользователь ", row[1])
                try:
                    await bot.send_message(row[1], text)
                    print('сообщение было отправлено пользователю: ', row[1])
                    if int(row[1]) != 1:
                        db.set_active(row[0], 1)
                except:
                    db.set_active(row[0], 0)

            await bot.send_message(message.from_user.id, 'Успешная расссылка')


# START THE BOT
if __name__ == '__main__':
    executor.start_polling(dp)
