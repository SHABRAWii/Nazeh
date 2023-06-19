if __name__.find("uiLIb") != -1:
    import UI.uiLIb.Barcode as Barcode
else:
    import Barcode as Barcode
import tkinter as tk
import customtkinter as ctk
from PIL import Image, ImageTk, ImageDraw
# import uiLIb.Barcode as Barcode

import importlib.util

# spec = importlib.util.spec_from_file_location("font", "assets/font.py")
# ft = importlib.util.module_from_spec(spec)
# spec.loader.exec_module(ft)

Team = [
    ["Dr.Abeer Twakol","Dr.Abeer.png"],
    ["Eng. Omar Wahba","Youssef.jpg"],
    ["Youssef El Shabrawii","Youssef.jpg"],
    ["Ahmed Kamal", "Youssef.jpg"],
    ["Mohamed Awadin","Youssef.jpg"],
    ["Belal El Mikkawy","Youssef.jpg"],
    ["Mahmoud Labib", "Youssef.jpg"],
    ["Mohamed Sarary", "Youssef.jpg"],
    ["Mohammed Allam", "Youssef.jpg"],
    ["Mohamed Fahmy", "Youssef.jpg"],
    ["Mohammed Alaa", "Youssef.jpg"],
    ["Abd El Rahman Ehab", "Youssef.jpg"],
]

# import font as ft
# WINDOW2.w2_open_second_window()

Frame = None

def open_barcodeScreen():
    Frame.place_forget()
    Barcode.Frame.place(x=0, y=0)
    canvas.itemconfig(ID_text, text="---------")
    Enter.configure(state="disabled")
    # WINDOW2.w2_open_second_window()
def readID(ID):
    canvas.itemconfig(ID_text, text=ID)
    Enter.configure(state="normal")

def Test():
    Frame.after(1500, readID, "800161991")
    Frame.after(2500, Enter.invoke)
photos = []

def init(app, W, H):

    # Create a new tkinter window
    global Frame, canvas

    # print(W, H)
    # Create the homeFrame
    Frame = ctk.CTkFrame(master=app, width=W, height=H, bg_color="transparent" ,fg_color="transparent")
    Frame.place(x=0, y=0)

    # make canvas
    canvas = ctk.CTkCanvas(Frame, width=W, height=H,bg = "blue")
    canvas.place(x=0, y=0, anchor=tk.NW)

    
    # Load the image
    img = Image.open("src/UI/assets/background3.jpg")
    img = img.resize((W, H+10))  # Resize the image to match the frame's dimensions
    # img.show()
    # Create the background image label
    photos.append(ImageTk.PhotoImage(img))
    canvas.create_image(0, 0, image=photos[-1], anchor="nw")
    

    # Welcome text box
    canvas.create_text(5, 90, text="     Welcome to 'Nazeh' ", font=("Arial", 14, "bold"), fill="#B03A2E", anchor=tk.NW)
    canvas.create_text(5, 90, text="\n\n             Attendance Project", font=("Arial", 10, "bold"), fill="#B03A2E", anchor=tk.NW)


    # Photo box
    img = Image.open("src/UI/assets/nazeh.png")
    img = img.resize((200, 200))  
    photos.append(ImageTk.PhotoImage(img))
    canvas.create_image(30, 135, image=photos[-1], anchor="nw")
    # canvas.image = image  # Keep a reference to the image object
    # Waiting text box
    canvas.create_text(20, 330, text="Waiting for DR Access...", font=("Arial", 14, "bold"), fill="black", anchor=tk.NW)

    # ID text box
    canvas.create_text(50, 355, text="ID/", font=("Arial", 14, "bold"), fill="black", anchor=tk.NW)

    # ID Number Output box
    global ID_text
    ID_text = canvas.create_text(90, 355, text="---------", font=("Arial", 14, "bold"), fill="black", anchor=tk.NW)
    #Button 
    global Enter
    Enter = ctk.CTkButton(Frame, text="Enter", command=open_barcodeScreen, bg_color="transparent", state="disabled")
    Enter.place(relx=0.16, rely=0.83, anchor=tk.CENTER)
    # button.pack()

    # Meet Our Team text box
    canvas.create_text(500, 50, text="Meet Our Team", font=("Arial", 30, "bold"), fill="black", anchor=tk.CENTER)
    
    
    x1, y1 = 280, 115
    x2, y2 = 405, 107
    i = 0
    for person in Team:
        i += 1
        if i > 1:
            if i % 2:
                y1 += 60
                y2 += 60
                x1, x2 = 280, 405
            else:
                x1, x2 = 540, 675

        # img = Image.open("assets/" + person[1])
        # img = img.resize((70, 70))  # Resize the image to desired dimensions
        
        # Create a circular mask for the image
        # if i < 5:
            # mask = Image.new("L", (70, 70), 0)
            # draw = ImageDraw.Draw(mask)
            # draw.ellipse((0, 0, 70, 70), fill=255)
            # masked_img = ImageTk.PhotoImage(Image.composite(img, Image.new("RGBA", img.size), mask))
            # photos.append(masked_img)
            # print(x1, y1, x2, y2)
            # canvas.create_image(x1, y1, image=masked_img, anchor=tk.CENTER)
        if i > 2:
            canvas.create_text(x2, y2, text=person[0], font=("Arial", 12, "bold"), fill="#148F77", anchor=tk.CENTER)
        else:
            canvas.create_text(x2, y2, text=person[0], font=("Arial", 14, "bold"), fill="#E64345", anchor=tk.CENTER)
    # border = ctk.CTkFrame(canvas, border_width=3, border_color="#EAECEE", width=200, height=200, bg_color="transparent", fg_color="transparent", background_corner_colors="transparent")
    canvas.create_rectangle(305, 88, 795, 430, outline="Black", width=3)
    # border.place(x=305, y=115, anchor=tk.CENTER)

    # canvas.create_text(435, 127, text="Project Supervisor", font=(ft.fonts[70], 12, ), fill="black", anchor=tk.CENTER)
    # canvas.create_text(700, 127, text="Project Supervisor", font=(ft.fonts[70], 12, ), fill="black", anchor=tk.CENTER)
    # canvas.create_text(525, 185, text="Team Leader", font=(ft.fonts[70], 12, ), fill="black", anchor=tk.CENTER)
        



if __name__ == "__main__":
    app = tk.Tk()
    app.title("Nazeh - Home Screen")
    app.geometry("800x480")
    W, H = 800, 480
    init(app, 800, 480)
    Barcode.init(app, W, H)
    Frame.place(x=0, y=0)
    app.mainloop()