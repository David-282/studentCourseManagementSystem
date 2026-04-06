from repositories.student_repository import StudentRepository
from schemas.assign_grade import AssignGradeSchema
from utility import id_generator

from fastapi import HTTPException
from models.course import Course
from models.facilitator import Facilitator
from repositories.courses_repository import CoursesRepository
from repositories.facilitators_repository import FacilitatorsRepository
from schemas.course_create import CourseCreate
from schemas.facilitaor_create import FacilitatorCreate

course_repo = CoursesRepository()
facilitator_repo = FacilitatorsRepository()
student_repo = StudentRepository()

async def create_course(course:CourseCreate):
    existing_course = await course_repo.find_by_course_code(course.course_code)
    if existing_course is not None:
        raise HTTPException(status_code=409, detail="Course already exists")

    facilitator = await validate_facilitator(course.facilitator_id)

    new_course = Course(
        course_code = course.course_code,
        course_title = course.course_title,
        course_description = course.course_description,
        facilitator_id = course.facilitator_id
    )

    await course_repo.save(new_course.model_dump())

    return {
        "message": "Course created successfully",
        "course_code": new_course.course_code,
        "facilitator": {
            "name": facilitator["name"],
            "id": facilitator["facilitator_id"]
        }
    }

async def register_facilitator(facilitator:FacilitatorCreate):
    existing = await facilitator_repo.find_by_email(facilitator.email)

    if existing:
        raise HTTPException(status_code=409, detail="Facilitator already exists")

    new_facilitator = Facilitator(
        name = facilitator.name,
        email = facilitator.email,
        phone_number = facilitator.phone_number,
        facilitator_id = await id_generator.generate_facilitator_id(facilitator.name)
    )

    await facilitator_repo.save(new_facilitator.model_dump())

    return {
        "message": "Facilitator registered successfully",
        "facilitator": new_facilitator.model_dump()
    }

async def view_student_offering_course(facilitator_id:str,course_code):
    await validate_facilitator(facilitator_id)

    course = await validate_course(course_code)

    if course['facilitator_id'] != facilitator_id:
        raise HTTPException(status_code=403, detail="Facilitator does not handle this course")

    return course["students_offering_id"]


async def view_courses_handling(facilitator_id):

    await validate_facilitator(facilitator_id)

    return await course_repo.find_by_facilitator_id(facilitator_id)


async def assign_grade_to_student(grade_assignment: AssignGradeSchema):
    course = await validate_course(grade_assignment.course_code)

    await validate_facilitator(grade_assignment.facilitator_id)

    student = await validate_student(grade_assignment.student_id)

    if course['facilitator_id'] != grade_assignment.facilitator_id:
        raise HTTPException(status_code=403, detail="Facilitator does not handle this course")

    if grade_assignment.student_id not in course['students_offering_id']:
        raise HTTPException(status_code=404, detail="Student does not offer this course")

    for grade in student["grades"]:
        if grade["course_code"] == grade_assignment.course_code:
            grade["course_score"] = grade_assignment.score
            grade["course_grade"] = grade_assignment.grade

    await student_repo.update_student(
        grade_assignment.student_id,
        "grades",
        student["grades"]
    )
    return {"message": "Grade assigned successfully"}


async def view_student_result(facilitator_id: str, student_id: str, course_code: str):
    await validate_facilitator(facilitator_id)

    course = await validate_course(course_code)

    if course["facilitator_id"] != facilitator_id:
        raise HTTPException(status_code=403, detail="Facilitator does not handle this course")

    student = await validate_student(student_id)

    for grade in student["grades"]:
        if grade["course_code"] == course_code:
            return {"result": grade}

    raise HTTPException(status_code=404, detail="No grade found for this student in this course")

async def validate_facilitator(facilitator_id: str):
    facilitator = await facilitator_repo.find_by_id(facilitator_id)
    if facilitator is None:
        raise HTTPException(status_code=404, detail="Facilitator does not Exist")
    return facilitator


async def validate_course(course_code: str):
    course = await course_repo.find_by_course_code(course_code)
    if course is None:
        raise HTTPException(status_code=404, detail="Course Not Found")
    return course


async def validate_student(student_id: str):
    student = await student_repo.find_by_id(student_id)
    if student is None:
        raise HTTPException(status_code=404, detail="Student does not Exist")
    return student












