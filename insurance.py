from farm import *

#Class for Insurance
class Insurance: 

    spring_price = {
    'canolapolish':16.33,
    'canolaargentine':16.33,
    'CPS':8.44,
    'HRS':8.71
    }
    number_of_crops = 0

    #initiate class with instance variables: 
    def __init__(self, farm, insured_acres, crop, field, coverage, hail_endorsement):
        self.farm = farm #pass in farm 
        self.insured_acres = insured_acres #insured_acres: how many acres of crop being insured 
        self.crop = crop #crop: either 'canolapolish', 'canolaargentine', 'CPS', 'HRS'
        self.field = field #field: either "S" stubble, "F" fallow, or "I" irrigated
        self.coverage = coverage #coverage: either 50, 60, 70 or 80 (percent)
        self.hail_endorsement = hail_endorsement #hail_endoresement: 'Y' if yes, 'N' if no
        Insurance.number_of_crops = Insurance.number_of_crops + 1 #adds 1 to number of insured crops

    #Method retrieves the hail insurance base rate for the specific farm  
    #based on passed in township, range, and meridian, and data from baserate.csv 
    @property
    def base_rate(self): 
        fi = pd.read_csv("baserate.csv")
        farm_info = fi.values.tolist()
        for i in farm_info: 
            if i[0] == self.farm.township and i[1] == self.farm.range and i[2] == self.farm.meridian:
                base_rate = i[3]
                break
        return base_rate

    #Method retrives the AFSC yield estimate for the passed in risk area and crop
    #from data in yield.csv
    @property
    def yield_estimate(self): 
        #convert yield csv data to list
        cy = pd.read_csv("yield.csv")
        yields = cy.values.tolist()
        for i in yields: 
            if i[0] == self.farm.risk_area and i[1] == self.crop: 
                #find yield if fallow
                if self.field == "F": 
                    crop_yield = i[2]
                #find yield if stubble 
                elif self.field == "S": 
                    crop_yield = i[3]
                #find yield if irrigated 
                else: 
                    crop_yield = i[4]
                break
        return crop_yield


    # method calculates per acre dollar liability 
    @property
    def dollars_liability(self): 
        #liability = spring insured price x coverage level x normal expected yield
        return(round(self.spring_price[self.crop] * self.coverage/100 * self.yield_estimate, 2))

    # gets the total farm dollar liability 
    @property
    def total_liability(self): 
        #total liability = per acre liability x insured acres
        return(self.dollars_liability*self.insured_acres)
    
    #method gets the subsidized hail endorsement rate 
    @property
    def hail_endorsement_rate(self):
        base_rate = self.base_rate
        #if elect for hail endorsement and coverage level is greater than 50%
        if self.hail_endorsement == 'Y' and self.coverage > 50:
            if self.crop == "canolapolish" or self.crop == "canolaargentine": 
                hail_endorsement_rate = round(.383 * 1.5 * base_rate, 2) 
            elif self.crop == "peas":
                hail_endorsement_rate = round(.383 * 1.75 * base_rate, 2)
            else: 
                hail_endorsement_rate = round(.383 * base_rate, 2) 
        else: 
            hail_endorsement_rate = 0 
        return hail_endorsement_rate

    #method gets the per acre hail endorsement premium
    @property
    def per_acre_hail_endorsement_premium(self):
        #hail endorsement premium = dollars liability x hail endorsement rate
        return(round(self.dollars_liability * self.hail_endorsement_rate/100, 2))

    #method gets total farm hail endorsement premium 
    @property
    def total_hail_endorsement_premium(self):
        #total hail endorsement premium = hail endorsement premium x insured acres 
        return(self.per_acre_hail_endorsement_premium * self.insured_acres)

    #method retrieves the risk area crop premium as a percentage
    @property
    def crop_premium(self): 
        p = pd.read_csv("premium.csv")
        crop_premium = p.values.tolist()
        for i in crop_premium: 
            if i[0] == self.farm.risk_area and i[1] == self.crop and i[2] == self.field and i[3] == self.coverage: 
                percent_premium = round(i[4]*100, 2)
        return percent_premium
    
    #method retrieves the risk area crop premium as a dollar amount per acre
    @property
    def per_acre_crop_premium(self):
        #per acre premium = crop premium percentage x dollars liability
        return(round(self.crop_premium/100 * self.dollars_liability, 2))

    #method retrieves the total crop premium as a dollar amount for all acres insured
    @property
    def total_crop_premium(self): 
        #total premium = per acre crop premium x insured acres
        return(self.per_acre_crop_premium*self.insured_acres)

    #method retrieves the total premium per acre (crop premium + hail endorsement premium)
    @property
    def total_premium_per_acre(self): 
        #total premium = crop premium + hail endorsement
        return(round(self.per_acre_crop_premium + self.per_acre_hail_endorsement_premium, 2))

    #method retrieves the total premium paid per farm for both crop insurance and hail endorsement
    @property
    def total_premium(self):
        #total premium = total acre premium x insured acres
        return(self.total_premium_per_acre * self.insured_acres)

    #calculate yield guarantee under specified coverage level, given expected yield
    @property
    def yield_guarantee(self): 
        #yield guarantee = yield estimate x coverage level
        return(self.yield_estimate * self.coverage / 100)

    #calculates the total indemnity payment, method gets called by passing in final yield
    def calc_indemnity(self, y):
        guarantee = self.yield_guarantee 
        if guarantee > y: 
            payment = round((guarantee - y) * self.spring_price[self.crop] * self.insured_acres, 2)
            # print(f"Yield of {y} bu/acre is less than yield guarantee of {guarantee} bu/acre, thus insurance payment of ${payment} received" "\n")
        else: 
            payment = 0
            # print(f"Yield of {y} bu/acre is higher than yield guarantee of {guarantee} bu/acre, thus no indemnity payment received" "\n")
        return(round(payment, 2)) 

    def get_insurance_information(self): 
        print(f"Insurance information for {self.insured_acres} acres of {self.crop} at {self.coverage}% coverage:")
        print(f"Farm Location: mer {self.farm.meridian}, twn {self.farm.township}, rng {self.farm.range}, RA {self.farm.risk_area}")
        if self.hail_endorsement == "Y":
            print("Farmer has elected for crop insurance with hail endorsement")
        else:
            print("Farmer has elected for crop insurance WITHOUT hail endorsement")
        print(f"The farmers estimated yield is: {self.yield_estimate} bushels/acre, and yield guarantee is: {self.yield_guarantee} bushels/acre")
        print(f"The farmers per/acre premium is: ${self.total_premium_per_acre} and total premium is: ${self.total_premium}" "\n")
 
 
    #calculates the number of crops being insured
    @classmethod
    def num_of_crops(cls):
        return cls.number_of_crops
