headers=''

session = Session()
session.headers.update(headers)

limit=10000

url_coin = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
# url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest'
parameters = {
  'start':'1',
  'limit':limit,
  'convert':'USDT',
  # 'sort':'market_cap'
  'sort':'volume_24h'
  # 'sort':'cmc_rank'
}

try:    



        response = session.get(url_coin, params=parameters)
        datee=datetime.now()
        data = json.loads(response.text)['data']
        
        # print(data)
        for i in range(limit):
            
            symbol= data[i]['symbol']
           
            datee=datetime.now()
            
            symbol=symbol+'USDT'
