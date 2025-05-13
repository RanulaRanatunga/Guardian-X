import psutil
from tkinter import *
import tkinter as tk
from tkinter import ttk, font, messagebox
from PIL import  ImageTk,Image
from tkinter import messagebox, ttk, simpledialog
from datetime import datetime
import hashlib
import os
import threading
from cryptography.fernet import Fernet
from sklearn.ensemble import RandomForestClassifier
import numpy as np
import shutil

#Initialize page variable
thisPage = 11

#Create the main application window
root = Tk()
root.title("GuardianX Prototype > Protection_History")
root.geometry("1270x720")
root.minsize(1270,720)
root.maxsize(1270,720)
root.configure(bg="#131314")

#Define color constants
backgroundColor = "#131314"
not_active_color = "#606060"
active_color = "#DCDCDD"
box_background = "#26262C"

#For the Nav buttons
def hoverMenuButtons(event,i):
    global buttonsMain
    # All buttons left aligned at relx=0.07
    relys = [0.4, 0.45, 0.50, 0.55, 0.595, 0.645, 0.695, 0.74, 0.785, 0.83, 0.875]
    buttonsMain[i].config(font=("Lucida Sans",16,"bold"),bg=backgroundColor, fg="#DEDEE0", activeforeground="#5A5A5B")
    buttonsMain[i].place(relx=0.07, rely=relys[i])

def leaveMenuButtons(event, i):
    global buttonsMain
    # All buttons left aligned at relx=0.07
    relys = [0.4, 0.45, 0.50, 0.55, 0.595, 0.645, 0.695, 0.74, 0.785, 0.83, 0.875]
    if i == 0:
        buttonsMain[i].config(font=("Lucida Sans", 12), fg=not_active_color, bg=backgroundColor)
    elif i == 5:
        buttonsMain[i].config(font=("Lucida Sans", 12, "bold"), fg=not_active_color, bg=backgroundColor)
    elif i == 10:
        buttonsMain[i].config(font=("Lucida Sans", 12), fg=active_color, bg=backgroundColor)
    else:
        buttonsMain[i].config(font=("Lucida Sans", 12), fg=not_active_color, bg=backgroundColor)
    buttonsMain[i].place(relx=0.07, rely=relys[i])

def nextPage(i):
    if i == 0 and thisPage != 1:
        root.destroy()
        import page1
    elif i == 1 and thisPage != 2:
        root.destroy()
        import page2
    elif i == 2 and thisPage != 3:
        root.destroy()
        import page3
    elif i == 3 and thisPage != 4:
        root.destroy()
        import page4
    elif i == 4 and thisPage != 5:
        root.destroy()
        import page5
    elif i == 5 and thisPage != 6:
        root.destroy()
        import page6
    elif i == 6 and thisPage != 7:
        root.destroy()
        import page7
    elif i == 7 and thisPage != 8:
        root.destroy()
        import page8
    elif i == 8 and thisPage != 9:
        root.destroy()
        import page9
    elif i == 9 and thisPage != 10:
        root.destroy()
        import page10
    elif i == 10 and thisPage != 11:
        root.destroy()
        import page11

