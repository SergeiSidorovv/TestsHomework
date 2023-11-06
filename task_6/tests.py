import pytest

from main import NumberLists


def test_average_first_list():
    num_lists = NumberLists([1, 2, 3, 4], [3, 5, 7, 8])
    assert num_lists.average_value_first_list() == 2.5


def test_average_second_list():
    num_lists = NumberLists([1, 2, 3, 4], [3, 5, 7, 8])
    assert num_lists.average_value_second_list() == 5.75


def test_compare_values_first_more():
    num_lists = NumberLists([1, 2, 2, 2], [3, 1, 1, 1])
    av_first = num_lists.average_value_first_list()
    av_second = num_lists.average_value_second_list()
    assert num_lists.compare_values(
        av_first, av_second) == "Первый список имеет большее среднее значение"


def test_compare_values_second_more():
    num_lists = NumberLists([1, 2, 3, 4], [9, 9, 9, 9])
    av_first = num_lists.average_value_first_list()
    av_second = num_lists.average_value_second_list()
    assert num_lists.compare_values(
        av_first, av_second) == "Второй список имеет большее среднее значение"


def test_compare_values_equal():
    num_lists = NumberLists([1, 1, 1, 1], [1, 1, 1, 1])
    av_first = num_lists.average_value_first_list()
    av_second = num_lists.average_value_second_list()
    assert num_lists.compare_values(
        av_first, av_second) == "Средние значения равны"


def test_zero_division():
    num_lists = NumberLists([1, 1, 1, 1], [0, 0, 0, 0])
    with pytest.raises(ZeroDivisionError, match='Делить на ноль нельзя'):
        num_lists.average_value_first_list()

    with pytest.raises(ZeroDivisionError, match='Делить на ноль нельзя'):
        num_lists.average_value_second_list()
