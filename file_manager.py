import os
import sys
import shutil

from account import account
from victorina import victorina


def make_directory():

    folder_name = input('Введите имя папки: ')
    if not os.path.exists(folder_name):
        os.mkdir(folder_name)
        print('Папка успешно создана')
    else:
        print('Папка с таким именем уже существует - придумайте другое имя!')


def delete_file_dir():
    f_name = input('Введите имя папки(файла) для удаления: ')
    if os.path.exists(f_name):
        shutil.rmtree(f_name, ignore_errors=True)
        if os.path.exists(f_name):
            print('Файл НЕ удален!')
        else:
            print('Файл(папка) успешно удален!')
    else:
        print('Такого объекта не сущестует!')


def copy_file_dir():
    path_from = input('Введите название исходного файла(папки) для копирования: ')
    if os.path.exists(path_from):
        path_to = input('Введите новое название для копии файла(папки): ')
        if path_from == path_to:
            print('Имена исходного и конечного объектов должны быть разными! Попробуйте снова.')
        else:
            if os.path.exists(path_to):
                print('Объект с таким именем уже существует. Введите другое имя для копии.')
            else:
                if os.path.isfile(path_from):

                    shutil.copy(path_from, path_to)
                    if os.path.exists(path_to):
                        print('Объект успешно скопирован')
                    else:
                        print('Что-то пошло не так с этим копированием...')
                else:
                    shutil.copytree(path_from, path_to)
                    if os.path.exists(path_to):
                        print('Объект успешно скопирован')
                    else:
                        print('Что-то пошло не так с этим копированием...')
    else:
        print('Исходного объекта не существует, введите другое имя!')


def change_dir():
    dir_path = input('Введите путь к новой рабочей директори: ')
    if os.path.exists(dir_path):
        os.chdir(dir_path)
        print(f'Вы перешли в деректорию: {os.getcwd()}')
    else:
        print('Нет такой директории! Попробуйте еще раз.')


while True:
    print('\n1. создать папку')
    print('2. удалить (файл/папку)')
    print('3. копировать (файл/папку)')
    print('4. просмотр содержимого рабочей директории')
    print('5. посмотреть только папки')
    print('6. посмотреть только файлы')
    print('7. просмотр информации об операционной системе')
    print('8. создатель программы')
    print('9. играть в викторину')
    print('10. мой банковский счет')
    print('11. смена рабочей директории')
    print('0. выход')

    choice = input('Выберите пункт меню: ')
    if choice == '1':
        make_directory()
    elif choice == '2':
        delete_file_dir()
    elif choice == '3':
        copy_file_dir()
    elif choice == '4':
        print(os.listdir())
    elif choice == '5':
        print([x for x in os.listdir() if not os.path.isfile(x)])
    elif choice == '6':
        print([x for x in os.listdir() if os.path.isfile(x)])
    elif choice == '7':
        print(sys.platform)
    elif choice == '8':
        print('*** Build by Human Intelligence of DmitryChe! ***')
    elif choice == '9':
        victorina()
    elif choice == '10':
        account()
    elif choice == '11':
        change_dir()
    elif choice == '0':
        break
    else:
        print('\nНеверный пункт меню\n')
