import tkinter as tk
import UI.uiLIb.Home as Home
import UI.uiLIb.Barcode as Barcode
import UI.uiLIb.solveIssues as solveIssues
import UI.uiLIb.Finish as Finish
import Data_Management.AttendanceManager as AttendanceManager
# import customtkinter as ctk
import customtkinter as ctk
import time
cared_List = []
computer_vision_List = []
Total_Attendance_List = []
card_cout, computer_vision_count, Total_Attendance_count = 0, 0, 0
def Test():
    # Home.Frame.after(1500, Home.readID, "800161991")
    # # Home.Frame.after(1500, readBarcode, "800161991")
    # Home.Frame.after(3500, readBarcode, "800159950")
    # Home.Frame.after(7500, readBarcode, "800161979")
    # Home.Frame.after(11500, readBarcode, "800161991")
    # Home.Frame.after(15500, readBarcode, "803084355")
    # Home.Frame.after(19500, readBarcode, "800168127")
    # Home.Frame.after(23500, readBarcode, "800167244")
    # Barcode.Frame.after(5500, readBarcode, "800161991")
    # Home.Test()
    # Barcode.Test()
    # solveIssues.Test()
    pass
def Update_computerVision(ID):
    global card_cout, computer_vision_count, Total_Attendance_count, cared_List, computer_vision_List, Total_Attendance_List
    ID = int(ID)
    if ID not in computer_vision_List:
        print("Got ID from computer vision " + str(ID) + " at " + str(time.time()))
        computer_vision_List.append(ID)
        computer_vision_count += 1
        if ID not in Total_Attendance_List and ID in cared_List:
            Total_Attendance_count += 1
            Total_Attendance_List.append(ID)
        Barcode.change_status(Total_Attendance_count, card_cout, computer_vision_count)
        solveIssues.change_status(Total_Attendance_count, card_cout, computer_vision_count)
        Finish.change_status(Total_Attendance_count, card_cout, computer_vision_count)

    pass
def readBarcode(ID):
    global card_cout, computer_vision_count, Total_Attendance_count, cared_List, computer_vision_List, Total_Attendance_List
    ID = int(ID)
    if Home.Frame.winfo_viewable():
        # print("in home " + ID)
        # Home read Barcode
        Home.readID(ID)
        pass
    else:
        if ID in cared_List:
            Barcode.set_not_finished_again()
            return
        # print("heelo " + ID)
        data = AttendanceManager.fetchData(ID)
        if data is not None:
            name, group, id, department, level, image_path, card_attendace, computer_vision_attendace = data
            # Rest of your code here
            Barcode.set_not_finished(name, group, id, department, level, image_path, card_attendace)
            AttendanceManager.addAttendance(id, 1, 1)
            cared_List.append(ID)
            if int(computer_vision_attendace) == 1 and ID not in Total_Attendance_List:
                Total_Attendance_count += 1
                Total_Attendance_List.append(ID)
            card_cout += 1
            Barcode.change_status(Total_Attendance_count, computer_vision_count, card_cout)
            solveIssues.change_status(Total_Attendance_count, computer_vision_count, card_cout)
            Finish.change_status(Total_Attendance_count, computer_vision_count, card_cout)
        else:
            print("Student Not Found")
        # Barcode.Frame.after(2000)
        # Barcode.set_finished()
        # Fetech Data
        # Save Attendance QR Code
        # Show Data on Screen
        # wait for 2 Seconds and let the student scan again
        pass
start_time = time.time()
def main():
    app = ctk.CTk()
    app.title("Nazeh - Attendance Project")
    app.geometry("800x480")
    Home.init(app, 800, 480)
    Barcode.init(app, 800, 480)
    solveIssues.init(app, 800, 480)
    Finish.init(app, 800, 480)

    Test()
    # Home.Frame.place(x=0, y=0)
    app.mainloop()


if __name__ == "__main__":
    main()