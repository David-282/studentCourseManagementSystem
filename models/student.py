

from typing import List

from models.grade import Grade
from models.role import Role
from models.user import User


class Student(User):
    role:Role = Role.STUDENT
    courses_offered: List[str]= []
    grades: List[Grade] = []
    student_id:str


