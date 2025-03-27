# lib/helpers.py
from models.Course import Course

def create_course():
    classname = input("Enter the classname: ")
    teacher = input("Enter the teacher name: ")
    term = input("Enter the term: ")
    try:
        course = Course.create(teacher, classname, term)
        print(f'Success: {course}')
    except Exception as exc:
        print("Error creating course: ", exc)

def update_course():
    idnumber = input("Enter the Course id: ")
    if course := Course.find_by_id(idnumber):
        try:
            teacher = input("Enter the new teacher: ")
            Course.teacher = teacher
            classname = input("Enter the new classname: ")
            Course.classname = classname
            term = input("Enter the new term: ")
            Course.term = term

            course.update()
            print(f'Success: {course}')

        except Exception as exc:
            print("Error updating course: ", exc)
    else:
        print(f'Course {idnumber} not found')

def delete_course():
    idnumber = input("Enter the Course id: ")
    if course := Course.find_by_id(idnumber):
       course.delete()
       print(f'Course {idnumber} deleted')
    else:
        print(f'Course {idnumber} not found')

def display_courses():
    courses = Course.get_all()
    for course in courses:
        print(course)
def find_by_coursename():
    coursename = input("Enter the Course name: ")
    course=Course.find_by_name(coursename)
    print(course) if course else print("not found")





def exit_program():
    print("Goodbye!")
    exit()
