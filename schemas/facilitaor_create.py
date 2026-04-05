from pydantic import BaseModel


class FacilitatorCreate(BaseModel):
    name: str
    email: str
    phone_number: str