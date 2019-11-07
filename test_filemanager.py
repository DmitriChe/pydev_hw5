from file_manager import make_directory, delete_file_dir, change_dir
from os import path, mkdir, rmdir, getcwd


def test_make_directory():
    assert make_directory('delme') == 'Папка успешно создана', 'Test failed!!!'
    assert path.exists('delme'), 'Test failed!!!'

    rmdir('delme')


def test_delete_file_dir():
    mkdir('delme')
    assert delete_file_dir('delme') == 'Файл(папка) успешно удален!', 'Test failed!!!'
    assert delete_file_dir('delme') == 'Такого объекта не сущестует!', 'Test failed!!!'


def test_change_dir():
    if path.exists(path.join(getcwd(), 'delme')):
        rmdir('delme')
    mkdir('delme')
    fpath_start = getcwd()
    fpath_end = path.join(getcwd(), 'delme')
    assert change_dir('delme') == f'Вы перешли в деректорию: {fpath_end}', 'Test failed!!!'
    assert change_dir('..') == f'Вы перешли в деректорию: {fpath_start}', 'Test failed!!!'
    rmdir('delme')
    assert change_dir('delme') == 'Нет такой директории! Попробуйте еще раз.', 'Test failed!!!'

