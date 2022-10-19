phonebook = {}
duplicate_error = 'Такой контакт уже есть'
absence_error = 'Контакта не существует'


def write_file(data):
    file = open('database/db.txt', 'w')
    file.write(f'{data}\n')
    file.close()


def init_phonebook():
    global phonebook
    file = open('database/db.txt', 'r')
    for line in file:
        contact = line.split(' — ')
        phonebook[contact[0]] = contact[1]


def get_key(key_name):
    global phonebook
    for key in phonebook.keys():
        if key == key_name:
            return key
    return 0


def get_contact(key_name):
    global phonebook
    if get_key(key_name) != 0:
        return f'{get_key(key_name)} — {phonebook[key_name]}'
    else:
        print(absence_error)


def set_new_data():
    global phonebook
    name = input('Имя: ')
    if get_key(name) == 0:
        number = input('Телефон: ')
        phonebook[name] = number
        contact = get_contact(name)
        write_file(contact)
        print(f'Контакт сохранен: {contact}')
    else:
        print(duplicate_error)
