# """
# Project: Super Health App
# Creators: Aaryan Sharma, Ayush Bhardwaj
# SparkHacks-2024 (University of Illinois at Chicago)
# """
#
# print("Welcome to create prescription page!")
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
from tkinter import Label, Entry, Button, messagebox, Toplevel


class PrescriptionPage(tk.Frame):
    def __init__(self, master=None, callback=None):
        super().__init__(master)
        self.master = master
        self.callback = callback
        self.pack()
        self.main_menu()

    def main_menu(self):
        self.clear_widgets()

        Label(self, text="Prescription Management", font=('Helvetica', 16)).pack(pady=20)

        Button(self, text="View Prescriptions", command=self.view_prescriptions).pack(pady=10)
        Button(self, text="Create New Prescription", command=self.create_prescription_form).pack(pady=10)
        Button(self, text="Back", command=self.back).pack(pady=10)

    def view_prescriptions(self):
        # Placeholder for viewing prescriptions logic
        messagebox.showinfo("View Prescriptions", "This would show all existing prescriptions.")

    def create_prescription_form(self):
        self.clear_widgets()

        Label(self, text="Create Prescription", font=('Helvetica', 16)).pack(pady=20)

        # Simplified form based on the given structure
        self.entries = {
            'pres_name': None,
            'num_Meds': None,
            # You would dynamically generate entries for each medication based on num_Meds
            # This is a simplified representation
        }

        Label(self, text="Prescription Name:").pack()
        self.entries['pres_name'] = Entry(self)
        self.entries['pres_name'].pack()

        Label(self, text="Number of Meds Prescribed:").pack()
        self.entries['num_Meds'] = Entry(self)
        self.entries['num_Meds'].pack()

        Button(self, text="Submit", command=self.submit_prescription).pack(pady=10)
        Button(self, text="Back", command=self.main_menu).pack(pady=10)

    def submit_prescription(self):
        pres_name = self.entries['pres_name'].get().upper()
        num_meds = self.entries['num_Meds'].get().upper()
        # Implement logic for handling prescription data here
        messagebox.showinfo("Prescription Created", f"Prescription '{pres_name}' with {num_meds} meds added.")
        self.main_menu()

    def back(self):
        if self.callback:
            self.callback()

    def clear_widgets(self):
        for widget in self.winfo_children():
            widget.destroy()




