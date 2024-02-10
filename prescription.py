"""
Project: Super Health App
Creators: Aaryan Sharma, Ayush Bhardwaj
SparkHacks-2024 (University of Illinois at Chicago)
     """



import tkinter as tk
from tkinter import messagebox
from addPrescription import AddPrescriptionForm
import sqlite3

class PrescriptionPage(tk.Frame):
    def __init__(self, master, goBackCall):
        super().__init__(master)
        self.master = master
        self.goBackCall = goBackCall
        self.database = 'project.db'
        self.configure(bg='white')
        self.createWidgets()
        self.pack()

    def createWidgets(self):
        self.master.title('Prescription Manager')

        # Label for Prescription Manager section
        viewPrescriptionLabel = tk.Label(self, text="View Prescription", font=('Helvetica', 18, 'bold'))
        viewPrescriptionLabel.pack(pady=20)

        # Listbox for prescriptions
        self.prescriptionListBox = tk.Listbox(self, width=50, height=10)
        self.prescriptionListBox.pack(pady=20)
        self.loadPrescriptions()

        # Buttons for different actions
        viewButton = tk.Button(self, text="View",fg = "purple4", bg = "white", font =("Arial", 20, "bold"), command=self.viewPrescription)
        viewButton.pack(side=tk.TOP, padx=20, pady=5)

        addButton = tk.Button(self, text="Add New",fg = "purple4", bg = "white", font =("Arial", 20, "bold"), command=self.addNewPrescription)
        addButton.pack(side=tk.TOP, padx=20, pady=5)

        removeButton = tk.Button(self, text="Remove",fg = "purple4", bg = "white", font =("Arial", 20, "bold"), command=self.removePrescription)
        removeButton.pack(side=tk.TOP, padx=20, pady=5)

        backButton = tk.Button(self, text="Back",fg = "purple4", bg = "white", font =("Arial", 20, "bold"), command=self.goBack)
        backButton.pack(side=tk.TOP, pady=5)
        bottom_frame = tk.Frame(self, bg='purple4', height=50)
        bottom_frame.pack(side='bottom', fill='x', expand=False)
        bottom_frame.pack_propagate(False)

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
        # First, clear the current content of the PrescriptionPage
        for widget in self.winfo_children():
            widget.destroy()

        # Then, instantiate and pack the AddPrescriptionForm onto the master window
        # Note that this will place the form on top of the background image, which remains intact
        self.add_prescription_form = AddPrescriptionForm(self.master, self.goBackCall, self.database)
        self.add_prescription_form.pack(expand=True, fill=tk.BOTH)

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