class AntivirusApp:
    def __init__(self, root):
        self.root = root


        self.protection_history = []
        self.is_signed_in = False
        self.onedrive_linked = False
        self.current_user_role = "Guest"  # Roles: Admin, User, Guest
        self.current_language = "English"

        # UI Components
        self.create_menu()
        self.create_protection_history_frame()
        self.create_settings_frame()
        self.create_onedrive_setup_frame()
        self.create_scan_scheduler_frame()
        self.create_notifications_frame()

    def create_menu(self):
        menubar = tk.Menu(self.root)
        self.root.config(menu=menubar)

        account_menu = tk.Menu(menubar, tearoff=0)
        account_menu.add_command(label="Sign in with Microsoft", command=self.sign_in_with_microsoft)
        account_menu.add_command(label="Switch User Role", command=self.switch_user_role)
        menubar.add_cascade(label="Account", menu=account_menu)

        language_menu = tk.Menu(menubar, tearoff=0)
        language_menu.add_command(label="English", command=lambda: self.set_language("English"))
        language_menu.add_command(label="Spanish", command=lambda: self.set_language("Spanish"))
        menubar.add_cascade(label="Language", menu=language_menu)

    def create_protection_history_frame(self):
        self.history_frame = tk.LabelFrame(self.root, text="Quarantine History", padx=10, pady=10,bg="#131314",fg="white",font=("Helvetica", 11))
        self.history_frame.pack(fill="x", padx=10, pady=5)

        self.history_search_var = tk.StringVar()
        search_entry = tk.Entry(self.history_frame, textvariable=self.history_search_var,bg="#131314",fg="white",font=("Helvetica", 10))
        search_entry.pack(side="left", padx=5)

        search_button = tk.Button(self.history_frame, text="Search", command=self.search_protection_history,bg="#131314",fg="white",font=("Helvetica", 10))
        search_button.pack(side="left", padx=5)

        self.history_listbox = tk.Listbox(self.history_frame, height=5,bg="#131314",fg="white",font=("Helvetica", 10))
        self.history_listbox.pack(fill="both", padx=5, pady=5)

        self.export_button = tk.Button(self.history_frame, text="Export History", command=self.export_protection_history,bg="black",fg="white",font=("Helvetica", 10))
        self.export_button.pack(pady=5)



        self.refresh_history_button = tk.Button(self.history_frame, text="Refresh History", command=self.refresh_protection_history,bg="black",fg="white",font=("Helvetica", 10))
        self.refresh_history_button.pack(pady=5)

    def create_settings_frame(self):
        self.settings_frame = tk.LabelFrame(self.root, text="Protection Settings", padx=10, pady=10,bg="#131314",fg="white",font=("Helvetica", 11))
        self.settings_frame.pack(fill="x", padx=20, pady=10)

        self.block_potentially_unwanted_var = tk.IntVar()
        self.block_potentially_unwanted_cb = tk.Checkbutton(self.settings_frame, text="Block Potentially Unwanted Applications (PUA)", variable=self.block_potentially_unwanted_var,bg="#131314",fg="blue",font=("Helvetica", 10))
        self.block_potentially_unwanted_cb.pack(anchor="w")

        self.block_malware_var = tk.IntVar()
        self.block_malware_cb = tk.Checkbutton(self.settings_frame, text="Block Malware", variable=self.block_malware_var,bg="#131314",fg="blue",font=("Helvetica", 10))
        self.block_malware_cb.pack(anchor="w")

        self.block_ransomware_var = tk.IntVar()
        self.block_ransomware_cb = tk.Checkbutton(self.settings_frame, text="Block Ransomware", variable=self.block_ransomware_var,bg="#131314",fg="blue",font=("Helvetica", 10))
        self.block_ransomware_cb.pack(anchor="w")

        self.auto_update_var = tk.IntVar()
        self.auto_update_cb = tk.Checkbutton(self.settings_frame, text="Enable Auto-Updates", variable=self.auto_update_var,bg="#131314",fg="blue",font=("Helvetica", 10))
        self.auto_update_cb.pack(anchor="w")

        self.advanced_detection_var = tk.IntVar()
        self.advanced_detection_cb = tk.Checkbutton(self.settings_frame, text="Enable Advanced Threat Detection", variable=self.advanced_detection_var,bg="#131314",fg="blue",font=("Helvetica", 10))
        self.advanced_detection_cb.pack(anchor="w")

        save_button = tk.Button(self.settings_frame, text="Save Settings", command=self.save_protection_settings,bg="#131314",fg="white",font=("Helvetica", 10))
        save_button.pack(pady=5)

    def create_onedrive_setup_frame(self):
        self.onedrive_frame = tk.LabelFrame(self.root, text="OneDrive Setup", padx=10, pady=10,bg="#131314",fg="white",font=("Helvetica", 11))
        self.onedrive_frame.pack(fill="x", padx=20, pady=10)

        self.onedrive_status_label = tk.Label(self.onedrive_frame, text="OneDrive is not linked.",bg="#131314",fg="white",font=("Helvetica", 10))
        self.onedrive_status_label.pack(anchor="w")

        self.link_onedrive_button = tk.Button(self.onedrive_frame, text="Link OneDrive", command=self.link_onedrive,bg="#131314",fg="white",font=("Helvetica", 10))
        self.link_onedrive_button.pack(pady=5)

    def create_scan_scheduler_frame(self):
        self.scheduler_frame = tk.LabelFrame(self.root, text="Scan Scheduler", padx=10, pady=10,bg="#131314",fg="white",font=("Helvetica", 10))
        self.scheduler_frame.pack(fill="x", padx=20, pady=10)

        tk.Label(self.scheduler_frame, text="Schedule a scan:",bg="#131314",fg="white",font=("Helvetica", 10)).pack(anchor="w")

        self.scan_schedule_time = tk.StringVar()
        self.scan_schedule_time.set("00:00")
        schedule_entry = tk.Entry(self.scheduler_frame, textvariable=self.scan_schedule_time,bg="#131314",fg="white",font=("Helvetica", 10))
        schedule_entry.pack(pady=5)

        self.schedule_scan_button = tk.Button(self.scheduler_frame, text="Schedule Scan", command=self.schedule_scan,bg="#131314",fg="white",font=("Helvetica", 10))
        self.schedule_scan_button.pack(pady=5)

    def create_notifications_frame(self):
        self.notifications_frame = tk.LabelFrame(self.root, text="Notifications & Alerts", padx=10, pady=10)
        self.notifications_frame.pack(fill="x", padx=20, pady=10)

        self.notifications_var = tk.IntVar()
        self.notifications_cb = tk.Checkbutton(self.notifications_frame, text="Enable Notifications", variable=self.notifications_var)
        self.notifications_cb.pack(anchor="w")

        self.email_alerts_var = tk.IntVar()
        self.email_alerts_cb = tk.Checkbutton(self.notifications_frame, text="Enable Email Alerts", variable=self.email_alerts_var)
        self.email_alerts_cb.pack(anchor="w")

    def sign_in_with_microsoft(self):
        if not self.is_signed_in:
            # Simulating Microsoft Sign-In process
            sign_in_window = tk.Toplevel(self.root)
            sign_in_window.title("Sign In with Microsoft")
            sign_in_window.geometry("300x200")

            tk.Label(sign_in_window, text="Email:").pack(pady=5)
            email_entry = tk.Entry(sign_in_window)
            email_entry.pack(pady=5)

            tk.Label(sign_in_window, text="Password:").pack(pady=5)
            password_entry = tk.Entry(sign_in_window, show="*")
            password_entry.pack(pady=5)

            def process_sign_in():
                email = email_entry.get()
                password = password_entry.get()
                if email and password:
                    self.is_signed_in = True
                    sign_in_window.destroy()
                    messagebox.showinfo("Success", "Signed in with Microsoft successfully!")
                else:
                    messagebox.showerror("Error", "Please enter valid credentials.")

            tk.Button(sign_in_window, text="Sign In", command=process_sign_in).pack(pady=10)
        else:
            messagebox.showinfo("Info", "You are already signed in.")

    def link_onedrive(self):
        if not self.onedrive_linked:
            if self.is_signed_in:
                self.onedrive_linked = True
                self.onedrive_status_label.config(text="OneDrive is linked.")
                messagebox.showinfo("Success", "OneDrive linked successfully!")
            else:
                messagebox.showerror("Error", "Please sign in with Microsoft first.")
        else:
            messagebox.showinfo("Info", "OneDrive is already linked.")

    def save_protection_settings(self):
        settings = {
            "Block PUA": self.block_potentially_unwanted_var.get(),
            "Block Malware": self.block_malware_var.get(),
            "Block Ransomware": self.block_ransomware_var.get(),
            "Auto-Updates": self.auto_update_var.get(),
            "Advanced Detection": self.advanced_detection_var.get()
        }
        self.log_protection_history("Settings Updated", settings)
        messagebox.showinfo("Settings", "Protection settings saved successfully.")

    def schedule_scan(self):
        scheduled_time = self.scan_schedule_time.get()
        if scheduled_time:
            self.log_protection_history("Scan Scheduled", f"Scan scheduled at {scheduled_time}")
            messagebox.showinfo("Scan Scheduler", f"Scan scheduled successfully at {scheduled_time}.")
        else:
            messagebox.showerror("Error", "Please enter a valid time.")

    def log_protection_history(self, action, details):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_entry = f"{timestamp} - {action}: {details}"
        self.protection_history.append(log_entry)
        self.refresh_protection_history()

    def refresh_protection_history(self):
        self.history_listbox.delete(0, tk.END)
        for log in self.protection_history:
            self.history_listbox.insert(tk.END, log)

    def search_protection_history(self):
        search_term = self.history_search_var.get().lower()
        self.history_listbox.delete(0, tk.END)
        for log in self.protection_history:
            if search_term in log.lower():
                self.history_listbox.insert(tk.END, log)

    def export_protection_history(self):
        export_filename = f"protection_history_{datetime.now().strftime('%Y%m%d%H%M%S')}.txt"
        with open(export_filename, "w") as file:
            for log in self.protection_history:
                file.write(log + "\n")
        messagebox.showinfo("Export", f"Protection history exported to {export_filename}.")

    def switch_user_role(self):
        new_role = simpledialog.askstring("Switch User Role", "Enter role (Admin/User/Guest):")
        if new_role in ["Admin", "User", "Guest"]:
            self.current_user_role = new_role
            messagebox.showinfo("Role Changed", f"User role switched to {new_role}.")
        else:
            messagebox.showerror("Error", "Invalid role entered.")

    def set_language(self, language):
        self.current_language = language
        messagebox.showinfo("Language Changed", f"Language switched to {language}.")


