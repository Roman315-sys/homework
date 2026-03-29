from src.processing import filter_by_state, sort_by_date
import pytest

@pytest.mark.parametrize('state, key, expected',[
    # Успешные сценарии
    ([{'id': 414288290, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
    {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}], "EXECUTED",
     [{'id': 414288290, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
    {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}]),
    # Ошибочные сценарии
    ([{'id': 414288290, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
    {'id': 939719570, 'state': 'EX', 'date': '2018-06-30T02:08:58.425572'}], "EXECUTED",
     [{'id': 414288290, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}]),

    ([{'id': 414288290, 'st': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}], 'EXECUTED', []),

    ([{'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
    {'id': 615064591, 'state': 'EX', 'date': '2018-10-14T08:21:33.419441'}],
     'CANCELED', [{'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'}])
])
def test_filter_by_state(state, key, expected):
    assert filter_by_state(state, key) == expected


@pytest.mark.parametrize('state, revers, expected',[
    # Успешные сценарии
    ([{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}, {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}, {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'}, {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}],
     True, [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}, {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}, {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'}, {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}]),
    ([{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}, {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}],False, [{'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}, {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}]),
    ([{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}, {'id': 615064591, 'state': 'CANCELED', 'date': '2019-07-03T18:35:29.512364'}],False,[{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}, {'id': 615064591, 'state': 'CANCELED', 'date': '2019-07-03T18:35:29.512364'}]),
    # Ошибочные сценарии
    ([{'id': 41428829, 'state': 'EXECUTED', 'dat': '2019-07-03T18:35:29.512364'}],True,[]),
    ([{'id': 41428829, 'state': 'EXECUTED', 'dat': '201-07-03T18:35:29.512364'}],True,[])
])
def test_sort_by_date(state, revers, expected):
    assert sort_by_date(state, revers) == expected

