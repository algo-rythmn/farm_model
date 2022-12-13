import pandas as pd 

#Class for farm
class Farm: 
    #initiate class with instance variables: 
    def __init__(self, township = 7, range = 21, meridian =4, crop = "HRS", acres = 1000, field = "S", wealth = 500_000):
        self.township = township #farm township 
        self.range = range #farm range 
        self.meridian = meridian #farm meridian 
        self.crop = crop #farm crop 
        self.acres = acres #farm acres 
        self.field = field #farm land
        self.wealth = wealth #farmer initial wealth
        self.wealth_history = [] #keeps track of farmers wealth over time
        self.transaction_list = [] #farmers cash transactions 

    #Method retrieves the risk area for the specific farm  
    #based on passed in township, range, and meridian, and data from baserate.csv 
    @property
    def risk_area(self): 
        fi = pd.read_csv("DataSource/baserate.csv")
        farm_info = fi.values.tolist()
        for i in farm_info: 
            if i[0] == self.township and i[1] == self.range and i[2] == self.meridian:
                risk_area = i[4] 
                break
        return risk_area

    #method keeps track of the transactions that the farm makes
    def add_transaction(self, transaction_type, amount, date):
        self.transaction_list.append(
            {
                'Date' : date,
                'Transaction Type' : transaction_type,
                'Amount:': amount
            }
        )
    
    #allows the farmer to set their wealth at a later point
    def set_wealth(self, amount): 
        self.wealth = amount

    #Method prints out all of the farm information
    def get_farm_information(self): 
        print("Farm Information: ")
        print(f"Township: {self.township}, Range: {self.range}, Meridian: {self.meridian}")
        print(f"Risk Area: {self.risk_area}")
        print(f"Crop: {self.crop}")
        print(f"Acres: {self.acres}")
        print(f"Field: {self.field}")
        print("\n")

