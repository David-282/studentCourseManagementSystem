from pydantic import BaseModel


class EnrollForCourse(BaseModel):
    course_code:str
    student_id:str