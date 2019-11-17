def print_function_info(f):

    def inner(*args, **kwargs):
        print(f'\n*** Вызвана функция {f.__name__} ***\n')
        result = f(*args, **kwargs)
        print(f'\n*** Функция {f.__name__} отработала ***\n')
        return result

    return inner

