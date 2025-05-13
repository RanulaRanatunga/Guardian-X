import psutil
from tkinter import *
import tkinter as tk
from tkinter import ttk, font, messagebox, simpledialog
from PIL import  ImageTk,Image

#Initialize page variable
thisPage = 10

#Create the main application window
root = Tk()
root.title("GuardianX Prototype > AI_Option")
root.geometry("1270x720")
root.minsize(1270,720)
root.maxsize(1270,720)
root.configure(bg="#131314")

#Define color constants
backgroundColor = "#131314"
not_active_color = "#606060"
active_color = "#DCDCDD"
box_background = "#26262C"


# For the Nav buttons
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
    if i == 4 or i == 5 or i == 6:
        # Keep bold for these buttons if needed
        buttonsMain[i].config(font=("Lucida Sans", 12, "bold"), fg=not_active_color, bg=backgroundColor)
    elif i == 9:
        # Special color for Parental Control
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

class FamilyOptionsApp:
    def __init__(self, root):
        self.root = root


        # Password protection for advanced settings
        self.password_protected = True
        self.password = "admin123"

        # User profiles
        self.user_profiles = {
            "Parent": {"restrict_web": False, "time_limits": False, "monitor_browsing": False, "monitor_apps": False,
                       "screen_time": False, "device_access": False},
            "Child 1": {"restrict_web": True, "time_limits": True, "monitor_browsing": True, "monitor_apps": True,
                        "screen_time": True, "device_access": True},
            "Child 2": {"restrict_web": True, "time_limits": True, "monitor_browsing": True, "monitor_apps": True,
                        "screen_time": True, "device_access": True}
        }

        self.selected_profile = tk.StringVar(value="Parent")

        # Main UI Components
        self.create_profile_selector()
        self.create_parental_controls_frame()
        self.create_activity_monitoring_frame()
        self.create_device_management_frame()
        self.create_ai_recommendations_frame()

        # Apply Changes Button
        apply_button = tk.Button(root, text="Apply Changes", command=self.apply_changes,bg="black",fg="white",font=("Helvetica", 11))
        apply_button.pack(pady=20)

    def create_profile_selector(self):
        frame = tk.LabelFrame(self.root, text="Select User Profile", padx=10, pady=10,bg="#131314",fg="white",font=("Helvetica", 11))
        frame.pack(fill="x", padx=20, pady=10)

        profile_menu = ttk.Combobox(frame, textvariable=self.selected_profile, values=list(self.user_profiles.keys(),),
                                    state="readonly")
        profile_menu.pack()
        profile_menu.bind("<<ComboboxSelected>>", self.load_profile_settings,)

    def create_parental_controls_frame(self):
        self.parental_frame = tk.LabelFrame(self.root, text="Parental Controls", padx=10, pady=10,bg="#131314",fg="white",font=("Helvetica", 11))
        self.parental_frame.pack(fill="x", padx=20, pady=10)

        self.restrict_web_content_var = tk.IntVar()
        restrict_web_content_cb = tk.Checkbutton(self.parental_frame, text="Restrict Web Content",
                                                 variable=self.restrict_web_content_var,bg="#131314",fg="red",font=("Helvetica", 10))
        restrict_web_content_cb.pack(anchor="w")

        self.time_limits_var = tk.IntVar()
        time_limits_cb = tk.Checkbutton(self.parental_frame, text="Set Time Limits", variable=self.time_limits_var,bg="#131314",fg="red",font=("Helvetica", 10))
        time_limits_cb.pack(anchor="w")

        # Button to access advanced settings
        advanced_button = tk.Button(self.parental_frame, text="Advanced Settings", command=self.check_password,bg="black",fg="white",font=("Helvetica", 11))
        advanced_button.pack(anchor="e", pady=5)

    def create_activity_monitoring_frame(self):
        self.activity_frame = tk.LabelFrame(self.root, text="Activity Monitoring", padx=10, pady=10,bg="#131314",fg="white",font=("Helvetica", 11))
        self.activity_frame.pack(fill="x", padx=20, pady=10)

        self.monitor_browsing_var = tk.IntVar()
        monitor_browsing_cb = tk.Checkbutton(self.activity_frame, text="Monitor Browsing History",
                                             variable=self.monitor_browsing_var,bg="#131314",fg="red",font=("Helvetica", 10))
        monitor_browsing_cb.pack(anchor="w")

        self.monitor_app_usage_var = tk.IntVar()
        monitor_app_usage_cb = tk.Checkbutton(self.activity_frame, text="Monitor App Usage",
                                              variable=self.monitor_app_usage_var,bg="#131314",fg="red",font=("Helvetica", 10))
        monitor_app_usage_cb.pack(anchor="w")

    def create_device_management_frame(self):
        self.device_frame = tk.LabelFrame(self.root, text="Device Management", padx=10, pady=10,bg="#131314",fg="white",font=("Helvetica", 11))
        self.device_frame.pack(fill="x", padx=20, pady=10)

        self.manage_screen_time_var = tk.IntVar()
        manage_screen_time_cb = tk.Checkbutton(self.device_frame, text="Manage Screen Time",
                                               variable=self.manage_screen_time_var,bg="#131314",fg="red",font=("Helvetica", 10))
        manage_screen_time_cb.pack(anchor="w")

        self.manage_device_access_var = tk.IntVar()
        manage_device_access_cb = tk.Checkbutton(self.device_frame, text="Manage Device Access",
                                                 variable=self.manage_device_access_var,bg="#131314",fg="red",font=("Helvetica", 10))
        manage_device_access_cb.pack(anchor="w")

    def create_ai_recommendations_frame(self):
        frame = tk.LabelFrame(self.root, text="AI-Powered Recommendations", padx=10, pady=10,bg="#131314",fg="white",font=("Helvetica", 11))
        frame.pack(fill="x", padx=20, pady=10)

        recommend_button = tk.Button(frame, text="Get AI Recommendations", command=self.show_ai_recommendations,bg="red",fg="white",font=("Helvetica", 11,"bold"))
        recommend_button.pack(pady=5)

    def load_profile_settings(self, event=None):
        profile = self.selected_profile.get()
        settings = self.user_profiles[profile]

        self.restrict_web_content_var.set(settings["restrict_web"])
        self.time_limits_var.set(settings["time_limits"])
        self.monitor_browsing_var.set(settings["monitor_browsing"])
        self.monitor_app_usage_var.set(settings["monitor_apps"])
        self.manage_screen_time_var.set(settings["screen_time"])
        self.manage_device_access_var.set(settings["device_access"])

    def save_profile_settings(self):
        profile = self.selected_profile.get()
        self.user_profiles[profile] = {
            "restrict_web": self.restrict_web_content_var.get(),
            "time_limits": self.time_limits_var.get(),
            "monitor_browsing": self.monitor_browsing_var.get(),
            "monitor_apps": self.monitor_app_usage_var.get(),
            "screen_time": self.manage_screen_time_var.get(),
            "device_access": self.manage_device_access_var.get()
        }

    def apply_changes(self):
        self.save_profile_settings()
        summary = f"Changes Applied for {self.selected_profile.get()}:\n"
        summary += f"Restrict Web Content: {'Enabled' if self.restrict_web_content_var.get() else 'Disabled'}\n"
        summary += f"Set Time Limits: {'Enabled' if self.time_limits_var.get() else 'Disabled'}\n"
        summary += f"Monitor Browsing History: {'Enabled' if self.monitor_browsing_var.get() else 'Disabled'}\n"
        summary += f"Monitor App Usage: {'Enabled' if self.monitor_app_usage_var.get() else 'Disabled'}\n"
        summary += f"Manage Screen Time: {'Enabled' if self.manage_screen_time_var.get() else 'Disabled'}\n"
        summary += f"Manage Device Access: {'Enabled' if self.manage_device_access_var.get() else 'Disabled'}"

        messagebox.showinfo("Settings Applied", summary)

    def show_ai_recommendations(self):
        recommendations = "AI Recommendations:\n"
        recommendations += "- Increase browsing monitoring for Child 1.\n"
        recommendations += "- Consider limiting screen time for Child 2.\n"
        recommendations += "- Enable app usage monitoring for Parent."

        # Advanced AI settings to customize these recommendations
        def apply_ai_recommendations():
            for profile, settings in self.user_profiles.items():
                if profile == "Child 1":
                    settings["monitor_browsing"] = True
                if profile == "Child 2":
                    settings["screen_time"] = True
                if profile == "Parent":
                    settings["monitor_apps"] = True
            messagebox.showinfo("AI Applied", "AI recommendations have been applied to the profiles.")
            ai_window.destroy()

        ai_window = tk.Toplevel(self.root)
        ai_window.title("AI-Powered Recommendations")
        ai_window.geometry("400x300")

        info_label = tk.Label(ai_window, text=recommendations, padx=10, pady=10)
        info_label.pack()

        apply_button = tk.Button(ai_window, text="Apply Recommendations", command=apply_ai_recommendations,bg="black",fg="white",font=("Helvetica", 11))
        apply_button.pack(pady=10)

    def check_password(self):
        if self.password_protected:
            pwd = simpledialog.askstring("Password", "Enter password for advanced settings:", show='*')
            if pwd == self.password:
                self.open_advanced_settings()
            else:
                messagebox.showerror("Error", "Incorrect password")
        else:
            self.open_advanced_settings()

    def open_advanced_settings(self):
        def save_advanced_settings():
            messagebox.showinfo("Advanced Settings", "Settings saved successfully!")
            advanced_window.destroy()

        advanced_window = tk.Toplevel(self.root)
        advanced_window.title("Advanced Settings")
        advanced_window.geometry("500x400")

        tab_control = ttk.Notebook(advanced_window)

        # Advanced settings for each profile
        for profile in self.user_profiles:
            frame = ttk.Frame(tab_control)
            tab_control.add(frame, text=profile)

            restrict_web_var = tk.IntVar(value=self.user_profiles[profile]["restrict_web"])
            time_limits_var = tk.IntVar(value=self.user_profiles[profile]["time_limits"])
            monitor_browsing_var = tk.IntVar(value=self.user_profiles[profile]["monitor_browsing"])
            monitor_apps_var = tk.IntVar(value=self.user_profiles[profile]["monitor_apps"])
            screen_time_var = tk.IntVar(value=self.user_profiles[profile]["screen_time"])
            device_access_var = tk.IntVar(value=self.user_profiles[profile]["device_access"])

            tk.Checkbutton(frame, text="Restrict Web Content", variable=restrict_web_var).pack(anchor="w")
            tk.Checkbutton(frame, text="Set Time Limits", variable=time_limits_var).pack(anchor="w")
            tk.Checkbutton(frame, text="Monitor Browsing History", variable=monitor_browsing_var).pack(anchor="w")
            tk.Checkbutton(frame, text="Monitor App Usage", variable=monitor_apps_var).pack(anchor="w")
            tk.Checkbutton(frame, text="Manage Screen Time", variable=screen_time_var).pack(anchor="w")
            tk.Checkbutton(frame, text="Manage Device Access", variable=device_access_var).pack(anchor="w")

            # Save settings for this profile
            def save_profile_settings():
                self.user_profiles[profile] = {
                    "restrict_web": restrict_web_var.get(),
                    "time_limits": time_limits_var.get(),
                    "monitor_browsing": monitor_browsing_var.get(),
                    "monitor_apps": monitor_apps_var.get(),
                    "screen_time": screen_time_var.get(),
                    "device_access": device_access_var.get()
                }

            save_button = tk.Button(frame, text="Save Profile Settings", command=save_profile_settings,bg="black",fg="white",font=("Helvetica", 11))
            save_button.pack(pady=10)

        tab_control.pack(expand=1, fill="both")

        save_button = tk.Button(advanced_window, text="Save All Advanced Settings", command=save_advanced_settings,bg="black",fg="white",font=("Helvetica", 11))
        save_button.pack(pady=20)


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
# buttonsMain[2].place(relx=0.07, rely=0.50)

