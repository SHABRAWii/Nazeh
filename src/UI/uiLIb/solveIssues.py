if __name__.find("uiLIb") != -1:
    import UI.uiLIb.Barcode as Barcode
    import UI.uiLIb.Finish  as Finish
    import UI.UI as UI

else:
    import Barcode as Barcode
    import Finish  as Finish
import Data_Management.AttendanceManager as AttendanceManager
import tkinter as tk
import customtkinter as ctk
import time
import random
from PIL import Image, ImageTk, ImageDraw


import importlib.util


Frame = None
def Test():
    push("800160074")
    push("800161991")
    push("800160074")
    push("800161991")
    Frame.after(7500, pop)
    Frame.after(8000, pop)
    Frame.after(8500, pop)
    Frame.after(9000, pop)

def goBack():
    Frame.place_forget()
    Barcode.Frame.place(x=0, y=0)

def show(ID):
    global Cam_Detected_output_box, QR_Detected_output_box 
    name, group, id, department, level, image_path, card_attendace, coputer_vision_attendace = AttendanceManager.fetchData(ID)
    if int(card_attendace) == 0:
        QR_Detected_output_box.configure(text='✖️',fg_color="red")
    else:
        QR_Detected_output_box.configure(text='✔️',fg_color="green")
    if int(coputer_vision_attendace) == 0:
        Cam_Detected_output_box.configure(text='✖️',fg_color="red")
    else:
        Cam_Detected_output_box.configure(text='✔️',fg_color="green")
    img = Image.open("src/Database/" + image_path)
    img = img.resize((200, 200))  # Resize the image to match the frame's dimensions
    photos[id_photo_listID] = ImageTk.PhotoImage(img)
    canvas.itemconfig(id_photo_canvasID, image=photos[-1])
    _name.configure(text=name)
    _group.configure(text=group)
    _id.configure(text=id)
    _department.configure(text=department)
    _level.configure(text=level)
    pass
photos = []
ID_has_issues = []
once = True
def push(ID):
    global once
    if once:
        once = False
        show(ID)
        return

    # Append the data to the list
    ID_has_issues.append(ID)

    # Update the listbox to display the new data
    listbox.insert(tk.END, "  -   " + str(ID))
    
    

# Function to delete the first element from the listbox
def pop():
    global ID_has_issues
    if len(ID_has_issues) == 0:
        Frame.place_forget()
        Finish.Frame.place(x = 0, y = 0)
        return
    show(ID_has_issues[0])
    # Delete the first item in the listbox
    listbox.delete(0)

    # Remove the first item from the sensor data list
    ID_has_issues.pop(0)

def attend():
    global ID_has_issues
    ID = _id._text
    # 1-csv 
    AttendanceManager.solveIssue(ID,1)
    UI.Total_Attendance_count += 1
    Barcode.change_status(UI.Total_Attendance_count, UI.computer_vision_count, UI.card_cout)
    change_status(UI.Total_Attendance_count, UI.computer_vision_count, UI.card_cout)
    Finish.change_status(UI.Total_Attendance_count, UI.computer_vision_count, UI.card_cout)
    # 2-sign
    global Cam_Detected_output_box, QR_Detected_output_box 
    Cam_Detected_output_box.configure(text='✔️',fg_color="green")
    QR_Detected_output_box.configure(text='✔️',fg_color="green")
    # Position...#Cam_Detected_output_box.place(relx=0.56, rely=0.20, anchor=tk.NW)
    # 3-pop
    Frame.after(2000 + int(time.time() - UI.start_time), pop)

    
def absence():
    global ID_has_issues
    ID = _id._text
    # 1-csv 
    AttendanceManager.solveIssue(ID, 0)
    # 2-sign
    global Cam_Detected_output_box, QR_Detected_output_box 
    Cam_Detected_output_box.configure(text='✖️',fg_color="red")
    QR_Detected_output_box.configure(text='✖️',fg_color="red")
    # Position...#QR_Detected_output_box.place(relx=0.56, rely=0.28, anchor=tk.NW)
    # 3-pop
    Frame.after(2000 + int(time.time() - UI.start_time), pop)

def change_status(Total_attendance, Computer_vision_detect, Id_detected):
    global attendance_output_box, cv_detected_output_box, id_detected_output_box, total_attendance, id_detected, computer_vision_detect
    total_attendance = Total_attendance
    computer_vision_detect = Computer_vision_detect
    id_detected = Id_detected
    attendance_output_box.configure(text=str(total_attendance))
    cv_detected_output_box.configure(text=str(computer_vision_detect))
    id_detected_output_box.configure(text=str(id_detected))
    return


