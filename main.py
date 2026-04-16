

class Student:
    def __init__(self, sid, name):
        self.sid = sid
        self.name = name
        self.courses = {}  # course -> grade

    def add_grade(self, course, grade):
        self.courses[course] = grade

    def gpa(self):
        if not self.courses:
            return 0
        return sum(self.courses.values()) / len(self.courses)


class University:
    def __init__(self):
        self.students = {}

    def add_student(self, student):
        self.students[student.sid] = student

    def transcript(self, sid):
        s = self.students[sid]
        return {
            "name": s.name,
            "courses": s.courses,
            "gpa": s.gpa()
        }

    def top_students(self):
        return sorted(
            self.students.values(),
            key=lambda s: s.gpa(),
            reverse=True
        )
