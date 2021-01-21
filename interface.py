from myqueue import MyQueue, QueueIsEmpty, AllQueuesAreEmpty
from prompts import Prompts
from ticket import Ticket
from wrappers import input_to_upper, clear_console

from time import sleep


class UnknownOperation(Exception):
    pass


class ServiceModeException(Exception):
    pass


class Interface:
    CATEGORIES = ("A", "B", "C")
    SECRET_PASSWORD = "secretPassword"

    @staticmethod
    @input_to_upper
    def validate_input(string: str) -> None:
        if string == Interface.SECRET_PASSWORD:
            raise ServiceModeException
        elif string not in Interface.CATEGORIES and string != Interface.SECRET_PASSWORD:
            raise UnknownOperation

    @staticmethod
    def check_empty_queues(queues: dict) -> None:
        if all([len(queue) == 0 for queue in queues.values()]):
            raise AllQueuesAreEmpty

    @staticmethod
    @input_to_upper
    def create_ticket(category: str, queues: dict) -> Ticket:
        Interface.validate_input(category)
        number = queues[category].get_last_number()
        ticket = Ticket(category, number)
        Interface.add_ticket_to_queue(ticket, queues)
        return ticket

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
    def get_ticket_to_display(category: str, queues: dict) -> Ticket:
        try:
            Interface.validate_input(category)
            Interface.check_empty_queues(queues)
            queue = queues[category]
            ticket = queue.get_next_ticket()
            return ticket
        except QueueIsEmpty:
            print(Prompts.empty_queue_prompt())
            sleep(2)
            category = input(Prompts.select_queue_for_service_prompt())
            return Interface.get_ticket_to_display(category, queues)
        except UnknownOperation:
            print(Prompts.incorrect_input_prompt())
            sleep(2)
            category = input(Prompts.select_queue_for_service_prompt())
            return Interface.get_ticket_to_display(category, queues)
        except ServiceModeException:
            category = input(Prompts.select_queue_for_service_prompt())
            return Interface.get_ticket_to_display(category, queues)
