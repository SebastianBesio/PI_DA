import json
import pandas as pd
from pycoingecko import CoinGeckoAPI
from datetime import date
from dateutil.rrule import rrule, DAILY
import time

# Creemos la funcionalidad de Coin Gecko.
cg = CoinGeckoAPI()

def new_data_request(coin_id, dateRequest):
    r = cg.get_coin_history_by_id(coin_id, date=dateRequest, localization=False)

    # Agregarle la fecha al dato levantado
    r['date'] = dateRequest

    # Eliminar images que no la vamos a precisar
    del(r['image'])

    # Me quedo con el valore en dolares de estas tres variables importantes y borro el resto de la data en 'market_data'
    r['current_price'] = r['market_data']['current_price']['usd']
    r['market_cap'] = r['market_data']['market_cap']['usd']
    r['total_volume'] = r['market_data']['total_volume']['usd']
    del(r['market_data'])

    # Sacar de community_data para llevarlo a la raiz.
    r.update(r['community_data'])
    del(r['community_data'])

    # Sacar de developer_data para llevarlo a la raiz.
    r.update(r['developer_data'])
    del(r['developer_data'])

    # Sacar de public_interest_stats para llevarlo a la raiz.
    r.update(r['public_interest_stats'])
    del(r['public_interest_stats'])

    # Sacar de code_additions_deletions_4_weeks para llevarlo a la raiz.
    r.update(r['code_additions_deletions_4_weeks'])
    del(r['code_additions_deletions_4_weeks'])

    # Guardo el nuevo registro en el json.
    with open("datasets/raw_coins_data.json", "a") as outfile:
        json.dump(r, outfile)
        outfile.write("\n")


# initializing the start and end date
start_date = date(2021, 1, 4)
end_date = date(2023, 7, 31)

# coinNames = ['bitcoin', 'ethereum', 'tether', 'binancecoin', 'ripple', 'usd-coin', 'staked-ether', 'dogecoin', 'cardano', 'solana']
coinNames = ['ethereum', 'tether', 'binancecoin', 'ripple', 'usd-coin', 'staked-ether', 'dogecoin', 'cardano', 'solana']

# iterating over the dates
for d in rrule(DAILY, dtstart=start_date, until=end_date):
    d = d.strftime("%d-%m-%Y")
    for coin in coinNames:
        new_data_request(coin, d)
        print(d, coin)
        time.sleep(5)   