from ticket import Ticket


class QueueIsEmpty(Exception):
    pass


class AllQueuesAreEmpty(Exception):
    pass


class MyQueue:

    def __init__(self, category: str):
        self._last_number = 1
        self._category = category
        self._queue = []

    def check_if_queue_is_empty(self):
        if not self._queue:
            raise QueueIsEmpty

    def add_ticket(self, ticket: Ticket):
        self._last_number += 1
        self._queue.append(ticket)

    def get_next_ticket(self) -> Ticket:
        self.check_if_queue_is_empty()
        ticket = self._queue.pop(0)
        return ticket

    def get_last_number(self) -> int:
        return self._last_number

    def __len__(self):
        return len(self._queue)