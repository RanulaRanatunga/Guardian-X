import tkinter as tk
from tkinter import *
import tkinter as tk
from tkinter import ttk, font, messagebox
from PIL import  ImageTk,Image
from tkinter import messagebox, filedialog, scrolledtext
import hashlib
import os
import threading
from cryptography.fernet import Fernet
from sklearn.ensemble import RandomForestClassifier
import numpy as np
import shutil
import json

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


class MLModel:
    def __init__(self):
        #RandomForest is just a placeholder. In a real scenario, you'd train this model on real data.
        self.model = RandomForestClassifier()

        #Fake training data: feature vectors and labels (0 for safe, 1 for malicious)
        X_train = np.array([[100, 200, 50], [300, 100, 70], [120, 110, 30], [400, 200, 60], [150, 130, 40]])
        y_train = np.array([0, 1, 0, 1, 0])
        self.model.fit(X_train, y_train)

    def predict(self, features):
        """Predict whether a file is safe or malicious based on its features."""
        return self.model.predict([features])[0]


#Security Engine with Deep Scan, Quarantine, and System Integrity Check
class SecurityEngine:
    def __init__(self):
        self.infected_files = []
        self.quarantined_files = []
        self.encryption_key = Fernet.generate_key()
        self.cipher_suite = Fernet(self.encryption_key)
        self.ml_model = MLModel()
        self.known_signatures = self.load_known_signatures()
        self.critical_files_hashes = {}

    def load_known_signatures(self):
        #Load known malware signatures from a JSON file
        try:
            with open('signatures.json', 'r') as f:
                signatures = json.load(f)
            return signatures
        except FileNotFoundError:
            #If the signatures file doesn't exist, create a default one
            default_signatures = {
                'a' * 64: "MalwareA",
                'b' * 64: "MalwareB"
            }
            with open('signatures.json', 'w') as f:
                json.dump(default_signatures, f)
            return default_signatures

    def generate_hash(self, file_path):
        """Generates SHA-256 hash for a given file"""
        hash_sha256 = hashlib.sha256()
        try:
            with open(file_path, "rb") as f:
                for chunk in iter(lambda: f.read(4096), b""):
                    hash_sha256.update(chunk)
        except Exception as e:
            return None
        return hash_sha256.hexdigest()

    def extract_features(self, file_path):
        """Extract features for machine learning model (e.g., file size, entropy, etc.)"""
        try:
            file_size = os.path.getsize(file_path)
            entropy = self.calculate_entropy(file_path)
            num_sections = 5  # Placeholder for number of sections in a PE file
            return [file_size, entropy, num_sections]
        except Exception:
            return [0, 0, 0]

    def calculate_entropy(self, file_path):
        """Calculate the entropy of the file for heuristic analysis"""
        with open(file_path, 'rb') as f:
            data = f.read()
        if len(data) == 0:
            return 0
        entropy = 0
        for x in range(256):
            p_x = float(data.count(chr(x).encode())) / len(data)
            if p_x > 0:
                entropy += - p_x * np.log2(p_x)
        return entropy

    def scan_file(self, file_path):
        """Scans a file using signature-based and heuristic analysis"""
        file_hash = self.generate_hash(file_path)
        if file_hash and file_hash in self.known_signatures:
            self.infected_files.append(file_path)
            return f"Signature-based Threat detected: {self.known_signatures[file_hash]} in {file_path}"
        else:
            #Heuristic Analysis using ML model
            features = self.extract_features(file_path)
            prediction = self.ml_model.predict(features)
            if prediction == 1:
                self.infected_files.append(file_path)
                return f"Heuristic-based Threat detected in {file_path}"
            else:
                return f"No threat found in {file_path}"

    def deep_scan(self, directory):
        """Performs a deep scan on all files in the directory"""
        results = []
        for root, dirs, files in os.walk(directory):
            for file in files:
                file_path = os.path.join(root, file)
                result = self.scan_file(file_path)
                results.append(result)
        return "\n".join(results)

    def encrypt_file(self, file_path):
        """Encrypts a file using symmetric encryption"""
        try:
            with open(file_path, "rb") as file:
                file_data = file.read()
                encrypted_data = self.cipher_suite.encrypt(file_data)

            with open(file_path, "wb") as file:
                file.write(encrypted_data)
            return f"File encrypted: {file_path}"
        except Exception as e:
            return f"Failed to encrypt file: {file_path}"

    def decrypt_file(self, file_path):
        """Decrypts a previously encrypted file"""
        try:
            with open(file_path, "rb") as file:
                encrypted_data = file.read()
                decrypted_data = self.cipher_suite.decrypt(encrypted_data)

            with open(file_path, "wb") as file:
                file.write(decrypted_data)
            return f"File decrypted: {file_path}"
        except Exception as e:
            return f"Failed to decrypt file: {file_path}"

    def quarantine_file(self, file_path):
        """Moves an infected file to quarantine"""
        quarantine_dir = os.path.join(os.getcwd(), "quarantine")
        if not os.path.exists(quarantine_dir):
            os.makedirs(quarantine_dir)

        try:
            quarantined_path = os.path.join(quarantine_dir, os.path.basename(file_path))
            shutil.move(file_path, quarantined_path)
            self.quarantined_files.append(quarantined_path)
            return f"File quarantined: {file_path}"
        except Exception as e:
            return f"Failed to quarantine file: {file_path}"

    def add_critical_file(self, file_path):
        """Adds a file to the list of critical files to monitor"""
        file_hash = self.generate_hash(file_path)
        if file_hash:
            self.critical_files_hashes[file_path] = file_hash
            return f"File added to system integrity check: {file_path}"
        else:
            return f"Failed to add file for integrity check: {file_path}"

    def system_integrity_check(self):
        """Checks the integrity of critical system files"""
        if not self.critical_files_hashes:
            return "No critical files have been set for integrity check."
        results = []
        for file_path, original_hash in self.critical_files_hashes.items():
            if not os.path.exists(file_path):
                results.append(f"Critical file missing: {file_path}")
                continue
            current_hash = self.generate_hash(file_path)
            if current_hash != original_hash:
                results.append(f"Integrity violation detected: {file_path}")
            else:
                results.append(f"File integrity intact: {file_path}")
        return "\n".join(results)

    def update_signatures(self):
        """Simulates updating the virus signature database"""
        #Simulate fetching updated signatures from a local JSON file
        try:
            with open('updated_signatures.json', 'r') as f:
                updated_signatures = json.load(f)
            self.known_signatures.update(updated_signatures)
            # Save the combined signatures back to the main signatures file
            with open('signatures.json', 'w') as f:
                json.dump(self.known_signatures, f)
            return "Signatures successfully updated."
        except FileNotFoundError:
            return "Updated signatures file not found."

