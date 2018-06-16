#!/usr/bin/env python
# -*- coding: utf-8 -*-
from os import getenv
from telegram.ext import Updater, CommandHandler
import logging
from dotenv import load_dotenv, find_dotenv
import datetime
from pprint import pprint

from toggl_client import TogglClient

# Load env data
load_dotenv(find_dotenv())
toggl_token = getenv('TOGGL_REPORT_API_KEY')
telegram_token = getenv('TELEGRAM_TOKEN')

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.DEBUG)

logger = logging.getLogger(__name__)



def main():
    """Run bot."""
    updater = Updater(telegram_token)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # on different commands - answer in Telegram
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))
    dp.add_handler(CommandHandler("set", set_alarm,
                                  pass_args=True,
                                  pass_job_queue=True,
                                  pass_chat_data=True))
    dp.add_handler(CommandHandler("unset", unset_alarm, pass_chat_data=True))

    # log all errors
    dp.add_error_handler(error)

    # Start the Bot
    updater.start_polling()

    # Block until you press Ctrl-C or the process receives SIGINT, SIGTERM or
    # SIGABRT. This should be used most of the time, since start_polling() is
    # non-blocking and will stop the bot gracefully.
    updater.idle()

def start(bot, update):
    update.message.reply_text('Hi! Use /set to start toggl productivity alarm')

def help(bot, update):
    """Send a message when the command /help is issued."""
    update.message.reply_text('If you want to start alarm, use /set')
    update.message.reply_text('If you want to stop alarm, use /unset')
    update.message.reply_text('This is a test bot. You can read more about this in https://www.fenomenomutante.com/8')

def error(bot, update, error):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, error)

def set_alarm(bot, update, args, job_queue, chat_data):
    """Add a job to the queue."""
    logger.info(update.message)
    chat_id = update.message.chat_id
    time_of_day = (datetime.datetime.now() + datetime.timedelta(seconds=10)).time()
    #TODO: User defines weekdays of alarm
    days = tuple(range(7))

    job = job_queue.run_daily(job_toggl_status, time_of_day, days, context=chat_id)
    chat_data['job'] = job

    update.message.reply_text('Alarm successfully set!')

def job_toggl_status(bot, job):
    """Get toggl info"""
    toggl = TogglClient(toggl_token)
    result = toggl.get_summary_results()
    if result:
        bot.send_message(job.context, text=u'\U0001f483')
    else:
        bot.send_message(job.context, text=u'\U0001f4A9')


def unset_alarm(bot, update, chat_data):
    """Remove the job if the user changed their mind."""
    if 'job' not in chat_data:
        update.message.reply_text('You have no active alarm')
        return

    job = chat_data['job']
    job.schedule_removal()
    del chat_data['job']

    update.message.reply_text('Alarm successfully unset!')


if __name__ == '__main__':
    main()
