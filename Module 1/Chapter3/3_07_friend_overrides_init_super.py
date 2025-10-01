from typing import ClassVar, List

#added type hints and used ClassVar for the shared registry
#more readable and type checked.

class Contact:
    # Class-level registry of all Contact instances
    all_contacts: ClassVar[List["Contact"]] = []

    def __init__(self, name: str, email: str) -> None:
        self.name = name
        self.email = email
        Contact.all_contacts.append(self)


class Friend(Contact):
    def __init__(self, name: str, email: str, phone: str) -> None:
        # Delegate name/email initialization to the base class to avoid duplication
        super().__init__(name, email)
        self.phone = phone
