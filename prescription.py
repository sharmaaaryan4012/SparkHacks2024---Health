"""
Project: Super Health App
Creators: Aaryan Sharma, Ayush Bhardwaj
SparkHacks-2024 (University of Illinois at Chicago)
"""


import tkinter as tk
from tkinter import messagebox, simpledialog
import sqlite3


class PrescriptionPage(tk.Frame):
    def __init__(self, master, goBackCallback):
        super().__init__(master)
        self.master = master
        self.goBackCallback = goBackCallback
        self.database = 'project.db'
        self.createWidgets()
        self.pack()

    def createWidgets(self):
        self.master.title('Prescription Manager')
        self.configureWidgets()
        self.loadPrescriptions()

    def configureWidgets(self):
        viewPrescriptionLabel = tk.Label(self, text="View Prescription", font=('Helvetica', 18, 'bold'))
        viewPrescriptionLabel.pack(pady=20)

        self.prescriptionListBox = tk.Listbox(self, width=50, height=10)
        self.prescriptionListBox.pack(pady=20)

        buttonsFrame = tk.Frame(self)
        buttonsFrame.pack(pady=10)

        viewButton = tk.Button(buttonsFrame, text="View", command=self.viewPrescription)
        viewButton.pack(side=tk.LEFT, padx=10, pady=10)

        addButton = tk.Button(buttonsFrame, text="Add New", command=self.addNewPrescription)
        addButton.pack(side=tk.LEFT, padx=10, pady=10)

        removeButton = tk.Button(buttonsFrame, text="Remove", command=self.removePrescription)
        removeButton.pack(side=tk.LEFT, padx=10, pady=10)

        backButton = tk.Button(buttonsFrame, text="Back", command=self.goBack)
        backButton.pack(side=tk.LEFT, padx=10, pady=10)

    def loadPrescriptions(self):
        self.prescriptionListBox.delete(0, tk.END)
        conn = sqlite3.connect(self.database)
        cursor = conn.cursor()
        cursor.execute("SELECT DISTINCT prescriptionName FROM prescriptions")
        for prescription_name in cursor.fetchall():
            self.prescriptionListBox.insert(tk.END, prescription_name[0])
        conn.close()

    def viewPrescription(self):
        selected = self.prescriptionListBox.curselection()
        if selected:
            prescription_name = self.prescriptionListBox.get(selected)
            conn = sqlite3.connect(self.database)
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM prescriptions WHERE prescriptionName = ?", (prescription_name,))
            prescriptions = cursor.fetchall()
            details = "\n\n".join(f"Medication Name: {pres[1]}\nStomach Requirement: {pres[2]}\nTiming: {pres[3]}\nMeal Times: {pres[4]}\nDuration: {pres[5]} days\nNumber of Pills: {pres[6]}\nReminder Required: {'Yes' if pres[7] else 'No'}" for pres in prescriptions)
            messagebox.showinfo("Prescription Details", details)
            conn.close()

    def addNewPrescription(self):
        prescriptionName = simpledialog.askstring("Input", "Enter the name of the prescription:")
        if not prescriptionName:
            messagebox.showerror("Error", "You must enter a name for the prescription.")
            return

        numMedications = simpledialog.askinteger("Input", "How many medications in this prescription?", minvalue=1)
        if not numMedications:
            return

        AddMedicationWindow(self, self.addPrescriptionsToDatabase, prescriptionName, numMedications)

    def addPrescriptionsToDatabase(self, prescriptions):
        conn = sqlite3.connect(self.database)
        cursor = conn.cursor()

        try:
            for pres in prescriptions:
                cursor.execute("""INSERT INTO prescriptions (prescriptionId, prescriptionName, medicationName, stomachRequirement, timing, 
                    mealTimes, duration, numberOfPills, reminderRequired) 
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)""", pres)

            conn.commit()
        except sqlite3.IntegrityError as e:
            messagebox.showerror("Database Error", f"An error occurred: {e}")
        finally:
            conn.close()

    def removePrescription(self):
        selected = self.prescriptionListBox.curselection()
        if selected:
            prescription_name = self.prescriptionListBox.get(selected)
            result = messagebox.askyesno("Remove Prescription", f"Are you sure you want to remove the prescription '{prescription_name}' and all associated medications?")
            if result:
                conn = sqlite3.connect(self.database)
                cursor = conn.cursor()
                cursor.execute("DELETE FROM prescriptions WHERE prescriptionName = ?", (prescription_name,))
                conn.commit()
                conn.close()
                self.loadPrescriptions()

    def goBack(self):
        self.destroy()
        self.goBackCallback()


class AddMedicationWindow(tk.Toplevel):
    def __init__(self, master, callback, prescriptionName, numMedications):
        super().__init__(master)
        self.master = master
        self.callback = callback
        self.prescriptionName = prescriptionName
        self.numMedications = numMedications
        self.currentMedication = 0
        self.prescriptions = []
        self.createWidgets()

    def createWidgets(self):
        self.title('Add New Medication')

        tk.Label(self, text="Medication Name:").pack()
        self.medicationNameEntry = tk.Entry(self)
        self.medicationNameEntry.pack()

        tk.Label(self, text="Stomach Requirement (empty/full):").pack()
        self.stomachRequirementEntry = tk.Entry(self)
        self.stomachRequirementEntry.pack()

        tk.Label(self, text="Timing (morning/evening/night):").pack()
        self.timingEntry = tk.Entry(self)
        self.timingEntry.pack()

        tk.Label(self, text="Meal Times (comma-separated):").pack()
        self.mealTimesEntry = tk.Entry(self)
        self.mealTimesEntry.pack()

        tk.Label(self, text="Duration (in days):").pack()
        self.durationEntry = tk.Entry(self)
        self.durationEntry.pack()

        tk.Label(self, text="Number of Pills:").pack()
        self.numberOfPillsEntry = tk.Entry(self)
        self.numberOfPillsEntry.pack()

        tk.Label(self, text="Reminder Required (yes/no):").pack()
        self.reminderRequiredEntry = tk.Entry(self)
        self.reminderRequiredEntry.pack()

        submitButton = tk.Button(self, text="Add Medication", command=self.submitMedication)
        submitButton.pack()

    def submitMedication(self):
        medicationName = self.medicationNameEntry.get()
        stomachRequirement = self.stomachRequirementEntry.get()
        timing = self.timingEntry.get()
        mealTimes = self.mealTimesEntry.get()
        duration = self.durationEntry.get()
        numberOfPills = self.numberOfPillsEntry.get()
        reminderRequired = self.reminderRequiredEntry.get()

        # Validation can be performed here
        # For simplicity, assume the user has entered all values correctly

        prescriptionId = f"{self.prescriptionName}-{self.currentMedication + 1}"
        reminderRequired = 1 if reminderRequired.lower() == 'yes' else 0

        self.prescriptions.append((prescriptionId, self.prescriptionName, medicationName, stomachRequirement, timing, mealTimes, int(duration), int(numberOfPills), reminderRequired))
        self.currentMedication += 1

        # Clear the entries for the next medication
        self.medicationNameEntry.delete(0, tk.END)
        self.stomachRequirementEntry.delete(0, tk.END)
        self.timingEntry.delete(0, tk.END)
        self.mealTimesEntry.delete(0, tk.END)
        self.durationEntry.delete(0, tk.END)
        self.numberOfPillsEntry.delete(0, tk.END)
        self.reminderRequiredEntry.delete(0, tk.END)

        if self.currentMedication >= self.numMedications:
            self.callback(self.prescriptions)
            self.destroy()
