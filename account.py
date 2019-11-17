from os import path
import json

from decorators import print_function_info


def account():

    @print_function_info
    def add_money(account_data, summa):

        while not summa.isnumeric():
            input('\nВведите сумму ЦЕЛЫМ ЧИСЛОМ: ')

        account_data['account'] += int(summa)
        print(f"Сумма на вашем счете: {account_data['account']} р.")
        return account_data

    @print_function_info
    def bue(account_data, summa):

        while not summa.isnumeric():
            summa = input('Введите сумму ЦЕЛЫМ ЧИСЛОМ: ')

        summa = int(summa)

        if summa > account_data['account']:
            print('Недостаточно средств на счете!')
        else:
            account_data['account'] -= summa
            account_data[input('Введите название товара: ')] = summa

        return account_data

    @print_function_info
    def print_shopping_list(account_data):
        if len(account_data) > 1:
            print('\nИстория покупок:')
            for key, val in account_data.items():
                if key != 'account':
                    print(f'{key} --> {val} р.')
        else:
            print('\nСписок покупок пока пуст!')


    account_data = {
        'account': 0,
    }

    account_file_path = './account_data'
    try:
        if path.exists(account_file_path):
            with open(account_file_path, 'r', encoding='utf-8') as f:
                account_data = json.load(f)
    except OSError as e:
        print(e.errno)

    while True:
        print('\n1. пополнение счета')
        print('2. покупка')
        print('3. история покупок')
        print('4. выход')

        choice = input('Выберите пункт меню: ')
        if choice == '1':
            account_data = add_money(account_data, input('\nВведите сумму для пополнения счета: '))
        elif choice == '2':
            account_data = bue(account_data, input('\nВведите сумму покупки: '))
        elif choice == '3':
            print_shopping_list(account_data)
        elif choice == '4':
            break
        else:
            print('\nНеверный пункт меню\n')

    try:
        with open(account_file_path, 'w', encoding='utf-8') as f:
            f.write(json.dumps(account_data))
    except OSError as e:
        print(e.errno)


if __name__ == '__main__':

    account()
