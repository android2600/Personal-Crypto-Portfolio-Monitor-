import requests
import json

class generate:
    api_base_url="https://api.coingecko.com/api/v3/"

    def coin_list(self):
        result=requests.get(f"{self.api_base_url}coins/list")
        data_list=result.json()
        with open("list.json","w") as outfile:
            json.dump(data_list,outfile,indent=5)
    
run_=generate()
run_.coin_list()