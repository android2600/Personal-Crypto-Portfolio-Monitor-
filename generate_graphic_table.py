import json
import plotly.graph_objects as go

class generate:
    def __init__(self) -> None:
        self.dict_={}
        self.list_=[]

    def read(self):
        with open("data.json","r") as readfile:
            self.list_=json.load(readfile)
            for i in range(len(self.list_)):
                self.dict_[self.list_[i]["id"]]=self.list_[i]
    
    def create_market_data_table(self):
        self.read()
        id=[]
        curr_price=[]
        m_cap=[]
        cir_supply=[]
        total_supply=[]
        max_supply=[]
        #print(self.list_)
        
        for i in range(len(self.list_)):
            id.append(self.list_[i]["id"])
            curr_price.append('%.2f'%self.list_[i]["current_price"])
            m_cap.append(round(int(self.list_[i]["market_cap"])))
            cir_supply.append(round(int(self.list_[i]["circulating_supply"])))
            total_supply.append(round(int(self.list_[i]["total_supply"])))
            
            max_supply.append(round(int(self.list_[i]["max_supply"])) if self.list_[i]["max_supply"]!=None else "null")
        
        fig = go.Figure(data=go.Table(
            header=dict(values=["Id","Current price","Market cap","Circulating supply","Total supply","Max supply"],
            align=['center','center'],
            font=dict(color='black', size=12),
            height=50,
            ),
            cells=dict(values=[id,curr_price,m_cap,cir_supply,total_supply,max_supply],
            font=dict(size=10)
            )))
            
        fig.show()
    
    def create_portfolio_value_table(self):
        pass

run_=generate()
run_.create_market_data_table()