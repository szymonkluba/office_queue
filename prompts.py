from wrappers import clear_console


class Prompts:

    @staticmethod
    @clear_console
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
    @clear_console
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
    @clear_console
    def incorrect_input_prompt() -> str:
        prompt = "Nieznana operacja"
        return prompt

    @staticmethod
    @clear_console
    def empty_queue_prompt() -> str:
        prompt = "Kolejka jest pusta. Wybierz inną"
        return prompt

    @staticmethod
    @clear_console
    def all_queues_empty_prompt() -> str:
        prompt = "Wszystkie kolejki są puste"
        return prompt

    @staticmethod
    @clear_console
    def ticket_created_info(ticket):
        prompt = f"Twój numerek w kolejce to {ticket.get_full_ticket()}"
        return prompt

    @staticmethod
    @clear_console
    def ticket_to_be_served(ticket):
        prompt = f"Aktualnie obsługiwany numerek to: {ticket.get_full_ticket()}"
        return prompt
