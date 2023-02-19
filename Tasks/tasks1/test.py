class ServiceDatabase(dict):
    def __str__(self):
        result = ''
        for key in self:
            histories = self[key]
            for elem in histories:
                for index, value in enumerate(elem):
                    elem[index] = str(value)
            str_histories = ["-".join(elem) for elem in histories]
            result += f'{key}: {";".join(str_histories)}\n'
        return result


technic = [
    ('Ноутбук', 1500, 'Татьяна', '89002001020'),
    ('Смартфон', 500, 'Анна',    '89202202325'),
    ('Проектор ', 300, 'Андрей', '89505205656'),
    ('Принтер', 750, 'Игорь',    '89303303236'),
    ('Планшет', 2300, 'Игорь',   '89303303236'),
    ('Смартфон', 1000, 'Андрей', '89505205656'),
    ('Ноутбук', 4800, 'Татьяна', '89002001020'),
    ('Наушники', 780, 'Марина',  '89562002350'),
    ('Сканер', 550, 'Сергей',    '89808564559'),
    ('Планшет', 1200, 'Анна',    '89202202325'),
    ('Ноутбук', 1100, 'Игорь',    '89303303236'),
    ('Смартфон', 3500, 'Татьяна', '89002001020')
]

total_clients_db = ServiceDatabase()


def optimization_data():
    phone_set = set(client[3] for client in technic)
    for phone in phone_set:
        start_history = [client for client in technic if client[3] == phone]
        client_name = start_history[0][2]
        total_history = [list(client)[0:2] for client in start_history]
        key = phone+' '+client_name
        total_clients_db[key] = total_history


