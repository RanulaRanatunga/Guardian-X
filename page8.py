#import necessary libraries
from tkinter import *    #building the GUI
import tkinter as tk
from tkinter import ttk, font, messagebox, scrolledtext     #Additional GUI components
from PIL import  ImageTk,Image  #handling images
import random   #For simulating random outcomes
import time     #For sleep functions in simulations
import threading        #For real-time operations in the background

#Initialize page variable
thisPage = 8

#Create the main application window
root = Tk()
root.title("GuardianX Prototype > AI_App_Control")
root.geometry("1270x720")
root.minsize(1270,720)
root.maxsize(1270,720)
root.configure(bg="#131314")

#Define color constants
backgroundColor = "#131314"
not_active_color = "#606060"
active_color = "#DCDCDD"
box_background = "#26262C"

#Handle the hover effect for navigation buttons
def hoverMenuButtons(event,i):
    global buttonsMain
    # All navigation buttons left-aligned at relx=0.07
    buttonsMain[i].config(font=("Lucida Sans",16,"bold"),bg=backgroundColor, fg="#DEDEE0", activeforeground="#5A5A5B")
    if i == 0:
        buttonsMain[i].place(relx=0.07, rely=0.4)
    elif i == 1:
        buttonsMain[i].place(relx=0.07, rely=0.45)
    elif i == 2:
        buttonsMain[i].place(relx=0.07, rely=0.50)
    elif i == 3:
        buttonsMain[i].place(relx=0.07, rely=0.55)
    elif i == 4:
        buttonsMain[i].place(relx=0.07, rely=0.595)
    elif i == 5:
        buttonsMain[i].place(relx=0.07, rely=0.645)
    elif i == 6:
        buttonsMain[i].place(relx=0.07, rely=0.695)
    elif i == 7:
        buttonsMain[i].place(relx=0.07, rely=0.74)
    elif i == 8:
        buttonsMain[i].place(relx=0.07, rely=0.785)
    elif i == 9:
        buttonsMain[i].place(relx=0.07, rely=0.83)
    elif i == 10:
        buttonsMain[i].place(relx=0.07, rely=0.875)

#Handle the unhover effect for navigation buttons
def leaveMenuButtons(event, i):
    global buttonsMain
    root.after(50)
    # All navigation buttons left-aligned at relx=0.07
    if i == 0:
        buttonsMain[i].config(font=("Lucida Sans", 12, "bold"), fg=active_color, bg=backgroundColor)
        buttonsMain[i].place(relx=0.07, rely=0.4)
    elif i == 1:
        buttonsMain[i].config(font=("Lucida Sans", 12), fg=not_active_color, bg=backgroundColor)
        buttonsMain[i].place(relx=0.07, rely=0.45)
    elif i == 2:
        buttonsMain[i].config(font=("Lucida Sans", 12), fg=not_active_color, bg=backgroundColor)
        buttonsMain[i].place(relx=0.07, rely=0.50)
    elif i == 3:
        buttonsMain[i].config(font=("Lucida Sans", 12), fg=not_active_color, bg=backgroundColor)
        buttonsMain[i].place(relx=0.07, rely=0.55)
    elif i == 4:
        buttonsMain[i].config(font=("Lucida Sans", 12), fg=not_active_color, bg=backgroundColor)
        buttonsMain[i].place(relx=0.07, rely=0.595)
    elif i == 5:
        buttonsMain[i].config(font=("Lucida Sans", 12), fg=not_active_color, bg=backgroundColor)
        buttonsMain[i].place(relx=0.07, rely=0.645)
    elif i == 6:
        buttonsMain[i].config(font=("Lucida Sans", 12), fg=not_active_color, bg=backgroundColor)
        buttonsMain[i].place(relx=0.07, rely=0.695)
    elif i == 7:
        buttonsMain[i].config(font=("Lucida Sans", 12), fg=not_active_color, bg=backgroundColor)
        buttonsMain[i].place(relx=0.07, rely=0.74)
    elif i == 8:
        buttonsMain[i].config(font=("Lucida Sans", 12), fg=not_active_color, bg=backgroundColor)
        buttonsMain[i].place(relx=0.07, rely=0.785)
    elif i == 9:
        buttonsMain[i].config(font=("Lucida Sans", 12), fg=not_active_color, bg=backgroundColor)
        buttonsMain[i].place(relx=0.07, rely=0.83)
    elif i == 10:
        buttonsMain[i].config(font=("Lucida Sans", 12), fg=not_active_color, bg=backgroundColor)
        buttonsMain[i].place(relx=0.07, rely=0.875)

#Switch to the next page by importing the relevant module
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

