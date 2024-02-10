# """
# Project: Super Health App
# Creators: Aaryan Sharma, Ayush Bhardwaj
# SparkHacks-2024 (University of Illinois at Chicago)
# """
#
# print("Welcome to prescription column!")
#
# pres_name = input("Kindly enter prescription name \n").upper()
# num_Meds = input("Kindly enter the number of meds prescribed \n").upper()
# meds_name = []
# meds_dur = []
# meds_empty = []
# meds_time = []
# meal_time = []
#
# for i in range(int(num_Meds)):
#     meds_name.append(input("Kindly enter the name of medicine: ").upper())
#     meds_dur.append(input("Kindly enter the Duration of Doses (In Days) for the Medicine: ").upper())
#     meds_empty.append(input("Kindly enter whether the medicine is to be taken on an empty or full stomach (Enter E or F):\n").upper())
#     meds_time.append(input("Kindly enter the time of the medicine\n Enter M for morning \n Enter A for afternoon \n Enter E for evening \n Enter N for Night\ne.g. me").upper())
#
# for i in range(3):
#     meal_time.append(input("Kindly enter the time of your meal (enter 3:00am as 3 and 3:00pm as 15): ").upper())
#
#
#
#


# prescription.py

import tkinter as tk
from tkinter import Label, Entry, Button, messagebox

class PrescriptionPage(tk.Frame):
    def __init__(self, master=None, callback=None):
        super().__init__(master)
        self.master = master
        self.callback = callback
        self.create_widgets()

    def create_widgets(self):
        # Prescription name entry
        self.lbl_pres_name = Label(self, text="Prescription Name:")
        self.lbl_pres_name.grid(row=0, column=0)
        self.entry_pres_name = Entry(self)
        self.entry_pres_name.grid(row=0, column=1)

        # Number of meds entry
        self.lbl_num_meds = Label(self, text="Number of Meds Prescribed:")
        self.lbl_num_meds.grid(row=1, column=0)
        self.entry_num_meds = Entry(self)
        self.entry_num_meds.grid(row=1, column=1)

        # Submit button
        self.submit_button = Button(self, text="Submit", command=self.submit)
        self.submit_button.grid(row=2, column=0, columnspan=2)

    def submit(self):
        pres_name = self.entry_pres_name.get().upper()
        num_meds = self.entry_num_meds.get().upper()
        # Implement logic for handling prescription data here
        messagebox.showinfo("Submission", f"Prescription '{pres_name}' with {num_meds} meds submitted.")
        # Optionally call the callback to return to the main window
        if self.callback:
            self.callback()


