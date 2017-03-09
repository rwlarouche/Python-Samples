#showinfo.py
#GUI program that displays your name and address when a button is clicked
#Ryan LaRouche

from tkinter import *

class ShowInfo():
    def __init__(self):
        self.visible = False
        self.main_window = Tk()
        self.main_window.title("Name and Adress App") #Change window title

        self.buttons_frame = Frame() #Buttons
        self.buttons_frame.pack(side = BOTTOM)
        self.info_button = Button(self.buttons_frame, text = "Show Info", \
                         command = self.show_info)
        self.info_button.pack(side = 'left')
        self.quit_button = Button(self.buttons_frame, text = "Quit", \
                         command = self.main_window.destroy)
        self.quit_button.pack(side = 'left')

        self.info_frame = Frame() #Info frame
        self.name_label = Label(self.info_frame, \
                             text = "Ryan LaRouche") #Name
        self.name_label.pack(side = TOP) #Pack

        self.street_label = Label(self.info_frame, \
                             text = "130 John Rezza Drive") #Street
        self.street_label.pack(side = TOP)
    
        self.street_label = Label(self.info_frame, \
                             text = "North Attleboro, MA 02763") #Location
        self.street_label.pack(side = TOP)

    def show_info(self):
        if (self.visible == False):
            self.info_frame.pack()
            self.info_button.config(text = "Hide Info")
            self.visible = True
            
        elif(self.visible == True):
            self.info_frame.pack_forget()
            self.info_button.config(text = "Show Info")
            self.visible = False

personal_info = ShowInfo()
