import math
import curses
import numpy as np

class Student:
    def __init__(self,s_id,name, dob):
        self.__id = s_id
        self.__name = name
        self.__dob = dob 
        self.__marks= {}
        self.__gpa =0.0

    def get_id(self):
        return self.__id
    def get_name(self):
        return self.__name
    def get_dob(self):
        return self.__dob
    def get_marks(self):
        return self.__marks
    def get_gpa (self):
        return self.__gpa
    
    def set_mark(self, course_id, mark):
        self.__marks[course_id]=mark
    def caculate_gpa(self, course):
        marks_list = []
        credits_list= []
        for c in course:
            c_id = c.get_id()
            if c_id in self.__marks:
                marks_list.append(self.__marks[c_id])
                credits_list.append(c.get_credits())
        np_marks = np.array(marks_list, dtype=float)
        np_credits = np.array(credits_list, dtype =float)

        self.__gpa = np.sum(np_marks *np_credits) / np.sum(np_credits)
        return self.__gpa

class Course:
    def __init__(self, c_id, name, credits):
        self.__id = c_id
        self.__name = name
        self.__credits = credits

    def get_id(self):
        return self.__id
    def get_name(self):
        return self.__name
    def get_credits(self):
        return self.__credits
def round_down(score):
    return math.floor(score *10) /10.0
    
def input_data():
    student = []
    courses = []
    num_s = int(input("input number of students: "))
    for i in range(num_s):
        print(f"input for student {i+1}: ")
        s_id =input("student id: ").strip()
        name = input("student name: ").strip()
        dob =input("student dob: ").strip()
        student.append(Student(s_id,name,dob))

    num_c = int(input("enter number of courses: "))
    for i in range(num_c):
        print(f"enter for course {i+1}")
        c_id = input("course id: ").strip()
        name = input("course name: ").strip()
        credits = int(input("credits: "))
        courses.append(Course(c_id,name,credits))

    print("Enter Marks: ")
    for c in courses: 
        for s in student:
            print(f"enter marks of course: {c.get_name()}:  ")    
            mark = float(input(f"mark for student {s.get_name()}: "))
            mark = round_down(mark)
            s.set_mark(c.get_id(), mark)
    
    for s in student:
        s.caculate_gpa(courses)

    student.sort(key = lambda s: s.get_gpa(), reverse =True)
    return student, courses

def display_curses(stdscr, students):
    stdscr.clear()
    stdscr.addstr(0,0,"   Student ranking by GPA    ")

    for row, s in enumerate(students, start = 2):
        stdscr.addstr(row, 0 ,f"{s.get_id()} - {s.get_name()}: GPA = {s.get_gpa(): .2f}")

    stdscr.addstr(len(students) + 3, 0,"Press any ket to exit!")
    stdscr.refresh()
    stdscr.getch()

def main():
    Student, Course = input_data()
    curses.wrapper(display_curses, Student)

if __name__ =="__main__":
    main()