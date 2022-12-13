from costs import *

class Calc: 
    def __init__(self, costs, sale_price, final_yield): 
        self.costs = costs #instance of costs class (COSTS)
        self.acres = costs.acres #Num of insured acres (int)
        self.sale_price = sale_price #final sale price ($/bu) of crop (flt)
        self.final_yield = final_yield #final yield (bu/acre) of crop (flt)
        self.spot_revenue = round(self.sale_price*self.final_yield*self.acres, 2) #revenue from selling crop at sale_price (flt)
        self.total_revenue = self.spot_revenue + self.indemnity_payment #revenue including sale revenue and insurance revenue (flt)
        self.operating_margin = round((self.total_revenue - self.costs.total_costs) / self.total_revenue * 100, 2) #operating margin of farmer (flt)

    #calculates the indemnity payment, and sets to zero if farmer elects for no insurance to be used
    @property 
    def indemnity_payment(self):
        if self.costs.insurance == None: 
            indemnity_payment = 0
        else: 
            indemnity_payment = self.costs.insurance.calc_indemnity(self.final_yield)
        return indemnity_payment
    
    # returns information about farm revenue, cost and operating margin 
    def farm_results(self): 
        print(f"The farmer produced {self.final_yield} bu/acre & sold at the spot price of ${self.sale_price}/bu")
        if self.indemnity_payment == 0:
            print("No indemnity payment was received")
        else: 
            print(f"An indemnity payment was received totalling: ${self.indemnity_payment}")
        
        print(f"Total revenue was: ${self.total_revenue}, total cost was: ${self.costs.total_costs}")
        print(f"Operating margin was: {self.operating_margin}%")
        
    #returns information about farm revenue, cost and operating margin on a per acre basis
    def farm_results_per_acre(self): 
        print(f"The farmer produced {self.final_yield} bu/acre & sold at the spot price of ${self.sale_price}/bu")
        if self.indemnity_payment == 0:
            print("No indemnity payment was received")
        else: 
            print(f"An indemnity payment was received totalling: ${round(self.indemnity_payment/self.acres, 2)}/acre")
        
        print(f"Total revenue was: ${round(self.total_revenue/self.acres, 2)}/acre, total cost was: ${round(self.costs.total_costs/self.acres, 2)}/acre")
        print(f"Operating margin was: {self.operating_margin}%")