image_frame = ImageTk.PhotoImage(Image.open("1x/Panel.png"))
main_frame = tk.Frame(root,bg="black")
main_frame.pack(side=tk.LEFT, fill=tk.Y)
main_frame.pack_propagate(FALSE)
main_frame.configure(width=275,height=720)
label = Label(main_frame, image= image_frame, borderwidth=0)
label.pack()

#Name of the Program
nameAnti = Label(root, text="GuardianX", font=('Century Gothic',30,"bold"), bg=backgroundColor, fg=active_color, pady=0, padx=0)
nameAnti.place(relx=0.02, rely=0.08)
desAnti = Label(root, text="Prototype", font=('Century Gothic',13), bg=backgroundColor, fg="#5A5A5B", pady=0, padx=0)
desAnti.place(relx=0.02, rely=0.155)

# Navigation Buttons
buttonsMain = [
    "button_monitoring",      # 0
    "button_security",        # 1
    "button_update",          # 2
    "button_task",            # 3
    "button_license",         # 4
    "button_firewall",        # 5
    "button_AI",              # 6
    "button_AIAppControl",    # 7
    "button_AIDeviceSecurity",# 8
    "button_AIOptions",       # 9
    "Protection_history"      # 10
]

buttonsMain[0] = Button(root, text="Monitoring",       font=("Lucida Sans",12, "bold"), fg=active_color, bg=backgroundColor, activebackground=backgroundColor, highlightthickness=0, borderwidth=0, command=lambda: nextPage(0))
buttonsMain[0].place(relx=0.07,  rely=0.40)

