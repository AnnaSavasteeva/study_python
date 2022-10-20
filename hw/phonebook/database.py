db_path = 'database/db.txt'


def get_db_path():
    return db_path


def prepare_data(name, phone):
    # здесь данные как-то обрабатываются
    return name, phone


def insert_to_db(data):
    db = open(db_path, 'w')
    db.write(f'{data[0]} — {data[1]}\n')
    db.close()


def get_data():
    return open(db_path, 'r')
