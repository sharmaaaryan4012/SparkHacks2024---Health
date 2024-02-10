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
            """Our \"super\" health app aims to aid your wellness journey by bringing together a variety of essential health services and information all in one place. \n
Just like Tata Neu(an Indian \"super\" app) offers a versatile shopping experience, our app provides personalized solutions for your health needs. From accessing telemedicine\n
services and even mental health support, our app tries to offer convenience and support for your well-being. Say hello to a healthier,happier you with our super health app!"""
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
