import pytest
from main import hello
import time

# Test de base
def test_hello():
    assert hello() == "Hello, GitHub Actions!"

# Test avec nom personnalisé
def test_hello_custom_name():
    assert hello("EPSI") == "Hello, EPSI!"

# Test de type incorrect
def test_hello_type_error():
    with pytest.raises(TypeError):
        hello(123)

# Test de performance
def test_hello_performance():
    start = time.time()
    for _ in range(1000):
        hello("EPSI")
    duration = time.time() - start
    assert duration < 1

# Test avec deux paramètres
def test_hello_full_name():
    def hello_full(firstname="John", lastname="Doe"):
        return f"Hello, {firstname} {lastname}!"
    assert hello_full("Jane", "Smith") == "Hello, Jane Smith!"
