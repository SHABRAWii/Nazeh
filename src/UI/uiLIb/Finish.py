if __name__.find("uiLIb") != -1:
    import UI.uiLIb.Home as Home
else:
    import Home as Home
import tkinter as tk
import customtkinter as ctk
from PIL import Image, ImageTk, ImageDraw

def goHome():
    Frame.place_forget()
    Home.Frame.place(x = 0, y = 0)

photos = []

def change_status(Total_attendance, Computer_vision_detect, Id_detected):
    global camera_detect, ID_Card_detect, Actual_Attend, camera_detect_output_box, ID_Card_detect_output_box, Actual_Attend_output_box
    Actual_Attend = Total_attendance
    camera_detect = Computer_vision_detect
    ID_Card_detect = Id_detected
    canvas.itemconfig(camera_detect_output_box, text=camera_detect)
    canvas.itemconfig(ID_Card_detect_output_box, text=ID_Card_detect)
    canvas.itemconfig(Actual_Attend_output_box, text=Actual_Attend)
    return

def init(app, W, H):
    global Frame, canvas, camera_detect, ID_Card_detect, Actual_Attend, camera_detect_output_box, ID_Card_detect_output_box, Actual_Attend_output_box
    # Create the homeFrame
    Frame = ctk.CTkFrame(master=app, width=W, height=H, )
    # Frame.place(x=0, y=0)

    # make canvas
    canvas = ctk.CTkCanvas(Frame, width=W, height=H,)
    canvas.place(x=0, y=0)

    # Load the image
    img = Image.open("src/UI/assets/background.png")
    img = img.resize((W, H))  # Resize the image to match the frame's dimensions

    # Create the background image label
    photos.append(ImageTk.PhotoImage(img))
    canvas.create_image(0, 0, image=photos[-1], anchor="nw")


    # welcome_text = tk.Label(canvas, text="Attendance Done", font=("Arial", 16))
    canvas.create_text(400, 20, text="Attendance Done", font=("Arial", 16), fill="black", anchor="center")
    # welcome_text.place(relx=0.5, rely=0.1, anchor="center")

    # Photo box
    img = Image.open("src/UI/assets/nazeh.png")
    img = img.resize((200, 200))  
    photos.append(ImageTk.PhotoImage(img))
    canvas.create_image(300, 40, image=photos[-1], anchor="nw")

    # Statics text box
    ################
    camera_detect = 0
    ID_Card_detect= 0
    Actual_Attend= 0
    ################


    canvas.create_text(400, 260, text="Statics", font=("Arial", 15), fill="black", anchor="center")

    #Camera _detect
    canvas.create_text(100, 300, text="Camera Detect:", font=("Arial", 12), fill="black", anchor="center")
    
    camera_detect_output_box = canvas.create_text(180, 300, text=camera_detect, font=("Arial", 12), fill="black", anchor="center")

    #Actual_Attend
    canvas.create_text(380, 300, text="Actual_Attend:", font=("Arial", 12), fill="black", anchor="center")

    Actual_Attend_output_box = canvas.create_text(460, 300, text=Actual_Attend, font=("Arial", 12), fill="black", anchor="center")

    ##ID_Card_detect
    canvas.create_text(630, 300, text="ID Card Detect:", font=("Arial", 12), fill="black", anchor="center")
    ID_Card_detect_output_box = canvas.create_text(710, 300, text=ID_Card_detect, font=("Arial", 12), fill="black", anchor="center")



    #Button 
    button = ctk.CTkButton(canvas, text="Back to Main", command=goHome, )
    button.place(relx=0.5, rely=0.71, anchor=tk.CENTER )


    

    # Meet Our Team text box
    canvas.create_text(400, 375, text="Meet Our Team", font=("Arial", 15, "bold"), fill="black", anchor="center")

    # Team Names text box
    canvas.create_text(400, 425, text="Mohamed Awadin - Youssef Elshabrawy - Ahmed Kamal - Belal Mekkawy - Mohamed Fahmy", font=("Arial", 12), fill="black", anchor="center")

    canvas.create_text(400, 455, text="Mohamed Sarary - Mahmoud Labib - Mohamed Alaa - Mohamed Allam - Abdelrahman Ehab", font=("Arial", 12), fill="black", anchor="center")

if __name__ == "__main__":
    app = tk.Tk()
    app.title("Nazeh - Home Screen")
    app.geometry("800x480")
    W, H = 800, 480
    init(app, 800, 480)
    Frame.place(x=0, y=0)
    app.mainloop()