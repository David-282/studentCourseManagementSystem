from typing import Optional

from pydantic import BaseModel

from models.grade import Grade


class Enrollment(BaseModel):
    student_id: str
    course_code: str
    course_grade:Optional [Grade]= None