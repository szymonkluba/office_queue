from interface import Interface, UnknownOperation, ServiceModeException
from myqueue import AllQueuesAreEmpty
from time import sleep


if __name__ == '__main__':
    queues = Interface.initialize_queues()
    while True:
        category = input(Interface.category_select_prompt())
        try:
            Interface.create_ticket(category, queues)
        except UnknownOperation:
            print(Interface.incorrect_input_prompt())
        except ServiceModeException:
            category = input(Interface.select_queue_for_service_prompt())
            try:
                print(Interface.get_ticket_to_display(category, queues))
                sleep(10)
            except AllQueuesAreEmpty:
                print(Interface.all_queues_empty_prompt())
