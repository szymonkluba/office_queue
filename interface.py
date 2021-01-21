from myqueue import MyQueue, QueueIsEmpty, AllQueuesAreEmpty

from ticket import Ticket
from wrappers import input_to_upper, clear_console


class UnknownOperation(Exception):
    pass


class ServiceModeException(Exception):
    pass


class Interface:
    CATEGORIES = ("A", "B", "C")
    SECRET_PASSWORD = "secretPassword"

    def __init__(self):
        pass

    @staticmethod
    def category_select_prompt() -> str:
        prompt = (
            "Wybierz kolejkę (wpisz odpowiednią literę):\n"
            "A - rejestracja pojazdów\n"
            "B - prawa jazdy\n"
            "C - dowody osobiste\n"
            "Którą kolejkę wybierasz?: "
        )
        return prompt

    @staticmethod
    def select_queue_for_service_prompt() -> str:
        prompt = (
            "Z której kolejki będziesz obsługiwał klienta?\n"
            "A - rejestracja pojazdów\n"
            "B - prawa jazdy\n"
            "C - dowody osobiste\n"
            "Którą kolejkę wybierasz?: "
        )
        return prompt

    @staticmethod
    def incorrect_input_prompt() -> str:
        prompt = (
            "Nieznana operacja"
        )
        return prompt

    @staticmethod
    @input_to_upper
    def validate_input(string: str) -> None:
        if string == Interface.SECRET_PASSWORD:
            raise ServiceModeException
        elif string not in Interface.CATEGORIES and string != Interface.SECRET_PASSWORD:
            raise UnknownOperation

    @staticmethod
    def check_empty_queues(queues: dict):
        if all([len(queue) == 0 for queue in queues.values()]):
            raise AllQueuesAreEmpty

    @staticmethod
    def empty_queue_prompt() -> str:
        prompt = "Kolejka jest pusta. Wybierz inną"
        return prompt

    @staticmethod
    def all_queues_empty_prompt() -> str:
        prompt = "Wszystkie kolejki są puste"
        return prompt

    @staticmethod
    @input_to_upper
    @clear_console
    def create_ticket(category: str, queues: dict) -> None:
        Interface.validate_input(category)
        number = queues[category].get_last_number()
        ticket = Ticket(category, number)
        Interface.add_ticket_to_queue(ticket, queues)

    @staticmethod
    @clear_console
    def initialize_queues() -> dict:
        queues = {}
        for category in Interface.CATEGORIES:
            queue = MyQueue(category)
            queues[category] = queue
        return queues

    @staticmethod
    def add_ticket_to_queue(ticket: Ticket, queues: dict) -> None:
        queue = queues[ticket.get_category()]
        queue.add_ticket(ticket)

    @staticmethod
    @input_to_upper
    @clear_console
    def get_ticket_to_display(category: str, queues: dict) -> str:
        try:
            Interface.validate_input(category)
            Interface.check_empty_queues(queues)
            queue = queues[category]
            ticket = queue.get_next_ticket()
            return ticket.get_full_ticket()
        except QueueIsEmpty:
            print(Interface.empty_queue_prompt())
            category = input(Interface.select_queue_for_service_prompt())
            return Interface.get_ticket_to_display(category, queues)
        except UnknownOperation:
            print(Interface.incorrect_input_prompt())
            category = input(Interface.select_queue_for_service_prompt())
            return Interface.get_ticket_to_display(category, queues)
        except ServiceModeException:
            category = input(Interface.select_queue_for_service_prompt())
            return Interface.get_ticket_to_display(category, queues)

