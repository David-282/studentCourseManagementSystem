import random

from repositories.facilitators_repository import FacilitatorsRepository
from repositories.student_repository import StudentRepository

student_repo = StudentRepository()
facilitators_repo = FacilitatorsRepository()

async def generate_facilitator_id(name:str) -> str:
    prefix = name[:3].upper()
    while True:
        number = random.randint(1000,9999)
        new_id = f"{prefix}-{number}-FACILITATOR"

        existing_id = await facilitators_repo.find_by_id(new_id)
        if existing_id is None:
            return new_id




async def generate_student_id(name:str) -> str:
    prefix = name[:3].upper()
    while True:
        number = random.randint(1000, 9999)
        new_id = f"{prefix}-{number}-STUDENT"

        existing_id = await student_repo.find_by_id(new_id)
        if existing_id is None:
            return new_id


