import pandas as pd
from costs import *
from calc import *
import matplotlib.pyplot as plt


#a datelist from start_date to end date in list form
def get_datelist_string(start_date, end_date): 
    date_list = pd.date_range(start_date, end_date, freq='D').strftime("%Y-%m-%d").tolist()
    return date_list

#a datelist from start date to end date in date time
def get_datelist(start_date, end_date):
    return(pd.date_range(start_date, end_date, freq='D'))

"""
Method is called within insurance_app.py to help plot final wealth calculation
"""
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

"""
Method calculates operating margin based on sale price, final yield, 
and specified farm and insurance contract
"""
def calc_operating_margin(sale_price, final_yield, farm, insurance):
    return(Calc(Costs(farm, insurance), sale_price, final_yield).operating_margin)

"""
color dictionary used to assign a color to each crop and location combo 
is used when graphing 
Called in crop_plotter.py
"""
def get_color(crop, location): 

    color_dict = {
        'cwrs': {
            'N AB': 'xkcd:purple',
            'S AB': 'xkcd:royal blue',
            'PEACE': 'xkcd:forest',
        },

        'cpsr': {
            'N AB': 'xkcd:purpley pink',
            'S AB': 'xkcd:blue', 
            'PEACE': 'xkcd:green', 
        }, 

        'rs':{
            'N AB': 'xkcd:light purple',  
            'S AB': 'xkcd:light blue',
            'PEACE': 'xkcd:lightish green',

        }
        }
    return(color_dict[crop][location])

"""
color dictionary used to assign a color to each crop and location combo 
is used when graphing 
Called in crop_plotter.py
"""
def futures_color(future): 

    x = ['WC1', 'WC3', 'WC2', 'KWC1', 'KWC3', 'KWC2', 'MWC1', 'MWC3', 'MWC2']

    color_dict = {
        'WC1': 'xkcd:black', 
        'WC2': 'xkcd:grey', 
        'WC3': 'xkcd:brown', 
        'KWC1': 'xkcd:orange', 
        'KWC2': 'xkcd:red', 
        'KWC3': 'xkcd:yellow', 
        'MWC1': 'xkcd:cyan', 
        'MWC2': 'xkcd:pink', 
        'MWC3': 'xkcd:olive',
        'RSC1': 'xkcd:wheat', 
        'RSC2': 'xkcd:gunmetal', 
        'RSC3': 'xkcd:peachy pink',
        }
    return(color_dict[future])

"""
Method creates a dataframe of cwrs data including spot price for years
2016 - 2022 
called in crop_plotter.py
"""
def get_cwrs(): 
    cwrs = pd.read_csv("DataSource/cwrs_prices.csv")
    years = ['2016', '2017', '2018', '2019', '2020', '2021', '2022']
    for year in years: 
        cwrs[year] = pd.to_datetime(cwrs[year])
    return cwrs

"""
Method creates a dataframe of cpsr data including spot price for years
2016 - 2022
called in crop_plotter.py
"""
def get_cpsr(): 
    cpsr = pd.read_csv("DataSource/cpsr_prices.csv")
    years = ['2016', '2017', '2018', '2019', '2020', '2021', '2022']
    for year in years: 
        cpsr[year] = pd.to_datetime(cpsr[year])  
    return cpsr

"""
Method creates a dataframe of rs data including spot price for years
2016 - 2022
called in crop_plotter.py
"""
def get_rs(): 
    rs = pd.read_csv("DataSource/rs_prices.csv")
    years = ['2016', '2017', '2018', '2019', '2020', '2021', '2022']
    for year in years: 
        rs[year] = pd.to_datetime(rs[year])
    return rs

"""
helper method to add plot of crop, year, and location to specified axis
called in crop_plotter.py
"""
def plot(crop, year, location, ax): 
    plot_label = crop + " " + location
    y_data = location + " CASH " + year
    color_selected = get_color(crop, location)

    if crop == 'cwrs':
        crop_selected = get_cwrs()

    if crop == 'cpsr': 
        crop_selected = get_cpsr()

    if crop == 'rs':
        crop_selected = get_rs()

    crop_selected.plot(label=plot_label, x=year, y =y_data, ax=ax, color=color_selected)

"""
method generates plots for array of crops, years and locations 
for specified caxis
called in crop_plotter.py
"""
def crop_plotter(crops, years, locations, ax):
    for crop in crops: 
        for year in years: 
            for location in locations: 
                plot(crop, year, location ,ax)

    handles, labels = ax.get_legend_handles_labels()
    handle_list, label_list = [], []
    for handle, label in zip(handles, labels):
        if label not in label_list:
            handle_list.append(handle)
            label_list.append(label)
    ax.legend(handle_list, label_list)



