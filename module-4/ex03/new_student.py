import random
import string
from dataclasses import dataclass, field


def generate_id() -> str:
    return "".join(random.choices(string.ascii_lowercase, k=15))


@dataclass
class Student:
    """
    Student class
    """
    name: str
    surname: str
    active: bool = True
    login: str = field(init=False, default="")
    id: str = field(init=False, default_factory=generate_id)

    def __post_init__(self):
        self.login = self.name[0] + self.surname
