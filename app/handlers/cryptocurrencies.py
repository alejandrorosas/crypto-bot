import json
import requests
import telegram


def request_currency(name):
    r = requests.get(f'https://api.coinmarketcap.com/v1/ticker/{name}/')
    return json.loads(r.content)[0]


def format_currency_message(coin_info):
    symbol = coin_info['symbol']
    price = coin_info['price_usd']
    hour_change = coin_info['percent_change_1h']
    day_change = coin_info['percent_change_24h']
    return '*{} = {} USD*\n1h. {}%\n24h. {}'.format(symbol, price, hour_change, day_change)


def intense_handler(bot, update):
    coin_handler(bot, update, 'intensecoin')


def bitcoin_handler(bot, update):
    coin_handler(bot, update, 'bitcoin')


def coin_handler(bot, update, coin_id):
    intense = request_currency(coin_id)
    message = format_currency_message(intense)
    bot.send_message(
        chat_id=update.message.chat_id,
        text=message,
        parse_mode=telegram.ParseMode.MARKDOWN)
