from telegram import Update
from telegram.ext import Updater, MessageHandler, Filters, CallbackContext
import configparser
import logging


def echo(update: Update, context: CallbackContext) -> None:
    reply_message = update.message.text.upper()
    logging.info("Update: " + str(update))
    logging.info("Context: " + str(context))
    context.bot.send_message(chat_id=update.effective_chat.id, text=reply_message)

def main():
    config = configparser.ConfigParser()
    config.read('config.ini')
    updater = Updater(token=config['TELEGRAM']['ACCESS_TOKEN'], use_context=True)
    dispatcher = updater.dispatcher
    logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                         level=logging.INFO)
    echo_handler = MessageHandler(Filters.text & (~Filters.command), echo)
    dispatcher.add_handler(echo_handler)

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
