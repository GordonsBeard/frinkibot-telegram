import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

from config import bot_token

import frinkiac

logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

def screen_grabber(bot, update, args):
    cmd = update.message.text.split()[0].lower()
    if cmd == '/fut':
        simpscreen = False
    else:
        simpscreen = True

    if len(args) > 0:
        # Search terms supplied
        pass
    else:
        # Random screen
        random_screen = frinkiac.random(simpscreen)
        update.message.reply_text(random_screen.meme_url())

def start(bot, update):
    """
        Display commands that are possible.
    """

    msg = '*GREETINGS FROM THE WORLD OF TOMORROW*\n'
    msg += '\n'
    msg += '/simp - Get a random Simpson\'s screen.\n'
    msg += '/simp search - Search for a Simpson\'s screen.\n'
    msg += '/simp "search" - Search (and caption /w search) for Simpson\'s screen.\n'
    msg += '(You can replace /simp with /fut to get Futurama screens)'
    msg += '\n\n'
    msg += 'Simpsons - frinkiac.com\n'
    msg += 'Futurama - morbotron.com\n'

    bot.sendMessage(update.message.chat_id,
                    text = msg,
                    parse_mode = 'Markdown')

def error(bot, update, error):
    logger.warn('Update "%s" caused error "%s"' % (update, error))

def unknown(bot, update):
    """
        Fallback behavior for unknown commands.
    """
    msg = 'https://morbotron.com/meme/S05E01/378728/m/RnJpbmtpQm90IGRvZXMgbm90IAp3b3JrIHRoYXQgd2F5'
    bot.sendMessage(update.message.chat_id,
                    text = msg)

def main():
    updater = Updater(token = bot_token)
    dp = updater.dispatcher

    # Dispatchers
    dp.add_handler(CommandHandler('start', start))
    dp.add_handler(CommandHandler('simp', screen_grabber, pass_args = True))
    dp.add_handler(CommandHandler('fut', screen_grabber, pass_args = True))
    dp.add_handler(MessageHandler(Filters.command, unknown))
    dp.add_error_handler(error)

    updater.start_polling()
    print("Bot online.")
    updater.idle()

if __name__ == '__main__':
    main()