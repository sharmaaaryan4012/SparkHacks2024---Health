"""
Project: Super Health App
Creators: Aaryan Sharma, Ayush Bhardwaj
SparkHacks-2024 (University of Illinois at Chicago)
"""

import tkinter as tk
from addPrescription import AddPrescriptionForm
from tkinter import messagebox
import sqlite3

class PrescriptionPage(tk.Frame):
    def __init__(self, master, goBackCall):
        super().__init__(master)
        self.master = master
        self.goBackCall = goBackCall
        self.database = 'project.db'
        self.createWidgets()
        self.pack()


    def createWidgets(self):
        self.master.title('Prescription Manager')

        viewPrescriptionLabel = tk.Label(self, text="View Prescription", font=('Helvetica', 18, 'bold'))
        viewPrescriptionLabel.pack(pady=20)

        self.prescriptionListBox = tk.Listbox(self, width=50, height=10)
        self.prescriptionListBox.pack(pady=20)
        self.loadPrescriptions()

        viewButton = tk.Button(self, text="View", command=self.viewPrescription)
        viewButton.pack(side=tk.LEFT, padx=20, pady=10)

        addButton = tk.Button(self, text="Add New", command=self.addNewPrescription)
        addButton.pack(side=tk.LEFT, padx=20, pady=10)

        removeButton = tk.Button(self, text="Remove", command=self.removePrescription)
        removeButton.pack(side=tk.LEFT, padx=20, pady=10)

        backButton = tk.Button(self, text="Back", command=self.goBack)
        backButton.pack(pady=20)


    def loadPrescriptions(self):
        self.prescriptionListBox.delete(0, tk.END)
        conn = sqlite3.connect(self.database)
        cursor = conn.cursor()
        cursor.execute("SELECT prescriptionName FROM prescriptions")
        for row in cursor.fetchall():
            self.prescriptionListBox.insert(tk.END, row[0])
        conn.close()


    def viewPrescription(self):
        selected = self.prescriptionListBox.curselection()
        if selected:
            prescriptionName = self.prescriptionListBox.get(selected)
            conn = sqlite3.connect(self.database)
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM prescriptions WHERE prescriptionName = ?", (prescriptionName,))
            prescription = cursor.fetchone()
            details = f"Prescription Name: {prescription[0]}\nMedication Name: {prescription[1]}\nStomach Requirement: {prescription[2]}\nTiming: {prescription[3]}\nBreakfast Time: {prescription[4]}\nDuration: {prescription[5]} days\nNumber of Pills: {prescription[6]}\nReminder Required: {'Yes' if prescription[7] else 'No'}\nLunch Time: {prescription[8]}\nDinner Time: {prescription[9]}"
            messagebox.showinfo("Prescription Details", details)
            conn.close()


    def addNewPrescription(self):
        self.clearWidgets()
        AddPrescriptionForm(self.master, self.goBackCall, self.database)


    def removePrescription(self):
        selected = self.prescriptionListBox.curselection()
        if selected:
            result = messagebox.askyesno("Remove Prescription", "Are you sure you want to remove this prescription?")
            if result:
                prescriptionName = self.prescriptionListBox.get(selected)
                conn = sqlite3.connect(self.database)
                cursor = conn.cursor()
                cursor.execute("DELETE FROM prescriptions WHERE prescriptionName = ?", (prescriptionName,))
                conn.commit()
                conn.close()
                self.loadPrescriptions()


    def goBack(self):
        self.destroy()
        self.goBackCall()

    def clearWidgets(self):
        for widget in self.winfo_children():
            widget.destroy()