"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest

from src.item import Item


@pytest.fixture
def item_list():
    Item("Смартфон", 10000, 20)
    Item("Ноутбук", 20000, 5)
    return Item.all


def test_repr(item_list):
    assert repr(item_list[0]) == "Item('Смартфон', 10000, 20)"
    assert str(item_list[0]) == 'Смартфон'


def test_calculate_total_price(item_list):
    assert item_list[0].calculate_total_price() == 200_000
    assert item_list[1].calculate_total_price() == 100_000


def test_apply_discount(item_list):
    Item.pay_rate = 0.8
    item_list[0].apply_discount()

    assert item_list[0].price == 8_000
    assert item_list[1].price == 20_000


def test_name_length(item_list):
    item_list[0].name = "CуперСмартфон"
    assert len(item_list[0].name) == 10


def test_instantiate_from_csv():
    Item.instantiate_from_csv('../src/items.csv')
    assert len(Item.all) == 5
    assert Item.all[0].name == 'Смартфон'


def test_string_to_number():
    assert Item.string_to_number('5') == 5
    assert Item.string_to_number('5.0') == 5
    assert Item.string_to_number('5.5') == 5

