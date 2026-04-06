from fastapi import APIRouter

from schemas.assign_grade import AssignGradeSchema
from schemas.course_create import CourseCreate
from schemas.facilitaor_create import FacilitatorCreate
from services import facilitator_services


router = APIRouter()


@router.post("/register_facilitator")
async def register_facilitator(facilitator:FacilitatorCreate):
    return await facilitator_services.register_facilitator(facilitator)

@router.post("/create_course")
async def create_course(course:CourseCreate):
    return await facilitator_services.create_course(course)

@router.get("/view_course_facilitator_handles")
async def view_course_facilitator_handles(facilitator_id:str):
    return await facilitator_services.view_courses_handling(facilitator_id)


@router.get("/view_student_offering_course")
async def view_student_offering_course(facilitator_id:str,course_code:str):
    return await facilitator_services.view_student_offering_course(facilitator_id,course_code)


@router.put("/assign_grade")
async def assign_grade(grade:AssignGradeSchema):
    return await facilitator_services.assign_grade_to_student(grade)

@router.get("/view_student_grade")
async def view_student_grade(facilitator_id: str, student_id: str, course_code: str):
    return await facilitator_services.view_student_result(facilitator_id,student_id,course_code)