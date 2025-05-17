import psutil   
from tkinter import *  
import tkinter as tk
from tkinter import ttk, font
from PIL import  ImageTk,Image 
import time
import threading
import datetime
import json
import os


thisPage = 1

root = Tk()
root.title("GuardianX Prototype > Home")
root.geometry("1270x720")
root.minsize(1270,720)
root.maxsize(1270,720)
root.configure(bg="#131314")

backgroundColor = "#131314"
not_active_color = "#606060"
active_color = "#DCDCDD"
box_background = "#26252C"

def update_label(label):
    cpu_usage = psutil.cpu_percent(interval=0.1)
    ram_usage = psutil.virtual_memory().percent

    info_text = f"CPU Usage: {cpu_usage}%\nRAM Usage: {ram_usage}%"
    label.config(text=info_text)

    root.after(300, lambda: update_label(label))

def hoverMenuButtons(event,i):
    global buttonsMain
    buttonsMain[i].config(font=("Lucida Sans",16,"bold"),bg=backgroundColor, fg="#DEDEE0", activeforeground="#5A5A5B")
    relys = [0.4, 0.45, 0.50, 0.55, 0.45, 0.5, 0.55, 0.6, 0.65, 0.7, 0.75]
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


image_frame = ImageTk.PhotoImage(Image.open("1x/Panel.png"))
main_frame = tk.Frame(root,bg="black")
main_frame.pack(side=tk.LEFT, fill=tk.Y)
main_frame.pack_propagate(FALSE)
main_frame.configure(width=275,height=720)
label = Label(main_frame, image= image_frame, borderwidth=0)
label.pack()

imgAnti = ImageTk.PhotoImage(Image.open("1x/AntiPanel.png"))


canvas = Canvas(root, bg="#131314", highlightthickness=0)
labelAnti = Label(root,fg="white",image= imgAnti, borderwidth=0)
labelAnti.pack(pady=20)
textAnit = Label(root, text="No active threats\n found", font=('Lucida Sans',27,'bold'),bg="#001C24", fg="white", justify="left")
textAnit.place(relx = 0.72, rely = 0.2, anchor = "center")
C = Canvas(root,bg="#131314",width=992, height=512.5,highlightthickness=0)
C.place(rely=0.77, relx = 0.61, anchor = "center")
boxImage= ImageTk.PhotoImage(Image.open("1x/box.png"))


labelBox = Label(root,bg="#131314",image= boxImage, borderwidth=0)
labelBox.place(rely=0.52, relx = 0.409, anchor ="center")
bigBoxImage= ImageTk.PhotoImage(Image.open("1x/bigBox.png"))



text_Info = Label(root, text="Reports",bg= box_background, fg= active_color, font=("Lucida Sans",11,"bold"))
text_Info.place(relx=0.34, rely=0.46)
report_img = ImageTk.PhotoImage(Image.open("1x/icon1.png"))
Label(root,image=report_img, bg= box_background).place(relx=0.458,rely=0.45)
info_label = Label(root, bg= box_background, fg= "#989899", font=("Lucida Sans",11,"bold"),justify=LEFT)
info_label.place(relx=0.35, rely=0.517)

update_label(info_label)


#Name of the Program
nameAnti = Label(root, text="GuardianX", font=('Century Gothic',30,"bold"), bg=backgroundColor, fg=active_color, pady=0, padx=0)
nameAnti.place(relx=0.02, rely=0.08)
desAnti = Label(root, text="Prototype", font=('Century Gothic',13), bg=backgroundColor, fg="#5A5A5B", pady=0, padx=0)
desAnti.place(relx=0.02, rely=0.155)

#Navigation Buttons
buttonsMain = ["button_monitoring","button_security","button_update","button_task","button_license","button_firewall","button_AI","button_AIAppControl","button_AIDeviceSecurity","button_AIOptions","Protection_history"]

buttonsMain[0] = Button(root, text="Monitoring", font=("Lucida Sans",12, "bold"), fg=active_color, bg= backgroundColor, activebackground=backgroundColor, highlightthickness=0, borderwidth=0, command=lambda: nextPage(0))
buttonsMain[0].place(relx=0.07, rely=0.4)


buttonsMain[4] = Button(root, text="License", font=("Lucida Sans",12), fg=not_active_color, bg= backgroundColor, activebackground= backgroundColor, highlightthickness=0, borderwidth=0, command=lambda: nextPage(4))
buttonsMain[4].place(relx=0.07, rely=0.45)

buttonsMain[5] = Button(root, text="FireWall", font=("Lucida Sans",12), fg=not_active_color, bg= backgroundColor, activebackground= backgroundColor, highlightthickness=0, borderwidth=0, command=lambda: nextPage(5))
buttonsMain[5].place(relx=0.07, rely=0.5)

buttonsMain[6] = Button(root, text="Scanning", font=("Lucida Sans",12), fg=not_active_color, bg= backgroundColor, activebackground= backgroundColor, highlightthickness=0, borderwidth=0, command=lambda: nextPage(5))
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


threat_status_var = tk.StringVar()
threat_status_var.set("Threat Monitor: Not started yet.")


threat_monitor_frame = Frame(root, bg=box_background, bd=1, relief="solid")
threat_monitor_frame.place(relx=0.34, rely=0.62, relwidth=0.32, relheight=0.19)

threat_status_label = Label(threat_monitor_frame, textvariable=threat_status_var, bg=box_background, fg=active_color, font=("Lucida Sans", 12, "bold"), anchor="w", padx=12, pady=8)
threat_status_label.pack(fill="x", pady=(6, 2))

