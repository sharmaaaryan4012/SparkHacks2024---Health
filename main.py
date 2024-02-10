"""
Project: Super Health App
Creators: Aaryan Sharma, Ayush Bhardwaj
SparkHacks-2024 (University of Illinois at Chicago)
"""


import tkinter as tk
from mindful import MindfulPage
from tkinter import messagebox
import subprocess
import sys
import os

class MainPage(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Super Health App')
        self.state('zoomed')
        self.createWidgets()

    def createWidgets(self):
        welcome_label = tk.Label(self, text="Welcome to the Onboard with the All-in-one Health Companion!", fg='black', bg='white', font=('Helvetica', 25, 'bold'))
        welcome_label.pack(pady=20)

        doctors_button = tk.Button(self, text="Doctors", font=('Helvetica', 12), command=self.gotoDoctors)
        doctors_button.pack(pady=10, ipadx=20, ipady=10)

        prescription_button = tk.Button(self, text="Prescription Manager", font=('Helvetica', 12), command=self.gotoPrescription)
        prescription_button.pack(pady=10, ipadx=20, ipady=10)

        reminders_button = tk.Button(self, text="Reminders", font=('Helvetica', 12), command=self.gotoReminders)
        reminders_button.pack(pady=10, ipadx=20, ipady=10)

        mindful_button = tk.Button(self, text="Mindful Space", font=('Helvetica', 12), command=self.gotoMindful)
        mindful_button.pack(pady=10, ipadx=20, ipady=10)

        about_button = tk.Button(self, text="About", font=('Helvetica', 10), command=self.gotoAbout)
        about_button.place(relx=0.01, rely=0.95, anchor=tk.W)

        space_game_button = tk.Button(self, text="Space Game", font=('Helvetica', 12), command=self.launchSpaceGame)
        space_game_button.pack(pady=10, ipadx=20, ipady=10, side='bottom', anchor='e')

    def gotoDoctors(self):
        messagebox.showinfo("Go to Doctors", "This will go to the Doctors section.")

    def gotoPrescription(self):
        messagebox.showinfo("Go to Prescriptions", "This will go to the Prescription Manager section.")

    def gotoReminders(self):
        messagebox.showinfo("Go to Reminders", "This will go to the Reminders section.")

    def gotoMindful(self):
        for widget in self.winfo_children():
            widget.destroy()
        MindfulPage(self, self.CallBack)

    def gotoAbout(self):
        messagebox.showinfo("About", "Creators: Aaryan Sharma, Ayush Bhardwaj\nSparkHacks-2024 (University of Illinois at Chicago)")

    def gotoSpaceGame(self):
        messagebox.showinfo("Space Game", "Starting the Space Game...")


    def launchSpaceGame(self):
        current_dir = os.path.dirname(os.path.abspath(__file__))
        space_game_path = os.path.join(current_dir, 'SpaceGame', 'space.py')
        subprocess.Popen([sys.executable, space_game_path])

    def CallBack(self):
        for widget in self.winfo_children():
            widget.destroy()
        self.createWidgets()

if __name__ == '__main__':
    app = MainPage()
    app.mainloop()
