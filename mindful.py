"""
Project: Super Health App
Creators: Aaryan Sharma, Ayush Bhardwaj
SparkHacks-2024 (University of Illinois at Chicago)
"""

import tkinter as tk
import sqlite3


class MindfulPage(tk.Frame):
    def __init__(self, master, goBackCall):
        super().__init__(master)
        self.master = master
        self.master.title('Mindful Space')
        self.widget()
        self.goBackCall = goBackCall
        self.pack()

    def widget(self):
        intro_label = tk.Label(self,
                               text="A tech solution that prioritizes mental health and well-being within communities.",
                               wraplength=500, justify="left")
        intro_label.pack(pady=(10, 20))

        tk.Label(self, text="Enter tags for search:").pack()
        self.search_entry = tk.Entry(self)
        self.search_entry.pack()

        self.content_var = tk.StringVar()
        self.content_var.set('book')

        tk.Radiobutton(self, text="Books/Articles", variable=self.content_var, value='book').pack(anchor=tk.W)
        tk.Radiobutton(self, text="Videos", variable=self.content_var, value='video').pack(anchor=tk.W)

        search_button = tk.Button(self, text="Search", command=self.searchContent)
        search_button.pack(pady=20)

        back_button = tk.Button(self, text="Back", command=self.goBack)
        back_button.pack(pady=20)

        self.output_label = tk.Label(self, text="", wraplength=500, justify="left")
        self.output_label.pack(pady=20)

    def searchContent (self):
        content_type = self.content_var.get()
        search_tags = self.search_entry.get()
        results = self.getContent(content_type, search_tags)

        output_text = "Results:\n\n"
        for title, url in results:
            output_text += f"Title: {title}\nURL: {url}\n\n"

        self.output_label.config(text=output_text)

    def getContent (self, content_type, search_tags):
        conn = sqlite3.connect('project.db')
        cursor = conn.cursor()

        search_query = f"%{search_tags}%"
        cursor.execute("SELECT title, url FROM mindful_space WHERE contentType=? AND tags LIKE ?", (content_type, search_query))
        results = cursor.fetchall()

        conn.close()
        return results

    def goBack(self):
        self.destroy()
        self.goBackCall()
