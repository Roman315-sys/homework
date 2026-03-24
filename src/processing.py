def filter_by_state(state: list, key: str = 'EXECUTED') -> list:
    """Фильтрует список словарей по значению ключа 'state'"""
    new_list = []
    for item in state:
        if item['state'] == key:
            new_list.append(item)
        else:
            continue
    return new_list


def sort_by_date(data: list, date_field: str) -> list:
    """Сортирует список словарей по указанному полю с датой"""
    pass
