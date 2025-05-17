# filepath: c:\Users\Ranula\Documents\app\2232322\page7.py
#import necessary libraries
import hashlib  #Check file intergrity (MD5)
import os   #File mnagement (OS interact)
from tkinter import *    #building the GUI
import tkinter as tk
from tkinter import ttk, font, messagebox, filedialog   # For GUI components and dialogs
from PIL import  ImageTk,Image  #handling images
import threading  # For background scanning
import time  # For timing operations
import random  # For simulating detection


#Initialize page variable
thisPage = 7

#Create the main application window
root = Tk()
root.title("GuardianX Prototype > AI")
root.geometry("1270x720")
root.minsize(1270,720)
root.maxsize(1270,720)
root.configure(bg="#131314")

#Define color constants
backgroundColor = "#131314"
not_active_color = "#606060"
active_color = "#DCDCDD"
box_background = "#26262C"


def hoverMenuButtons(event,i):
    global buttonsMain
    relys = [0.4, 0.45, 0.50, 0.55, 0.45, 0.5, 0.55, 0.6, 0.65, 0.7, 0.75]
    buttonsMain[i].config(font=("Lucida Sans",16,"bold"),bg=backgroundColor, fg="#DEDEE0", activeforeground="#5A5A5B")
    buttonsMain[i].place(relx=0.07, rely=relys[i])


def leaveMenuButtons(event, i):
    global buttonsMain
    relys = [0.4, 0.45, 0.50, 0.55, 0.45, 0.5, 0.55, 0.6, 0.65, 0.7, 0.75]
    if i == 0:
        buttonsMain[i].config(font=("Lucida Sans", 12, "bold"), fg=active_color, bg=backgroundColor)
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


def calculate_md5(file_path):
    md5_hash = hashlib.md5()
    with open(file_path, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            md5_hash.update(chunk)
    return md5_hash.hexdigest()


def scan_file(file_path):
    try:
        file_hash = calculate_md5(file_path)
        is_malicious = random.random() < 0.1
        return is_malicious, file_hash
    except Exception as e:
        messagebox.showerror("Error", f"Failed to scan file: {e}")
        return False, None
    
    

def scan_action():
    file_path = filedialog.askopenfilename(title="Select a file to scan")
    if file_path:
        threading.Thread(target=lambda: scan_and_report(file_path), daemon=True).start()

#Scan box
img_scan = ImageTk.PhotoImage(Image.open("1x/scan.png"))
button_scan = Button(root,image=img_scan,bg=backgroundColor,width=300, borderwidth=0, height=370 , command=scan_action, activebackground=backgroundColor)
button_scan.place(relx=0.35, rely=0.16)


# Function to simulate virus scanning (replace with actual detection logic)
def scan_for_virus(file_path):
    # In a real antivirus, you would:
    # 1. Calculate file hash and check against known virus signatures
    # 2. Perform heuristic analysis
    # 3. Run the file in a sandbox environment
    # 4. Use machine learning models to detect suspicious behavior
    
    # For this prototype, we'll just simulate detection with random chance
    is_virus = random.random() < 0.2  # 20% chance of being "detected" for demo
    scan_time = random.uniform(0.5, 2.0)  # Simulate scan taking between 0.5-2 seconds
    time.sleep(scan_time)
    return is_virus

# Function to handle file selection and virus scanning
def open_and_scan_file():
    file_path = filedialog.askopenfilename(title="Select file to scan")
    if not file_path:
        return  # User cancelled
    
    # Show scanning progress
    progress_window = Toplevel(root)
    progress_window.title("Scanning")
    progress_window.geometry("300x100")
    progress_window.transient(root)
    
    Label(progress_window, text=f"Scanning file: {os.path.basename(file_path)}").pack(pady=10)
    progress_bar = ttk.Progressbar(progress_window, mode="indeterminate")
    progress_bar.pack(fill="x", padx=20)
    progress_bar.start()
    
    # Run scan in a separate thread to avoid freezing UI
    def run_scan():
        try:
            result = scan_for_virus(file_path)
            progress_window.destroy()
            if result:
                messagebox.warning("Scan Complete", "Threat detected! This file appears to be malicious.")
            else:
                messagebox.showinfo("Scan Complete", "No threats detected in this file.")
        except Exception as e:
            progress_window.destroy()
            messagebox.showerror("Error", f"Scan failed: {str(e)}")
    
    threading.Thread(target=run_scan, daemon=True).start()

#AI Prediction box
img_scanai = ImageTk.PhotoImage(Image.open("1x/aipredection.png"))
button_scanai = Button(root,image=img_scanai,bg=backgroundColor,width=300, borderwidth=0, height=370 , command=open_and_scan_file, activebackground=backgroundColor)
button_scanai.place(relx=0.65, rely=0.16)

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
buttonsMain[4].place(relx=0.07, rely=0.45)

buttonsMain[5] = Button(root, text="FireWall", font=("Lucida Sans",12), fg=not_active_color, bg= backgroundColor, activebackground= backgroundColor, highlightthickness=0, borderwidth=0, command=lambda: nextPage(5))
buttonsMain[5].place(relx=0.07, rely=0.5)

buttonsMain[6] = Button(root, text="Scanning", font=("Lucida Sans",12), fg=not_active_color, bg= backgroundColor, activebackground= backgroundColor, highlightthickness=0, borderwidth=0, command=lambda: nextPage(6))
buttonsMain[6].place(relx=0.07, rely=0.55)

buttonsMain[7] = Button(root, text="Threat Detection", font=("Lucida Sans",12), fg=not_active_color, bg= backgroundColor, activebackground= backgroundColor, highlightthickness=0, borderwidth=0, command=lambda: nextPage(7))
buttonsMain[7].place(relx=0.07, rely=0.6)

buttonsMain[8] = Button(root, text="Data Security", font=("Lucida Sans",12), fg=not_active_color, bg= backgroundColor, activebackground= backgroundColor, highlightthickness=0, borderwidth=0, command=lambda: nextPage(8))
buttonsMain[8].place(relx=0.07, rely=0.65)

buttonsMain[9] = Button(root, text="Parental Control", font=("Lucida Sans",12), fg=not_active_color, bg= backgroundColor, activebackground= backgroundColor, highlightthickness=0, borderwidth=0, command=lambda: nextPage(9))
buttonsMain[9].place(relx=0.07, rely=0.7)

buttonsMain[10] = Button(root, text="Quarantine", font=("Lucida Sans",12), fg=not_active_color, bg= backgroundColor, activebackground= backgroundColor, highlightthickness=0, borderwidth=0, command=lambda: nextPage(10))
buttonsMain[10].place(relx=0.07, rely=0.75)

buttonsMain[0].bind("<Enter>", lambda event, i=0: hoverMenuButtons(event, i))
buttonsMain[0].bind("<Leave>", lambda event, i=0: leaveMenuButtons(event, i))

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

root.mainloop()
