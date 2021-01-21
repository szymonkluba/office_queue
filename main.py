from time import sleep

from interface import Interface, UnknownOperation, ServiceModeException
from myqueue import AllQueuesAreEmpty
from prompts import Prompts

if __name__ == '__main__':
    queues = Interface.initialize_queues()
    while True:
        category = input(Prompts.category_select_prompt())
        try:
            ticket = Interface.create_ticket(category, queues)
            print(Prompts.ticket_created_info(ticket))
            sleep(2)
        except UnknownOperation:
            print(Prompts.incorrect_input_prompt())
        except ServiceModeException:
            category = input(Prompts.select_queue_for_service_prompt())
            try:
                ticket = Interface.get_ticket_to_display(category, queues)
                print(Prompts.ticket_to_be_served(ticket))
                sleep(10)
            except AllQueuesAreEmpty:
                print(Prompts.all_queues_empty_prompt())
