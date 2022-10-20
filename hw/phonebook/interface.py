from os.path import exists
import database as db
import actions as act
import data_provider as dp


def show_menu():
    print('1 — Добавить новый контакт')
    print('2 — Показать контакт')
    print('6 — Закрыть приложение')
    return input('Укажите пункт меню: ')


def add_contact():
    name = dp.get_name()
    if act.is_contact_exists(name):
        print(act.get_duplicate_error(name))
    else:
        phone = dp.get_phone()
        act.set_new_contact(name, phone)


def view_contact():
    name = dp.get_name()
    if act.is_contact_exists(name):
        print(f'{name}: {act.get_phone(name)}')
    else:
        print(act.get_no_contact_error(name))


# def run_app():
#     if exists(db.get_db_path()):
#         act.init_phonebook()
#
#     match show_menu():
#         case 1:
#             add_contact()
