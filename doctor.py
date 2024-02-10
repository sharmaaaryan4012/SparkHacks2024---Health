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
        super().__init__(master, bg='white')  # Set the frame background to white
        self.master = master
        self.master.title('Find a Doctor')
        self.goBackCall = goBackCall
        self.createWidgets()
        self.pack(fill=tk.BOTH, expand=True)

        bottom_frame = tk.Frame(self, bg='purple4', height=50)
        bottom_frame.pack(side='bottom', fill='x', expand=False)
        bottom_frame.pack_propagate(False)

    def createWidgets(self):
        tk.Label(self, text="Search for doctors by name, specialty, or location:",
                 fg="purple4", bg="white", font=('Arial', 30, "bold")).pack(pady=(10, 5))

        self.searchEntry = tk.Entry(self, fg="purple4", bg="white",
                                    font=('Arial', 30, "bold"), width=50)
        self.searchEntry.pack(pady=(0, 10))

        searchButton = tk.Button(self, text="Search", fg="purple4", bg="white", font=('Arial', 20, "bold"),
                                 command=self.searchDoctors)
        searchButton.pack(pady=(5, 20))

        self.resultsText = scrolledtext.ScrolledText(self, font=('Helvetica', 12), wrap=tk.WORD,
                                                     height=10, bg='white')  # Set the scrolledtext background to white
        self.resultsText.pack(fill=tk.BOTH, expand=True, pady=(0, 10))

        backButton = tk.Button(self, text="Back", fg="purple4", bg="white",
                               font=('Arial', 20, "bold"), command=self.goBack)
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
                entry = f"Name: {name}\nSpeciality: {speciality}\nLocation: {location}\nRatings: {ratings}\n\n"
                self.resultsText.insert(tk.END, entry)

        # Configure a tag to change the foreground color to black and increase the font size
        self.resultsText.tag_configure('black_text', foreground='black',
                                       font=('Helvetica', 16))  # Increased font size to 14
        # Apply the tag to all the text in the widget
        self.resultsText.tag_add('black_text', '1.0', tk.END)


    def goBack(self):
        self.destroy()
        self.goBackCall()
