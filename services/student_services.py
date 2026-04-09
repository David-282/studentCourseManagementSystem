from fastapi import HTTPException

from models.enrollment import Enrollment
from models.grade import Grade
from models.student import Student
from repositories.courses_repository import CoursesRepository
from repositories.enrollment_repository import EnrollmentRepository
from repositories.student_repository import StudentRepository
from schemas.create_student import CreateStudentSchema
from schemas.enroll_for_course import EnrollForCourse
from utility import id_generator

student_repo = StudentRepository()
course_repo = CoursesRepository()
enrollment_repo = EnrollmentRepository()

async def register_student(student:CreateStudentSchema):
    existing_student = await student_repo.find_by_email(student.email)

    if existing_student is not None:
        raise HTTPException(status_code=409, detail="Student already exists")

    new_student = Student(

        name = student.name,
        email = student.email,
        phone_number = student.phone_number,
        student_id = await id_generator.generate_student_id(student.name)
    )

    await student_repo.save(new_student.model_dump())

    return {
        "message": "Student registered successfully",
        "student_id": new_student.student_id
    }


async def enroll_course(enroll_for_course:EnrollForCourse):

    student = await student_repo.find_by_id(enroll_for_course.student_id)
    if student is None:
        raise HTTPException(status_code=404, detail="Student not found")

    course = await course_repo.find_by_course_code(enroll_for_course.course_code)
    if course is None:
        raise HTTPException(status_code=404, detail="Course not found")

    enrollment = await enrollment_repo.find_by_course_code_and_student_id(enroll_for_course.course_code, enroll_for_course.student_id)
    if enrollment is not None:
        raise HTTPException(status_code= 409, detail="Student is already offering this course.")

    new_enrollment = Enrollment(
        course_code= enroll_for_course.course_code,
        student_id = enroll_for_course.student_id,

    )

    await enrollment_repo.save(new_enrollment.model_dump())

    return{
        "message": "Course registered successfully",
    }

async def view_student_details(student_id):
    student = await student_repo.find_by_id(student_id)
    if student is None:
        raise HTTPException(status_code=404, detail="Student not found")

    return{
        "student_id": student["student_id"],
        "student_name":student["name"],
        "student_email":student["email"],
        "student_phone_number":student["phone_number"]
    }


async def view_courses_offering(student_id: str):
    student = await student_repo.find_by_id(student_id)
    if student is None:
        raise HTTPException(status_code=404, detail="Student not found")

    enrollments = await enrollment_repo.find_by_student_id(student_id)
    return {"courses": [enrollment["course_code"] for enrollment in enrollments]}
