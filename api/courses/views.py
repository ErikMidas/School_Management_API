from flask_restx import Namespace, Resource, fields
from ..models.courses import Course
from ..models.students import Student
from ..models.student_registration import StudentRegistration
from ..utils.util import admin_required
from http import HTTPStatus
from flask_jwt_extended import jwt_required

course_ns = Namespace("courses", description="Namespace for Courses")

course_model = course_ns.model(
    "Course", {
        "id": fields.Integer(description="Course's ID"),
        "name": fields.String(description="Course's Name", required=True),
        "teacher": fields.String(description="Course's Teacher", required=True)
    }
)

course_student_model = course_ns.model(
    "Course Student Model", {
        "course_id": fields.Integer(description="Course's ID"),
        "student_id": fields.Integer(description="Student's User ID")
    }
)


@course_ns.route("")
class GetCreateCourses(Resource):

    @course_ns.marshal_with(course_model)
    @course_ns.doc(
        description = "Get All Available Courses"
    )
    @jwt_required()
    def get(self):
        """
            Get All Available Courses
        """
        courses = Course.query.all()

        return courses, HTTPStatus.OK
    
    @course_ns.expect(course_model)
    @course_ns.doc(
        description="Add a New Course"
    )
    @admin_required()
    def post(self):
        """
            Add a New Course
        """
        data = course_ns.payload

        # Check if course already exists
        course = Course.query.filter_by(name=data["name"]).first()
        if course:
            return {"message": "Course Already Exists"}, HTTPStatus.CONFLICT

        # Register new course
        new_course = Course(
            name = data["name"],
            teacher = data["teacher"]
        )

        new_course.save()

        course_resp = {}
        course_resp["id"] = new_course.id
        course_resp["name"] = new_course.name
        course_resp["teacher"] = new_course.teacher

        return course_resp, HTTPStatus.CREATED
    

@course_ns.route("/<int:course_id>")
class GetUpdateDeleteCourse(Resource):
    
    @course_ns.marshal_with(course_model)
    @course_ns.doc(
        description = "Retrieve a Course's Details by ID",
        params = {
            "course_id": "The Course's ID"
        }
    )
    @admin_required()
    def get(self, course_id):
        """
            Retrieve a Course's Details by ID
        """
        course = Course.get_by_id(course_id)
        
        return course, HTTPStatus.OK
    
    @course_ns.expect(course_model)
    @course_ns.marshal_with(course_model)
    @course_ns.doc(
        description = "Update a Course's Details by ID",
        params = {
            "course_id": "The Course's ID"
        }
    )
    @admin_required()
    def put(self, course_id):
        """
            Update a Course's Details by ID
        """
        course = Course.get_by_id(course_id)

        data = course_ns.payload

        course.name = data["name"]
        course.teacher = data["teacher"]

        course.update()

        return course, HTTPStatus.OK
    
    @course_ns.doc(
        description = "Delete a Course by ID",
        params = {
            "course_id": "The Course's ID"
        }
    )
    @admin_required()
    def delete(self, course_id):
        """
            Delete a Course by ID
        """
        course = Course.get_by_id(course_id)

        course.delete()

        return {"message": "Course Deleted!"}, HTTPStatus.OK


@course_ns.route("/<int:course_id>/students")
class GetAllCourseStudents(Resource):

    @course_ns.doc(
        description = "Get all Students Registered for a Course",
        params = {
            "course_id": "The Course's ID"
        }
    )
    @admin_required()
    def get(self, course_id):
        """
            Get all Students Registered for a Course
        """
        students = StudentRegistration.get_students_in_course(course_id)
        resp = []

        for student in students:
            student_resp = {}
            student_resp["id"] = student.id
            student_resp["full_name"] = student.full_name
            # student_resp["last_name"] = student.last_name            
            student_resp["matric_no"] = student.matric_no

            resp.append(student_resp)

        return resp, HTTPStatus.OK


@course_ns.route("/<int:course_id>/students/<int:student_id>")
class AddDropCourseStudent(Resource):
    
    @course_ns.doc(
        description = "Register a Student for a Course",
        params = {
            "course_id": "The Course's ID"
        }
    )
    @admin_required()
    def post(self, course_id, student_id):
        """
            Register a Student for a Course
        """
        course = Course.get_by_id(course_id)
        student = Student.get_by_id(student_id)
        
        student_in_course = StudentRegistration.query.filter_by(
                student_id=student.id, course_id=course.id
            ).first()
        if student_in_course:
            return {
                "message": f"{student.full_name} is already registered for {course.name}"
            }, HTTPStatus.OK
        
        course_student =  StudentRegistration(
            course_id = course_id,
            student_id = student_id
        )

        course_student.save()

        course_student_resp = {}
        course_student_resp["course_id"] = course_student.course_id
        course_student_resp["name"] = course.name
        course_student_resp["course_teacher"] = course.teacher
        course_student_resp["student_id"] = course_student.student_id
        course_student_resp["student_full_name"] = student.full_name
        # course_student_resp['student_last_name'] = student.last_name
        course_student_resp["student_matric_no"] = student.matric_no

        return course_student_resp, HTTPStatus.CREATED

    @course_ns.doc(
        description="Remove a Student from a Course",
        params = {
            "course_id": "The Course's ID",
            "student_id": "The Student's ID"
        }
    )
    @admin_required()
    def delete(self, course_id, student_id):
        """
            Remove a Student from a Course
        """

        # Confirm existence of student and course
        course = Course.query.filter_by(id=course_id).first()
        student = Student.query.filter_by(id=student_id).first()
        if not student or not course:
            return {"message": "Student or Course Not Found"}, HTTPStatus.NOT_FOUND
        
        # Check if student is not registered for the course
        student_in_course = StudentRegistration.query.filter_by(
                student_id=student.id, course_id=course.id
            ).first()
        if not student_in_course:
            return {
                "message": f"{student.full_name} is not registered for {course.name}"
            }, HTTPStatus.NOT_FOUND

        # Remove the student from the course
        student_in_course.delete()

        return {"message": f"{student.full_name} has been successfully removed from {course.name}"}, HTTPStatus.OK