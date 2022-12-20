------------------------------------------------- FARM CLASS --------------------------------------------------

initiate a Farm instance with the following parameters: 
	Farm(township, range, meridian, crop, acres, field, wealth)
	- township: farm township (int)
	- range: farm range (int)
	- meridian: farm meridian (int)
	** township, range and meridian is a locator system used in Alberta to identify a farm
	   see https://www.alberta.ca/alberta-township-survey-system.aspx for more information
	- acres: # of acres for that crop (int)
	- crop: either 'canolapolish', 'canolaargentine', 'CPS' (canadian Prairie Spring), or 'HRS' (Hard Red Spring) (string)
	- field: either "S" (stubble), "F" (fallow), or "I" (irrigated) (string)
	- wealth: farmers initial wealth (int)

Farm Attributes:
	** call farm.attribute to retrieve ** 
	- township: farm township (int)
	- range: farm range (int)
	- meridian: farm meridian (int)
	- risk_area: farm risk area (int)
	- acres (int)
	- crop (string)
	- field (string)
	- wealth (int)
	- wealth_history (array)
	- transaction_list (array)

Farm Methods: 
	** call farm.method() to retrieve ** 
	- get_farm_information: prints farm information (none)
	- add_transaction(transaction type, amount, date): add transaction to farms transaction list
	- set_wealth(amount): allows the farmer to set their wealth at a later point


------------------------------------------------- INSURANCE CLASS --------------------------------------------------

initiate an Insurance instance with the following parameters: 
	Insurance(farm, coverage, hail_endorsement)
		- farm: instance of Farm class (Farm)  
    	- coverage: either 50, 60, 70 or 80 (percent)(int)
    	- hail_endorsement: either 'Y' if yes, 'N' if no (string)

Instance Attributes: 
	** call instance.attribute to retrieve ** 
	- farm: instance of Farm class (Farm)  
	- insured_acres: # of acres being insured for that crop (int)
    	- crop: either 'canolapolish', 'canolaargentine', 'CPS' (canadian Prairie Spring), 'HRS' (Hard Red Spring) (string)
	- field: either "S" (stubble), "F" (fallow), or "I" (irrigated) (string)
    	- coverage: either 50, 60, 70 or 80 (percent)(int)
    	- hail_endorsement: either 'Y' if yes, 'N' if no (string)
	- base_rate: returns hail insurance base rate for the farm (flt)
	- yield_estimate: returns AFSC per-acre yield estimate for the farm (flt)
	- dollars_liability: returns the per acre dollar liability (flt)
	- total_liability: returns the total dollar liability (flt)
	- hail_endorsement_rate: returns the subsidized hail endorsement rate (%) (flt)
	- per_acre_hail_endorsement_premium: returns the per acre hail endorsement premium ($) (flt)
	- total_hail_endorsement_premium: returns the total farm hail endorsement premium ($) (flt)
	- crop_premium: returns the risk area crop premium per acre as a % (flt)
	- per_acre_crop_premium: returns the per acre crop premium in $ (flt)
	- total_crop_premium: returns the total crop premium in $ for all acres insured (flt)
	- total_premium_per_acre: returns the total premium/acre in $ and includes crop + hail endorsement (flt)
	- total_premium: returns the total premium in $ for both crop insurance and hail endorsement (flt)
	- yield_guarantee: returns the farmers yield guarantee (bu/acre) (flt)


Instance Methods:
	** call instance.method() to retrieve ** 
	- calc_indemnity(yield): returns the indemnity payment based on passed in final yield (int)
	- get_insurance_information: prints basic insurance information (none)

------------------------------------------------- COSTS CLASS --------------------------------------------------
Cost information comes from : https://publications.saskatchewan.ca/#/categories/1412 Saskatchewan Crop Planning Guides 2022
and is scaled based on crop soil zones in Alberta: https://www1.agric.gov.ab.ca/soils/soils.nsf/soilgroupmap?readform

initiate a Costs instance with the following parameters: 
	Costs(farm, insurance (optional))
	- farm : instance of farm class (farm)
	- insurance: instance of Insurance class (Insurance) **optional if elect for no insurance

Instance Attributes: 
	** call instance.attribute to retrieve **
	- farm: farm instance (Farm)
	- insurance: insurance instance (INSURANCE)
	- crop: type of crop (string)
	- risk_area: farm risk area (int) 
	- acres: number of acres of crop (int)
	- cost_detail_wheat: dictionary of cost detail for wheat (dictionary)
	- cost_detail_canola: dictionary of cost detail for canola (dictionary)
	- per_acre_variable_cost: returns operational costs per acre (flt)
	- per_acre_fixed_cost: returns fixed costs per acre (flt)
	- total_cost_per_acre: returns total cost per acre (fixed + variable costs) (flt)
	- total_cost: returns total cost (flt)


Instance Methods:
	** call instance.method() to retrieve ** 
	- correct_for_risk_area(cost): updates passed in cost to account for farm location and soil type (flt)
	- calc_breakeven_yield(price): given a known price calculate breakeven yield (flt)
	- calc_breakeven_price(yield): given a known yield calculate breakeven price (flt)
	- get_premium: calculates insurance premium if farmer elected for insurance
	- set_variable_cost_canola(item, value): update the value of dictonary variable costs canola
	- set_fixed_cost_canola(item, value): update the value of dictionary fixed costs canola
	- set_variable_cost_wheat(item, value): update the value of dictionary variable costs wheat
	- set_fixed_cost_wheat(item, value): update the value of dictionary variable costs wheat


------------------------------------------------- CALC CLASS --------------------------------------------------

initiate a Calc instance with the following parameters: 
	Calc(costs, sale_price, final_yield)
	- costs: instance of costs class (Costs)
	- sale_price: final sale price ($/bu) of crop (flt)
	- final_yield: final yield (bu/acre) of crop (flt)


Instance Attributes: 
	** call instance.attribute to retrieve ** 
	- costs: instance of costs class (Costs)
	- insured_acres: Num of insured acres (int)
	- sale_price: final sale price ($/bu) of crop (flt)
	- final_yield: final yield (bu/acre) of crop (flt)
	- indemnity_payment: indemnity payment received ($) (flt)
	- spot_revenue: revenue from selling crop at sale_price (flt)
	- total_revenue: revenue including sale revenue and insurance revenue (flt)
	- operating_margin: operating margin of farmer (flt)

Instance Methods:
	** call instance.method() to retrieve ** 
	- farm_results: returns information about farm revenue, cost and operating margin 
	- farm_results_per_acre: returns information about farm revenue, cost and operating
	  margin on a per acre basis

---------------------------------------------------- OTHER NOTES ----------------------------------------------------
- util.py: 
	- util contains helper methods that are used in different classes - see file for comments 

- graph_app.py
	- call to run a tkinter app that has graphing functionality for crop basis and prices
	- see comments within code for deeper understanding of how it works

- insurance_app.py
	- call to run a tkinter app that includes an insurance calculator as well as a wealth plotter
	- see comments within code for deeper understanding of how it works

------------------------------------------------------- Example -----------------------------------------------------

There are Four test farms you can use:
    farm 1: Township 26, Range 29, Mer 4 (Near Airdrie Alberta)
    farm 2: Township 32, Range 1, Mer 5 (Near Olds Alberta)
    farm 3: Township 7, Range 21, Mer 4 (Near Lethbridge Alberta)
    farm 4: Township 19, Range 14, Mer 4 (near Brooks Alberta)

See example.py for an example of using the code!