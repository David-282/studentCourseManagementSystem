from fastapi import  APIRouter

from schemas.create_student import CreateStudentSchema
from schemas.register_course import RegisterCourseSchema
from services import student_services

router = APIRouter()




@router.post("/register_student")
async def register_student(student: CreateStudentSchema):
    return await student_services.register_student(student)


@router.post("/register_course")
async def register_course(course:RegisterCourseSchema):
    return await student_services.register_for_course(course)


@router.get("/view_student_details")
async def view_student_details(student_id:str):
    return await student_services.view_student_details(student_id)


@router.get("/view_courses")
async def view_courses(student_id:str):
    return await student_services.view_courses_offering(student_id)


@router.get("/view_student_grades")
async def view_student_grades(student_id:str):
    return await student_services.view_results(student_id)
