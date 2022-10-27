#python-telegram-bot==13.14
from telegram.ext import Updater, CommandHandler, Filters,MessageHandler
from bot_commands import *
from API import TOKEN #файл с токеном
    
app = Updater(TOKEN)
dispatcher = app.dispatcher
app.dispatcher.add_handler(CommandHandler('help', help))
conv_handler = ConversationHandler(
    entry_points=[CommandHandler('start', start)],
    states={
        NEXT: [MessageHandler(Filters.text & ~Filters.command, turn)],
        PLAY: [MessageHandler(Filters.text & ~Filters.command, game)]
    },
    fallbacks=[CommandHandler('cancel', cancel)]
)

dispatcher.add_handler(conv_handler)

print('бот работает')
app.start_polling()
app.idle()