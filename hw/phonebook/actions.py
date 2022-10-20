import database as db

phonebook = {}


def init_phonebook():
    database = db.get_data()
    for line in database:
        contact = line.split(' — ')
        phonebook[contact[0]] = contact[1]


def is_contact_exists(name):
    return name in phonebook


def get_no_contact_error(name):
    return f'Контакта {name} не существует'


def get_duplicate_error(name):
    return f'Контакт с именем {name} уже есть в телефонной книге'


def get_phone(name):
    return phonebook[name]


def set_new_contact(name, phone):
    contact = db.prepare_data(name, phone)
    phonebook[contact[0]] = contact[1]
    db.insert_to_db(contact)
    print(f'Контакт сохранен')