"""
Method creates a dataframe of mw futures data including current futures month
prices for years 2016 - 2022
called in crop_plotter.py
"""
def get_mw(): 
    mw_futures = pd.read_csv("DataSource/mw_futures.csv")
    years = ['2016', '2017', '2018', '2019', '2020', '2021', '2022']
    for year in years: 
        mw_futures[year] = pd.to_datetime(mw_futures[year])  
    return mw_futures

"""
Method creates a dataframe of kw futures data including current futures month
prices for years 2016 - 2022
called in crop_plotter.py
"""
def get_kw(): 
    kw_futures = pd.read_csv("DataSource/kw_futures.csv")
    years = ['2016', '2017', '2018', '2019', '2020', '2021', '2022']
    for year in years: 
        kw_futures[year] = pd.to_datetime(kw_futures[year])  
    return kw_futures

"""
Method creates a dataframe of w futures data including current futures month
prices for years 2016 - 2022
called in crop_plotter.py
"""
def get_w(): 
    w_futures = pd.read_csv("DataSource/w_futures.csv")
    years = ['2016', '2017', '2018', '2019', '2020', '2021', '2022']
    for year in years: 
        w_futures[year] = pd.to_datetime(w_futures[year])  
    return w_futures

"""
Method creates a dataframe of w futures data including current futures month
prices for years 2016 - 2022
called in crop_plotter.py
"""
def get_rs_futures(): 
    rs_futures = pd.read_csv("DataSource/rs_futures.csv")
    years = ['2016', '2017', '2018', '2019', '2020', '2021', '2022']
    for year in years: 
        rs_futures[year] = pd.to_datetime(rs_futures[year])  
    return rs_futures

"""
helper method to add plot of crop, year, and location to specified axis
called in crop_plotter.py
"""
def futures_plot(futures, year, ax): 
    plot_label = futures
    y_data = futures + " " + year
    color_selected = futures_color(futures)

    if futures == 'WC1' or futures == 'WC2' or futures == 'WC3':
        futures_df = get_w()

    if futures == 'KWC1' or futures == 'KWC2' or futures == 'KWC3':
        futures_df = get_kw()

    if futures == 'MWC1' or futures == 'MWC2' or futures == 'MWC3':
        futures_df = get_mw()

    if futures == 'RSC1' or futures == 'RSC2' or futures == 'RSC3':
        futures_df = get_rs_futures()

    futures_df.plot(label=plot_label, x=year, y =y_data, ax=ax, color=color_selected)

"""
method generates plots for array of crops, years and locations 
for specified caxis
called in crop_plotter.py
"""
def futures_plotter(futures, years, ax):
    for future in futures: 
        for year in years: 
            futures_plot(future, year, ax)

    handles, labels = ax.get_legend_handles_labels()
    handle_list, label_list = [], []
    for handle, label in zip(handles, labels):
        if label not in label_list:
            handle_list.append(handle)
            label_list.append(label)
    ax.legend(handle_list, label_list)

"""
method calculates the basis between two columns of price data -> returns series of basis
"""
def calc_basis(df1, df2):
    #basis = cash - futures
    result = (df1 - df2).dropna()
    return result

"""
method is used to plot basis to an existing graph axis
accepts a crop and location for spot price
accepts a future code for futures price W
accepts a list of years
Method is called in graph_app.py

"""
def basis_plotter(crop, location, futures, years, ax):
    for year in years:
        label = f"{location} {crop} {futures} basis"
        crop_row = location + " CASH " + year
        futures_row = futures + " " + year
        color = futures_color(futures)

        if crop == 'cwrs':
            crop_df = get_cwrs()

        if crop == 'cpsr': 
            crop_df = get_cpsr()

        if crop == 'rs':
            crop_df = get_rs()
        
        if futures == 'WC1' or futures == 'WC2' or futures == 'WC3':
            futures_df = get_w()

        if futures == 'KWC1' or futures == 'KWC2' or futures == 'KWC3':
            futures_df = get_kw()

        if futures == 'MWC1' or futures == 'MWC2' or futures == 'MWC3':
            futures_df = get_mw()

        if futures == 'RSC1' or futures == 'RSC2' or futures == 'RSC3':
            futures_df = get_rs_futures()

        crop_input = crop_df[crop_row]
        futures_input = futures_df[futures_row]

        #create two series, one with basis and one with corresponeing dates
        result = calc_basis(crop_input, futures_input)
        date_list = crop_df[year].dropna()

        #create new data frame by concattenating series and set column titles
        df = pd.concat([date_list, result], axis=1).dropna()
        df.columns = ['date', 'basis']

        df.plot(label=label, x='date', y='basis', ax=ax, color=color)

    #remove duplicate labels from legend
    handles, labels = ax.get_legend_handles_labels()
    handle_list, label_list = [], []
    for handle, label in zip(handles, labels):
        if label not in label_list:
            handle_list.append(handle)
            label_list.append(label)
    ax.legend(handle_list, label_list)

    return


