import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

from config import bot_token

import frinkiac

logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s', level=logging.INFO, filename='frinklog.log')
logger = logging.getLogger(__name__)

def screen_grabber(bot, update, args):
    """
        Retrieves the screenshot from frinkiac.py
    """
    cmd = update.message.text.split()[0].lower()
    query = " ".join(args)

    if cmd == '/fut':
        simpscreen = False
    else:
        simpscreen = True

    if len(args) > 0:
        # Search terms supplied
        search = frinkiac.search(query, simpscreen)
        if query.startswith('"') and query.endswith('"'):
            returned_screen = search[0].meme_url(caption = query.split('"')[1])
        else:
            returned_screen = search[0].meme_url()
    else:
        # Random screen
        random_screen = frinkiac.random(simpscreen)
        returned_screen = random_screen.meme_url()

    logger.info('User "{0}" Search: {1} Url: {2}'.format(update.message.from_user.username, update.message.text, returned_screen))
    update.message.reply_text(returned_screen)

def start(bot, update):
    """
        Display commands that are possible.
    """

    msg = '*GREETINGS FROM THE WORLD OF TOMORROW*\n'
    msg += '\n'
    msg += '/simp - Get a random screenshot.\n'
    msg += '/simp search - Search for a specific screenshot.\n'
    msg += '/simp "search" - Search for a screenshot then caption it with the search.\n'
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
    msg = 'https://morbotron.com/meme/S05E01/378728.jpg?b64lines=RnJpbmtpQm90IGRvZXMgbm90IAp3b3JrIHRoYXQgd2F5'
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