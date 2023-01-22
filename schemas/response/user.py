from models import RoleType
from schemas.request.user import UserBase


class UserOut(UserBase):
    id: str
    phone: str
    first_name: str
    last_name: str
    iban: str
    role: RoleType