# buttonsMain[1] = Button(root, text="Security",         font=("Lucida Sans",12), fg=not_active_color, bg=backgroundColor, activebackground=backgroundColor, highlightthickness=0, borderwidth=0, command=lambda: nextPage(1))
# buttonsMain[1].place(relx=0.07, rely=0.45)

# buttonsMain[2] = Button(root, text="Update",           font=("Lucida Sans",12), fg=not_active_color, bg=backgroundColor, activebackground=backgroundColor, highlightthickness=0, borderwidth=0, command=lambda: nextPage(2))
# buttonsMain[2].place(relx=0.07, rely=0.50)

# buttonsMain[3] = Button(root, text="Tasks",            font=("Lucida Sans",12), fg=not_active_color, bg=backgroundColor, activebackground=backgroundColor, highlightthickness=0, borderwidth=0, command=lambda: nextPage(3))
# buttonsMain[3].place(relx=0.07, rely=0.55)

buttonsMain[4] = Button(root, text="License",           font=("Lucida Sans",12), fg=not_active_color, bg=backgroundColor, activebackground=backgroundColor, highlightthickness=0, borderwidth=0, command=lambda: nextPage(4))
buttonsMain[4].place(relx=0.07, rely=0.595)

buttonsMain[5] = Button(root, text="FireWall",          font=("Lucida Sans",12), fg=not_active_color, bg=backgroundColor, activebackground=backgroundColor, highlightthickness=0, borderwidth=0, command=lambda: nextPage(5))
buttonsMain[5].place(relx=0.07, rely=0.645)

