import requests
import json

class QuantData:
    api_base_url="https://api.coingecko.com/api/v3/"
    def market_data(self,tickers):
        currency="usd"
        list_="%2C".join(tickers)
        sparkline="false"
        result=requests.get(f"{self.api_base_url}coins/markets?vs_currency={currency}&ids={list_}&order=market_cap_desc&per_page=100&page=1&sparkline={sparkline}")
        result_json=result.json()
        with open("data.json","w") as outfile:
            json.dump(result_json,outfile,indent=5)
                   

portfolio=QuantData()
list_=["avalanche-2","stellar","near","oasis-network","acala","moonbeam","astar","helium","juno-network","crypto-com-chain","illuvium"]
portfolio.market_data(list_)
