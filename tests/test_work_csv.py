from unittest.mock import patch, MagicMock
from src.work_csv import load_csv, load_excel


@patch('builtins.open')
@patch('csv.DictReader')
def test_load_csv(mock_dict_reader, mock_open):
    mock_open.return_value.__enter__.return_value = []
    mock_dict_reader.return_value = [{'id': '1', 'name': 'Alice'}, {'id': '2', 'name': 'Bob'}]

    result = load_csv("C:/Users/user/Downloads/transactions.csv")
    result_2 = load_csv("C:/Users/user/Downloads/transactions_2.xlsx")

    assert result == [{'id': '1', 'name': 'Alice'}, {'id': '2', 'name': 'Bob'}]
    mock_dict_reader.assert_called_once()
    assert result_2 == []
    mock_dict_reader.assert_called_once()


@patch('os.path.getsize')
@patch('builtins.open')
@patch('csv.DictReader')
def test_load_csv_2(mock_dict_reader, mock_open, mock_getsize):
    mock_getsize.return_value = 0
    mock_open.return_value.__enter__.return_value = []
    mock_dict_reader.return_value = []

    result = load_csv("C:/Users/user/Downloads/transactions.csv")

    assert result == []
    mock_dict_reader.assert_not_called()


@patch('pandas.read_excel')
def test_load_excel(mock_read_excel):
    mock_df =  MagicMock()
    mock_df.to_dict.return_value = [{'id': '1', 'name': 'Alice'}, {'id': '2', 'name': 'Bob'}]

    mock_read_excel.return_value = mock_df

    result = load_excel("C:/Users/user/Downloads/transactions_excel.xlsx")

    assert result == [{'id': '1', 'name': 'Alice'}, {'id': '2', 'name': 'Bob'}]
    mock_read_excel.assert_called_once()


@patch('os.path.getsize')
@patch('pandas.read_excel')
def test_load_excel_2(mock_read_excel, mock_getsize):
    mock_getsize.return_value = 0

    mock_df = MagicMock()
    mock_df.to_dict.return_value = []

    mock_read_excel.return_value = mock_df

    result = load_excel("C:/Users/user/Downloads/transactions_excel.xlsx")

    assert result == []
    mock_read_excel.assert_called_once()
