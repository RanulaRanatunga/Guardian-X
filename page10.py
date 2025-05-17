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
    if i == 4 or i == 5 or i == 6:
        buttonsMain[i].config(font=("Lucida Sans", 12, "bold"), fg=not_active_color, bg=backgroundColor)
    elif i == 9:
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

        self.password_protected = True
        self.password = "admin123"

        self.user_profiles = {
            "Parent": {
                "restrict_web": False, 
                "time_limits": False, 
                "monitor_browsing": False, 
                "monitor_apps": False,
                "screen_time": False, 
                "device_access": False,
                "block_inappropriate": False,
                "website_filter": False,
                "monitor_social_media": False,
                "online_activity_alerts": False,
                "search_monitoring": False
            },
            "Child 1": {
                "restrict_web": True, 
                "time_limits": True, 
                "monitor_browsing": True, 
                "monitor_apps": True,
                "screen_time": True, 
                "device_access": True,
                "block_inappropriate": True,
                "website_filter": True,
                "monitor_social_media": True,
                "online_activity_alerts": True,
                "search_monitoring": True
            },
            "Child 2": {
                "restrict_web": True, 
                "time_limits": True, 
                "monitor_browsing": True, 
                "monitor_apps": True,
                "screen_time": True, 
                "device_access": True,
                "block_inappropriate": True,
                "website_filter": True,
                "monitor_social_media": True,
                "online_activity_alerts": False,
                "search_monitoring": True
            }
        }

        self.selected_profile = tk.StringVar(value="Parent")

        self.create_profile_selector()
        self.create_parental_controls_frame()
        self.create_activity_monitoring_frame()
        self.create_device_management_frame()
        self.create_ai_recommendations_frame()

        apply_button = tk.Button(root, text="Apply Changes", command=self.apply_changes,bg="black",fg="white",font=("Helvetica", 11))
        apply_button.pack(pady=20)

    def create_profile_selector(self):
        frame = tk.LabelFrame(self.root, text="Select User Profile", padx=10, pady=10,bg="#131314",fg="white",font=("Helvetica", 11))
        frame.pack(fill="x", padx=20, pady=10)
        profile_menu = ttk.Combobox(frame, textvariable=self.selected_profile, values=list(self.user_profiles.keys()),
                                    state="readonly")
        profile_menu.pack()
        profile_menu.bind("<<ComboboxSelected>>", self.load_profile_settings)
        
    def create_parental_controls_frame(self):
        self.parental_frame = tk.LabelFrame(self.root, text="Parental Controls", padx=10, pady=10,bg="#131314",fg="white",font=("Helvetica", 11))
        self.parental_frame.pack(fill="x", padx=20, pady=10)

        # Content Restriction Section
        content_frame = tk.Frame(self.parental_frame, bg="#131314")
        content_frame.pack(fill="x", padx=5, pady=5)
        
        tk.Label(content_frame, text="Content Restrictions:", bg="#131314", fg="white", font=("Helvetica", 10, "bold")).pack(anchor="w")
        
        self.restrict_web_content_var = tk.IntVar()
        restrict_web_content_cb = tk.Checkbutton(content_frame, text="Restrict Web Content",
                                                 variable=self.restrict_web_content_var,bg="#131314",fg="red",font=("Helvetica", 10))
        restrict_web_content_cb.pack(anchor="w")
        
        self.block_inappropriate_var = tk.IntVar()
        block_inappropriate_cb = tk.Checkbutton(content_frame, text="Block Inappropriate Content",
                                               variable=self.block_inappropriate_var,bg="#131314",fg="red",font=("Helvetica", 10))
        block_inappropriate_cb.pack(anchor="w")
        
        self.website_filter_var = tk.IntVar()
        website_filter_cb = tk.Checkbutton(content_frame, text="Enable Website Filter",
                                         variable=self.website_filter_var,bg="#131314",fg="red",font=("Helvetica", 10))
        website_filter_cb.pack(anchor="w")
        
        # Time Management Section
        time_frame = tk.Frame(self.parental_frame, bg="#131314")
        time_frame.pack(fill="x", padx=5, pady=5)
        
        tk.Label(time_frame, text="Time Management:", bg="#131314", fg="white", font=("Helvetica", 10, "bold")).pack(anchor="w")
        
        self.time_limits_var = tk.IntVar()
        time_limits_cb = tk.Checkbutton(time_frame, text="Set Time Limits", 
                                      variable=self.time_limits_var,bg="#131314",fg="red",font=("Helvetica", 10))
        time_limits_cb.pack(anchor="w")
        
        # Monitoring Section
        monitoring_frame = tk.Frame(self.parental_frame, bg="#131314")
        monitoring_frame.pack(fill="x", padx=5, pady=5)
        
        tk.Label(monitoring_frame, text="Online Activity Monitoring:", bg="#131314", fg="white", font=("Helvetica", 10, "bold")).pack(anchor="w")
        
        self.monitor_social_media_var = tk.IntVar()
        monitor_social_media_cb = tk.Checkbutton(monitoring_frame, text="Monitor Social Media Activity",
                                               variable=self.monitor_social_media_var,bg="#131314",fg="red",font=("Helvetica", 10))
        monitor_social_media_cb.pack(anchor="w")
        
        self.online_activity_alerts_var = tk.IntVar()
        online_activity_alerts_cb = tk.Checkbutton(monitoring_frame, text="Enable Activity Alerts",
                                                variable=self.online_activity_alerts_var,bg="#131314",fg="red",font=("Helvetica", 10))
        online_activity_alerts_cb.pack(anchor="w")
        
        self.search_monitoring_var = tk.IntVar()
        search_monitoring_cb = tk.Checkbutton(monitoring_frame, text="Monitor Search History",
                                           variable=self.search_monitoring_var,bg="#131314",fg="red",font=("Helvetica", 10))
        search_monitoring_cb.pack(anchor="w")
        
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
        
        # Create container for scrollable content
        self.ai_canvas = tk.Canvas(frame, bg="#131314", highlightthickness=0)
        self.ai_canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        
        # Add scrollbar
        ai_scrollbar = ttk.Scrollbar(frame, orient=tk.VERTICAL, command=self.ai_canvas.yview)
        ai_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
          # Configure canvas
        self.ai_canvas.configure(yscrollcommand=ai_scrollbar.set)
        self.ai_canvas.bind('<Configure>', lambda e: self.ai_canvas.configure(scrollregion=self.ai_canvas.bbox("all")))
        
        # Create frame inside canvas for buttons and content
        self.ai_content_frame = tk.Frame(self.ai_canvas, bg="#131314")
        self.ai_canvas.create_window((0, 0), window=self.ai_content_frame, anchor="nw", width=frame.winfo_width()-15)

        recommend_button = tk.Button(self.ai_content_frame, text="Get AI Recommendations", command=self.show_ai_recommendations,bg="red",fg="white",font=("Helvetica", 11,"bold"))
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
        for widget in self.ai_content_frame.winfo_children():
            if widget != self.ai_content_frame.winfo_children()[0]:  # Keep the button
                widget.destroy()
        
        recommendations = [
            "Increase browsing monitoring for Child 1",
            "Consider limiting screen time for Child 2",
            "Enable app usage monitoring for Parent",
            "Block inappropriate content for all profiles",
            "Enable website filtering for Child profiles",
            "Monitor social media activity for teenagers",
            "Enable search history monitoring for all children",
            "Set up online activity alerts for younger children",
            "Apply stricter content restrictions during school hours",
            "Implement regular device access schedules",
            "Monitor frequently visited websites"
        ]
        
        # Add recommendations to the scrollable frame
        header_label = tk.Label(self.ai_content_frame, text="AI Recommendations:", bg="#131314", fg="white", 
                               font=("Helvetica", 11, "bold"))
        header_label.pack(anchor="w", pady=(10,5))
        
        # Create a frame for recommendations with checkboxes
        rec_frame = tk.Frame(self.ai_content_frame, bg="#131314")
        rec_frame.pack(fill="x", padx=5, pady=5)
        
        # Add recommendations with checkboxes
        rec_vars = {}
        for i, rec in enumerate(recommendations):
            rec_vars[i] = tk.IntVar()
            rec_cb = tk.Checkbutton(rec_frame, text=rec, variable=rec_vars[i], 
                                    bg="#131314", fg="red", font=("Helvetica", 10),
                                    selectcolor="black", activebackground="#131314")
            rec_cb.pack(anchor="w", pady=2)
        
        # Define what happens when recommendations are applied
        def apply_ai_recommendations():
            if rec_vars[0].get(): 
                self.user_profiles["Child 1"]["monitor_browsing"] = True
            if rec_vars[1].get(): 
                self.user_profiles["Child 2"]["screen_time"] = True
            if rec_vars[2].get():
                self.user_profiles["Parent"]["monitor_apps"] = True
            if rec_vars[3].get():
                for profile in self.user_profiles:
                    self.user_profiles[profile]["block_inappropriate"] = True
            if rec_vars[4].get(): 
                self.user_profiles["Child 1"]["website_filter"] = True
                self.user_profiles["Child 2"]["website_filter"] = True
            
            self.load_profile_settings()
            
            messagebox.showinfo("AI Applied", "Selected AI recommendations have been applied to the profiles.")
        
        apply_button = tk.Button(self.ai_content_frame, text="Apply Selected Recommendations", 
                               command=apply_ai_recommendations, bg="black", fg="white", 
                               font=("Helvetica", 11))
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


