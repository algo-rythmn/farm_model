from farm import *
from insurance import *
from costs import *
from calc import *

"""
Step 1: Define the farm parameters
In this example we will use the lethbridge test farm with township = 7, range = 21, and meridian = 4
We will grow 1000 acres of Hard Red Spring Wheat (HRS) using stubble farming
"""
township = 7
range = 21
meridian = 4 
crop = "HRS" #crop is Hard Red Spring Wheat
acres = 1000 #1000 acres being insured
land = "S" #stubble farming

"""
Step 2: Initiate farm instance with parameters defined in step 1
"""
test_farm = Farm(township, range, meridian, crop, acres, land)
test_farm.get_farm_information() #can call method to get test farm information

"""
Step 3: Define the Insurance parameters
In this exampe we will assume we are insuring our crop at 80% overage, with hail endorsement
"""

coverage = 80 #80% insurance coverage
hail_endorsement = "Y" #Hail endorsement added (this is typically the case)

"""
Step 4: Initiate insurance instance and pass in test farm along with defined parameters
from step 3
"""
test_farm_insurance = Insurance(test_farm, coverage, hail_endorsement)

"""
Step 5: See README to access all of the methods and data you can retrieve
to see an overview of insurance information call get_insurance_information (see below)
"""
test_farm_insurance.get_insurance_information() #returns summary of basic insurance information

"""
Step 6: Can find the farmers end of year insurance payout by passing in the final yield in bushels/acre
see example below
"""
test_farm_insurance.calc_indemnity(28) #testing to see what the indemnity payment is if ave yield is 28 bu/acre

"""
Step 7: Can create a costs class which calculates the farmers costs
Pass in instance farm and of insurance into costs class 
insurance is optional if farmer elects for no insurance
"""
test_farm_costs = Costs(test_farm, test_farm_insurance)
print(f"Farm costs per acre: ${test_farm_costs.total_cost_per_acre}/acre")
print(f"Farm costs total: ${test_farm_costs.total_costs}" "\n")

"""
Step 8: can initiate instance of calc class which calculates the farmers results
Must pass in the expected price and yield at harvest
"""
price_estimate = 11 
yield_estimate = 45

test_farm_results = Calc(test_farm_costs, price_estimate, yield_estimate)
test_farm_results.farm_results()