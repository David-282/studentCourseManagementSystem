from pydantic import BaseModel


class RegisterCourseSchema(BaseModel):
    course_code:str
    student_id:str