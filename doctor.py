"""
Project: Super Health App
Creators: Aaryan Sharma, Ayush Bhardwaj
SparkHacks-2024 (University of Illinois at Chicago)
"""


import tkinter as tk
from tkinter import scrolledtext
import sqlite3


class DoctorsPage(tk.Frame):
    def __init__(self, master, goBackCall):
        super().__init__(master)
        self.master = master
        self.master.title('Find a Doctor')
        self.goBackCall = goBackCall
        self.createWidgets()
        self.pack(fill=tk.BOTH, expand=True)


    def createWidgets(self):
        tk.Label(self, text="Search for doctors by name, specialty, or location:", font=('Helvetica', 14)).pack(pady=(10, 5))

        self.searchEntry = tk.Entry(self, font=('Helvetica', 12), width=50)
        self.searchEntry.pack(pady=(0, 10))

        searchButton = tk.Button(self, text="Search", command=self.searchDoctors)
        searchButton.pack(pady=(5, 20))

        self.resultsText = scrolledtext.ScrolledText(self, font=('Helvetica', 12), wrap=tk.WORD, height=10)
        self.resultsText.pack(fill=tk.BOTH, expand=True, pady=(0, 10))

        backButton = tk.Button(self, text="Back", command=self.goBack)
        backButton.pack(pady=(0, 10))


    def searchDoctors(self):
        searchQuery = self.searchEntry.get().strip().lower()
        results = self.getDoctorsFromDB(searchQuery)
        self.displayResults(results)


    def getDoctorsFromDB(self, searchQuery):
        conn = sqlite3.connect('project.db')
        cursor = conn.cursor()

        cursor.execute("SELECT name, speciality, location, ratings FROM doctors WHERE LOWER(name) LIKE ? OR LOWER(speciality) LIKE ? OR LOWER(location) LIKE ? ORDER BY name ASC, ratings DESC", (f'%{searchQuery}%', f'%{searchQuery}%', f'%{searchQuery}%'))
        results = cursor.fetchall()

        conn.close()
        return results


    def displayResults(self, results):
        self.resultsText.delete('1.0', tk.END)
        if not results:
            self.resultsText.insert(tk.END, "No matching doctors found.\n")
        else:
            for name, speciality, location, ratings in results:
                self.resultsText.insert(tk.END, f"Name: {name}\nSpeciality: {speciality}\nLocation: {location}\nRatings: {ratings}\n\n")


    def goBack(self):
        self.destroy()
        self.goBackCall()
