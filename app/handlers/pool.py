import json
import requests
import telegram


def request_stats():
    r = requests.get('http://151.80.43.131:8117/stats')
    return json.loads(r.content)


def format_pool_message(stats):
    pool = stats['pool']
    pool_miners = pool['miners']
    pool_hashrate = pool['hashrate']
    pool_blocks = pool['totalBlocks']
    return 'Hashrate: {}H/s\nMiners: {}\nBlocks found: {}'.format(pool_hashrate, pool_miners, pool_blocks)


def pool_handler(bot, update):
    stats = request_stats()
    message = format_pool_message(stats)
    bot.send_message(
        chat_id=update.message.chat_id,
        text=message,
        parse_mode=telegram.ParseMode.MARKDOWN)
