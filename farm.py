import pandas as pd 

#Class for Farm
class Farm: 
    #initiate class with instance variables: 
    def __init__(self, township, range, meridian, crop, acres, field):
        self.township = township #farm township 
        self.range = range #farm range 
        self.meridian = meridian #farm meridian 
        self.crop = crop #farm crop 
        self.acres = acres #farm acres 
        self.field = field #farm land

    #Method retrieves the risk area for the specific farm  
    #based on passed in township, range, and meridian, and data from baserate.csv 
    @property
    def risk_area(self): 
        fi = pd.read_csv("baserate.csv")
        farm_info = fi.values.tolist()
        for i in farm_info: 
            if i[0] == self.township and i[1] == self.range and i[2] == self.meridian:
                risk_area = i[4] 
                break
        return risk_area

    #Method prints out all of the farm information
    def get_farm_information(self): 
        print("Farm Information: ")
        print(f"Township: {self.township}, Range: {self.range}, Meridian: {self.meridian}")
        print(f"Risk Area: {self.risk_area}")
        print(f"Crop: {self.crop}")
        print(f"Acres: {self.acres}")
        print(f"Field: {self.field}")
        print("\n")
