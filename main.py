"""
Project: Super Health App
Creators: Aaryan Sharma, Ayush Bhardwaj
SparkHacks-2024 (University of Illinois at Chicago)
"""


import tkinter as tk
from mindful import MindfulPage
from tkinter import messagebox


class MainPage(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Super Health App')
        # self.configure(bg='black')
        self.geometry('600x400')
        self.create_widgets()

    def create_widgets(self):
        welcome_label = tk.Label(self, text="Welcome To The Super Health App", fg='black', bg='white', font=('Helvetica', 25, 'bold'))
        welcome_label.pack(pady=20)

        doctors_button = tk.Button(self, text="Doctors", font=('Helvetica', 12), command=self.gotoDoctors)
        doctors_button.pack(pady=10, ipadx=20, ipady=10)

        prescription_button = tk.Button(self, text="Prescription Manager", font=('Helvetica', 12), command=self.gotoPrescription)
        prescription_button.pack(pady=10, ipadx=20, ipady=10)

        reminders_button = tk.Button(self, text="Reminders", font=('Helvetica', 12), command=self.gotoReminders)
        reminders_button.pack(pady=10, ipadx=20, ipady=10)

        mindful_button = tk.Button(self, text="Mindful Space", font=('Helvetica', 12), command=self.gotoMindful)
        mindful_button.pack(pady=10, ipadx=20, ipady=10)

    def gotoDoctors(self):
        messagebox.showinfo("Go to Doctors", "This will go to the Doctors section.")

    def gotoPrescription(self):
        messagebox.showinfo("Go to Prescriptions", "This will go to the Prescription Manager section.")

    def gotoReminders(self):
        messagebox.showinfo("Go to Reminders", "This will go to the Reminders section.")

    def gotoMindful(self):
        for widget in self.winfo_children():
            widget.destroy()
        MindfulPage(self)


if __name__ == '__main__':
    app = MainPage()
    app.mainloop()
