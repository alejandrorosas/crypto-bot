import logging

# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO)

logger = logging.getLogger(__name__)


def start_handler(bot, update):
    """Send a message when the command /start is issued."""
    update.message.reply_text('Hi!')


def help_handler(bot, update):
    """Send a message when the command /help is issued."""
    update.message.reply_text('Help!')


def error_handler(bot, update, error):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, error)
