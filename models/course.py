from typing import List

from pydantic import BaseModel


class Course(BaseModel):
    course_title: str
    course_description: str
    course_code: str
    facilitator_id: str
