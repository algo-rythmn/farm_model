from farm import *
from insurance import *
from costs import *
from calc import *

"""
Step 1: Define the farm parameters
In this example we will use the lethbridge test farm with township = 7, range = 21, and meridian = 4
"""
township = 7
range = 21
meridian = 4 

"""
Step 2: Initiate farm instance with parameters
"""
test_farm = Farm(township, range, meridian)

test_farm.get_farm_information() #can call method to get test farm information

"""
Step 3: Define the Insurance parameters
In this exampe we will assume we are insuring 250 acres of Hard Red Spring Wheat (HRS)
under stubble farming (S) with 80% coverage including crop premium and hail endorsement
"""
insured_acres = 1000 #1000 acres being insured
crop = "HRS" #crop is Hard Red Spring Wheat
field = "S" #stubble farming
coverage = 80 #80% insurance coverage
hail_endorsement = "Y" #Hail endorsement added (this is typically the case)

"""
Step 4: Initiate insurance instance and pass in test farm along with defined parameters
"""
test_farm_insurance = Insurance(test_farm, insured_acres, crop, field, coverage, hail_endorsement)

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
Pass in instance of insurance into costs class 
"""
test_farm_costs = Costs(test_farm_insurance)

"""
Step 8: can initiate instance of calc class which calculates the farmers results
Must pass in the expected price and yield at harvest
"""
price_estimate = 11 
yield_estimate = 45

test_farm_results = Calc(test_farm_costs, price_estimate, yield_estimate)
test_farm_results.farm_results()