"""
Project: Super Health App
Creators: Aaryan Sharma, Ayush Bhardwaj
SparkHacks-2024 (University of Illinois at Chicago)
"""

import tkinter as tk
from tkinter import messagebox
import sqlite3
from datetime import datetime, timedelta


class ReminderPage(tk.Frame):
    def __init__(self, master, goBackCall, database='project.db'):
        super().__init__(master)
        self.master = master
        self.goBackCall = goBackCall
        self.database = database
        self.createWidgets()
        self.pack()

    def createWidgets(self):
        self.master.title('Reminders')

        self.reminderLabel = tk.Label(self, text="Medication Reminders", font=('Helvetica', 18, 'bold'))
        self.reminderLabel.pack(pady=20)

        self.reminderListBox = tk.Listbox(self, width=80, height=10)
        self.reminderListBox.pack(pady=20)
        self.loadReminders()

        self.backButton = tk.Button(self, text="Back", command=self.goBack)
        self.backButton.pack(pady=20)

    def loadReminders(self):
        self.reminderListBox.delete(0, tk.END)
        try:
            conn = sqlite3.connect(self.database)
            cursor = conn.cursor()
            cursor.execute("""SELECT prescriptionName, medicationName, timing, stomachRequirement, bTime, lTime, dTime, duration, numberOfPills 
                              FROM prescriptions 
                              WHERE reminderRequired = 1""")
            for row in cursor.fetchall():
                takeMedicineTime = self.calculateTakeMedicineTime(row)
                reminderEntry = f"{row[0]} - {row[1]}, Take at: {takeMedicineTime}"
                self.reminderListBox.insert(tk.END, reminderEntry)
            conn.close()
        except sqlite3.Error as e:
            messagebox.showerror("Database Error", f"An error occurred: {e}")

    def calculateTakeMedicineTime(self, prescription):
        _, _, timing, stomachRequirement, bTime, lTime, dTime, _, _ = prescription

        mealTimeStr = bTime if timing == "morning" else lTime if timing == "afternoon" else dTime
        mealTime = datetime.strptime(mealTimeStr, "%H:%M")

        takeTime = (mealTime - timedelta(hours=1)) if stomachRequirement == "empty" else (mealTime + timedelta(hours=1))

        return takeTime.strftime("%H:%M")

    def goBack(self):
        self.destroy()
        self.goBackCall()