threat_history_listbox = Listbox(threat_monitor_frame, height=5, bg=box_background, fg="white", font=("Lucida Sans", 10), bd=0, highlightthickness=0)
threat_history_listbox.pack(fill="both", expand=True, padx=12, pady=(0, 8))

threat_history = []
def periodic_threat_monitor(interval=60):
    """
    Periodically scans for threats every `interval` seconds.
    This is a simple simulation. Replace the logic in `scan_for_threats` with real threat detection as needed.
    """
    def scan_for_threats():
        detected_threats = []
        if detected_threats:
            threat_message = f"Threats detected: {detected_threats}"
        else:
            threat_message = "No threats detected."
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        dashboard_message = f"[{timestamp}] {threat_message}"
        threat_status_var.set(f"Threat Monitor: {threat_message}")
        threat_history.append(dashboard_message)
        if len(threat_history) > 10:
            threat_history.pop(0)
        def update_listbox():
            threat_history_listbox.delete(0, tk.END)
            for entry in threat_history:
                threat_history_listbox.insert(tk.END, entry)
        root.after(0, update_listbox)

    def monitor_loop():
        while True:
            scan_for_threats()
            time.sleep(interval)

    monitor_thread = threading.Thread(target=monitor_loop, daemon=True)
    monitor_thread.start()


periodic_threat_monitor(interval=300)
advanced_dashboard_frame = Frame(root, bg=box_background, bd=2, relief="ridge")
advanced_dashboard_frame.place(relx=0.68, rely=0.62, relwidth=0.29, relheight=0.19)


advanced_title = Label(advanced_dashboard_frame, text="Advanced Threat Detection", bg=box_background, fg=active_color, font=("Lucida Sans", 13, "bold"), anchor="w", padx=12, pady=6)
advanced_title.pack(fill="x")

advanced_summary_var = tk.StringVar()
advanced_summary_var.set("No suspicious activity detected.")
advanced_summary_label = Label(advanced_dashboard_frame, textvariable=advanced_summary_var, bg=box_background, fg="#F7C873", font=("Lucida Sans", 11), anchor="w", padx=12)
advanced_summary_label.pack(fill="x", pady=(0, 4))
advanced_listbox = Listbox(advanced_dashboard_frame, height=4, bg=box_background, fg="white", font=("Lucida Sans", 10), bd=0, highlightthickness=0)
advanced_listbox.pack(fill="both", expand=True, padx=12, pady=(0, 8))

advanced_history = []

 # develop by rana 5/10/2025
def advanced_threat_detection():
    """
    Simulate advanced threat detection (e.g., anomaly detection, suspicious process, etc.).
    Replace this with real logic as needed.
    """

    import random
    suspicious = random.choice([False, False, False, True])
    timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
    if suspicious:
        event = f"[{timestamp}] Suspicious process detected!"
        advanced_summary_var.set("Suspicious activity detected!")
    else:
        event = f"[{timestamp}] System normal."
        advanced_summary_var.set("No suspicious activity detected.")
    advanced_history.append(event)
    if len(advanced_history) > 8:
        advanced_history.pop(0)
    def update_advanced_listbox():
        advanced_listbox.delete(0, tk.END)
        for entry in advanced_history:
            advanced_listbox.insert(tk.END, entry)
    root.after(0, update_advanced_listbox)


def periodic_advanced_detection(interval=180):
    def loop():
        while True:
            advanced_threat_detection()
            time.sleep(interval)
    t = threading.Thread(target=loop, daemon=True)
    t.start()

periodic_advanced_detection(interval=180)
threads_monitor_frame = Frame(root, bg=box_background, bd=1, relief="solid")
threads_monitor_frame.place(relx=0.68, rely=0.83, relwidth=0.29, relheight=0.13)

threads_title = Label(threads_monitor_frame, text="Background Threads", bg=box_background, fg=active_color, font=("Lucida Sans", 12, "bold"), anchor="w", padx=12, pady=4)
threads_title.pack(fill="x")

threads_listbox = Listbox(threads_monitor_frame, height=3, bg=box_background, fg="white", font=("Lucida Sans", 10), bd=0, highlightthickness=0)
threads_listbox.pack(fill="both", expand=True, padx=12, pady=(0, 8))

def update_threads_listbox():
    threads_listbox.delete(0, tk.END)
    for t in threading.enumerate():
        status = "Alive" if t.is_alive() else "Stopped"
        threads_listbox.insert(tk.END, f"{t.name} ({status})")
    root.after(2000, update_threads_listbox) 

update_threads_listbox()

TRIAL_FILE = "trial_info.json"
TRIAL_DAYS = 5

def get_trial_info():
    if os.path.exists(TRIAL_FILE):
        try:
            with open(TRIAL_FILE, 'r') as f:
                data = json.load(f)
                start_date = datetime.datetime.strptime(data['start_date'], '%Y-%m-%d')
                return start_date
        except Exception:
            pass
    start_date = datetime.datetime.now()
    with open(TRIAL_FILE, 'w') as f:
        json.dump({'start_date': start_date.strftime('%Y-%m-%d')}, f)
    return start_date

def check_trial(root):
    start_date = get_trial_info()
    now = datetime.datetime.now()
    days_used = (now - start_date).days
    days_left = TRIAL_DAYS - days_used
    if days_left < 0:
        days_left = 0
    if days_left == 0:
        root.after(1000, lambda: tk.messagebox.showwarning("Trial Expired", "Your 5-day trial has ended. Please activate your license to continue using GuardianX."))
    return days_left

trial_days_left = check_trial(root)
root.mainloop()