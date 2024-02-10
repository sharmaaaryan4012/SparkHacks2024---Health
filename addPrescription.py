"""
Project: Super Health App
Creators: Aaryan Sharma, Ayush Bhardwaj
SparkHacks-2024 (University of Illinois at Chicago)
   hey"""


import tkinter as tk
from tkinter import messagebox, simpledialog
import sqlite3


class AddPrescriptionForm(tk.Frame):
    def __init__(self, master, goBackCall, database='project.db'):
        super().__init__(master)
        self.master = master
        self.goBackCall = goBackCall
        self.database = database
        self.createForm()
        self.pack()

    def createForm(self):
        self.master.title('Add New Prescription')

        # Name of the Prescription
        tk.Label(self, text="Prescription Name:", fg = "purple4", bg = "white", font =("Arial", 15, "bold")).pack()
        self.prescriptionNameEntry = tk.Entry(self)
        self.prescriptionNameEntry.pack()

        # Medication Name
        tk.Label(self, text="Medication Name:", fg = "purple4", bg = "white", font =("Arial", 15, "bold")).pack()
        self.medicationNameEntry = tk.Entry(self)
        self.medicationNameEntry.pack()

        # Stomach Requirement
        tk.Label(self, text="Stomach Requirement (empty/full):", fg = "purple4", bg = "white", font =("Arial", 15, "bold")).pack()
        self.stomachRequirementEntry = tk.Entry(self)
        self.stomachRequirementEntry.pack()

        # Timing
        tk.Label(self, text="Timing (morning/afternoon/night):", fg = "purple4", bg = "white", font =("Arial", 15, "bold")).pack()
        self.timingEntry = tk.Entry(self)
        self.timingEntry.pack()

        # Meal Timings
        tk.Label(self, text="Breakfast Time(HH:MM):", fg = "purple4", bg = "white", font =("Arial", 15, "bold")).pack()
        self.bTimeEntry = tk.Entry(self)
        self.bTimeEntry.pack()

        tk.Label(self, text="Lunch Time(HH:MM):", fg = "purple4", bg = "white", font =("Arial", 15, "bold")).pack()
        self.lTimeEntry = tk.Entry(self)
        self.lTimeEntry.pack()

        tk.Label(self, text="Dinner Time(HH:MM):", fg = "purple4", bg = "white", font =("Arial", 15, "bold")).pack()
        self.dTimeEntry = tk.Entry(self)
        self.dTimeEntry.pack()

        # Number of Pills
        tk.Label(self, text="Number of Pills:", fg = "purple4", bg = "white", font =("Arial", 15, "bold")).pack()
        self.numberOfPillsEntry = tk.Entry(self)
        self.numberOfPillsEntry.pack()

        # Duration
        tk.Label(self, text="Duration (in days):", fg = "purple4", bg = "white", font =("Arial", 15, "bold")).pack()
        self.durationEntry = tk.Entry(self)
        self.durationEntry.pack()

        # Reminder Required
        self.reminderRequiredVar = tk.BooleanVar()
        tk.Checkbutton(self, text="Reminder Required", variable=self.reminderRequiredVar).pack()

        # Submit Button
        submitButton = tk.Button(self, text="Submit", command=self.submitPrescription)
        submitButton.pack()

        # Back Button
        backButton = tk.Button(self, text="Back", command=self.goBack)
        backButton.pack()

        bottom_frame = tk.Frame(self, bg='purple4', height=50)
        bottom_frame.pack(side='bottom', fill='x', expand=False)
        bottom_frame.pack_propagate(False)

    def submitPrescription(self):
        # Collect the data
        prescriptionName = self.prescriptionNameEntry.get()
        medicationName = self.medicationNameEntry.get()
        stomachRequirement = self.stomachRequirementEntry.get().lower()
        timing = self.timingEntry.get().lower()
        bTime = self.bTimeEntry.get()
        lTime = self.lTimeEntry.get()
        dTime = self.dTimeEntry.get()
        numberOfPills = int(self.numberOfPillsEntry.get())
        duration = int(self.durationEntry.get())
        reminderRequired = self.reminderRequiredVar.get()

        # Validate the data
        if not all([prescriptionName, medicationName, stomachRequirement, timing, bTime, lTime, dTime]):
            messagebox.showerror("Error", "All fields are required!")
            return

        if stomachRequirement not in ["empty", "full"] or timing not in ["morning", "afternoon", "night"]:
            messagebox.showerror("Error", "Invalid stomach requirement or timing!")
            return

        # Insert the data into the database
        conn = sqlite3.connect(self.database)
        cursor = conn.cursor()
        cursor.execute("""INSERT INTO prescriptions (prescriptionName, medicationName, stomachRequirement, timing, bTime, duration, numberOfPills, reminderRequired, lTime, dTime)
                          VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""",
                       (prescriptionName, medicationName, stomachRequirement, timing, bTime, duration, numberOfPills, reminderRequired, lTime, dTime))
        conn.commit()
        conn.close()

        # Confirmation message
        messagebox.showinfo("Success", "Prescription added successfully.")
        self.goBack()

    def goBack(self):
        self.destroy()
        self.goBackCall()
