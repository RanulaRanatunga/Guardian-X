import webbrowser  
import cv2         
from tkinter import * 
import tkinter as tk
from tkinter import ttk, font
from PIL import  ImageTk,Image


thisPage = 5


root = Tk()
root.title("GuardianX Prototype > License")
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
    if i == 4:
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

#open URLs when clicked
def callback(url):
    webbrowser.open_new_tab(url)


Label(root, text="Enter activation code",background=backgroundColor, fg=active_color, font=("Lucida Sans",16, "bold"), justify=LEFT).place(relx=0.29, rely=0.14)
Label(root, text=" Activation code format: XXXXX-XXXXX-XXXXX-XXXXX.", background=backgroundColor, fg=active_color, font=("Lucida Sans",10),justify=LEFT).place(relx=0.29, rely=0.2)


link = Label(root, text=" Where can I find an activation code?", background=backgroundColor, fg="light green", font=("Lucida Sans",11,"bold"),justify=LEFT)
link.place(relx= 0.29, rely=0.25)
link.bind("<Button-1>", lambda e: callback("https://github.com/"))


e1 = tk.Entry(root,fg=active_color, bg=backgroundColor, highlightcolor=active_color, highlightthickness=1,font=("Lucida Sans",10,"bold"))
e1.place(relx= 0.3, rely=0.3, width =100, height=33)

e2 = tk.Entry(root,fg=active_color, bg=backgroundColor, highlightcolor=active_color, highlightthickness=1,font=("Lucida Sans",10,"bold"))
e2.place(relx= 0.4, rely=0.3, width =100, height=33)

e3 = tk.Entry(root,fg=active_color, bg=backgroundColor, highlightcolor=active_color, highlightthickness=1,font=("Lucida Sans",10,"bold"))
e3.place(relx= 0.5, rely=0.3, width =100, height=33)

e4 = tk.Entry(root,fg=active_color , bg=backgroundColor, highlightcolor=active_color, highlightthickness=1,font=("Lucida Sans",10,"bold"))
e4.place(relx= 0.6, rely=0.3, width =100, height=33)


Button(root, bg="dark green",borderwidth=0, fg=active_color,text="Save activation code",font=("Lucida Sans",13,"bold")).place(relx=0.3, rely=0.4,height= 40, width= 200)


Label(root, text="No activation code?",bg=backgroundColor, fg=active_color,font=("Lucida Sans",13)).place(relx=0.3, rely=0.55)
Label(root, text="If you do not have an activation code, you can\npurchase one in the online store.",bg=backgroundColor, fg=active_color,font=("Lucida Sans",10),justify=LEFT).place(relx=0.3, rely=0.6)


renew_button = Button(root, text="Renew license", bg="dark red", fg=active_color, font=("Lucida Sans",13), borderwidth=0)
renew_button.place(relx=0.3, rely=0.67)
renew_button.bind("<Button-1>", lambda e: callback("https://docs.google.com/spreadsheets/d/124MUHT96d140tM3avFDwRl64eYvPvTIv/edit?usp=sharing&ouid=108049753977338285544&rtpof=true&sd=true"))


last_img = ImageTk.PhotoImage(Image.open("1x/boxTiny.png"))
Label(image=last_img,bg=backgroundColor).place(relx = 0.72, rely =0.8)
Label(text="\n@ \"GuardianX\"\n 2024", font=("Lucida Sans",8),fg=active_color,background=backgroundColor, justify=LEFT).place(relx=0.73,rely=0.82)


nameAnti = Label(root, text="GuardianX", font=('Century Gothic',30,"bold"), bg=backgroundColor, fg=active_color, pady=0, padx=0)
nameAnti.place(relx=0.02, rely=0.08)
desAnti = Label(root, text="Prototype", font=('Century Gothic',13), bg=backgroundColor, fg="#5A5A5B", pady=0, padx=0)
desAnti.place(relx=0.02, rely=0.155)


buttonsMain = ["button_monitoring","button_security","button_update","button_task","button_license","button_firewall","button_AI","button_AIAppControl","button_AIDeviceSecurity","button_AIOptions","Protection_history"]

buttonsMain[0] = Button(root, text="Monitoring", font=("Lucida Sans",12, "bold"), fg=active_color, bg= backgroundColor, activebackground=backgroundColor, highlightthickness=0, borderwidth=0, command=lambda: nextPage(0))
buttonsMain[0].place(relx=0.07, rely=0.4)


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