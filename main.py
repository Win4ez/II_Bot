from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import telegram

TOKEN = "5306659845:AAHTmWESy9upZAK3I6iY4T2jOnAYrnZjt5U"

bot = telegram.Bot(token=TOKEN)

updater = Updater(token=TOKEN, use_context=True)
dispatcher = updater.dispatcher


def startCommand(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text='Привет, давай пообщаемся?')


def textMessage(bot, update):
    response = 'Получил Ваше сообщение: ' + update.message.text
    bot.send_message(chat_id=update.message.chat_id, text=response)


start_command_handler = CommandHandler('start', startCommand)
text_message_handler = MessageHandler(Filters.text, textMessage)
dispatcher.add_handler(start_command_handler)
dispatcher.add_handler(text_message_handler)
updater.start_polling(drop_pending_updates=True)
updater.idle()
