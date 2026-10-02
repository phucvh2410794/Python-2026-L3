def input_students():
    student_ids = []
    student_names = []
    student_dobs =[]
    n = int(input("input the number of students: "))
    for i in range(n):
        print(f"\n student {i + 1}")
        s_id = input("student_id:  ").strip()
        name = input("name: ").strip()
        dob = input("Dob: ").strip()

        student_ids.append(s_id)
        student_names.append(name)
        student_dobs.append(dob)

    return student_ids, student_names, student_dobs

def input_courses():
    course_ids =[]
    course_names = []
    m = int(input("input the number of courses: "))
    for i in range(m):
        print(f"input course {i+1}")
        c_id = input("course_id: ").strip()
        c_name = input("course name: ").strip()

        course_ids.append(c_id)
        course_names.append(c_name)
    return course_names,course_ids

def input_marks(student_ids, course_ids):
    student_marks = {c_id: {} for c_id in course_ids}
    for c_id in course_ids:
        print(f"input marks of {c_id}")
        for s_id in student_ids:
            if c_id not in student_marks:
                student_marks[c_id]= {}
            mark = float(input(f"input the mark of student {s_id} of {c_id} course:  "))
            student_marks[c_id][s_id] = mark
    return student_marks

def show_student_marks(student_ifs, student_names,student_dob,course_ids,student_marks):
    print(f"{'Student ID':<12} | {'Student Name':<25} | {'DoB':<12} | {'Marks':<30}")
    for i in range(len(student_ids)):
        s_id = student_ids[i]
        name = student_names[i]
        dob = student_dobs[i]

        f"{c_id}: {student_marks[c_id].get(s_id, 'N/A')}" 
        for c_id in course_ids:
            print(f"{s_id:<12} | {name:<25} | {dob:<12} ")

if __name__ == "__main__":
    student_ids, student_names, student_dobs = input_students()
    course_ids, course_names = input_courses()
    student_marks = input_marks(student_ids, course_ids)
    
    show_student_marks(student_ids, student_names, student_dobs, course_ids, student_marks)