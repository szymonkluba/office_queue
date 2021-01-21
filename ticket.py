class Ticket:

    def __init__(self, category: str, number: int):
        self._category = category
        self._number = number

    def get_full_ticket(self) -> str:
        return f"{self._category}{self._number}"

    def get_category(self) -> str:
        return self._category

    def get_number(self) -> int:
        return self._number