#GUI for Antivirus
class AntivirusApp:
    def __init__(self, root):
        self.root = root
        self.engine = SecurityEngine()

        #Scrolled Text for displaying output
        self.output_text = scrolledtext.ScrolledText(root, wrap=tk.WORD,bg="#131314",fg="white", width=80, height=30)
        self.output_text.pack(pady=10)

        #Frame for buttons
        self.button_frame = tk.Frame(root,bg="#131314")
        self.button_frame.pack(pady=5)

        #Buttons for actions
        self.deep_scan_button = tk.Button(self.button_frame, text="Deep Scan", command=self.deep_scan, width=25,height=2,bg="black",fg="white",font=("Helvetica", 11))
        self.deep_scan_button.grid(row=0, column=0, padx=5, pady=5)

        self.encrypt_file_button = tk.Button(self.button_frame, text="Encrypt File", command=self.encrypt_file,width=25,height=2,bg="black",fg="white",font=("Helvetica", 11))
        self.encrypt_file_button.grid(row=0, column=1, padx=5, pady=5)

        self.decrypt_file_button = tk.Button(self.button_frame, text="Decrypt File", command=self.decrypt_file,
                                             width=25,height=2,bg="black",fg="white",font=("Helvetica", 11))
        self.decrypt_file_button.grid(row=0, column=2, padx=5, pady=5)

        self.quarantine_file_button = tk.Button(self.button_frame, text="Quarantine File", command=self.quarantine_file,
                                                width=25,height=2,bg="black",fg="white",font=("Helvetica", 11))
        self.quarantine_file_button.grid(row=1, column=0, padx=5, pady=5)

        self.add_critical_file_button = tk.Button(self.button_frame, text="Add Critical File",
                                                  command=self.add_critical_file, width=25,height=2,bg="black",fg="white",font=("Helvetica", 11))
        self.add_critical_file_button.grid(row=1, column=1, padx=5, pady=5)

        self.system_integrity_check_button = tk.Button(self.button_frame, text="System Integrity Check",
                                                       command=self.system_integrity_check, width=25,height=2,bg="black",fg="white",font=("Helvetica", 11))
        self.system_integrity_check_button.grid(row=1, column=2, padx=5, pady=5)

        self.update_signatures_button = tk.Button(self.button_frame, text="Update Signatures",
                                                  command=self.update_signatures, width=25,height=2,bg="black",fg="white",font=("Helvetica", 11))
        self.update_signatures_button.grid(row=2, column=1, padx=5, pady=5)

    def output_callback(self, text):
        """Callback function to display output"""
        self.output_text.insert(tk.END, text + "\n")
        self.output_text.see(tk.END)  # Auto-scroll to the end

    def deep_scan(self):
        directory = filedialog.askdirectory()
        if directory:
            self.output_callback(f"Starting deep scan in directory: {directory}")
            threading.Thread(target=self.perform_deep_scan, args=(directory,)).start()

    def perform_deep_scan(self, directory):
        result = self.engine.deep_scan(directory)
        self.output_callback(result)
        self.output_callback("Deep scan completed.")

    def encrypt_file(self):
        file_path = filedialog.askopenfilename()
        if file_path:
            result = self.engine.encrypt_file(file_path)
            self.output_callback(result)

    def decrypt_file(self):
        file_path = filedialog.askopenfilename()
        if file_path:
            result = self.engine.decrypt_file(file_path)
            self.output_callback(result)

    def quarantine_file(self):
        file_path = filedialog.askopenfilename()
        if file_path:
            result = self.engine.quarantine_file(file_path)
            self.output_callback(result)

    def add_critical_file(self):
        file_path = filedialog.askopenfilename()
        if file_path:
            result = self.engine.add_critical_file(file_path)
            self.output_callback(result)

    def system_integrity_check(self):
        result = self.engine.system_integrity_check()
        self.output_callback(result)

    def update_signatures(self):
        result = self.engine.update_signatures()
        self.output_callback(result)

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

if __name__ == "__main__":
    #Create dummy updated signatures file for simulation
    updated_signatures = {
        'c' * 64: "MalwareC",
        'd' * 64: "MalwareD"
    }
    with open('updated_signatures.json', 'w') as f:
        json.dump(updated_signatures, f)

app = AntivirusApp(root)
root.mainloop()
