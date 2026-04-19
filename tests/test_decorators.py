import pytest
from src.decorators import log


def test_log(capsys):
    """Тестирование декоратора, вывод результата в кансоль"""
    @log()
    def add(a, b):
        return a + b

    add(5, 3)

    captured = capsys.readouterr()
    assert "add ok" in captured.out
    assert "function result: 8" in captured.out
    assert "function operation time" in captured.out


def test_log_error(capsys):
    """Тестирование ошибки декоратора, вывод результата в кансоль"""
    @log()
    def add(a, b):
        return a + b
    with pytest.raises(TypeError):
        add(5, "2")

    captured = capsys.readouterr()
    assert "add error: TypeError" in captured.out
    assert "inputs: (5, '2')" in captured.out


def test_log_writes_file(tmp_path):
    """Тест записи логов в файл"""
    log_file = tmp_path / "mylog.txt"
    @log(filename=str(log_file))
    def add(a, b):
        return a + b

    add(3, 5)

    assert log_file.exists()

    log_file.read_text(encoding='utf-8')
    assert f'add ok\n ' f'function result 8\n'


def test_log_writes_error(tmp_path):
    """Тест записи логов в файл (вариант с ошибкой)"""
    @log(filename=str(tmp_path / "mylog.txt"))
    def add(a, b):
        return a + b

    assert tmp_path.exists()
    with pytest.raises(TypeError):
        add(3, "5")
    assert f"add error: TypeError. inputs: (3, '5'), "
