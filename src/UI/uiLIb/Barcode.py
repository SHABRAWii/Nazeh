# print(__file__)
if __name__.find("uiLIb") != -1:
    import UI.uiLIb.Home as Home
    import UI.uiLIb.solveIssues as solveIssues
    import UI.uiLIb.Finish as Finish
    import UI.UI as UI
else:
    import Home as Home
    import solveIssues as solveIssues
    import Finish as Finish

import Data_Management.AttendanceManager as AttendanceManager
from PIL import Image, ImageTk, ImageDraw
import tkinter as tk
import customtkinter as ctk
import datetime
import time

def Test():
    # Pass
    Frame.after(3500, set_not_finished, "Youssef El Shabrawii", "3", "800161991", "MTE", "300", "assets/Youssef.jpg", "800161991")
    Frame.after(5000, set_finished)
    Frame.after(6500, goSolveIssues)
def finish():
    goSolveIssues()
def set_finished():
    img = Image.open("src/UI/assets/nazeh.png")
    img = img.resize((200, 200))  # Resize the image to match the frame's dimensions
    photos[id_photo_listID] = ImageTk.PhotoImage(img)
    canvas.itemconfig(id_photo_canvasID, image=photos[-1])
    state_label.configure(text="=> You can Scan ID now ^_^ <=",fg_color = "Green", width = 450, height=50)
    _name.configure(text="------- -------")
    _group.configure(text="-")
    _id.configure(text="---------")
    _department.configure(text="---")
    _level.configure(text="---")
    pass
def set_not_finished(name, group, id, department, level, image_path, card_attendace):
    
    state_label.configure(text="=> Data Processing... Don't SCAN !! <=",fg_color = "Red", width = 450, height=50)
    img = Image.open('src/Database/'+image_path)
    img = img.resize((200, 200))  # Resize the image to match the frame's dimensions
    photos[id_photo_listID] = ImageTk.PhotoImage(img)
    canvas.itemconfig(id_photo_canvasID, image=photos[-1])
    _name.configure(text=name)
    _group.configure(text=group)
    _id.configure(text=id)
    _department.configure(text=department)
    _level.configure(text=level)
    _id_detected.configure(text=card_attendace)
    Frame.after(2000 + int(time.time() - UI.start_time), set_finished)
    # set_finished()
    return
def set_not_finished_again():
    
    state_label.configure(text="=> Data Processing... Don't SCAN !! <=",fg_color = "Red", width = 450, height=50)
    img = Image.open('src/UI/assets/nazeh.png')
    img = img.resize((200, 200))  # Resize the image to match the frame's dimensions
    photos[id_photo_listID] = ImageTk.PhotoImage(img)
    canvas.itemconfig(id_photo_canvasID, image=photos[-1])
    _name.configure(text="Already Scanned")
    _group.configure(text="Already Scanned")
    _id.configure(text="Already Scanned")
    _department.configure(text="Already Scanned")
    _level.configure(text="Already Scanned")
    Frame.after(2000 + int(time.time() - UI.start_time), set_finished)
    # set_finished()
    return
def goSolveIssues():
    IDs = AttendanceManager.Conflict_Linear_Search()
    if len(IDs) == 0:
        Frame.place_forget()
        Finish.Frame.place(x=0, y=0)
    else:
        for ID in IDs:
            # print(str(ID) + " JO")
            solveIssues.push(ID)
        Frame.place_forget()
        solveIssues.Frame.place(x=0, y=0)
    # pass
def goHome():
    Frame.place_forget()
    Home.Frame.place(x=0, y=0)
    
def w2_open_fourth_window():
    pass
    # window2.destroy()
    # WINDOW4.w4_open_fourth_window()    

def update_datetime():
    # Get the current date and time
    current_datetime = datetime.datetime.now()

    # Extract the date and time components
    current_date = current_datetime.date()
    current_time = current_datetime.time().strftime("%I:%M %p")


    # Check if there is a change in the date or time
    if current_date != date_label.current_date or current_time != time_label.current_time:
        # Update the label text with the current date and time
        date_label.configure(text=f"Date: {current_date}")
        time_label.configure(text=f"Time: {current_time}")
        date_label.current_date = current_date
        time_label.current_time = current_time

    # Schedule the next update after 1 second (1000 milliseconds)
    date_label.after(1000, update_datetime)

