from insurance import * 

class Costs: 
    def __init__(self, farm, insurance = None): 
        self.farm = farm #pass in instance of farm
        self.insurance = insurance #pass in insurance instance
        self.crop = farm.crop
        self.risk_area = farm.risk_area
        self.acres = farm.acres

        #dictionary of wheat costs 
        self.cost_detail_wheat = {
        'Variable Cost': {
            'Seed':26.92,
            'Seed Treatment': 0.74,
            'Fertilizer': 158.05,
            'Pesticide':101.19,
            'Fuel':15.31,
            'Machinery_Operation':9.98,
            'Labour Hired':22.05,
            'Utilities and Misc': 4.23,
            'Insurance Premium': self.get_premium(),
            'Interest On Operation': 7.13,
        },
        'Fixed Cost': {
            'Building Repair': 0.69,
            'Property Taxes': 5.55, 
            'Business Overhead': 3.19, 
            'Machinery Depreciation': 41.06,
            'Building Depreciation' : 1.45, 
            'Machinery Investment': 15.83,
            'Building Investment' :0.48,
            'Land Investment' : 39.28,
        }
        }

        #dictionary of canola costs
        self.cost_detail_canola = {
        'Variable Cost': {
            'Seed':75.73,
            'Seed Treatment': 9,
            'Fertilizer': 187.62,
            'Pesticide':74.88,
            'Fuel':16.21,
            'Machinery_Operation':9.98,
            'Labour Hired':21.05,
            'Utilities and Misc': 4.23,
            'Insurance Premium': self.get_premium(),
            'Interest On Operation': 8.46,
        },
        'Fixed Cost': {
            'Building Repair': 0.69,
            'Property Taxes': 5.55, 
            'Business Overhead': 3.19, 
            'Machinery Depreciation': 41.06,
            'Building Depreciation' : 1.45, 
            'Machinery Investment': 15.83,
            'Building Investment' :0.48,
            'Land Investment' : 39.28,
        }
        }

    #returns total operational costs per acre
    @property
    def per_acre_variable_costs(self):

        if self.crop == "HRS" or self.crop == "CPS":
            variable_costs = sum(list(map(lambda x: 0 if x is None else x, self.cost_detail_wheat['Variable Cost'].values())))
        elif self.crop == "canolapolish" or self.crop == "canolaargentine": 
            variable_costs = sum(list(map(lambda x: 0 if x is None else x, self.cost_detail_canola['Variable Cost'].values())))
        else: 
            variable_costs = 0
        return(round(self.correct_for_risk_area(variable_costs), 2))

    #returns total fixed costs per acre
    @property 
    def per_acre_fixed_costs(self): 
        if self.crop == "HRS" or self.crop == "CPS":
            fixed_costs =sum(list(map(lambda x: 0 if x is None else x, self.cost_detail_wheat['Fixed Cost'].values())))
        elif self.crop == "canolapolish" or self.crop == "canolaargentine": 
            fixed_costs =sum(list(map(lambda x: 0 if x is None else x, self.cost_detail_canola['Fixed Cost'].values())))
        else: 
            fixed_costs = 0
        return(round(self.correct_for_risk_area(fixed_costs), 2))

    #method corrects the passed in cost bsaed on the farm risk area soil type
    def correct_for_risk_area(self, cost):
        if self.risk_area == 3 or self.risk_area == 4: 
            variable_costs = cost*.9
        elif self.risk_area == 5 or self.risk_area == 7: 
            variable_costs = cost*1.1
        else: 
            variable_costs = cost
        return cost 

    #get insurance premium, if farmer elected for insurance
    def get_premium(self): 
        if self.insurance == None: 
            premium = 0
        else: 
            premium = self.insurance.total_premium_per_acre
        return premium 

    #returns total costs per acre
    @property
    def total_cost_per_acre(self): 
        total_acre_costs = round(self.per_acre_fixed_costs + self.per_acre_variable_costs, 2)
        return(total_acre_costs)

    #returns total cost
    @property
    def total_costs(self): 
        total_cost = self.total_cost_per_acre * self.acres
        return(round(total_cost, 2))

    #if knowing target price, can calculate yield needed to break even
    def calc_breakeven_yield(self, price): 
        breakeven = self.total_cost_per_acre / price
        print(f"Given a price of: ${price}/bu, to cover fixed & variable costs you would need to grow {round(breakeven, 2)} bu/acre")
        return breakeven

    #if knowing target yield, can calculate price needed to break even
    def calc_breakeven_price(self, y): 
        price = round(self.total_cost_per_acre / y, 2) 
        print(f"Given a yield of: {y} bu/acre, to cover fixed & variable costs you would need to sell at ${price}/bu")
        return price