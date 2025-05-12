import pytest
from main import hello
import time


def test_hello():
    assert hello() == "Hello, GitHub Actions!"


def test_hello_custom_name():
    assert hello("EPSI") == "Hello, EPSI!"


def test_hello_type_error():
    with pytest.raises(TypeError):
        hello(123)


def test_hello_performance():
    start = time.time()
    for _ in range(1000):
        hello("EPSI")
    duration = time.time() - start
    assert duration < 1


def test_hello_full_name():
    def hello_full(firstname="John", lastname="Doe"):
        return f"Hello, {firstname} {lastname}!"
    assert hello_full("Jane", "Smith") == "Hello, Jane Smith!"
