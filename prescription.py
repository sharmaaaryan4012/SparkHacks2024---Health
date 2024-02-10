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
from tkinter import Label, Entry, Button, messagebox

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
        messagebox.showinfo("View Prescriptions", "This would show all existing prescriptions.")

    def create_prescription_form(self):
        self.clear_widgets()
        Label(self, text="Create Prescription", font=('Helvetica', 16)).pack(pady=20)
        Label(self, text="Prescription Name:").pack()
        self.pres_name_entry = Entry(self)
        self.pres_name_entry.pack()
        Label(self, text="Number of Meds Prescribed:").pack()
        self.num_meds_entry = Entry(self)
        self.num_meds_entry.pack()
        Button(self, text="Next", command=self.meds_detail_form).pack(pady=10)
        Button(self, text="Back", command=self.main_menu).pack(pady=10)

    def meds_detail_form(self):
        try:
            num_meds = int(self.num_meds_entry.get())
            self.prescription_details = {
                'pres_name': self.pres_name_entry.get().upper(),
                'meds': [],
                'reminder': False  # Initialize the reminder attribute
            }
            self.clear_widgets()
            Label(self, text=f"Enter Details for {num_meds} Medications", font=('Helvetica', 16)).pack(pady=20)
            self.meds_entries = []
            for i in range(num_meds):
                Label(self, text=f"Medicine {i + 1} Name:").pack()
                med_name_entry = Entry(self)
                med_name_entry.pack()

                Label(self, text=f"Number of Pills:").pack()
                num_pills_entry = Entry(self)
                num_pills_entry.pack()

                Label(self, text=f"Duration (Days):").pack()
                med_dur_entry = Entry(self)
                med_dur_entry.pack()

                Label(self, text="Empty or Full Stomach (E/F):").pack()
                med_empty_entry = Entry(self)
                med_empty_entry.pack()

                Label(self, text="Time (M/A/E/N):").pack()
                med_time_entry = Entry(self)
                med_time_entry.pack()

                self.meds_entries.append(
                    (med_name_entry, num_pills_entry, med_dur_entry, med_empty_entry, med_time_entry))

            Label(self, text="Do you want to set a reminder? (Y/N):").pack()
            self.reminder_entry = Entry(self)
            self.reminder_entry.pack()

            Button(self, text="Submit", command=self.collect_meds_details).pack(pady=10)
            Button(self, text="Back", command=self.create_prescription_form).pack(pady=10)
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid number of medications.")
            self.create_prescription_form()

    def collect_meds_details(self):
        for entries in self.meds_entries:
            med_name, num_pills, med_dur, med_empty, med_time = (entry.get().upper() for entry in entries)
            # Translate "E" to "Empty" and "F" to "Full"
            med_empty_translated = "Empty" if med_empty == "E" else "Full" if med_empty == "F" else "Unknown"

            self.prescription_details['meds'].append({
                'name': med_name,
                'pills': num_pills,
                'duration': med_dur,
                'empty': med_empty_translated,
                'time': med_time,
            })

        reminder_response = self.reminder_entry.get().lower()
        self.prescription_details['reminder'] = True if reminder_response == 'y' else False

        self.show_prescription_summary()

    def show_prescription_summary(self):
        self.clear_widgets()
        Label(self, text="Prescription Summary", font=('Helvetica', 16)).pack(pady=20)
        Label(self, text=f"Prescription Name: {self.prescription_details['pres_name']}").pack()
        for med in self.prescription_details['meds']:
            Label(self,
                  text=f"Name of the Medicine: {med['name']}\n The number of Pills: {med['pills']}\n The Medicine is prescribed for: {med['duration']} days\n The Medicine should be taken: {med['empty']} stomach\n The medicine is to be taken at: (M : Morning, A : Afternoon, E : Evening, N : Night) {med['time']}").pack()
        reminder_text = "Yes" if self.prescription_details['reminder'] else "No"
        Label(self, text=f"Reminder Set: {reminder_text}").pack()

        Button(self, text="Back to Main Menu", command=self.main_menu).pack(pady=10)

    def back(self):
        if self.callback:
            self.callback()

    def clear_widgets(self):
        for widget in self.winfo_children():
            widget.destroy()










