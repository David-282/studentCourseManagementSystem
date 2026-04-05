from pydantic import BaseModel


class CourseCreate(BaseModel):
    course_title: str
    course_description: str
    course_code: str
    facilitator_id: str
