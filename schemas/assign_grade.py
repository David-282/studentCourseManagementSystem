from pydantic import BaseModel


class AssignGradeSchema(BaseModel):
    facilitator_id:str
    course_code:str
    student_id:str
    course_grade: str
