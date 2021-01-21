import os


def input_to_upper(func):
    def wrapper(string, *args, **kwargs):
        if len(string) == 1:
            string = string.upper()
        return func(string, *args, **kwargs)
    return wrapper


def clear_console(func):
    def wrapper(*args, **kwargs):
        os.system("cls" if os.name == 'nt' else 'clear')
        return func(*args, **kwargs)
    return wrapper
