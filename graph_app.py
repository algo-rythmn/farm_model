import tkinter as tk
import tkinter.ttk as ttk
from tkinter import *
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from util import *

"""
Run graph_app.py to use the graph app
graph app includes both crop and basis plotter

"""

class GraphApp(tk.Tk): 
    def __init__(self):
        super().__init__()

        #initialize arrays to store data inputs
        self.crop_list = []
        self.date_list = []
        self.date_list_basis = []
        self.location_list = []
        self.futures_list = []

        #configure the root window
        self.geometry('750x800')
        self.columnconfigure(0, weight=1)
        self.title("Crop Grapher")
        self.style = ttk.Style(self)
        self.style.theme_use('vista')

        #create a notebook
        self.notebook = ttk.Notebook(self)
        self.notebook.pack()

        #create frame 1: Crop plotter frame
        self.price_plotter = ttk.Frame(self.notebook, height=400, width=750)
        self.price_plotter.columnconfigure(0, weight=1)
        self.price_plotter.pack(fill="both", expand=1)
        self.notebook.add(self.price_plotter, text="Price Plotter")
        self.create_price_plotter(self.price_plotter)

        #create frame 2 Basis plotter: 
        self.basis_plotter = ttk.Frame(self.notebook, height=700, width=750)
        self.basis_plotter.columnconfigure(0, weight=1)
        self.basis_plotter.pack(fill="both", expand=1)
        self.notebook.add(self.basis_plotter, text="Basis Plotter")
        self.create_basis_plotter(self.basis_plotter)
    

    ##-------------------------------------- Global Methods for any frame -------------------------------------##
    
    #call this method to create frame which holds the title
    def create_title_frame(self, frame, text):
        title_frame = ttk.Frame(frame, height=30, width=750)
        title_frame.grid(row=0, column=0, pady=2)
        title_label = ttk.Label(title_frame, text = text)
        title_label.pack(anchor='center', pady=6)

    #method creates submit button 
    def create_submit_button(self, frame, text, command): 
        submit_frame = ttk.Frame(frame, height=10, width=750)
        submit_frame.grid(row=2, column=0, pady=2)
        submit_button = ttk.Button(submit_frame, text=text, command=command)
        submit_button.pack(pady=5)
    
    ##-------------------------------------- Helper Methods for Price Plotter -------------------------------------##

    #call this method to populate passed in frame with the price plotter application
    def create_price_plotter(self, frame):
        #create frame to hold the title
        self.create_title_frame(frame, "Crop Price Plotter")
        #create frame's to hold the data inputs
        self.create_data_frame(frame)        
        #create frame to hold submit button 
        self.create_submit_button(frame, "Submit", self.submit)  
        #create frame to hold the graph
        self.graph_frame = ttk.Frame(frame, height=200, width=750)
        self.graph_frame.grid(row=3, column=0, pady=10)
        #create figure
        self.fig = Figure()
        self.subplot = self.fig.add_subplot(111)
        self.canvas = FigureCanvasTkAgg(self.fig,self.graph_frame)
        self.canvas.draw()
        self.canvas.get_tk_widget().pack(side='top', fill='both', expand=1)
    
    #create a data frame that contains the date selector, spot price selector and futures selector
    def create_data_frame(self, frame):
        #create data frame within master frame passed in
        data_frame = ttk.Frame(frame, height=130, width=750)
        data_frame.grid(row=1, column=0, sticky='we')

        #create three columns within the frame, each of equal weight
        data_frame.columnconfigure(0, weight=1)
        data_frame.columnconfigure(1, weight=1)
        data_frame.columnconfigure(2, weight=1)

        #create data frame one to populate column one of data frame 
        #this column will hold the date selector
        data_frame_one = ttk.Frame(data_frame, height=180)
        data_frame_one.grid(row=0, column=0, sticky='nsew')
        self.create_date_selector(data_frame_one)

        #create data frame two to populate column two of data frame 
        #this column will hold the spot price selector
        data_frame_two = ttk.Frame(data_frame, height=180)
        data_frame_two.grid(row=0, column=1, sticky='nsew')
        self.create_spot_price_selector(data_frame_two) 

        #create data frame three to populate column three of data frame 
        #this column will hold the futures selector
        data_frame_three = ttk.Frame(data_frame, height=180)
        data_frame_three.grid(row=0, column=2, sticky='nsew')  
        self.create_futures_selector(data_frame_three)

    #method creates the date checkbuttons in passed in frame
    def create_date_selector(self, frame):
        frame.columnconfigure(0, weight=1)
        frame.columnconfigure(1, weight=1)
        date_label = ttk.Label(frame, text = "Select Date(s): ")
        date_label.grid(row=0, columnspan=2, pady=2)

        self._2016_var = tk.IntVar()
        _2016_button = ttk.Checkbutton(frame, text ='2016', variable=self._2016_var, command=self.get_date_2016)
        _2016_button.grid(row=1, column=0, sticky='e', padx=2)
    
        self._2017_var = tk.IntVar()
        _2017_button = ttk.Checkbutton(frame, text ='2017', variable=self._2017_var, command=self.get_date_2017)
        _2017_button.grid(row=2, column=0, sticky='e', padx=2)

        self._2018_var = tk.IntVar()
        _2018_button = ttk.Checkbutton(frame, text ='2018', variable=self._2018_var, command = self.get_date_2018)
        _2018_button.grid(row=3, column=0, sticky='e', padx=2)
    
        self._2019_var = tk.IntVar()
        _2019_button = ttk.Checkbutton(frame, text ='2019', variable=self._2019_var, command=self.get_date_2019)
        _2019_button.grid(row=4, column=0, sticky='e', padx=2)

        self._2020_var = tk.IntVar()
        _2020_button = ttk.Checkbutton(frame, text ='2020', variable=self._2020_var, command=self.get_date_2020)
        _2020_button.grid(row=1, column=1, sticky='w', padx=2)
    
        self._2021_var = tk.IntVar()
        _2021_button = ttk.Checkbutton(frame, text ='2021', variable=self._2021_var, command=self.get_date_2021)
        _2021_button.grid(row=2,column=1, sticky='w', padx=2)

        self._2022_var = tk.IntVar()
        _2022_button = ttk.Checkbutton(frame, text ='2022', variable=self._2022_var, command=self.get_date_2022)
        _2022_button.grid(row=3, column=1, sticky='w', padx=2)

    #method creates spot price checkbuttons in passed in frame
    def create_spot_price_selector(self, frame):
        frame.columnconfigure(0, weight=1)
        frame.columnconfigure(1)
        frame.columnconfigure(2)
        frame.columnconfigure(3, weight=1)

        box_label = ttk.Label(frame, text = "Select Spot Price: ")
        box_label.grid(row=0, column=1, columnspan=2, pady=2)
        
        location_label = ttk.Label(frame, text = "Location(s)")
        location_label.grid(row=1, column=1, sticky='w', padx=2)

        self.n_ab_var = tk.IntVar()
        n_ab_button = ttk.Checkbutton(frame, text ='N AB', variable=self.n_ab_var, command=self.get_location_n_ab)
        n_ab_button.grid(row=2, column=1, sticky='w', padx=2)
    
        self.s_ab_var = tk.IntVar()
        s_ab_button = ttk.Checkbutton(frame, text ='S AB', variable=self.s_ab_var, command=self.get_location_s_ab)
        s_ab_button.grid(row=3, column=1, sticky='w', padx=2)
        
        self.peace_var = tk.IntVar()
        peace_button = ttk.Checkbutton(frame, text ='Peace', variable=self.peace_var, command=self.get_location_peace)
        peace_button.grid(row=4, column=1, sticky='w', padx=2)

        crop_label = ttk.Label(frame, text = "Crop(s): ")
        crop_label.grid(row=1, column=2, sticky='w')

        self.hrs_var = tk.IntVar()
        hrs_button = ttk.Checkbutton(frame, text ='HRS', variable=self.hrs_var, command=self.get_crop_selector_hrs)
        hrs_button.grid(row=2, column=2, sticky='w')
    
        self.cps_var = tk.IntVar()
        cps_button = ttk.Checkbutton(frame, text ='CPS', variable=self.cps_var, command=self.get_crop_selector_cps)
        cps_button.grid(row=3, column=2, sticky='w')
        
        self.rs_var = tk.IntVar()
        rs_button = ttk.Checkbutton(frame, text ='Canola', variable=self.rs_var, command=self.get_crop_selector_rs)
        rs_button.grid(row=4, column=2, sticky='w')

    #method creates futures checkboxes in passed in frame
    def create_futures_selector(self, frame):
        frame.columnconfigure(0, weight=1)
        frame.columnconfigure(1)
        frame.columnconfigure(2)
        frame.columnconfigure(3)
        frame.columnconfigure(4)
        frame.columnconfigure(5, weight=1)

        futures_label = ttk.Label(frame, text = "Select Futures Contracts: ")
        futures_label.grid(row=0, column=1, columnspan=4, sticky='n')

        self.zw1 = tk.IntVar()
        zw1_button = ttk.Checkbutton(frame, text ='ZW1', variable=self.zw1, command=self.get_zw1)
        zw1_button.grid(row=1, column=1, sticky='w', padx=2)
    
        self.zw2 = tk.IntVar()
        zw2_button = ttk.Checkbutton(frame, text ='ZW2', variable=self.zw2, command=self.get_zw2)
        zw2_button.grid(row=2, column=1, sticky='w', padx=2)

        self.zw3 = tk.IntVar()
        zw3_button = ttk.Checkbutton(frame, text ='ZW3', variable=self.zw3, command = self.get_zw3)
        zw3_button.grid(row=3, column=1, sticky='w', padx=2)
    
        self.kw1 = tk.IntVar()
        kw1_button = ttk.Checkbutton(frame, text ='KW1', variable=self.kw1, command=self.get_kw1)
        kw1_button.grid(row=1, column=2, sticky='w', padx=2)

        self.kw2 = tk.IntVar()
        kw2_button = ttk.Checkbutton(frame, text ='KW2', variable=self.kw2, command=self.get_kw2)
        kw2_button.grid(row=2, column=2, sticky='w', padx=2)
    
        self.kw3 = tk.IntVar()
        kw3_button = ttk.Checkbutton(frame, text ='KW3', variable=self.kw3, command=self.get_kw3)
        kw3_button.grid(row=3, column=2, sticky='w', padx=2)

        self.mw1 = tk.IntVar()
        mw1_button = ttk.Checkbutton(frame, text ='MW1', variable=self.mw1, command=self.get_mw1)
        mw1_button.grid(row=1, column=3, sticky='w', padx=2)

        self.mw2 = tk.IntVar()
        mw2_button = ttk.Checkbutton(frame, text ='MW2', variable=self.mw2, command=self.get_mw2)
        mw2_button.grid(row=2, column=3, sticky='w', padx=2)
    
        self.mw3 = tk.IntVar()
        mw3_button = ttk.Checkbutton(frame, text ='MW3', variable=self.mw3, command=self.get_mw3)
        mw3_button.grid(row=3, column=3, sticky='w', padx=2)

        self.rs1 = tk.IntVar()
        rs1_button = ttk.Checkbutton(frame, text ='RS1', variable=self.rs1, command=self.get_rs1)
        rs1_button.grid(row=1, column=4, sticky='w', padx=2)

        self.rs2 = tk.IntVar()
        rs2_button = ttk.Checkbutton(frame, text ='RS2', variable=self.rs2, command=self.get_rs2)
        rs2_button.grid(row=2, column=4, sticky='w', padx=2)
    
        self.rs3 = tk.IntVar()
        rs3_button = ttk.Checkbutton(frame, text ='RS3', variable=self.rs3, command=self.get_rs3)
        rs3_button.grid(row=3, column=4, sticky='w', padx=2)

    ## --------------------- below are getter / command methods used for price plotter frame ---------------------##
    def get_zw1(self):
        if 'WC1' in self.futures_list: 
            self.futures_list.remove('WC1')
        else:
            self.futures_list.append('WC1')

    def get_zw2(self):
        if 'WC2' in self.futures_list: 
            self.futures_list.remove('WC2')
        else:
            self.futures_list.append('WC2')

    def get_zw3(self):
        if 'WC3' in self.futures_list: 
            self.futures_list.remove('WC3')
        else:
            self.futures_list.append('WC3')

    def get_kw1(self):
        if 'KWC1' in self.futures_list: 
            self.futures_list.remove('KWC1')
        else:
            self.futures_list.append('KWC1')

    def get_kw2(self):
        if 'KWC2' in self.futures_list: 
            self.futures_list.remove('KWC2')
        else:
            self.futures_list.append('KWC2')

    def get_kw3(self):
        if 'KWC3' in self.futures_list: 
            self.futures_list.remove('KWC3')
        else:
            self.futures_list.append('KWC3')

    def get_mw1(self):
        if 'MWC1' in self.futures_list: 
            self.futures_list.remove('MWC1')
        else:
            self.futures_list.append('MWC1')

    def get_mw2(self):
        if 'MWC2' in self.futures_list: 
            self.futures_list.remove('MWC2')
        else:
            self.futures_list.append('MWC2')

    def get_mw3(self):
        if 'MWC3' in self.futures_list: 
            self.futures_list.remove('MWC3')
        else:
            self.futures_list.append('MWC3')

    def get_rs1(self):
        if 'RSC1' in self.futures_list: 
            self.futures_list.remove('RSC1')
        else:
            self.futures_list.append('RSC1')

    def get_rs2(self):
        if 'RSC2' in self.futures_list: 
            self.futures_list.remove('RSC2')
        else:
            self.futures_list.append('RSC2')

    def get_rs3(self):
        if 'RSC3' in self.futures_list: 
            self.futures_list.remove('RSC3')
        else:
            self.futures_list.append('RSC3')

    def get_crop_selector_hrs(self):
        if 'cwrs' in self.crop_list: 
            self.crop_list.remove('cwrs')
        else:
            self.crop_list.append('cwrs')

    def get_crop_selector_cps(self): 
        print(self.cps_var.get())
        if 'cpsr' in self.crop_list: 
            self.crop_list.remove('cpsr')
        else:
            self.crop_list.append('cpsr')

    def get_crop_selector_rs(self):
        if 'rs' in self.crop_list: 
            self.crop_list.remove('rs')
        else:
            self.crop_list.append('rs')

    def get_location_n_ab(self):
        if 'N AB' in self.location_list: 
            self.location_list.remove('N AB')
        else:
            self.location_list.append('N AB')

    def get_location_s_ab(self): 
        if 'S AB' in self.location_list: 
            self.location_list.remove('S AB')
        else:
            self.location_list.append('S AB')

    def get_location_peace(self):
        if 'PEACE' in self.location_list: 
            self.location_list.remove('PEACE')
        else:
            self.location_list.append('PEACE')

    def get_date_2016(self):
        if '2016' in self.date_list: 
            self.date_list.remove('2016')
        else:
            self.date_list.append('2016')

    def get_date_2017(self):
        if '2017' in self.date_list: 
            self.date_list.remove('2017')
        else:
            self.date_list.append('2017')


    def get_date_2018(self):
        if '2018' in self.date_list: 
            self.date_list.remove('2018')
        else:
            self.date_list.append('2018')


    def get_date_2019(self):
        if '2019' in self.date_list: 
            self.date_list.remove('2019')
        else:
            self.date_list.append('2019')


    def get_date_2020(self):
        if '2020' in self.date_list: 
            self.date_list.remove('2020')
        else:
            self.date_list.append('2020')


    def get_date_2021(self):
        if '2021' in self.date_list: 
            self.date_list.remove('2021')
        else:
            self.date_list.append('2021')

    def get_date_2022(self):
        if '2022' in self.date_list: 
            self.date_list.remove('2022')
        else:
            self.date_list.append('2022')

    #method plots selected crop prices using help of util futures_plotter method
    def submit(self):
        self.fig.clear()
        ax = self.fig.add_subplot(111)
        crop_plotter(self.crop_list, self.date_list, self.location_list, ax)
        futures_plotter(self.futures_list, self.date_list, ax)
        ax.set_ylabel("$/bushel")
        ax.set_xlabel("Date")
        self.canvas.draw_idle()


    ##-------------------------------------- Helper Methods for Basis Plotter -------------------------------------##
    
    #call this method to populate passed in frame with the basis plotter application
    def create_basis_plotter(self, frame):
        self.create_title_frame(frame, "Basis Plotter")
        self.create_data_frame_basis(frame)
        self.create_submit_button(frame, "Plot Basis", self.submit_basis)

        self.basis_graph_frame = ttk.Frame(frame, height=200, width=750)
        self.basis_graph_frame.grid(row=3, column=0, pady=10)
        self.basis_fig = Figure()
        self.basis_subplot = self.fig.add_subplot(111)
        self.canvas_basis = FigureCanvasTkAgg(self.basis_fig,self.basis_graph_frame)
        self.canvas_basis.draw()
        self.canvas_basis.get_tk_widget().pack(side='top', fill='both', expand=1)
        return
    
    #create a data frame that contains the date selector, spot price selector and futures selector
    def create_data_frame_basis(self, frame):
        #create data frame within master frame passed in
        data_frame = ttk.Frame(frame, height=130, width=750)
        data_frame.grid(row=1, column=0, sticky='we')

        #create three columns within the frame, each of equal weight
        data_frame.columnconfigure(0, weight=1)
        data_frame.columnconfigure(1, weight=1)
        data_frame.columnconfigure(2, weight=1)

        #create data frame one to populate column one of data frame
        #this column will hold the date selector
        data_frame_one = ttk.Frame(data_frame, height=180)
        data_frame_one.grid(row=0, column=0, sticky='nsew')
        self.create_date_selector_basis(data_frame_one)

        #create data frame two to populate column two of data frame
        #this column will hold the spot price dropdown
        data_frame_two = ttk.Frame(data_frame, height=180)
        data_frame_two.grid(row=0, column=1, sticky='nsew')
        self.create_spot_price_dropdown(data_frame_two)

        #create data frame three to populate column three of data frame
        #this column will hold the futures price dropdown
        data_frame_three = ttk.Frame(data_frame, height=180)
        data_frame_three.grid(row=0, column=2, sticky='nsew')
        self.create_futures_dropdown(data_frame_three)

    #method is called to create date selector within passed in frame
    def create_date_selector_basis(self, frame):
        frame.columnconfigure(0, weight=1)
        frame.columnconfigure(1, weight=1)
        date_label = ttk.Label(frame, text = "Select Date(s): ")
        date_label.grid(row=0, columnspan=2, pady=2)

        self._2016_var_basis = tk.IntVar()
        _2016_button = ttk.Checkbutton(frame, text ='2016', variable=self._2016_var_basis, command=self.get_date_2016_basis)
        _2016_button.grid(row=1, column=0, sticky='e', padx=2)
    
        self._2017_var_basis = tk.IntVar()
        _2017_button = ttk.Checkbutton(frame, text ='2017', variable=self._2017_var_basis, command=self.get_date_2017_basis)
        _2017_button.grid(row=2, column=0, sticky='e', padx=2)

        self._2018_var_basis = tk.IntVar()
        _2018_button = ttk.Checkbutton(frame, text ='2018', variable=self._2018_var_basis, command = self.get_date_2018_basis)
        _2018_button.grid(row=3, column=0, sticky='e', padx=2)
    
        self._2019_var_basis = tk.IntVar()
        _2019_button = ttk.Checkbutton(frame, text ='2019', variable=self._2019_var_basis, command=self.get_date_2019_basis)
        _2019_button.grid(row=4, column=0, sticky='e', padx=2)

        self._2020_var_basis = tk.IntVar()
        _2020_button = ttk.Checkbutton(frame, text ='2020', variable=self._2020_var_basis, command=self.get_date_2020_basis)
        _2020_button.grid(row=1, column=1, sticky='w', padx=2)
    
        self._2021_var_basis = tk.IntVar()
        _2021_button = ttk.Checkbutton(frame, text ='2021', variable=self._2021_var_basis, command=self.get_date_2021_basis)
        _2021_button.grid(row=2,column=1, sticky='w', padx=2)

        self._2022_var_basis = tk.IntVar()
        _2022_button = ttk.Checkbutton(frame, text ='2022', variable=self._2022_var_basis, command=self.get_date_2022_basis)
        _2022_button.grid(row=3, column=1, sticky='w', padx=2)

    #method creates the crop and location dropdown within passed in frame
    def create_spot_price_dropdown (self, frame): 
        label = ttk.Label(frame, text = 'Select desired spot price:').grid(row=0, columnspan=2, padx=10, pady=2)
        location_label = ttk.Label(frame, text = 'Location:').grid(column=0, row = 1, padx=10, pady=10)
        location_selector =["N AB", "S AB", "PEACE"]
        self.location_menu = StringVar(self)
        location_drop_down = ttk.OptionMenu(frame, self.location_menu, "-", *location_selector).grid(column=1, row=1)

        crop_label = ttk.Label(frame, text = 'Crop:').grid(column=0, row = 2, padx=10, pady=10)
        crop_selector =["cpsr", "cwrs", "rs"]
        self.crop_menu = StringVar(self)
        crop_drop_down = ttk.OptionMenu(frame, self.crop_menu, "-", *crop_selector).grid(column=1, row=2)

    #method creates the futures selector dropdown
    def create_futures_dropdown (self, frame): 
        frame.rowconfigure(0)
        frame.rowconfigure(1, weight=1)
        label = ttk.Label(frame, text = 'Select futures price:').grid(column=0, row=0, padx=10, pady=2)

        futures_selector = ["WC1", "WC2", "WC3", "KWC1", "KWC2", "KWC3", "MWC1", "MWC2", "MWC3", "RSC1", "RSC2", "RSC3"]
        self.futures_menu = StringVar(self)
        drop_down = ttk.OptionMenu(frame, self.futures_menu, "-", *futures_selector).grid(column=1, row=0, sticky='n')

     ## --------------------- below are getter / command methods used for basis plotter frame ---------------------##

    def get_date_2016_basis(self):
        if '2016' in self.date_list_basis: 
            self.date_list_basis.remove('2016')
        else:
            self.date_list_basis.append('2016')

    def get_date_2017_basis(self):
        if '2017' in self.date_list_basis: 
            self.date_list_basis.remove('2017')
        else:
            self.date_list_basis.append('2017')


    def get_date_2018_basis(self):
        if '2018' in self.date_list_basis: 
            self.date_list_basis.remove('2018')
        else:
            self.date_list_basis.append('2018')


    def get_date_2019_basis(self):
        if '2019' in self.date_list_basis: 
            self.date_list_basis.remove('2019')
        else:
            self.date_list_basis.append('2019')


    def get_date_2020_basis(self):
        if '2020' in self.date_list_basis: 
            self.date_list_basis.remove('2020')
        else:
            self.date_list_basis.append('2020')


    def get_date_2021_basis(self):
        if '2021' in self.date_list_basis: 
            self.date_list_basis.remove('2021')
        else:
            self.date_list_basis.append('2021')

    def get_date_2022_basis(self):
        if '2022' in self.date_list_basis: 
            self.date_list_basis.remove('2022')
        else:
            self.date_list_basis.append('2022')

    #upon submission plots the selected basis graph using helper method frum util - basis_plotter
    def submit_basis(self):
        location = self.location_menu.get()
        crop = self.crop_menu.get()
        futures = self.futures_menu.get()
        self.basis_fig.clear()
        ax = self.basis_fig.add_subplot(111)
        ax.set_ylabel("Basis: $/bushel")
        basis_plotter(crop, location, futures, self.date_list_basis, ax)
        self.canvas_basis.draw_idle()
        

if __name__ == "__main__":
  app = GraphApp()
  app.mainloop()
