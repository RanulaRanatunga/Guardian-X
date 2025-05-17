# filepath: c:\Users\Ranula\Documents\app\2232322\page9.py
from tkinter import *
import tkinter as tk
from tkinter import ttk, font, messagebox
from PIL import  ImageTk,Image
from tkinter import messagebox, filedialog, scrolledtext
from cryptography.fernet import Fernet
from sklearn.ensemble import RandomForestClassifier

#Initialize page variable
thisPage = 9

#Create the main application window
root = Tk()
root.title("GuardianX Prototype > AI_Device_Security")
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
    relys = [0.4, 0.45, 0.50, 0.55, 0.45, 0.5, 0.55, 0.6, 0.65, 0.7, 0.75]
    buttonsMain[i].config(font=("Lucida Sans",16,"bold"),bg=backgroundColor, fg="#DEDEE0", activeforeground="#5A5A5B")
    buttonsMain[i].place(relx=0.07, rely=relys[i])


def leaveMenuButtons(event, i):
    global buttonsMain
    relys = [0.4, 0.45, 0.50, 0.55, 0.45, 0.5, 0.55, 0.6, 0.65, 0.7, 0.75]
    if i == 9:
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


class MLModel:
    def __init__(self):
        self.model = RandomForestClassifier(n_estimators=100, random_state=42)
        
    def train(self, X, y):
        self.model.fit(X, y)
        
    def predict(self, X):
        return self.model.predict(X)


class SecurityEngine:
    def __init__(self):
        self.key = Fernet.generate_key()
        self.cipher = Fernet(self.key)
        
    def encrypt_file(self, file_path):
        try:
            with open(file_path, 'rb') as file:
                data = file.read()
            
            encrypted_data = self.cipher.encrypt(data)
            
            with open(file_path + '.encrypted', 'wb') as file:
                file.write(encrypted_data)
                
            return file_path + '.encrypted'
        except Exception as e:
            return str(e)
            
    def decrypt_file(self, encrypted_file):
        try:
            with open(encrypted_file, 'rb') as file:
                encrypted_data = file.read()
                
            decrypted_data = self.cipher.decrypt(encrypted_data)
            
            output_file = encrypted_file.replace('.encrypted', '.decrypted')
            with open(output_file, 'wb') as file:
                file.write(decrypted_data)
                
            return output_file
        except Exception as e:
            return str(e)

