import os
import csv
import pandas as pd
import logging
Debug = 0
# Student_list = []
Database_Path = ''
Original_Path = ''
df = None
# cc
def init(databasePath):
    global Database_Path, Original_Path, df
    Original_Path = databasePath
    logging.debug("init(){")
    logging.debug("----Setting database to: {}".format(databasePath))
    df = pd.read_csv(databasePath)
    Database_Path = os.path.dirname(databasePath) + '/Edited.csv'
    df.to_csv(Database_Path, encoding='utf-8', index=False)
    logging.debug("}")
    return


def addAttendance(studentID, state, version):
    Student_list = []
    global Database_Path, df
    studentID = int(studentID)

    logging.debug("Add Attendance(){")
    logging.debug("---- Got studentID: {}, {}, and {} its attendance".format(studentID,
                  "Card Attendance" if version else "Face Recognition Attendance", "marked" if state else "unmarked"))
    logging.debug("---- Database Path: {}".format(Database_Path))

    with open(Database_Path, 'r', errors="ignore") as Student_data:
        Student = csv.reader(Student_data)
        for row in Student:
            Student_list.append(row)  # 2d array
        # Binary Search
        start = 1
        end = len(Student_list) - 1
        flag = 0
        while start <= end:
            mid = int((start + end) / 2)

            if studentID == int(Student_list[mid][4]):
                flag = 1
                logging.debug(
                    "---- Found studentID: {} at index: {}".format(studentID, mid))
                df.iat[mid-1, 6 + (1 if version else 0)] = int(state)
                df.to_csv(Database_Path, encoding='utf-8', index=False)
                break
            elif (studentID > int(Student_list[mid][4])):
                start = mid + 1
            else:
                end = mid - 1
    if flag == 0:
        logging.debug("---- StudentID: {} not found".format(studentID))
    logging.debug("}")
    return
def solveIssue(studentID, attend):
    Student_list = []
    global Database_Path, df
    studentID = str(studentID)

    logging.debug("Add Attendance(){")
    # logging.debug("---- Got studentID: {}, {}, and {} its attendance".format(studentID,
                #   "Card Attendance" if version else "Face Recognition Attendance", "marked" if state else "unmarked"))
    logging.debug("---- Database Path: {}".format(Database_Path))

    with open(Database_Path, 'r', errors="ignore") as Student_data:
        Student = csv.reader(Student_data)
        for row in Student:
            Student_list.append(row)  # 2d array
        # Binary Search
        start = 1
        # print(len(Student_list))
        end = len(Student_list) - 1
        flag = 0
        while start <= end:
            mid = int((start + end) / 2)

            if studentID == Student_list[mid][4]:#4 idده ال
                # print(Student_list[mid][4])
                flag = 1
                if(attend):#CV=1
                    df.iat[mid - 1, 6] = 1
                    df.iat[mid - 1, 7] = 1
                else :#CV=1
                    df.iat[mid - 1, 6] = 0
                    df.iat[mid - 1, 7] = 0
                #df.at[mid-1, 'ID' if version else 'CV'] = int(state)
                df.to_csv(Database_Path, encoding='utf-8', index=False)
                # متعدلcsvمكنتش عاملها كده ف انا عاوز اطلع فايل 
                break
            elif (studentID > Student_list[mid][4]):
                start = mid + 1
            else:
                end = mid - 1
    if flag == 0:
        logging.debug("---- StudentID: {} not found".format(studentID))
    
    logging.debug("}")
    return
def fetchData(studentID):
    Student_list = []
    global Database_Path, df
    studentID = int(studentID)
    # print(studentID)
    #########################logging
    logging.debug("fetchData(){")
    # logging.debug("---- Database Path: {}".format(Database_Path))
    ###############################################Scan from csv
    with open(Database_Path, 'r', errors="ignore") as Student_data:
        Student = csv.reader(Student_data)
        for row in Student:
            Student_list.append(row)  # 2d array
        # Binary Search
        start = 1
        end = len(Student_list) - 1
        flag = 0
        while start <= end:
            mid = int((start + end) / 2)
            if studentID == int(Student_list[mid][4]):## ids coloumn
                # print(" I foound Onw")
                name=Student_list[mid][1]
                group=Student_list[mid][5]
                id=Student_list[mid][4]
                department=Student_list[mid][2]
                level=Student_list[mid][3]
                image_path=Student_list[mid][4]+'.png'## smae as id
                computer_vision_attendace=Student_list[mid][6]
                card_attendace=Student_list[mid][7]
                print("Computer Vision Attendance: ",computer_vision_attendace)
                print("Card Attendance: ",card_attendace)
                print("ID : ",id)
                return name, group, id, department, level, image_path, card_attendace, computer_vision_attendace
            elif (studentID > int(Student_list[mid][4])):
                start = mid + 1
            else:
                end = mid - 1
    if flag == 0:
        print("not found")
        logging.debug("---- StudentID: {} not found".format(studentID))
    logging.debug("}")
    return
def Conflict_Linear_Search():
    Student_list = []
    student_confilct = []
    with open(Database_Path, 'r', errors="ignore") as Student_data:
        Student = csv.reader(Student_data)
        for row in Student:
            Student_list.append(row)  # 2d array
        # Linear Search
        print(len(Student_list))
        start = 1
        end = len(Student_list) - 1
        while start <= end:
            if Student_list[start][6]!=Student_list[start][7]:#4 idده ال
                student_confilct.append(Student_list[start][4])#Present ID In List
                # print("Hello " + Student_list[start][4] + " " + str(start))
            start+=1
        return student_confilct
def finish():
    df.to_csv(Original_Path, encoding='utf-8', index=False)