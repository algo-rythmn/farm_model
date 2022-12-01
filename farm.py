import pandas as pd 

#Class for Farm
class Farm: 
    #initiate class with instance variables: 
    def __init__(self, township, range, meridian):
        self.township = township #farm township 
        self.range = range #farm range 
        self.meridian = meridian #farm meridian 
        self.risk_area = self.get_risk_area() #farm risk area

    #Method retrieves the risk area for the specific farm  
    #based on passed in township, range, and meridian, and data from baserate.csv 
    def get_risk_area(self): 
        fi = pd.read_csv("baserate.csv")
        farm_info = fi.values.tolist()
        for i in farm_info: 
            if i[0] == self.township and i[1] == self.range and i[2] == self.meridian:
                self.risk_area = i[4] 
                break
        return self.risk_area

    #Method prints out all of the farm information
    def get_farm_information(self): 
        print("Farm Information: ")
        print(f"Farm Meridian, Township, Range: {self.meridian},{self.township},{self.range}")
        print(f"Farm Risk Area: {self.risk_area}" "\n")
