import json
class Portfolio:
    def __init__(self) -> None:
        self.data_dict={}
        self.token_list=[]
        

    def check_token(self,token,flag):
        if flag==1:
            with open("list.json","r") as readfile:
                self.token_list=json.load(readfile)
                #print(self.token_list)
        for i in range(len(self.token_list)):
            if str(self.token_list[i]["name"]).lower()==str(token) or self.token_list[i]["symbol"]==str(token):
                return True
        return False
    
    def input_portfolio(self):
        n=0
        first_entry=1
        while(n!=2):
            print("1. Make an Entry")
            print("2. Exit")
            n=int(input("choose"))
            if n== 1:
                name=str(input("Enter Token Name")).lower()
                if self.check_token(name,first_entry)==True:
                    quantity=float(input("Enter amount you hold"))
                    self.data_dict[name]=quantity
                    first_entry=0
                else:
                    print("Token not found")
                    pass
            elif n!= 2:
                print("choose correct option")
        self.generate_file()

    def generate_file(self):
        with open("portfolio.json","w") as datafile:
            json.dump(self.data_dict,datafile,indent=5)

run_=Portfolio()
run_.input_portfolio()
