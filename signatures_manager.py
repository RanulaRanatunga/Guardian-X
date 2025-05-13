import tkinter as tk
from tkinter import ttk, messagebox, filedialog, simpledialog, scrolledtext
import json
import os
import hashlib
import time
import threading

class SignatureManager:
    def __init__(self, root):
        self.root = root
        self.root.title("GuardianX - Signature Database Manager")
        self.root.geometry("800x600")
        self.root.minsize(800, 600)
        self.root.config(bg="#131314")
        
        # Define color constants
        self.backgroundColor = "#131314"
        self.not_active_color = "#606060"
        self.active_color = "#DCDCDD"
        self.box_background = "#26262C"
        
        # Load signatures
        self.signatures = self.load_signatures()
        self.signature_categories = self.categorize_signatures()
        
        # Create GUI
        self.create_gui()
    
    def load_signatures(self):
        """Load signatures from the database file"""
        try:
            with open('signatures.json', 'r') as f:
                signatures = json.load(f)
            return signatures
        except (FileNotFoundError, json.JSONDecodeError):
            messagebox.showerror("Error", "Failed to load signature database.")
            return {}
    
    def categorize_signatures(self):
        """Categorize signatures by malware type"""
        categories = {}
        for hash_val, name in self.signatures.items():
            # Extract category from name (e.g., MalwareA.Gen -> MalwareA)
            category = name.split('.')[0] if '.' in name else "Unknown"
            if category not in categories:
                categories[category] = []
            categories[category].append((hash_val, name))
        return categories
    
    def create_gui(self):
        """Create the GUI elements"""
        # Title
        title_frame = tk.Frame(self.root, bg=self.backgroundColor)
        title_frame.pack(pady=10)
        
        title_label = tk.Label(title_frame, text="Signature Database Manager", 
                              font=("Arial", 18, "bold"), fg=self.active_color, bg=self.backgroundColor)
        title_label.pack(side=tk.LEFT, padx=10)
        
        # Stats frame
        stats_frame = tk.Frame(self.root, bg=self.box_background)
        stats_frame.pack(fill=tk.X, padx=20, pady=10)
        
        total_sigs = len(self.signatures)
        last_updated = time.strftime("%Y-%m-%d %H:%M:%S", 
                                    time.localtime(os.path.getmtime("signatures.json")))
        
        stats_label = tk.Label(stats_frame, 
                              text=f"Total Signatures: {total_sigs} | Last Updated: {last_updated}",
                              font=("Arial", 12), fg="white", bg=self.box_background)
        stats_label.pack(pady=10)
        
        # Create notebook for tabs
        notebook = ttk.Notebook(self.root)
        notebook.pack(fill=tk.BOTH, expand=True, padx=20, pady=10)
        
        # Signatures tab
        signatures_tab = tk.Frame(notebook, bg=self.backgroundColor)
        notebook.add(signatures_tab, text="Signatures")
        
        # Categories tab
        categories_tab = tk.Frame(notebook, bg=self.backgroundColor)
        notebook.add(categories_tab, text="Categories")
        
        # Updates tab
        updates_tab = tk.Frame(notebook, bg=self.backgroundColor)
        notebook.add(updates_tab, text="Updates")
        
        # Configure the signatures tab
        self.setup_signatures_tab(signatures_tab)
        
        # Configure the categories tab
        self.setup_categories_tab(categories_tab)
        
        # Configure the updates tab
        self.setup_updates_tab(updates_tab)
        
        # Button frame
        button_frame = tk.Frame(self.root, bg=self.backgroundColor)
        button_frame.pack(fill=tk.X, pady=10)
        
        add_sig_button = tk.Button(button_frame, text="Add Signature", 
                                  command=self.add_signature, bg="black", fg="white",
                                  width=15, height=2)
        add_sig_button.pack(side=tk.LEFT, padx=20)
        
        export_button = tk.Button(button_frame, text="Export Database", 
                                 command=self.export_database, bg="black", fg="white",
                                 width=15, height=2)
        export_button.pack(side=tk.LEFT, padx=20)
        
        import_button = tk.Button(button_frame, text="Import Database",
                                 command=self.import_database, bg="black", fg="white",
                                 width=15, height=2)
        import_button.pack(side=tk.LEFT, padx=20)
        
        close_button = tk.Button(button_frame, text="Close",
                               command=self.root.destroy, bg="black", fg="white",
                               width=15, height=2)
        close_button.pack(side=tk.RIGHT, padx=20)
    
    def setup_signatures_tab(self, parent):
        """Set up the signatures tab with a treeview"""
        # Search frame
        search_frame = tk.Frame(parent, bg=self.backgroundColor)
        search_frame.pack(fill=tk.X, pady=10)
        
        search_label = tk.Label(search_frame, text="Search:", 
                               font=("Arial", 10), fg="white", bg=self.backgroundColor)
        search_label.pack(side=tk.LEFT, padx=5)
        
        self.search_var = tk.StringVar()
        search_entry = tk.Entry(search_frame, textvariable=self.search_var, width=40)
        search_entry.pack(side=tk.LEFT, padx=5)
        
        search_button = tk.Button(search_frame, text="Search", 
                                command=self.search_signatures, bg="black", fg="white")
        search_button.pack(side=tk.LEFT, padx=5)
        
        clear_button = tk.Button(search_frame, text="Clear", 
                               command=lambda: (self.search_var.set(""), self.populate_signatures_tree()))
        clear_button.pack(side=tk.LEFT, padx=5)
        
        # Create treeview with scrollbar
        tree_frame = tk.Frame(parent, bg=self.backgroundColor)
        tree_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        columns = ("hash", "name")
        self.signatures_tree = ttk.Treeview(tree_frame, columns=columns, show="headings")
        self.signatures_tree.heading("hash", text="Signature Hash")
        self.signatures_tree.heading("name", text="Malware Name")
        
        self.signatures_tree.column("hash", width=350)
        self.signatures_tree.column("name", width=250)
        
        scrollbar = ttk.Scrollbar(tree_frame, orient="vertical", command=self.signatures_tree.yview)
        self.signatures_tree.configure(yscrollcommand=scrollbar.set)
        
        self.signatures_tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        # Context menu for right-click
        self.tree_context_menu = tk.Menu(self.signatures_tree, tearoff=0)
        self.tree_context_menu.add_command(label="Delete", command=self.delete_signature)
        self.tree_context_menu.add_command(label="Edit Name", command=self.edit_signature_name)
        
        self.signatures_tree.bind("<Button-3>", self.show_tree_context_menu)
        
        # Populate the treeview
        self.populate_signatures_tree()
    
    def setup_categories_tab(self, parent):
        """Set up the categories tab"""
        # Create a frame for the categories
        categories_frame = tk.Frame(parent, bg=self.backgroundColor)
        categories_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Create treeview with scrollbar
        columns = ("category", "count")
        self.categories_tree = ttk.Treeview(categories_frame, columns=columns, show="headings")
        self.categories_tree.heading("category", text="Category")
        self.categories_tree.heading("count", text="Count")
        
        self.categories_tree.column("category", width=300)
        self.categories_tree.column("count", width=100)
        
        scrollbar = ttk.Scrollbar(categories_frame, orient="vertical", command=self.categories_tree.yview)
        self.categories_tree.configure(yscrollcommand=scrollbar.set)
        
        self.categories_tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        # Populate categories tree
        for category, items in self.signature_categories.items():
            self.categories_tree.insert("", tk.END, values=(category, len(items)))
    
    def setup_updates_tab(self, parent):
        """Set up the updates tab"""
        updates_frame = tk.Frame(parent, bg=self.backgroundColor)
        updates_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Information label
        info_label = tk.Label(updates_frame, 
                             text="Check for updates to the signature database",
                             font=("Arial", 12), fg="white", bg=self.backgroundColor)
        info_label.pack(pady=10)
        
        # Update status textbox
        self.update_log = scrolledtext.ScrolledText(updates_frame, wrap=tk.WORD, 
                                                  bg="#1E1E1E", fg="white", 
                                                  width=70, height=15)
        self.update_log.pack(pady=10, fill=tk.BOTH, expand=True)
        self.update_log.insert(tk.END, "Update log will appear here...\n")
        
        # Update buttons
        button_frame = tk.Frame(updates_frame, bg=self.backgroundColor)
        button_frame.pack(fill=tk.X, pady=10)
        
        check_update_button = tk.Button(button_frame, text="Check for Updates",
                                       command=self.check_for_updates, bg="black", fg="white",
                                       width=20, height=2)
        check_update_button.pack(side=tk.LEFT, padx=10)
        
        download_button = tk.Button(button_frame, text="Download Updates",
                                   command=self.download_updates, bg="black", fg="white",
                                   width=20, height=2)
        download_button.pack(side=tk.LEFT, padx=10)
    
    def populate_signatures_tree(self):
        """Populate the signatures treeview with data"""
        # Clear existing items
        for item in self.signatures_tree.get_children():
            self.signatures_tree.delete(item)
        
        # Get search term if any
        search_term = self.search_var.get().lower()
        
        # Add signatures
        for hash_val, name in self.signatures.items():
            if search_term and search_term not in name.lower() and search_term not in hash_val.lower():
                continue
            self.signatures_tree.insert("", tk.END, values=(hash_val, name))
    
    def search_signatures(self):
        """Search for signatures based on the search term"""
        self.populate_signatures_tree()
    
    def show_tree_context_menu(self, event):
        """Show context menu on right-click in treeview"""
        iid = self.signatures_tree.identify_row(event.y)
        if iid:
            # Select the item
            self.signatures_tree.selection_set(iid)
            self.tree_context_menu.post(event.x_root, event.y_root)
    
    def delete_signature(self):
        """Delete the selected signature from the database"""
        selected = self.signatures_tree.selection()
        if not selected:
            return
        
        # Get the hash from the selected item
        hash_val = self.signatures_tree.item(selected, "values")[0]
        
        # Confirm deletion
        if messagebox.askyesno("Confirm", f"Delete signature for {self.signatures[hash_val]}?"):
            # Delete from dictionary
            del self.signatures[hash_val]
            
            # Save changes
            with open('signatures.json', 'w') as f:
                json.dump(self.signatures, f)
            
            # Remove from treeview
            self.signatures_tree.delete(selected)
            
            # Update categories
            self.signature_categories = self.categorize_signatures()
            
            # Refresh categories tab
            self.refresh_categories_tree()
    
    def edit_signature_name(self):
        """Edit the name of the selected signature"""
        selected = self.signatures_tree.selection()
        if not selected:
            return
        
        # Get the hash from the selected item
        hash_val = self.signatures_tree.item(selected, "values")[0]
        current_name = self.signatures[hash_val]
        
        # Ask for new name
        new_name = simpledialog.askstring("Edit Signature", 
                                         "Enter new name:", 
                                         initialvalue=current_name)
        
        if new_name and new_name != current_name:
            # Update dictionary
            self.signatures[hash_val] = new_name
            
            # Save changes
            with open('signatures.json', 'w') as f:
                json.dump(self.signatures, f)
            
            # Update treeview
            self.signatures_tree.item(selected, values=(hash_val, new_name))
            
            # Update categories
            self.signature_categories = self.categorize_signatures()
            
            # Refresh categories tab
            self.refresh_categories_tree()
    
    def refresh_categories_tree(self):
        """Refresh the categories treeview"""
        # Clear existing items
        for item in self.categories_tree.get_children():
            self.categories_tree.delete(item)
        
        # Add categories
        for category, items in self.signature_categories.items():
            self.categories_tree.insert("", tk.END, values=(category, len(items)))
    
    def add_signature(self):
        """Add a new signature to the database"""
        # Ask for file to hash
        file_path = filedialog.askopenfilename(title="Select File to Create Signature")
        if not file_path:
            return
        
        # Calculate hash
        try:
            hash_val = self.generate_hash(file_path)
            if not hash_val:
                messagebox.showerror("Error", "Failed to generate hash for the selected file.")
                return
        except Exception as e:
            messagebox.showerror("Error", f"Error generating hash: {str(e)}")
            return
        
        # Ask for malware name
        malware_name = simpledialog.askstring("Malware Name", "Enter a name for this malware:")
        if not malware_name:
            return
        
        # Add to signatures
        self.signatures[hash_val] = malware_name
        
        # Save changes
        with open('signatures.json', 'w') as f:
            json.dump(self.signatures, f)
        
        # Update treeview
        self.signatures_tree.insert("", tk.END, values=(hash_val, malware_name))
        
        # Update categories
        self.signature_categories = self.categorize_signatures()
        
        # Refresh categories tab
        self.refresh_categories_tree()
        
        messagebox.showinfo("Success", f"Added signature for {malware_name}")
    
    def generate_hash(self, file_path):
        """Generate SHA-256 hash for a file"""
        hash_sha256 = hashlib.sha256()
        try:
            with open(file_path, "rb") as f:
                for chunk in iter(lambda: f.read(4096), b""):
                    hash_sha256.update(chunk)
        except Exception:
            return None
        return hash_sha256.hexdigest()
    
    def export_database(self):
        """Export the signatures database to a file"""
        file_path = filedialog.asksaveasfilename(
            defaultextension=".json",
            filetypes=[("JSON files", "*.json")],
            title="Export Signature Database"
        )
        
        if file_path:
            try:
                with open(file_path, 'w') as f:
                    json.dump(self.signatures, f, indent=4)
                messagebox.showinfo("Success", "Database exported successfully!")
            except Exception as e:
                messagebox.showerror("Error", f"Failed to export database: {str(e)}")
    
    def import_database(self):
        """Import signatures from a JSON file"""
        file_path = filedialog.askopenfilename(
            defaultextension=".json",
            filetypes=[("JSON files", "*.json")],
            title="Import Signature Database"
        )
        
        if file_path:
            try:
                with open(file_path, 'r') as f:
                    imported_signatures = json.load(f)
                
                # Count new signatures
                new_count = 0
                for hash_val, name in imported_signatures.items():
                    if hash_val not in self.signatures:
                        new_count += 1
                
                # Confirm import
                if messagebox.askyesno("Confirm Import", 
                                      f"Import {len(imported_signatures)} signatures? {new_count} are new."):
                    # Merge with existing signatures
                    self.signatures.update(imported_signatures)
                    
                    # Save changes
                    with open('signatures.json', 'w') as f:
                        json.dump(self.signatures, f)
                    
                    # Update categories
                    self.signature_categories = self.categorize_signatures()
                    
                    # Refresh trees
                    self.populate_signatures_tree()
                    self.refresh_categories_tree()
                    
                    messagebox.showinfo("Success", f"Imported {len(imported_signatures)} signatures.")
            except Exception as e:
                messagebox.showerror("Error", f"Failed to import database: {str(e)}")
    
    def check_for_updates(self):
        """Check for updates to the signature database"""
        self.update_log.delete(1.0, tk.END)
        self.update_log.insert(tk.END, "Checking for updates...\n")
        
        # Simulate update check
        def check_update_thread():
            time.sleep(1)
            # Check if update file exists
            try:
                with open('updated_signatures.json', 'r') as f:
                    updated_signatures = json.load(f)
                
                # Count new signatures
                new_count = 0
                for hash_val in updated_signatures:
                    if hash_val not in self.signatures:
                        new_count += 1
                
                self.update_log.insert(tk.END, f"Found update package.\n")
                self.update_log.insert(tk.END, f"New signatures available: {new_count}\n")
                self.update_log.insert(tk.END, "Use 'Download Updates' button to apply these updates.\n")
            except FileNotFoundError:
                self.update_log.insert(tk.END, "No updates found. Signature database is up to date.\n")
            except Exception as e:
                self.update_log.insert(tk.END, f"Error checking for updates: {str(e)}\n")
        
        # Run in a separate thread to avoid blocking the UI
        threading.Thread(target=check_update_thread).start()
    
    def download_updates(self):
        """Download and apply updates to the signature database"""
        self.update_log.delete(1.0, tk.END)
        self.update_log.insert(tk.END, "Downloading and applying updates...\n")
        
        # Simulate update download
        def download_thread():
            time.sleep(1)
            try:
                with open('updated_signatures.json', 'r') as f:
                    updated_signatures = json.load(f)
                
                # Count new signatures
                new_count = 0
                for hash_val in updated_signatures:
                    if hash_val not in self.signatures:
                        new_count += 1
                
                # Update database
                self.signatures.update(updated_signatures)
                
                # Save changes
                with open('signatures.json', 'w') as f:
                    json.dump(self.signatures, f)
                
                # Update categories
                self.signature_categories = self.categorize_signatures()
                
                # Refresh trees
                self.populate_signatures_tree()
                self.refresh_categories_tree()
                
                self.update_log.insert(tk.END, f"Downloaded and applied {new_count} new signatures.\n")
                self.update_log.insert(tk.END, f"Total signatures in database: {len(self.signatures)}\n")
                self.update_log.insert(tk.END, "Update completed successfully!\n")
            except FileNotFoundError:
                self.update_log.insert(tk.END, "No update package found.\n")
                self.update_log.insert(tk.END, "Try checking for updates first or check your internet connection.\n")
            except Exception as e:
                self.update_log.insert(tk.END, f"Error applying updates: {str(e)}\n")
        
        # Run in a separate thread to avoid blocking the UI
        threading.Thread(target=download_thread).start()

if __name__ == "__main__":
    root = tk.Tk()
    app = SignatureManager(root)
    root.mainloop()
