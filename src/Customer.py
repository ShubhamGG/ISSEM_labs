from dataclasses import dataclass


@dataclass
class Customer:
    id: int
    security_question: str
    name: str
    accounts: list
    contact_details: dict