#GUI for Antivirus
class AntivirusApp:
    def __init__(self, master):
        self.master = master
        self.security_engine = SecurityEngine()
        
        # Create the main sections
        self.create_device_security_section()
        
    def create_device_security_section(self):
        # Device Security Section
        frame = Frame(self.master, bg=backgroundColor, height=500, width=800)
        frame.place(relx=0.35, rely=0.2)
        
        Label(frame, text="Device Security", font=("Lucida Sans", 18, "bold"), 
              fg=active_color, bg=backgroundColor).grid(row=0, column=0, columnspan=2, sticky="w", pady=(0, 20))
        
        # File Encryption Section
        Label(frame, text="Secure File Encryption", font=("Lucida Sans", 14, "bold"), 
              fg=active_color, bg=backgroundColor).grid(row=1, column=0, sticky="w", pady=(10, 5))
        
        Label(frame, text="Encrypt important files with military-grade encryption", 
              font=("Lucida Sans", 10), fg="#a0a0a0", bg=backgroundColor).grid(row=2, column=0, sticky="w", padx=(20, 0))
        
        # Encrypt button
        encrypt_btn = Button(frame, text="Encrypt Files", font=("Lucida Sans", 11),
                           bg="#26252C", fg=active_color, padx=15, pady=5,
                           command=self.encrypt_file_dialog)
        encrypt_btn.grid(row=3, column=0, sticky="w", padx=(20, 0), pady=(10, 5))
        
        # Decrypt button
        decrypt_btn = Button(frame, text="Decrypt Files", font=("Lucida Sans", 11),
                           bg="#26252C", fg=active_color, padx=15, pady=5,
                           command=self.decrypt_file_dialog)
        decrypt_btn.grid(row=3, column=1, sticky="w", padx=(20, 0), pady=(10, 5))
        
        # Device Protection Section
        Label(frame, text="Device Protection", font=("Lucida Sans", 14, "bold"), 
              fg=active_color, bg=backgroundColor).grid(row=4, column=0, sticky="w", pady=(30, 5))
        
        Label(frame, text="Protect your device from unauthorized access", 
              font=("Lucida Sans", 10), fg="#a0a0a0", bg=backgroundColor).grid(row=5, column=0, sticky="w", padx=(20, 0))
        
        # USB Protection toggle
        self.usb_var = BooleanVar(value=True)
        usb_frame = Frame(frame, bg=backgroundColor)
        usb_frame.grid(row=6, column=0, sticky="w", padx=(20, 0), pady=(10, 5))
        
        Label(usb_frame, text="USB Device Protection", font=("Lucida Sans", 11),
              fg=active_color, bg=backgroundColor).pack(side=LEFT, padx=(0, 10))
        
        Checkbutton(usb_frame, variable=self.usb_var, bg=backgroundColor,
                   activebackground=backgroundColor, selectcolor=backgroundColor,
                   fg=active_color).pack(side=LEFT)
        
        # Webcam Protection toggle
        self.webcam_var = BooleanVar(value=True)
        webcam_frame = Frame(frame, bg=backgroundColor)
        webcam_frame.grid(row=7, column=0, sticky="w", padx=(20, 0), pady=(5, 5))
        
        Label(webcam_frame, text="Webcam Protection", font=("Lucida Sans", 11),
              fg=active_color, bg=backgroundColor).pack(side=LEFT, padx=(0, 10))
        
        Checkbutton(webcam_frame, variable=self.webcam_var, bg=backgroundColor,
                   activebackground=backgroundColor, selectcolor=backgroundColor,
                   fg=active_color).pack(side=LEFT)
        
        # Status display area
        self.log_area = scrolledtext.ScrolledText(frame, width=60, height=8, 
                                                font=("Courier New", 10),
                                                bg="#26252C", fg="#c0c0c0")
        self.log_area.grid(row=9, column=0, columnspan=2, sticky="ew", pady=10)
        self.log_area.insert(END, "Device Security Module Initialized.\n")
        self.log_area.insert(END, "USB Protection: Active\n")
        self.log_area.insert(END, "Webcam Protection: Active\n")
        self.log_area.insert(END, "Status: Monitoring for threats\n")
    
    def encrypt_file_dialog(self):
        file_path = filedialog.askopenfilename(
            title="Select File to Encrypt",
            filetypes=(("Text files", "*.txt"), ("All files", "*.*"))
        )
        
        if file_path:
            result = self.security_engine.encrypt_file(file_path)
            if result.endswith('.encrypted'):
                messagebox.showinfo("Success", f"File encrypted successfully: {result}")
                self.log_area.insert(END, f"Encrypted: {file_path}\n")
            else:
                messagebox.showerror("Error", f"Encryption failed: {result}")
                self.log_area.insert(END, f"Error: {result}\n")
    
    def decrypt_file_dialog(self):
        file_path = filedialog.askopenfilename(
            title="Select File to Decrypt",
            filetypes=(("Encrypted files", "*.encrypted"), ("All files", "*.*"))
        )
        
        if file_path:
            result = self.security_engine.decrypt_file(file_path)
            if not result.startswith('Error'):
                messagebox.showinfo("Success", f"File decrypted successfully: {result}")
                self.log_area.insert(END, f"Decrypted: {file_path}\n")
            else:
                messagebox.showerror("Error", f"Decryption failed: {result}")
                self.log_area.insert(END, f"Error: {result}\n")

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

app = AntivirusApp(root)
root.mainloop()
