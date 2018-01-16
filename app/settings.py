import os

from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())

TELEGRAM_BOT_TOKEN = os.environ.get("TELEGRAM_BOT_TOKEN")
