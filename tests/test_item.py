"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest

from src.item import Item


@pytest.fixture
def item_list():
    Item("Смартфон", 10000, 20)
    Item("Ноутбук", 20000, 5)
    return Item.all


def test_calculate_total_price(item_list):
    assert item_list[0].calculate_total_price() == 200_000
    assert item_list[1].calculate_total_price() == 100_000


def test_apply_discount(item_list):
    Item.pay_rate = 0.8
    item_list[0].apply_discount()

    assert item_list[0].price == 8_000
    assert item_list[1].price == 20_000