# buttonsMain[3] = Button(root, text="Tasks", font=("Lucida Sans",12), fg=not_active_color, bg= backgroundColor, activebackground=backgroundColor, highlightthickness=0, borderwidth=0, command=lambda: nextPage(3))
# buttonsMain[3].place(relx=0.07, rely=0.55)

buttonsMain[4] = Button(root, text="License", font=("Lucida Sans",12, "bold"), fg=not_active_color, bg= backgroundColor, activebackground= backgroundColor, highlightthickness=0, borderwidth=0, command=lambda: nextPage(4))
buttonsMain[4].place(relx=0.07, rely=0.595)

buttonsMain[5] = Button(root, text="FireWall", font=("Lucida Sans",12, "bold"), fg=not_active_color, bg= backgroundColor, activebackground= backgroundColor, highlightthickness=0, borderwidth=0, command=lambda: nextPage(5))
buttonsMain[5].place(relx=0.07, rely=0.645)

buttonsMain[6] = Button(root, text="Scanning", font=("Lucida Sans",12, "bold"), fg=not_active_color, bg= backgroundColor, activebackground= backgroundColor, highlightthickness=0, borderwidth=0, command=lambda: nextPage(6))
buttonsMain[6].place(relx=0.07, rely=0.695)

buttonsMain[7] = Button(root, text="Threat Detection", font=("Lucida Sans",12), fg=not_active_color, bg= backgroundColor, activebackground= backgroundColor, highlightthickness=0, borderwidth=0, command=lambda: nextPage(7))
buttonsMain[7].place(relx=0.07, rely=0.74)

buttonsMain[8] = Button(root, text="Data Security", font=("Lucida Sans",12), fg=not_active_color, bg= backgroundColor, activebackground= backgroundColor, highlightthickness=0, borderwidth=0, command=lambda: nextPage(8))
buttonsMain[8].place(relx=0.07, rely=0.785)

buttonsMain[9] = Button(root, text="Parental Control", font=("Lucida Sans",12), fg=not_active_color, bg= backgroundColor, activebackground= backgroundColor, highlightthickness=0, borderwidth=0, command=lambda: nextPage(9))
buttonsMain[9].place(relx=0.07, rely=0.83)

buttonsMain[10] = Button(root, text="Quarantine", font=("Lucida Sans",12), fg=not_active_color, bg= backgroundColor, activebackground= backgroundColor, highlightthickness=0, borderwidth=0, command=lambda: nextPage(10))
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

app = FamilyOptionsApp(root)
root.mainloop()