buttonsMain[6] = Button(root, text="Scanning",          font=("Lucida Sans",12), fg=not_active_color, bg=backgroundColor, activebackground=backgroundColor, highlightthickness=0, borderwidth=0, command=lambda: nextPage(6))
buttonsMain[6].place(relx=0.07, rely=0.695)

buttonsMain[7] = Button(root, text="Threat Detection",  font=("Lucida Sans",12), fg=not_active_color, bg=backgroundColor, activebackground=backgroundColor, highlightthickness=0, borderwidth=0, command=lambda: nextPage(7))
buttonsMain[7].place(relx=0.07, rely=0.74)

buttonsMain[8] = Button(root, text="Data Security",     font=("Lucida Sans",12), fg=not_active_color, bg=backgroundColor, activebackground=backgroundColor, highlightthickness=0, borderwidth=0, command=lambda: nextPage(8))
buttonsMain[8].place(relx=0.07, rely=0.785)

buttonsMain[9] = Button(root, text="Parental Control",  font=("Lucida Sans",12), fg=not_active_color, bg=backgroundColor, activebackground=backgroundColor, highlightthickness=0, borderwidth=0, command=lambda: nextPage(9))
buttonsMain[9].place(relx=0.07, rely=0.83)

buttonsMain[10] = Button(root, text="Quarantine",       font=("Lucida Sans",12), fg=not_active_color, bg=backgroundColor, activebackground=backgroundColor, highlightthickness=0, borderwidth=0, command=lambda: nextPage(10))
buttonsMain[10].place(relx=0.07, rely=0.875)


buttonsMain[0].bind("<Enter>", lambda event, i=0: hoverMenuButtons(event, i))
buttonsMain[0].bind("<Leave>", lambda event, i=0: leaveMenuButtons(event, i))

# buttonsMain[1].bind("<Enter>", lambda event, i=1: hoverMenuButtons(event, i))
# buttonsMain[1].bind("<Leave>", lambda event, i=1: leaveMenuButtons(event, i))

# buttonsMain[2].bind("<Enter>", lambda event, i=2: hoverMenuButtons(event, i))
# buttonsMain[2].bind("<Leave>", lambda event, i=2: leaveMenuButtons(event, i))

# buttonsMain[3].bind("<Enter>", lambda event, i=3: hoverMenuButtons(event, i))
# buttonsMain[3].bind("<Leave>", lambda event, i=3: leaveMenuButtons(event, i))

buttonsMain[4].bind("<Enter>", lambda event, i=4: hoverMenuButtons(event, i))
buttonsMain[4].bind("<Leave>", lambda event, i=4: leaveMenuButtons(event, i))

buttonsMain[5].bind("<Enter>", lambda event, i=5: hoverMenuButtons(event, i))
buttonsMain[5].bind("<Leave>", lambda event, i=5: leaveMenuButtons(event, i))

buttonsMain[6].bind("<Enter>", lambda event, i=6: hoverMenuButtons(event, i))
buttonsMain[6].bind("<Leave>", lambda event, i=6: leaveMenuButtons(event, i))

buttonsMain[7].bind("<Enter>", lambda event, i=7: hoverMenuButtons(event, i))
buttonsMain[7].bind("<Leave>", lambda event, i=7: leaveMenuButtons(event, i))

buttonsMain[8].bind("<Enter>", lambda event, i=8: hoverMenuButtons(event, i))
buttonsMain[8].bind("<Leave>", lambda event, i=8: leaveMenuButtons(event, i))

buttonsMain[9].bind("<Enter>", lambda event, i=9: hoverMenuButtons(event, i))
buttonsMain[9].bind("<Leave>", lambda event, i=9: leaveMenuButtons(event, i))

buttonsMain[10].bind("<Enter>", lambda event, i=10: hoverMenuButtons(event, i))
buttonsMain[10].bind("<Leave>", lambda event, i=10: leaveMenuButtons(event, i))

app = AntivirusApp(root)
root.mainloop()
