import pytest

from src.phone import Phone


def test_repr():
    phone = Phone("iPhone 14", 120_000, 5, 2)
    assert repr(phone) == "Phone('iPhone 14', 120000, 5, 2)"

    with pytest.raises(ValueError):
        phone = Phone("iPhone 14", 120_000, 5, 0)


def test_setter():
    phone = Phone("iPhone 14", 120_000, 5, 2)
    phone.number_of_sim = 1
    assert phone.number_of_sim == 1

    with pytest.raises(ValueError):
        phone.number_of_sim = 0
