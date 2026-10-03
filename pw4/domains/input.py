import math
from student import Student
from course import Course

def round_down(score):
    return math.floor(score *10) /10.0
    
def input_data():
    student = []
    courses = []
    num_s = int(input("input number of students: "))
    with open("students.txt", "w", encoding="utf-8") as f:
        for i in range(num_s):
            print(f"input for student {i+1}: ")
            s_id =input("student id: ").strip()
            name = input("student name: ").strip()
            dob =input("student dob: ").strip()

            student.append({"id": s_id, "name": name, "dob": dob})
            f.write(f"{s_id},{name},{dob}\n")
        return student

    num_c = int(input("enter number of courses: "))
    with open("courses.txt", "w", encoding="utf-8") as f:
        for i in range(num_c):
            print(f"enter for course {i+1}")
            c_id = input("course id: ").strip()
            name = input("course name: ").strip()
            credits = int(input("credits: "))
            courses.append({"id": c_id, "name": name, "credits": credits})
            
            f.write(f"{c_id},{name},{credits}\n")

    print("Enter Marks: ")
    with open("marks.txt", "a", encoding="utf-8") as f:
        for c in courses: 
            for s in student:
                print(f"enter marks of course: {c.get_name()}:  ")    
                mark = float(input(f"mark for student {s.get_name()}: "))
                mark[(s['id'], courses)] = mark

                f.write(f"{s['id']},{courses},{mark}\n")
    
    for s in student:
        s.caculate_gpa(courses)

    student.sort(key = lambda s: s.get_gpa(), reverse =True)
    return student, courses
if __name__ == "__main__":
    input_data()

