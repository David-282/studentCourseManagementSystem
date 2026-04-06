from typing import Optional
from pydantic import BaseModel

class Grade(BaseModel):
    course_code: str
    course_grade: Optional[str] = None
    course_score: Optional[int] = None