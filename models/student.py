

from typing import List

from models.grade import Grade
from models.role import Role
from models.user import User


class Student(User):
    student_id:str
    role:Role = Role.STUDENT



