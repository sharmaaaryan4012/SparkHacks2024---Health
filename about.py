"""
Project: Super Health App
Creators: Aaryan Sharma, Ayush Bhardwaj
SparkHacks-2024 (University of Illinois at Chicago)
"""


import tkinter as tk

class AboutPage(tk.Frame):
    def __init__(self, master, backCallback):
        super().__init__(master, bg='white')
        self.master = master
        self.backCallback = backCallback
        self.createWidgets()

    def createWidgets(self):
        descriptionText = (
            "Project: Super Health App\n"
            "Creators: Aaryan Sharma, Ayush Bhardwaj\n"
            "Event: SparkHacks-2024\n"
            "University of Illinois at Chicago\n\n"
            "This application is designed to be an all-in-one health companion.\n"
            "It provides a platform for users to manage health-related activities\n"
            "including doctor appointments, prescriptions, health reminders, and\n"
            "mindfulness exercises."
        )

        titleLabel = tk.Label(self, text="About Super Health App", bg='white', fg='black', font=('Helvetica', 18, 'bold'))
        titleLabel.pack(pady=20)

        descriptionLabel = tk.Label(self, text=descriptionText, bg='white', fg='black', font=('Helvetica', 12), justify=tk.LEFT)
        descriptionLabel.pack(pady=20, padx=20)

        backButton = tk.Button(self, text="Back", command=self.goBack)
        backButton.pack(pady=20)

    def goBack(self):
        self.destroy()
        self.backCallback()
