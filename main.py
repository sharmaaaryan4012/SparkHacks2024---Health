"""
Project: Super Health App
Creators: Aaryan Sharma, Ayush Bhardwaj
SparkHacks-2024 (University of Illinois at Chicago)
"""


import tkinter as tk
from mindful import MindfulPage
from tkinter import messagebox
from prescription import PrescriptionPage
from about import AboutPage
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
        welcome_label = tk.Label(self, text="Welcome to the Onboard with the All-in-one Health Companion!", fg='black',
                                 bg='white', font=('Helvetica', 25, 'bold'))
        welcome_label.pack(pady=20)

        # Create a container frame for the buttons to center them
        buttons_frame = tk.Frame(self)
        buttons_frame.pack(expand=True)

        doctors_button = tk.Button(buttons_frame, text="Doctors", font=('Helvetica', 12), command=self.gotoDoctors)
        doctors_button.pack(pady=10, ipadx=20, ipady=10, fill='x')

        prescription_button = tk.Button(buttons_frame, text="Prescription Manager", font=('Helvetica', 12),
                                        command=self.gotoPrescription)
        prescription_button.pack(pady=10, ipadx=20, ipady=10, fill='x')

        reminders_button = tk.Button(buttons_frame, text="Reminders", font=('Helvetica', 12),
                                     command=self.gotoReminders)
        reminders_button.pack(pady=10, ipadx=20, ipady=10, fill='x')

        mindful_button = tk.Button(buttons_frame, text="Mindful Space", font=('Helvetica', 12),
                                   command=self.gotoMindful)
        mindful_button.pack(pady=10, ipadx=20, ipady=10, fill='x')

        # For the bottom buttons, we'll create another frame
        bottom_frame = tk.Frame(self)
        bottom_frame.pack(side='bottom', fill='x', expand=False)

        about_button = tk.Button(bottom_frame, text="About", font=('Helvetica', 12), command=self.gotoAbout)
        about_button.pack(side='left', padx=10, pady=10)

        space_game_button = tk.Button(bottom_frame, text="Space Game", font=('Helvetica', 12),
                                      command=self.gotoSpaceGame)
        space_game_button.pack(side='right', padx=10, pady=10)

    def gotoDoctors(self):
        messagebox.showinfo("Go to Doctors", "This will go to the Doctors section.")


    def gotoPrescription(self):
        for widget in self.winfo_children():
            widget.destroy()

        pres_page = PrescriptionPage(self, self.CallBack)
        pres_page.pack(fill=tk.BOTH, expand=True)


    def gotoReminders(self):
        messagebox.showinfo("Go to Reminders", "This will go to the Reminders section.")


    def gotoMindful(self):
        for widget in self.winfo_children():
            widget.destroy()
        MindfulPage(self, self.CallBack)


    def gotoAbout(self):
        for widget in self.winfo_children():
            widget.destroy()
        AboutPage(self, self.CallBack).pack(fill=tk.BOTH, expand=True)


    def gotoSpaceGame(self):
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