#Main Antivirus Application Class
class AntivirusApp:
    def __init__(self, root):
        self.root = root

        #Create a menu bar with File and Help options
        menubar = tk.Menu(self.root)
        file_menu = tk.Menu(menubar, tearoff=0)
        file_menu.add_command(label="Exit", command=self.root.quit)
        menubar.add_cascade(label="File", menu=file_menu)

        help_menu = tk.Menu(menubar, tearoff=0)
        help_menu.add_command(label="About", command=self.show_about)
        menubar.add_cascade(label="Help", menu=help_menu)

        self.root.config(menu=menubar)

        #Create a frame for main control buttons
        button_frame = tk.Frame(self.root,bg="#131314")
        button_frame.pack(pady=20)

        #Define buttons for core functionalities
        scan_button = tk.Button(button_frame, text="Scan", command=self.start_scan, width=25,height=2,bg="black",fg="white",font=("Helvetica", 11))
        scan_button.grid(row=0, column=0, padx=10,pady=10)

        update_button = tk.Button(button_frame, text="Update", command=self.update_virus_definitions, width=25,height=2,bg="black",fg="white",font=("Helvetica", 11))
        update_button.grid(row=0, column=1, padx=10)

        real_time_button = tk.Button(button_frame, text="Real-Time Protection", command=self.toggle_real_time_protection, width=25,height=2,bg="black",fg="white",font=("Helvetica", 11))
        real_time_button.grid(row=1, column=0, padx=5, pady=10)

        quarantine_button = tk.Button(button_frame, text="Quarantine", command=self.quarantine_files, width=25,height=2,bg="black",fg="white",font=("Helvetica", 11))
        quarantine_button.grid(row=1, column=1, padx=5, pady=10)

        settings_button = tk.Button(button_frame, text="Settings", command=self.open_settings, width=25,height=2,bg="black",fg="white",font=("Helvetica", 11))
        settings_button.grid(row=2, padx=5, pady=10)

        #Status label for AI operations
        self.ai_status_label = tk.Label(self.root, text="AI Status: Idle",bg="#131314",fg="white", font=("Arial", 12))
        self.ai_status_label.pack(pady=10)

        #Scrolled text area for displaying logs
        self.log_text = scrolledtext.ScrolledText(self.root, wrap=tk.WORD,bg="#131314",fg="white", width=80, height=20)
        self.log_text.pack(pady=10)

        #Attributes for real-time protection
        self.real_time_protection = False
        self.quarantined_files = []

    #Simulate AI threat detection (integrate AI model)
    def ai_threat_detection(self):
        time.sleep(2)
        return random.choice([True, False])

    #Simulate AI-based threat detection 
    def behavior_analysis(self, file):
        #Simulate behavior analysis 
        time.sleep(2)
        return random.choice([True, False])

    #Simulate scanning operation
    def start_scan(self):
        self.log_text.insert(tk.END, "Starting scan...\n")
        self.ai_status_label.config(text="AI Status: Scanning...")
        # Simulate scanning files
        for i in range(5):
            self.log_text.insert(tk.END, f"Scanning file {i+1}...\n")
            if self.ai_threat_detection():
                self.log_text.insert(tk.END, f"Threat detected in file {i+1}!\n")
                self.quarantined_files.append(f"file_{i+1}.exe")
            time.sleep(1)
        self.log_text.insert(tk.END, "Scan complete.\n")
        self.ai_status_label.config(text="AI Status: Idle")

    #Simulate updating virus definitions
    def update_virus_definitions(self):
        self.log_text.insert(tk.END, "Updating virus definitions from AI-based threat intelligence...\n")
        self.ai_status_label.config(text="AI Status: Updating...")
        time.sleep(2)
        self.log_text.insert(tk.END, "Virus definitions updated.\n")
        self.ai_status_label.config(text="AI Status: Idle")

    #Toggle real-time protection
    def toggle_real_time_protection(self):
        if self.real_time_protection:
            self.real_time_protection = False
            self.log_text.insert(tk.END, "Real-time protection disabled.\n")
            self.ai_status_label.config(text="AI Status: Idle")
        else:
            self.real_time_protection = True
            self.log_text.insert(tk.END, "Real-time protection enabled.\n")
            self.ai_status_label.config(text="AI Status: Monitoring files...")
            threading.Thread(target=self.real_time_protection_logic).start()

    def real_time_protection_logic(self):
        while self.real_time_protection:
            # Simulate monitoring a file access
            file_access = f"file_{random.randint(1, 10)}.exe"
            self.log_text.insert(tk.END, f"Monitoring {file_access}...\n")
            if self.behavior_analysis(file_access):
                self.log_text.insert(tk.END, f"Threat detected in {file_access}!\n")
                self.quarantined_files.append(file_access)
            time.sleep(3)
        self.ai_status_label.config(text="AI Status: Idle")

    #Display quarantined files
    def quarantine_files(self):
        if not self.quarantined_files:
            self.log_text.insert(tk.END, "No files in quarantine.\n")
        else:
            self.log_text.insert(tk.END, "Quarantined files:\n")
            for file in self.quarantined_files:
                self.log_text.insert(tk.END, f"- {file}\n")
            # Placeholder: Add options to restore or delete quarantined files

    def open_settings(self):
        self.log_text.insert(tk.END, "Opening settings...\n")
        # Placeholder for settings window logic

    def show_about(self):
        messagebox.showinfo("About", "AI-Powered Antivirus Software\nVersion 1.0\nUsing advanced AI techniques to detect and prevent threats.")

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

