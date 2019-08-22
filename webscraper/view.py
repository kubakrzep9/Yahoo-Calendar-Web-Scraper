# tkinter documentation: https://docs.python.org/3/library/tk.html

import tkinter as tk
import tkinter.ttk as ttk
from tkinter import font
import webscraper
import calendar_recipe

# Should root be a class member?

class GUI():
    def __init__(self):
        self.height_GUI = 500
        self.width_GUI  = 600
        self.width_eventMenu = 15

        self.bg_color = '#4e4f52'
        self.frame_color = '#c1cbdb'
        self.fontSize = 12
        self.fontType = 'song ti'
        self.fontStyle = self.fontType, self.fontSize
        self.scraper = webscraper.WebScraperHandle()


    #############################
    #       GUI functions       #
    #############################
    

    # Main class function that is called to build the entire GUI. Called from the controller.
    def buildGUI(self):
        root = tk.Tk()
        self.setGUI(root)
        self.setUpperFrame(root)
        self.setLowerFrame(root)
        root.mainloop()


    # Sets the dimensions and background color GUI screen.
    def setGUI(self, root):
        root.title("")
        # sets size of GUI 
        canvas = tk.Canvas(root, height=self.height_GUI, width=self.width_GUI)
        canvas.pack()
        # sets GUI background color
        background_label = tk.Label(root, bg=self.bg_color)
        background_label.place(relwidth=1, relheight=1)


    #############################
    #   Upper frame functions   #
    #############################


    # Combobox change event, called when user selects new event from eventMenu
    def newSelection_EventMenu(self, event):
        self.value_EventMenu = self.eventMenu.get()
        self.eventMenu.selection_clear()
        print(self.value_EventMenu)


    # Sets the dimensions and contents of the event menu combobox (drop down menu). This
    # menu allows the user to specify what type of event they are interested. The events 
    # are: earnings reports, divendend releases and initial public offerings. 
    def setEventMenu(self, root, upper_frame):
        # Styling combobox, this applies the new style 'combostyle' to all ttk.Combobox.
        combostyle = ttk.Style()
        combostyle.theme_create('combostyle', parent='alt',
                                settings = {'TCombobox':
                                            {'configure':
                                            { 'fieldbackground': 'white'
                                            }}})
        combostyle.theme_use('combostyle') 
        
        self.value_of_EventMenu = tk.StringVar(root)
        self.eventMenu = ttk.Combobox(upper_frame, width = self.width_eventMenu, textvariable=self.value_of_EventMenu, state="readonly")
        self.eventMenu.bind("<<ComboboxSelected>>", self.newSelection_EventMenu)
        self.eventMenu['values'] = ("Earnings Reports", "Stock Splits", "IPOs")
        self.eventMenu.current(0)
        self.value_EventMenu = self.eventMenu.get()

        self.eventMenu.place(x=0, width=130)


    # Sets the upper frame, which contains the Menu Options and the Condition Box 
    # for the user to customize their scan. The Menu Options consists of a drop down menu, 
    # ** drop down calendar menu **, and a button. The drop down menu allows the user to select 
    # between scanning for companies releasing earnings reports, stock splits or IPOs. The 
    # ** drop down calendar menu ** allows the user to select the date they would like to scan.
    # The button allows the user to add a 'Condition Box Row' to the Condition Box. The 
    # 'Condition Box Row' allows the user to filter their scan even further based upon a number
    # of conditions offered in the drop down menu of the 'Condition Box Row'.
    def setUpperFrame(self, root):
        # Upper frame, where the menu options and condition box is located 
        upper_frame = tk.Frame(root, bg=self.frame_color, bd=5)
        upper_frame.place(relx=0.5, y=50, relwidth=0.75, height=30, anchor='n')
        # Setting event menu
        self.setEventMenu(root, upper_frame)
        # Setting calendar / data picker 
        self.calendar = calendar_recipe.Datepicker(upper_frame)
        self.calendar.place(x= 140, width=72) 
        # Setting add condition button 
        self.btn_addCondition = tk.Button(upper_frame, text="Add condition", font=self.fontStyle, command=lambda: self.scraper.testingPrint())
        self.btn_addCondition.place(x=222, width=100, height=20)


    #############################
    #   Lower frame functions   #
    #############################


    # Sets the lower frame, which contains the Display Box (idk about name) that will display
    # the companies that fall within the users criteria. 
    #
    # Must implement 
    # The Display Box will have a header above each column. Clicking the column header will 
    # sort the Display Box based upon that column, either in ascending or descending order
    # depending on how many times the user clicks the column header. 
    def setLowerFrame(self, root):
        lower_frame = tk.Frame(root, bg=self.frame_color, bd=10)
        lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor='n')

        label = tk.Label(lower_frame, bg='white', font=self.fontStyle)
        label.place(relwidth=1, relheight= 1)
