------------------------------------------------- FARM CLASS --------------------------------------------------

initiate a Farm instance with the following parameters: 
	Farm(township, range, meridian)
	- township: farm township (int)
	- range: farm range (int)
	- meridian: farm meridian (int)
	** township, range and meridian is a locator system used in Alberta to identify a farm
	   see https://www.alberta.ca/alberta-township-survey-system.aspx for more information

Farm Attributes:
	** call farm.attribute to retrieve ** 
	- township: farm township (int)
	- range: farm range (int)
	- meridian: farm meridian (int)
	- risk_area: farm risk area (int)

Farm Methods: 
	** call farm.method() to retrieve ** 
	- get_risk_area: returns risk area that the farm is located in (int) (can also just call farm.risk_area)
	- get_farm_information: prints farm information including meridian, township, range and risk area (none)


------------------------------------------------- INSURANCE CLASS --------------------------------------------------

Class Variables: 
	- spring_price: includes spring insurance price for all crops 
	- number_of_crops: if insuring more than 1 crop takes count of total number

Class Methods:
	** call class.method() to retrieve **
	- num_of_crops: if insuring more than one crop, returns number of crops (int)

initiate an Insurance instance with the following parameters: 
	Insurance(farm, insured_acres, crop, field, coverage, hail_endorsement)
	- farm: instance of Farm class (Farm)  
	- insured_acres: # of acres being insured for that crop (int)
    	- crop: either 'canolapolish', 'canolaargentine', 'barley', 
	  'CPS' (canadian Prairie Spring), 'HRS' (Hard Red Spring) (string)
	- field: either "S" (stubble), "F" (fallow), or "I" (irrigated) (string)
    	- coverage: either 50, 60, 70 or 80 (percent)(int)
    	- hail_endorsement: either 'Y' if yes, 'N' if no (string)

Instance Attributes: 
	** call instance.attribute to retrieve ** 
	- farm: instance of Farm class (Farm)  
	- insured_acres: # of acres being insured for that crop (int)
    	- crop: either 'canolapolish', 'canolaargentine', 'barley', 
	  'CPS' (canadian Prairie Spring), 'HRS' (Hard Red Spring) (string)
	- field: either "S" (stubble), "F" (fallow), or "I" (irrigated) (string)
    	- coverage: either 50, 60, 70 or 80 (percent)(int)
    	- hail_endorsement: either 'Y' if yes, 'N' if no (string)

Instance Methods:
	** call instance.method() to retrieve ** 
	- get_base_rate: returns hail insurance base rate for the farm (int)
	- get_yield_estimate: returns AFSC per-acre yield estimate for the farm (int)
	- get_dollars_liability: returns the per acre dollar liability (int)
	- get_total_liability: returns the total dollar liability (int)
	- get_hail_endorsement_rate: returns the subsidized hail endorsement rate (%) (int)
	- get_per_acre_hail_endorsement_premium: returns the per acre hail endorsement premium ($) (int)
	- get_total_hail_endorsement_premium: returns the total farm hail endorsement premium ($) (int)
	- get_crop_premium: returns the risk area crop premium per acre as a % (int)
	- get_per_acre_crop_premium: returns the per acre crop premium in $ (int)
	- get_total_crop_premium: returns the total crop premium in $ for all acres insured (int)
	- get_total_premium_per_acre: returns the total premium/acre in $ and includes crop + hail endorsement (int)
	- get_total_premium: returns the total premium in $ for both crop insurance and hail endorsement (int)
	- get_yield_guarantee: returns the farmers yield guarantee (bu/acre) (int)
	- calc_indemnity(yield): returns the indemnity payment based on passed in final yield (int)
	- get_insurance_information: prints basic insurance information (none)
        

------------------------------------------------------- Example -----------------------------------------------------

There are Four test farms you can use:
    farm 1: Township 26, Range 29, Mer 4 (Near Airdrie Alberta)
    farm 2: Township 32, Range 1, Mer 5 (Near Olds Alberta)
    farm 3: Township 7, Range 21, Mer 4 (Near Lethbridge Alberta)
    farm 4: Township 19, Range 14, Mer 4 (near Brooks Alberta)

See example.py for an example of using the code!
