import pandas as pd
from costs import *
from calc import *

#a datelist from start_date to end date
def get_datelist_string(start_date, end_date): 
    date_list = pd.date_range(start_date, end_date, freq='D').strftime("%Y-%m-%d").tolist()
    return date_list


def get_datelist(start_date, end_date):
    return(pd.date_range(start_date, end_date, freq='D'))


def plotter(sale_price, final_yield, farm, insurance):

    test_farm = farm 
    test_farm_insurance = insurance
    test_farm_results = Calc(Costs(test_farm, test_farm_insurance), sale_price, final_yield) #farm result calculator
    start_date = '2020-01-01' #start of growing season
    end_date = '2020-12-31' #end of growing season

    #list of dates
    date_list = get_datelist_string(start_date, end_date)

    #important dates
    important_dates = {
        'agriinsurance_date': '2020-04-01',
        'plant_crop_date' : '2020-04-10',
        'sell_crop_date': '2020-11-03',
        'indemnity_date':'2020-11-05',
    }

    for date in date_list: 
        
        if date == important_dates['agriinsurance_date']:
            payment = test_farm_insurance.total_premium
            test_farm.add_transaction("Insurance Payment", f"-${payment}", date)
            test_farm.wealth -= payment 

        if date == important_dates['plant_crop_date']:
            cost = Costs(test_farm).total_costs
            test_farm.add_transaction("Crop Fixed and Variable Costs", f"-${cost}", date)
            test_farm.wealth -= cost

        if date == important_dates['sell_crop_date']: 
            revenue = test_farm_results.spot_revenue
            test_farm.add_transaction("Crop Sale", f"${revenue}", date)
            test_farm.wealth += revenue

        if date == important_dates['indemnity_date']: 
            indemnity = test_farm_results.indemnity_payment
            test_farm.add_transaction("Indemnity Received", f"${revenue}", date)
            test_farm.wealth += indemnity 

        test_farm.wealth_history.append(test_farm.wealth)
            
    
    return(get_datelist(start_date, end_date), test_farm.wealth_history)


def calc_operating_margin(sale_price, final_yield, farm, insurance):
    return(Calc(Costs(farm, insurance), sale_price, final_yield).operating_margin)