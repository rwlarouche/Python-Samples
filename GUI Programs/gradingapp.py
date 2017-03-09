#gradingapp.py
#App constructs a GUI to enter and calculate the average of three test grades
#Ryan LaRouche

from tkinter import *

class GradingApp():
    def __init__(self):
        self.main_window = Tk()
        self.main_window.title("Grading App") #Change window title
        
        self.t1_frame = Frame() #Test 1
        self.t1_frame.pack()
        self.t1_label = Label(self.t1_frame, \
                                 text = "Enter the score for test 1:") #Label
        self.t1_label.pack(side = LEFT) #Pack
        self.t1_entry = Entry(self.t1_frame) #Entry
        self.t1_entry.pack(side = RIGHT)
        
        self.t2_frame = Frame() #Test 2
        self.t2_frame.pack()
        self.t2_label = Label(self.t2_frame, \
                                 text = "Enter the score for test 2:")
        self.t2_label.pack(side = LEFT)
        self.t2_entry = Entry(self.t2_frame)
        self.t2_entry.pack(side = RIGHT)
        
        
        self.t3_frame = Frame() #Test 3
        self.t3_frame.pack()
        self.t3_label = Label(self.t3_frame, \
                                 text = "Enter the score for test 3:")
        self.t3_label.pack(side = LEFT)
        self.t3_entry = Entry(self.t3_frame)
        self.t3_entry.pack(side = RIGHT)

        self.buttons_frame = Frame() #Buttons
        self.buttons_frame.pack()
        self.calc_button = Button(self.buttons_frame, text = "Average", \
                         command = self.calc_avg)
        self.calc_button.pack(side = 'left')
        self.quit_button = Button(self.buttons_frame, text = "Quit", \
                         command = self.main_window.destroy)
        self.quit_button.pack(side = 'left')
        
    def calc_avg(self):
        try:
            self.test1 = int(self.t1_entry.get())
            self.test2 = int(self.t2_entry.get())
            self.test3 = int(self.t3_entry.get())
            self.average = ((self.test1 + self.test2 + self.test3) / 3)
            messagebox.showinfo("OUTPUT", "The average is " + \
                                str(round(self.average,2)))
        except:
            messagebox.showinfo("OUTPUT", "ERROR: Please enter valid \
numeric grades!")

average_grade = GradingApp()