photos = []
def change_status(Total_Attendance, Computer_Vision_Detect, ID_Detected):
    global total_attendance, computer_vision_detect, id_detected
    total_attendance = Total_Attendance
    computer_vision_detect = Computer_Vision_Detect
    id_detected = ID_Detected
    _total.configure(text=total_attendance)
    _computer_vision.configure(text=computer_vision_detect)
    _id_detected.configure(text=id_detected)
    pass
def init(app, W, H):
    
    # Create a new tkinter window
    global Frame, canvas, date_label, time_label, state_label, id_photo_listID, id_photo_canvasID, total_attendance, computer_vision_detect, id_detected, _name, _id, _level, _department, _group, _id_detected, _total, _computer_vision, _id_detected, total_attendance, computer_vision_detect, id_detected
    
    # Create the homeFrame
    Frame = ctk.CTkFrame(master=app, width=W, height=H )
    # Frame.place(x=0, y=0)
    
    # make canvas
    canvas = ctk.CTkCanvas(Frame, width=W, height=H)
    canvas.place(x=0, y=0)


    # Load the image
    img = Image.open("src/UI/assets/background3.jpg")
    img = img.resize((W, H))  # Resize the image to match the frame's dimensions

    # Create the background image label
    photos.append(ImageTk.PhotoImage(img))
    canvas.create_image(0, 0, image=photos[-1], anchor="nw")
    
    # Left Top Section
    ##############
    subject = 'Signal Processing'
    ##############

    
    subject_label = ctk.CTkLabel(canvas, text="Subject/" + subject,fg_color = "#036FA7", width = 200, text_color="white")
    subject_label.place(relx=0.16, rely=0.1, anchor=tk.W)

    date_label = ctk.CTkLabel(canvas, text="Date/",fg_color = "#036FA7", width = 150, text_color="white")
    date_label.place(relx=0.5, rely=0.1, anchor=tk.W)
    date_label.current_date = None
    

    
    time_label = ctk.CTkLabel(canvas, text="Time/",fg_color = "#036FA7", width = 150, text_color="white")
    time_label.place(relx=0.8, rely=0.1, anchor=tk.W)
    time_label.current_time = None

    # Start the initial update
    update_datetime()
    
    state_label = ctk.CTkLabel(canvas, text="=> You can Scan ID now ^_^ <=",fg_color = "Green", width = 450, height=50, text_color="white", font=("Helvetica", 30, "bold"), corner_radius=10)
    state_label.place(relx=0.5, rely=0.2, anchor=tk.CENTER)
    
    # Right Middle Section
    ##################
    total_attendance= 0
    computer_vision_detect= 0
    id_detected= 0
    ##################
    
    attendance_label  = ctk.CTkLabel(canvas, text="Total Attendance:",fg_color = "#036FA7", width = 150, text_color="white")
    attendance_label.place(relx=0.78, rely=0.3, anchor=tk.CENTER)

    _total = ctk.CTkLabel(canvas, text=total_attendance,fg_color = "Gray", width = 80, text_color="white", bg_color="transparent", corner_radius= 5)
    _total.place(relx=0.94, rely=0.3, anchor=tk.CENTER)
    
    cv_detected_label = ctk.CTkLabel(canvas, text="Camera Detected:",fg_color = "#036FA7", width = 150, text_color="white")
    cv_detected_label.place(relx=0.78, rely=0.4, anchor=tk.CENTER)

    
    _computer_vision = ctk.CTkLabel(canvas, text=computer_vision_detect,fg_color = "Gray", width = 80, text_color="white", bg_color="transparent", corner_radius= 5)
    _computer_vision.place(relx=0.94, rely=0.4, anchor=tk.CENTER)
    
    id_detected_label = ctk.CTkLabel(canvas, text="ID-Card Detected:",fg_color ="#036FA7", width = 150, text_color="white")
    id_detected_label.place(relx=0.78, rely=0.5, anchor=tk.CENTER)

    
    _id_detected = ctk.CTkLabel(canvas, text=id_detected,fg_color = "Gray", width = 80, text_color="white", bg_color="transparent", corner_radius= 5)
    _id_detected.place(relx=0.94, rely=0.5, anchor=tk.CENTER)
    
    # Middle Section
    ##################
    name_student = '------- -------'
    department_student= "---"
    level_student = "---"
    id_student= "---------"
    group_student = "-"
    ##################


    student_label = ctk.CTkLabel(canvas, text="Student Name:",fg_color = "#036FA7", width = 150, text_color="white")
    #student_label = tk.Label(window2, text="Student Name:")
    student_label.place(relx=0.38, rely=0.3, anchor=tk.CENTER)

    _name = ctk.CTkLabel(canvas, text=name_student,fg_color = "Gray", width = 150, text_color="white", bg_color="transparent", corner_radius= 5)
    _name.place(relx=0.58, rely=0.3, anchor=tk.CENTER)

    department_label = ctk.CTkLabel(canvas, text="Department",fg_color = "#036FA7", width = 150, text_color="white")
    #department_label = tk.Label(window2, text="Department")
    department_label.place(relx=0.38, rely=0.4, anchor=tk.CENTER)

    _department = ctk.CTkLabel(canvas, text=department_student,fg_color = "Gray", width = 150, text_color="white", bg_color="transparent", corner_radius= 5)
    _department.place(relx=0.58, rely=0.4, anchor=tk.CENTER)

    level_label = ctk.CTkLabel(canvas, text="Level/",fg_color = "#036FA7", width = 150, text_color="white")
    #level_label = tk.Label(window2, text="Level/")
    level_label.place(relx=0.38, rely=0.5, anchor=tk.CENTER)

    _level = ctk.CTkLabel(canvas, text=level_student,fg_color = "Gray", width = 150, text_color="white", bg_color="transparent", corner_radius= 5)
    _level.place(relx=0.58, rely=0.5, anchor=tk.CENTER)

    id_label = ctk.CTkLabel(canvas, text="ID/",fg_color = "#036FA7", width = 150, text_color="white")
    #id_label = tk.Label(window2, text="ID/")
    id_label.place(relx=0.38, rely=0.6, anchor=tk.CENTER)

    _id = ctk.CTkLabel(canvas, text=id_student,fg_color = "Gray", width = 150, text_color="white", bg_color="transparent", corner_radius= 5)
    _id.place(relx=0.58, rely=0.6, anchor=tk.CENTER)

    group_label = ctk.CTkLabel(canvas, text="Group/",fg_color = "#036FA7", width = 150, text_color="white")
    #group_label = tk.Label(window2, text="Group/")
    group_label.place(relx=0.38, rely=0.7, anchor=tk.CENTER)

    _group = ctk.CTkLabel(canvas, text=group_student,fg_color = "Gray", width = 150, text_color="white", bg_color="transparent", corner_radius= 5)
    _group.place(relx=0.58, rely=0.7, anchor=tk.CENTER)
    
    # Left Middle Section
    img = Image.open("src/UI/assets/nazeh.png")
    img = img.resize((200, 200))  # Resize the image to match the frame's dimensions

    # Create the background image label
    photos.append(ImageTk.PhotoImage(img))
    id_photo_listID = len(photos) - 1
    id_photo_canvasID = canvas.create_image(20, 150, image=photos[-1], anchor="nw")

    # Slove attendace button
    solveIsuue_button = ctk.CTkButton(canvas, text="Solve Attendance Issue", fg_color="#8B0000", command=goSolveIssues)
    solveIsuue_button.place(relx=0.78, rely=0.6, anchor=tk.CENTER)
    
    # Back to First screen button
    back_button = ctk.CTkButton(canvas, text="Back", fg_color="#808080", command=goHome)
    #back_button = tk.Button(window2, text="Back", command=w2_open_first_window)
    back_button.place(relx=0.15, rely=0.8, anchor=tk.CENTER)

    #Finish
    finish_button = ctk.CTkButton(canvas, text="Finish !",fg_color="#006400", command=finish)
    #finish_button = tk.Button(window2, text="Finish !", command=w2_open_fourth_window)
    finish_button.place(relx = 0.15, rely = 0.9, anchor=tk.CENTER)


    # Run the second window's event loop
##########################################

if __name__ == "__main__":
    app = tk.Tk()
    app.title("Nazeh - Home Screen")
    app.geometry("800x480")
    W, H = 800, 480
    init(app, 800, 480)
    Frame.place(x = 0, y = 0)
    app.mainloop()
