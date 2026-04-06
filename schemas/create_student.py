from fastapi.openapi.models import Schema
from pydantic import BaseModel


class CreateStudentSchema(BaseModel):
    name: str
    email: str
    phone_number: str
