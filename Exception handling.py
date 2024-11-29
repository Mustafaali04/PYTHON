class LowAttendenceError(Exception):
    def __init__(self, attendence, required):
        super().__init__(f"Attendence is too low! Current: {attendence}%, Required: {required}%")


def check_attendence(attendence, required=75):
      if attendence<required:
          raise LowAttendenceError(attendence, required)
      else:
          print("Attendence is sufficient.")


try:
    student_attendence=65
    check_attendence(student_attendence)
except LowAttendenceError as e:
    print(f"Error: {e}")
    
    
