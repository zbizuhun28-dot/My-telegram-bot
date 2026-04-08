from telegram import Update
from telegram.ext import Updater, MessageHandler, Filters, CallbackContext

TOKEN = "8772785235:AAEBcphDJp2VU-eZWeQwG8Qlw9-_WVFYm1M"  # Replace with your token from BotFather

def delete_joins(update: Update, context: CallbackContext):
    if update.message.new_chat_members:
        # Delete the join message
        context.bot.delete_message(chat_id=update.message.chat.id,
                                   message_id=update.message.message_id)

def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(MessageHandler(Filters.status_update.new_chat_members, delete_joins))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
