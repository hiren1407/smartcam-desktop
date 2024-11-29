from connection import db

import datetime

def insertFaceData(data,fid):
        
        try:
            db.users.update_one(
                {"fid":fid},
                {
                    "$set": {
                        "facialEncoding":list(data),
                    }
                }
                )
            return 'Inserted Face data successfully'
        except Exception as e:
            print(f"An error occurred: {e}")  # Print the exact error message
            return str(e)  # Return the error message

    
def read():
    data=db.users.find()
    
    
    return data
    #for i in data:
        #print(i)
def checkAttendance(fid):
    fno=db.facultyattendances.find_one({'faculty_id':fid,'attendanceDate':datetime.datetime.now().strftime('%Y-%m-%d')})
    
    return fno==None

def addAttendance(fid):
    if checkAttendance(fid):
    

        attendanceDate=datetime.datetime.now().strftime('%Y-%m-%d')
        attendanceTime=datetime.datetime.now().strftime("%H:%M:%S")
        #print(attendance)
        db.facultyattendances.insert_one({

                'faculty_id':fid,
                'attendanceDate':attendanceDate,
                'attendanceTime':attendanceTime,
                "facultyStatus":"P" #p is present
                },
            
            )
    

