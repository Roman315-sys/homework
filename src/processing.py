def filter_by_state(state: list, key: str = "EXECUTED") -> list:
    """Фильтрует список словарей по значению ключа 'state'"""
    new_list = []
    for item in state:
        if item.get("state") == key:
            new_list.append(item)
    return new_list


def sort_by_date(data_list: list, reverse: bool = True) -> list:
    """Сортирует список словарей по указанному полю с датой"""
    new_list = []
    for item in data_list:
        if item.get("date") is None:
            continue
        elif len(item.get("date")) != 26:
            continue
        else:
            new_list.append(item)
    return sorted(new_list, key=lambda x: x.get("date"), reverse=reverse)