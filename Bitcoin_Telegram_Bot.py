import requests
import time

#Global Variables
api_key = '4d340490-bb78-412e-ab3d-66d193f596cd'
bot_key = '6498590567:AAEx4SKFXqmZzocvnQ-ouPCjs3wrLFeceCk'
chat_id = '5791515227'
limit = 59000
time_interval = 10 * 60

def get_price():
    url = 'https://sandbox-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'

    parameters = {
        'start':'1',
        'limit':'5000',
        # 'convert':'USD'
    }

    headers = {
        'Accepts': 'application/json',
        'X-CMC_PRO_API_KEY': api_key,
    }

    response = requests.get(url, headers=headers).json()
    btc_price = response['data'][0]['quote']['USD']['price']
    return btc_price
    # return response

# print(get_price())

def send_update(chat_id, msg):
    url = f"https://api.telegram.org/bot{bot_key}/sendMessage?chat_id={chat_id}&text={msg}"
    requests.get(url)

def main():
    while True:
        price = get_price()
        price(price)
        if price < limit:
            send_update(chat_id, f"سعر النهارده : {price }")
        time.sleep(time_interval)

main()