nameAnti = Label(root, text="GuardianX", font=('Century Gothic',30,"bold"), bg=backgroundColor, fg=active_color, pady=0, padx=0)
nameAnti.place(relx=0.02, rely=0.08)
desAnti = Label(root, text="Prototype", font=('Century Gothic',13), bg=backgroundColor, fg="#5A5A5B", pady=0, padx=0)
desAnti.place(relx=0.02, rely=0.155)

buttonsMain = ["button_monitoring","button_security","button_update","button_task","button_license","button_firewall","button_AI","button_AIAppControl","button_AIDeviceSecurity","button_AIOptions","Protection_history"]

buttonsMain[0] = Button(root, text="Monitoring", font=("Lucida Sans",12, "bold"), fg=active_color, bg= backgroundColor, activebackground=backgroundColor, highlightthickness=0, borderwidth=0, command=lambda: nextPage(0))
buttonsMain[0].place(relx=0.07, rely=0.4)

buttonsMain[4] = Button(root, text="License", font=("Lucida Sans",12, "bold"), fg=not_active_color, bg= backgroundColor, activebackground= backgroundColor, highlightthickness=0, borderwidth=0, command=lambda: nextPage(4))
buttonsMain[4].place(relx=0.07, rely=0.45)

buttonsMain[5] = Button(root, text="FireWall", font=("Lucida Sans",12, "bold"), fg=not_active_color, bg= backgroundColor, activebackground= backgroundColor, highlightthickness=0, borderwidth=0, command=lambda: nextPage(5))
buttonsMain[5].place(relx=0.07, rely=0.5)

buttonsMain[6] = Button(root, text="Scanning", font=("Lucida Sans",12, "bold"), fg=not_active_color, bg= backgroundColor, activebackground= backgroundColor, highlightthickness=0, borderwidth=0, command=lambda: nextPage(6))
buttonsMain[6].place(relx=0.07, rely=0.55)

buttonsMain[7] = Button(root, text="Threat Detection", font=("Lucida Sans",12), fg=not_active_color, bg= backgroundColor, activebackground= backgroundColor, highlightthickness=0, borderwidth=0, command=lambda: nextPage(7))
buttonsMain[7].place(relx=0.07, rely=0.6)

buttonsMain[8] = Button(root, text="Data Security", font=("Lucida Sans",12), fg=not_active_color, bg= backgroundColor, activebackground= backgroundColor, highlightthickness=0, borderwidth=0, command=lambda: nextPage(8))
buttonsMain[8].place(relx=0.07, rely=0.65)

buttonsMain[9] = Button(root, text="Parental Control", font=("Lucida Sans",12), fg=active_color, bg= backgroundColor, activebackground= backgroundColor, highlightthickness=0, borderwidth=0, command=lambda: nextPage(9))
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

app = FamilyOptionsApp(root)
root.mainloop()