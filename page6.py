#import necessary libraries
import psutil    #CPU and memory usage statistics
from tkinter import *   #building the GUI
import tkinter as tk
from tkinter import ttk, font, messagebox
from PIL import  ImageTk,Image  #image handling
import subprocess   #controlling the network interface

#Initialize page variable
thisPage = 6

#Create the main application window
root = Tk()
root.title("GuardianX Prototype > Firewall")
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
    if i == 5:
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

def Private_Form():
    new_form = Toplevel(root)
    new_form.title("Private Network Settings")
    new_form.geometry("600x250")
    new_form.configure(bg="lightblue")

 
    button_frame = Frame(new_form, bg="darkblue")
    button_frame.pack(expand=True)

    activate_button = Button(button_frame, text="Enable", command=activate_action1, bg="green", fg="white",
                             font=("Helvetica", 12), width=10)
    activate_button.grid(row=0, column=0, padx=20, pady=10)

    deactivate_button = Button(button_frame, text="Disable", command=deactivate_action1, bg="red", fg="white",
                               font=("Helvetica", 12), width=10)
    deactivate_button.grid(row=0, column=1, padx=20, pady=10)


def activate_action1():
    messagebox.showinfo("Activation", "The Private Network Has Been Enabled!")

def deactivate_action1():
    messagebox.showinfo("Deactivation", "The Private Network Has Been Disabled!")

def enable_private_network():
    try:
        subprocess.run('netsh interface set interface "Private Network" enabled', shell=True, check=True)
        messagebox.showinfo("Activation", "The Private Network Has Been Enabled!")
    except subprocess.CalledProcessError as e:
        messagebox.showerror("Error", f"Failed to enable the Private Network: {e}")

def disable_private_network():
    try:
        #Disable the Private Network interface (replace "Private Network" with your actual interface name)
        subprocess.run('netsh interface set interface "Private Network" disabled', shell=True, check=True)
        messagebox.showinfo("Deactivation", "The Private Network Has Been Disabled!")
    except subprocess.CalledProcessError as e:
        messagebox.showerror("Error", f"Failed to disable the Private Network: {e}")

def Domain_Form():
    new_form = Toplevel(root)
    new_form.title("Domain Network Settings")
    new_form.geometry("600x250")
    new_form.configure(bg="lightblue")

    #Create a frame for the buttons
    button_frame = Frame(new_form, bg="darkblue")
    button_frame.pack(expand=True)

    activate_button = Button(button_frame, text="Enable", command=activate_action, bg="green", fg="white",
                             font=("Helvetica", 12), width=10)
    activate_button.grid(row=0, column=0, padx=20, pady=10)

    deactivate_button = Button(button_frame, text="Disable", command=deactivate_action1, bg="red", fg="white",
                               font=("Helvetica", 12), width=10)
    deactivate_button.grid(row=0, column=1, padx=20, pady=10)

#Functions for button actions
def activate_action():
    messagebox.showinfo("Activation", "The Domain Network Has Been Enabled!")

# def deactivate_action():
    messagebox.showinfo("Deactivation", "The Domain Network Has Been Disabled!")

def activate_domain_network():
    try:
        # Enable the Domain Network interface (replace "Domain Network" with the actual interface name)
        subprocess.run('netsh interface set interface "Domain Network" enabled', shell=True, check=True)
        messagebox.showinfo("Activation", "The Domain Network Has Been Enabled!")
    except subprocess.CalledProcessError as e:
        messagebox.showerror("Error", f"Failed to enable the Domain Network: {e}")

def deactivate_domain_network():
    try:
        # Disable the Domain Network interface (replace "Domain Network" with the actual interface name)
        subprocess.run('netsh interface set interface "Domain Network" disabled', shell=True, check=True)
        messagebox.showinfo("Deactivation", "The Domain Network Has Been Disabled!")
    except subprocess.CalledProcessError as e:
        messagebox.showerror("Error", f"Failed to disable the Domain Network: {e}")

image_frame = ImageTk.PhotoImage(Image.open("1x/Panel.png"))
main_frame = tk.Frame(root,bg="black")
main_frame.pack(side=tk.LEFT, fill=tk.Y)
main_frame.pack_propagate(FALSE)
main_frame.configure(width=275,height=720)
label = Label(main_frame, image= image_frame, borderwidth=0)
label.pack()

#Private Network box
img_scan = ImageTk.PhotoImage(Image.open("1x/Private.png"))
#Label(root, image= img_scan,  borderwidth=0).place(relx= 0.34, rely=0.15)
button_scan = Button(root,image=img_scan,bg=backgroundColor,width=259, borderwidth=0, height=194 , command= Private_Form, activebackground=backgroundColor).place(relx=0.35, rely=0.16)

#Domain Network Box
img_email = ImageTk.PhotoImage(Image.open("1x/DomainN.png"))
#Label(root, image= img_scan,  borderwidth=0).place(relx= 0.34, rely=0.45)
button_email = Button(root,image=img_email,bg=backgroundColor,width=259, borderwidth=0, height=194 , command= Domain_Form, activebackground=backgroundColor).place(relx=0.35, rely=0.56)

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

root.mainloop()