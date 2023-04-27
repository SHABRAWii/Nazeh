import serial.tools.list_ports


def listDevices():
    print("List of devices:")
    ## TODO: list Serial Devices
    # serial_ports = list(serial.tools.list_ports.comports())

    # for port in serial_ports:
    #     print("Device: {}, Description: {}".format(port.device, port.description))
    # # return list(serial.comports())

def init():
    print("Init Serial Communication")
    ## TODO: Choose Serial Device to start communincation with
    ## TODO: Create Two Threads for each device to read and write data