#Navigation Buttons
buttonsMain = ["button_monitoring","button_security","button_update","button_task","button_license","button_firewall","button_AI","button_AIAppControl","button_AIDeviceSecurity","button_AIOptions","Protection_history"]

buttonsMain[0] = Button(root, text="Monitoring", font=("Lucida Sans",12, "bold"), fg=active_color, bg= backgroundColor, activebackground=backgroundColor, highlightthickness=0, borderwidth=0, command=lambda: nextPage(0))
buttonsMain[0].place(relx=0.07, rely=0.4)

# buttonsMain[1] = Button(root, text="Security", font=("Lucida Sans",12), fg=not_active_color, bg= backgroundColor, activebackground=backgroundColor, highlightthickness=0, borderwidth=0, command=lambda : nextPage(1))
# buttonsMain[1].place(relx=0.075, rely=0.45)

# buttonsMain[2] = Button(root, text="Update", font=("Lucida Sans",12), fg=not_active_color, bg= backgroundColor, activebackground=backgroundColor, highlightthickness=0, borderwidth=0, command=lambda: nextPage(2))
# buttonsMain[2].place(relx=0.075, rely=0.50)

# buttonsMain[3] = Button(root, text="Tasks", font=("Lucida Sans",12), fg=not_active_color, bg= backgroundColor, activebackground=backgroundColor, highlightthickness=0, borderwidth=0, command=lambda: nextPage(3))
# buttonsMain[3].place(relx=0.078, rely=0.55)

buttonsMain[4] = Button(root, text="License", font=("Lucida Sans",12), fg=not_active_color, bg= backgroundColor, activebackground= backgroundColor, highlightthickness=0, borderwidth=0, command=lambda: nextPage(4))
buttonsMain[4].place(relx=0.07, rely=0.595)

buttonsMain[5] = Button(root, text="FireWall", font=("Lucida Sans",12), fg=not_active_color, bg= backgroundColor, activebackground= backgroundColor, highlightthickness=0, borderwidth=0, command=lambda: nextPage(5))
buttonsMain[5].place(relx=0.07, rely=0.645)

buttonsMain[6] = Button(root, text="Scanning", font=("Lucida Sans",12), fg=not_active_color, bg= backgroundColor, activebackground= backgroundColor, highlightthickness=0, borderwidth=0, command=lambda: nextPage(6))
buttonsMain[6].place(relx=0.07, rely=0.695)

buttonsMain[7] = Button(root, text="Threat Detection", font=("Lucida Sans",12), fg=not_active_color, bg= backgroundColor, activebackground= backgroundColor, highlightthickness=0, borderwidth=0, command=lambda: nextPage(7))
buttonsMain[7].place(relx=0.07, rely=0.74)

buttonsMain[8] = Button(root, text="Data Security", font=("Lucida Sans",12), fg=not_active_color, bg= backgroundColor, activebackground= backgroundColor, highlightthickness=0, borderwidth=0, command=lambda: nextPage(8))
buttonsMain[8].place(relx=0.07, rely=0.785)

buttonsMain[9] = Button(root, text="Parental Control", font=("Lucida Sans",12), fg=not_active_color, bg= backgroundColor, activebackground= backgroundColor, highlightthickness=0, borderwidth=0, command=lambda: nextPage(9))
buttonsMain[9].place(relx=0.07, rely=0.83)

buttonsMain[10] = Button(root, text="Quarantine", font=("Lucida Sans",12), fg=not_active_color, bg= backgroundColor, activebackground= backgroundColor, highlightthickness=0, borderwidth=0, command=lambda: nextPage(10))
buttonsMain[10].place(relx=0.07, rely=0.875)

# buttonsMain[0].bind("<Enter>", lambda event, i=0: hoverMenuButtons(event, i))
# buttonsMain[0].bind("<Leave>", lambda event, i=0: leaveMenuButtons(event, i))

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
