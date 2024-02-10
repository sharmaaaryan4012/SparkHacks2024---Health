"""
Project: Super Health App
Creators: Aaryan Sharma, Ayush Bhardwaj
SparkHacks-2024 (University of Illinois at Chicago)
"""


import tkinter as tk
from tkinter import *
from mindful import MindfulPage
from tkinter import messagebox
from prescription import PrescriptionPage
from about import AboutPage
from doctor import DoctorsPage
import subprocess
import sys
import os


class MainPage(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Super Health App')
        self.geometry('4000x2250')  # Unusually large, but kept as per request
        self.state('zoomed')

        # Load the background image
        self.bg = PhotoImage(file="IMG__2.png")
        label1 = Label(self, image=self.bg)
        label1.place(x=0, y=0, relwidth=1, relheight=1)  # Cover the whole window

        self.createWidgets()

    def createWidgets(self):


        welcomeLabel = tk.Label(self, text=" SUPER HEALTH", fg='purple4',
                                bg='white', font=('Bold Condensed', 60, 'bold'))
        welcomeLabel2 = tk.Label(self, text=" Welcome onboard with Mindful Technology: Your Personalized Wellness Oasis!", fg='purple4',
                                bg='white', font=('Bold Condensed', 20, 'bold'))
        welcomeLabel.pack(pady=20)
        welcomeLabel2.pack(pady=2)

        buttonsFrame = tk.Frame(self, bg='white')
        buttonsFrame.pack(expand=True)

        doctorsButton = tk.Button(buttonsFrame, text="Doctors", fg="purple4", font=('Helvetica', 20),
                                  command=self.gotoDoctors, bg='white')
        doctorsButton.pack(pady=10, ipadx=20, ipady=10, fill='x')

        prescriptionButton = tk.Button(buttonsFrame, text="Prescription Manager", fg="purple4", font=('Helvetica', 20),
                                       command=self.gotoPrescription, bg='white')
        prescriptionButton.pack(pady=10, ipadx=20, ipady=10, fill='x')

        remindersButton = tk.Button(buttonsFrame, text="Reminders", fg="purple4", font=('Helvetica', 20),
                                    command=self.gotoReminders, bg='white')
        remindersButton.pack(pady=10, ipadx=20, ipady=10, fill='x')

        mindfulButton = tk.Button(buttonsFrame, text="Mindful Space", fg="purple4", font=('Helvetica', 20),
                                  command=self.gotoMindful, bg='white')
        mindfulButton.pack(pady=10, ipadx=20, ipady=10, fill='x')

        spaceGameButton = tk.Button(buttonsFrame, text="Space Game", fg="purple4", font=('Helvetica', 20),
                                    command=self.launchSpaceGame, bg='white')
        spaceGameButton.pack(pady=10, ipadx=20, ipady=10, fill='x')

        bottomFrame = tk.Frame(self, bg='purple4')
        bottomFrame.pack(side='bottom', fill='x', expand=False)

        aboutButton = tk.Button(bottomFrame, text="About", fg="purple4", font=('Helvetica', 12), command=self.gotoAbout,
                                bg='white')
        aboutButton.pack(side='left', padx=10, pady=10)

        quitButton = tk.Button(bottomFrame, text="Quit", fg="purple4", font=('Helvetica', 12), command=self.Quit,
                               bg='white')
        quitButton.pack(side='right', padx=10, pady=10)



    def gotoDoctors(self):
        self.clearWidgets()
        DoctorsPage(self, self.callback).pack(fill=tk.BOTH, expand=True)


    def gotoPrescription(self):
        self.clearWidgets()
        PrescriptionPage(self, self.callback).pack(fill=tk.BOTH, expand=True)


    def gotoReminders(self):
        messagebox.showinfo("Go to Reminders", "This will go to the Reminders section.")


    def gotoMindful(self):
        self.clearWidgets()
        MindfulPage(self, self.callback).pack(fill=tk.BOTH, expand=True)


    def gotoAbout(self):
        self.clearWidgets()
        AboutPage(self, self.callback).pack(fill=tk.BOTH, expand=True)


    def Quit(self):
        sys.exit(0)


    def launchSpaceGame(self):
        currentDir = os.path.dirname(os.path.abspath(__file__))
        spaceGamePath = os.path.join(currentDir, 'SpaceGame', 'space.py')
        subprocess.Popen([sys.executable, spaceGamePath])


    def callback(self):
        self.clearWidgets()
        self.createWidgets()


    def clearWidgets(self):
        for widget in self.winfo_children():
            widget.destroy()


if __name__ == '__main__':
    app = MainPage()
    app.mainloop()
