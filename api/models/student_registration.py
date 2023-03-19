from ..utils import db
from .students import Student
from .courses import Course

class StudentRegistration(db.Model):
    __tablename__ = "student_registration"
    id = db.Column(db.Integer(), primary_key=True)
    student_id = db.Column(db.Integer(), db.ForeignKey("students.id"))
    course_id = db.Column(db.Integer(), db.ForeignKey("courses.id"))

    def __repr__(self):
        return f"<Student Registration {self.id}>"
        
    def save(self):
        db.session.add(self)
        db.session.commit()
    
    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    @classmethod
    def get_by_id(cls, id):
        return cls.query.get_or_404(id)
    
    def get_courses_by_student(cls, student_id):
        courses = Course.query.join(StudentRegistration).join(Student).filter(Student.id == student_id).all()
        return courses
    
    def get_students_in_course(cls, course_id):
        students = Student.query.join(StudentRegistration).join(Course).filter(Course.id == course_id).all()
        return students