def init(app, W, H):
    ID = 800160074 
    # Create a new tkinter window
    global Frame, canvas, ID_has_issues, listbox, _name, _department, _level, _id, _group, id_photo_listID, id_photo_canvasID, Cam_Detected_output_box, QR_Detected_output_box, cv_detected_output_box, id_detected_output_box, attendance_output_box, computer_vision_detect, id_detected, total_attendance

    # Create the homeFrame
    Frame = ctk.CTkFrame(master=app, width=W, height=H, )

    # make canvas
    canvas = ctk.CTkCanvas(Frame, width=W, height=H,)
    canvas.place(x=0, y=0)

    # Load the image
    img = Image.open("src/UI/assets/background3.jpg")
    img = img.resize((W, H))  # Resize the image to match the frame's dimensions

    # Create the background image label
    photos.append(ImageTk.PhotoImage(img))
    canvas.create_image(0, 0, image=photos[-1], anchor="nw")
    

    # Welcome text box
    
    # Top Section
    ##################
    total_attendance= 0
    computer_vision_detect= 0
    id_detected= 0
    ##################
    #canvas.create_text(0.3*W,0.05*H,text="Total Attendance", font=("Helvetica", 12), fill="black", anchor=tk.NW)
    attendance_label = ctk.CTkLabel(canvas, text="Total Attendance:",fg_color="#036FA7",text_color="white", width = 110)
    attendance_label.place(relx=0.45, rely=0.05, anchor=tk.W)


    
    attendance_output_box = ctk.CTkLabel(canvas, text=total_attendance,fg_color="white",text_color="black",width=80)
    attendance_output_box.place(relx=0.65, rely=0.05, anchor=tk.CENTER)
    
    cv_detected_label = ctk.CTkLabel(canvas, text="Camera Detected:",fg_color="#036FA7",text_color="white", width=110)
    cv_detected_label.place(relx=0.14, rely=0.13, anchor=tk.W)


    cv_detected_output_box = ctk.CTkLabel(canvas, text=computer_vision_detect,fg_color="white",text_color="black",width=80)
    cv_detected_output_box.place(relx=0.34, rely=0.13, anchor=tk.CENTER)

    id_detected_label = ctk.CTkLabel(canvas, text="ID-Card Detected:",fg_color="#036FA7",text_color="white", width=110)
    id_detected_label.place(relx=0.14, rely=0.05, anchor=tk.W)

    id_detected_output_box = ctk.CTkLabel(canvas, text=id_detected,fg_color="white",text_color="black",width=80)
    id_detected_output_box.place(relx=0.34, rely=0.05, anchor=tk.CENTER)


    # Middle Section
    ##################
    name_student = "Youssef El Shabrawii"
    department_student= "MTE"
    level_student = "300"
    id_student= "800161991"
    group_student = "3"
    ##################


    Cam_Detected_label = ctk.CTkLabel(canvas, text="Computer Vision detected:",fg_color="#036FA7",text_color="white", width=175, font=("Arial", 13, "bold"))
    Cam_Detected_label.place(relx=0.315, rely=0.20, anchor=tk.NW)

    Cam_Detected_output_box = ctk.CTkLabel(canvas, text='✔️',fg_color="green",text_color="white",width=27, font=("Arial", 25))
    Cam_Detected_output_box.place(relx=0.56, rely=0.20, anchor=tk.NW)

    QR_Detected_label = ctk.CTkLabel(canvas, text="ID Card detected:",fg_color="#036FA7",text_color="white",width=175)
    QR_Detected_label.place(relx=0.315, rely=0.28, anchor=tk.NW)

    QR_Detected_output_box = ctk.CTkLabel(canvas, text='✖️',fg_color="red",text_color="white",width=27, font=("Arial", 25))
    QR_Detected_output_box.place(relx=0.56, rely=0.28, anchor=tk.NW)


    student_label = ctk.CTkLabel(canvas, text="Name:  ",fg_color="#036FA7",text_color="white",width=70)
    student_label.place(relx=0.01, rely=0.6, anchor=tk.NW)

    _name = ctk.CTkLabel(canvas, text=name_student,fg_color="gray",text_color="white",width=130)
    _name.place(relx=0.10, rely=0.6, anchor=tk.NW)

    department_label = ctk.CTkLabel(canvas, text="Department/",fg_color="#036FA7",text_color="white",width=100)
    department_label.place(relx=0.37, rely=0.45, anchor=tk.CENTER)

    _department = ctk.CTkLabel(canvas, text=department_student,fg_color="gray",text_color="white",width=100)
    _department.place(relx=0.52, rely=0.45, anchor=tk.CENTER)

    level_label = ctk.CTkLabel(canvas, text="Level/",fg_color="#036FA7",text_color="white",width=100)
    level_label.place(relx=0.37, rely=0.6, anchor=tk.CENTER)

    _level = ctk.CTkLabel(canvas, text=level_student,fg_color="gray",text_color="white",width=100)
    _level.place(relx=0.52, rely=0.6, anchor=tk.CENTER)

    id_label = ctk.CTkLabel(canvas, text="ID/",fg_color="#036FA7",text_color="white",width=70)
    id_label.place(relx=0.01, rely=0.68, anchor=tk.NW)

    _id = ctk.CTkLabel(canvas, text=id_student,fg_color="gray",text_color="white",width=130)
    _id.place(relx=0.10, rely=0.68, anchor=tk.NW)

    group_label = ctk.CTkLabel(canvas, text="Group/",fg_color="#036FA7",text_color="white",width=100)
    group_label.place(relx=0.37, rely=0.75, anchor=tk.CENTER)

    _group = ctk.CTkLabel(canvas, text=group_student,fg_color="gray",text_color="white",width=100)
    _group.place(relx=0.52, rely=0.75, anchor=tk.CENTER)
    # attend_button = ctk.CTkButton(canvas, text="Attend",fg_color="green",text_color="white",width=130, font=("Arial", 15, "bold"))
    # attend_button.place(relx=0.38, rely=0.90, anchor=tk.CENTER)

    # Not_attend_button = ctk.CTkButton(canvas, text="Absence",fg_color="red",text_color="white",width=130, font=("Arial", 15, "bold"))
    # Not_attend_button.place(relx=0.58, rely=0.90, anchor=tk.CENTER)

    attend_button = ctk.CTkButton(canvas, text="Attend",fg_color="green",text_color="white",width=130, font=("Arial", 15, "bold"),command=attend)
    attend_button.place(relx=0.38, rely=0.90, anchor=tk.CENTER)

    Not_attend_button = ctk.CTkButton(canvas, text="Absence",fg_color="red",text_color="white",width=130, font=("Arial", 15, "bold"),command=absence)
    Not_attend_button.place(relx=0.58, rely=0.90, anchor=tk.CENTER)

    # Left Middle Section
    img = Image.open("src/UI/assets/nazeh.png")
    img = img.resize((200, 200))  
    photos.append(ImageTk.PhotoImage(img))
    id_photo_listID = len(photos) - 1
    id_photo_canvasID = canvas.create_image(30, 80, image=photos[-1], anchor="nw")
    
    


    

    
    ID_has_issues = []
    




    listbox = tk.Listbox(canvas, borderwidth=6, width=20, height=14, font=("Arial", 12, "bold"), fg="white", bg="#036FA7", highlightthickness=0, selectbackground="#036FA7", selectforeground="white")
    listbox.place(relx = 0.8, rely = 0.19, anchor=tk.N)
    # listbox.insert(tk.END, " ")


    # Create a button to delete first element in list 
    # next_button = ctk.CTkButton(canvas, text="Next",fg_color="#036FA7",text_color="white",command=pop)
    # next_button.place(relx = 0.8, rely = 0.84, anchor=tk.CENTER)

    #Back and Finish Buttons 
    finish_button = ctk.CTkButton(canvas, text="Finish !",fg_color="green",text_color="white", font=("Arial", 15, "bold"))
    finish_button.place(relx = 0.15, rely = 0.8, anchor=tk.CENTER)
    #Back
    back_button = ctk.CTkButton(canvas, text="Back",fg_color="red",text_color="white", font=("Arial", 15, "bold"), command=goBack)
    back_button.place(relx = 0.15, rely = 0.9, anchor=tk.CENTER)
    


if __name__ == "__main__":
    app = tk.Tk()
    app.title("Nazeh - Home Screen")
    app.geometry("800x480")
    W, H = 800, 480
    global Lwidth
    Lwidth = 150
    init(app, 800, 480)
    Frame.place(x=0, y=0)
    push(800161991)
    push(800161991)
    push(800161991)
    push(800161991)
    push(800161991)
    push(800161991)
    push(800161991)
    push(800161991)
    push(800161991)
    # pop()
    app.mainloop()