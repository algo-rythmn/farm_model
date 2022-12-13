import tkinter as tk
import tkinter.ttk as ttk
from tkinter import *
from farm import *
from insurance import *
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from util import *

class App(tk.Tk): 
    def __init__(self):
        super().__init__()

        #configure the root window
        self.geometry('750x600')
        self.title("Agriculture Calculator")
        self.style = ttk.Style(self)
        self.style.theme_use('vista')

        #create a notebook
        self.notebook = ttk.Notebook(self)
        self.notebook.pack()

        #create frame 1: Insurance calculator
        self.frame_1 = ttk.Frame(self.notebook, height=400, width=750)
        self.frame_1.pack(fill="both", expand=1)
        self.notebook.add(self.frame_1, text="Insurance Calculator")
        self.create_insurance_frame()

        #create frame 2 Wealth plotter: 
        self.frame_2 = ttk.Frame(self.notebook, height=700, width=750)
        self.frame_2.pack(fill="both", expand=1)
        self.data_frame = ttk.Frame(self.frame_2, height=100, width=750)
        self.data_frame.pack(fill="both", expand=1, padx=5, pady=5)
        self.notebook.add(self.frame_2, text="Wealth Plotter")
        self.create_wealth_frame()

    #method creates insurance frame
    def create_insurance_frame(self):
        self.heading = ttk.Label(self.frame_1, text = "Alberta Farm Insurance Calculator").grid(row=0, columnspan=6, padx=10, pady=10)
        self.create_location_input()
        self.create_farm_input()
        self.create_crop_dropdown()
        self.create_coverage_dropdown()
        self.create_land_dropdown()
        self.create_hail_dropdown()
        self.create_submit_button()  

    #method creates wealth plotter frame
    def create_wealth_frame(self):
        self.create_wealth_input()
        self.create_price_input()
        self.create_yield_input()
        self.create_submit_button_frame_two()

        #set initial variables to 0
        self.x_data = 0
        self.y_data = 0
        self.price = 0
        self.y = 0

        #create figure
        self.fig = Figure()
        self.subplot = self.fig.add_subplot(111)
        self.subplot.set_xlabel("Date")
        self.subplot.set_ylabel("Wealth ($)")
        self.subplot.plot(self.x_data, self.y_data)

        self.canvas = FigureCanvasTkAgg(self.fig,self.frame_2)
        self.canvas.draw()
        self.canvas.get_tk_widget().pack(side='top', fill='both', expand=1)

    #create label and input for location: township, range and meridian
    def create_location_input(self): 
        township_label = ttk.Label(self.frame_1, text = "Township: ").grid(column=0, row=1, padx=10, pady=10, sticky='E')
        self.township_input = StringVar(self)
        township_entry = ttk.Entry(self.frame_1, textvariable=self.township_input).grid(column=1, row=1)

        range_label = ttk.Label(self.frame_1, text = "Range: ").grid(column=2, row=1,  padx=10, pady=10)
        self.range_input = StringVar(self)
        range_entry = ttk.Entry(self.frame_1, textvariable=self.range_input).grid(column=3, row=1)

        meridian_label = ttk.Label(self.frame_1, text = "Meridian: ").grid(column=4, row=1, padx=10, pady=10)
        self.meridian_input = StringVar(self)
        meridian_entry = ttk.Entry(self.frame_1, textvariable=self.meridian_input).grid(column=5, row=1)

    #create label and input for farm insured acres
    def create_farm_input(self): 
        insured_acre_label = ttk.Label(self.frame_1, text = "Insured Acres: ").grid(column=0, row=2, padx=10, pady=10, sticky='E')
        self.insured_acres_input = StringVar(self)
        insured_acres_entry = ttk.Entry(self.frame_1, textvariable=self.insured_acres_input).grid(column=1, row=2)

    #get farm input
    def get_farm_input(self):
        self.township = int(self.township_input.get())
        self.range = int(self.range_input.get())
        self.meridian = int(self.meridian_input.get())
        self.insured_acres = int(self.insured_acres_input.get())


    #method creates the crop selector dropdown
    def create_crop_dropdown (self): 
        label = ttk.Label(self.frame_1, text = 'Select your crop:').grid(column=0, row=3, padx=10, pady=10, sticky='E')

        crop_selector = ["Hard Red Spring", "Canadian Prairie Spring", "Canola Polish", "Canola Argentine"]
        self.menu = StringVar(self)
        drop_down = ttk.OptionMenu(self.frame_1, self.menu, "-", *crop_selector, command=self.retrieve_crop_dropdown).grid(column=1, row=3, sticky="ew")

    #method retrieves the crop selected in the crop selector dropdown
    def retrieve_crop_dropdown(self, *args):
        if self.menu.get() == "Hard Red Spring": 
            self.crop = "HRS"
        if self.menu.get() == "Canadian Prairie Spring":
            self.crop = "CPS"
        if self.menu.get() == "Canola Polish": 
            self.crop = "canolapolish"
        if self.menu.get() == "Canola Argentine": 
            self.crop = "canolaargentine"
        print(self.crop)

    #method creates the coverage selector dropdown
    def create_coverage_dropdown (self): 
        label = ttk.Label(self.frame_1, text = 'Select your coverage level:').grid(column=0, row=4, padx=10, pady=10, sticky='E')

        coverage_selector = ["50%","60%","70%","80%"]
        self.coverage_menu = StringVar(self)
        drop_down = ttk.OptionMenu(self.frame_1, self.coverage_menu, "-", *coverage_selector, command=self.retrieve_coverage_dropdown).grid(column=1, row=4, sticky="ew")
  
    #method retrieves the coverage selected in the crop selector dropdown
    def retrieve_coverage_dropdown(self, *args):
        if self.coverage_menu.get() == "50%": 
            self.coverage = 50
        if self.coverage_menu.get() == "60%":
            self.coverage = 60
        if self.coverage_menu.get() == "70%": 
            self.coverage = 70
        if self.coverage_menu.get() == "80%": 
            self.coverage = 80
        print(self.coverage)

    #method creates the land selector dropdown
    def create_land_dropdown (self): 
        label = ttk.Label(self.frame_1, text = 'Select your land classification:').grid(column=0, row=5, padx=10, pady=10, sticky='E')

        land_selector = ["Stubble Farming","Fallow Farming","Irrigated Farming"]
        self.land_menu = StringVar(self)
        drop_down = ttk.OptionMenu(self.frame_1, self.land_menu, "-", *land_selector, command=self.retrieve_land_dropdown).grid(column=1, row=5,  sticky="ew")
  

    #method retrieves the land selected in the land selector dropdown
    def retrieve_land_dropdown(self, *args):
        if self.land_menu.get() == "Stubble Farming": 
            self.land = "S"
        if self.land_menu.get() == "Fallow Farming":
            self.land = "F"
        if self.land_menu.get() == "Irrigated Farming": 
            self.land = "I"
        print(self.land)

   #method creates the hail endorsement selector dropdown
    def create_hail_dropdown (self): 
        label = ttk.Label(self.frame_1, text = 'Elect for Hail Endorsement:').grid(column=0, row=6, padx=10, pady=10, sticky='E')

        hail_selector = ["Yes","No"]
        self.hail_menu = StringVar(self)
        drop_down = ttk.OptionMenu(self.frame_1, self.hail_menu, "-",  *hail_selector, command=self.retrieve_hail_dropdown).grid(column=1, row=6,  sticky="ew")
  
    #method retrieves the hail selected in the crop selector dropdown
    def retrieve_hail_dropdown(self, *args):
        if self.hail_menu.get() == "Yes": 
            self.hail_endorsement = "Y"
        if self.hail_menu.get() == "No":
            self.hail_endorsement = "N"
        print(self.hail_endorsement)

    #method creates submit button for agriinsurance
    def create_submit_button(self): 
        self.submit_button = ttk.Button(self.frame_1, text="Submit", command=self.submit).grid(column=1, row=7, padx=10, pady=10, sticky='ew')

    #method retrieves data and prints premium after submit button is pressed
    def submit(self):
        self.get_farm_input()
        print("SUBMITTED!")
        print(self.township)
        print(self.range)
        print(self.meridian)
        print(self.insured_acres)
        print(self.crop)
        print(self.coverage)
        print(self.land)
        self.test_farm = Farm(self.township, self.range, self.meridian, self.crop, self.insured_acres, self.land)
        self.insurance = Insurance(self.test_farm, self.coverage, self.hail_endorsement)
        premium_label = ttk.Label(self.frame_1, text = f"Premium Estimate: ${self.insurance.total_premium_per_acre}/acre, for total premium of: ${self.insurance.total_premium}").grid(column=2, row=7, columnspan=4, padx=10, pady=10, sticky='E')
        # test_farm.get_farm_information() #can call method to get test farm information

    #method creates label and input for initial wealth
    def create_wealth_input(self): 
        wealth_label = ttk.Label(self.data_frame, text = "Initial Wealth ($): ")
        self.wealth_input = IntVar(self)
        wealth_entry = ttk.Entry(self.data_frame, textvariable=self.wealth_input)
        wealth_label.pack(padx=5)
        wealth_entry.pack(pady=5)
    
    #create label and input for yield
    def create_yield_input(self): 
        yield_label = ttk.Label(self.data_frame, text = "Final Yield (bushels/acre): ")
        self.yield_input = IntVar(self)
        yield_entry = ttk.Entry(self.data_frame, textvariable=self.yield_input)
        yield_label.pack(padx=5, pady=5)
        yield_entry.pack(padx=5, pady=5)

    #method creates label and input for initial price
    def create_price_input(self): 
        price_label = ttk.Label(self.data_frame, text = "Sale Price ($/bushel): ")
        self.price_input = IntVar(self)
        price_entry = ttk.Entry(self.data_frame, textvariable=self.price_input)
        price_label.pack(padx=5)
        price_entry.pack(pady=5)

    #method creates frame two submit button
    def create_submit_button_frame_two(self): 
        self.submit_button_two = ttk.Button(self.data_frame, text="Submit", command=self.submit_frame_two)
        self.submit_button_two.pack(padx=5, pady=5)

    #method updates data after submit is pressed
    def submit_frame_two(self):
        self.price = self.price_input.get()
        self.y = self.yield_input.get()
        self.wealth = self.wealth_input.get()
        farm = Farm(self.township, self.range, self.meridian, self.crop, self.insured_acres, self.land, self.wealth)
        self.x_data, self.y_data = plotter(self.price, self.y, farm, self.insurance)
        self.draw_chart(farm)

    #method updates plot
    def draw_chart(self, farm):
        margin = calc_operating_margin(self.price, self.y, farm, self.insurance)
        self.fig.clear()
        plot = self.fig.add_subplot(111)
        plot.plot(self.x_data, self.y_data)
        plot.text(self.x_data[int(len(self.x_data)/2)], self.y_data[-10] + 4000 , f"Operating Margin: {margin}%", fontsize = 12)
        plot.set_xlabel("Date")
        plot.set_ylabel("Wealth ($)")
        self.canvas.draw_idle()

if __name__ == "__main__":
  app = App()
  app.mainloop()