from models.role import Role
from models.user import User


class Facilitator(User):
    role: Role = Role.FACILITATOR
    facilitator_id:str


