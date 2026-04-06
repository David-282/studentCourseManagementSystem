from fastapi import HTTPException

from models.grade import Grade
from models.student import Student
from repositories.courses_repository import CoursesRepository
from repositories.student_repository import StudentRepository
from schemas.create_student import CreateStudentSchema
from schemas.register_course import RegisterCourseSchema
from utility import id_generator

student_repo = StudentRepository()
course_repo = CoursesRepository()

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


async def register_for_course(register_course:RegisterCourseSchema):

    student = await student_repo.find_by_id(register_course.student_id)
    if student is None:
        raise HTTPException(status_code=404, detail="Student not found")

    course = await course_repo.find_by_course_code(register_course.course_code)
    if course is None:
        raise HTTPException(status_code=404, detail="Course not found")

    if register_course.course_code in student["courses_offered"]:
        raise HTTPException(status_code=409, detail="Student already registered for this course")

    student["courses_offered"].append(course["course_code"])

    course["students_offering_id"].append(student["student_id"])

    grade = Grade(
        course_code = register_course.course_code
    )

    student["grades"].append(grade.model_dump())

    await student_repo.update_student(
        register_course.student_id,
        "grades",
        student["grades"]
    )

    await student_repo.update_student(
        register_course.student_id,
        "courses_offered",
        student["courses_offered"]
    )
    await course_repo.update_course(
        register_course.course_code,
        "students_offering_id",
        course["students_offering_id"]

    )

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
        "courses_offered":student["courses_offered"]
    }


async def view_courses_offering(student_id: str):
    student = await student_repo.find_by_id(student_id)
    if student is None:
        raise HTTPException(status_code=404, detail="Student not found")
    return {"courses": student["courses_offered"]}

async def view_results(student_id: str):
    student = await student_repo.find_by_id(student_id)
    if student is None:
        raise HTTPException(status_code=404, detail="Student not found")
    return {"results": student["grades"]}
