# import SerialCommunication
import Data_Management.AttendanceManager as AttendanceManager
import sensorBarcode.sensorBarcode as sensorBarcode
import Logger
import threading
import UI.UI as UI
import glob
import sys

argv = sys.argv
camID = 0
showCase = 1
factor = 0.25
model = 'normal'
if len(argv) == 5 and argv[4] in ['Normal', 'Fast', 'soFast'] and argv[1].isdigit() and argv[2].isdigit():
    camID = int(argv[1])
    showCase = int(argv[2])
    factor = float(argv[3])
    model = 0 if argv[4] == 'normal' else 1 if argv[4] == 'fast' else 2
    print("CamID: " + str(camID) + " ShowCase: " + str(showCase) + " Factor: " + str(factor) + " Model: " + str(model))
else:
    print("Usage: ./Nazeh <camID> <showCase> <factorImage> <'Normal' or 'Fast' or 'soFast' model>")
    exit(1)

def find_ttyACM_device():
    devices = glob.glob('/dev/ttyACM*')
    if devices:
        return devices[0]
    else:
        print("Can not find Barcode Scanner")
        return None

# Usage
device = find_ttyACM_device()
def computer_vision():
    global camID, showCase, factor, model
    import Face_Recognition.Model as Model
    Model.start(camID, showCase, factor, model)
    pass
def barcode_callback():
    while True:
        if barcode.available() > 0:
            ID = barcode.Read()
            # print("Got " + str(ID))
            UI.readBarcode(str(ID))

def main():
    Logger.setMode('INFO') # Set the mode to DEBUG or INFO
    AttendanceManager.init('src/Data_Management/Data_Screen.csv') # Set the database path
    global barcode
    barcode = sensorBarcode.Barcode_Scanner(device, 9600) # Set the barcode scanner port and baud rate

    AttendanceManager.addAttendance(800161991, 1, 1) # Add attendance for studentID, state : add or remove, and version: face recognition (false) or card attendance (true)
    Barcode_Thread = threading.Thread(target=barcode_callback)
    Barcode_Thread.start()
    UI_Thread = threading.Thread(target=UI.main)
    UI_Thread.start()
    computer_vision_thread = threading.Thread(target=computer_vision)
    computer_vision_thread.start()

if __name__ == "__main__":
    main()


# ONE TIME OPERATION
# import libraries
# face recognition and detection for database


# REPEATETIVE OPERATIONs
# 1 Camera capture frame
# 2 edit : resize convert to specific format
# 3 apply face detection -> face locations
# 4 apply face recognition -> face encodings
# 5 compare face encodings with database
# 6 draw rectangle on face with name
# 7 Go back to Operation 1

# Optimizing
# 1 Reduce solution for every fram on line 2
# 2 Multi threading on code to make series operation parallel
# 3 Face tracking
# 4 Face recognition on GPU
# 5 face_recognition library "small" model