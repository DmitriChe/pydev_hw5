def account():

    def add_money(payment_account, summa):

        while not summa.isnumeric():
            input('\nВведите сумму ЦЕЛЫМ ЧИСЛОМ: ')

        payment_account += int(summa)
        print(f'Сумма на вашем счете: {payment_account} р.')
        return payment_account

    def bue(payment_account, history, summa):

        while not summa.isnumeric():
            input('Введите сумму ЦЕЛЫМ ЧИСЛОМ: ')

        summa = int(summa)

        if summa > payment_account:
            print('Недостаточно средств на счете!')
        else:
            payment_account -= summa
            history[input('Введите название товара: ')] = summa

        return payment_account, history

    def shopping_list(history):
        if len(history) > 0:
            print('\nИстория покупок:')
            for key, val in history.items():
                print(f'{key} --> {val} р.')
        else:
            print('\nСписок покупок пока пуст!')

    payment_account = 0
    history = {}

    while True:
        print('\n1. пополнение счета')
        print('2. покупка')
        print('3. история покупок')
        print('4. выход')

        choice = input('Выберите пункт меню: ')
        if choice == '1':
            payment_account = add_money(payment_account, input('\nВведите сумму для пополнения счета: '))
        elif choice == '2':
            payment_account, history = bue(payment_account, history, input('\nВведите сумму покупки: '))
        elif choice == '3':
            shopping_list(history)
        elif choice == '4':
            break
        else:
            print('\nНеверный пункт меню\n')
