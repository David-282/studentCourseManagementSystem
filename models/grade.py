from pydantic import BaseModel


class Grade(BaseModel):
    course_code: str
    course_grade:str
    course_score:float