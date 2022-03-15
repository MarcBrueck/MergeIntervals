import pytest
from merge_algorithm import IntervalCombinator

test_list1 = [[25, 30], [2, 19], [14, 23], [4, 8]]
test_list2 = [[14, 19], [12, 29], [-3, 12], [-3, 1], [31, 34]]
test_list3 = [[3, 6]]
test_list4 = [[14, 'abs'], [12, 29], [-3, 12], [-3, 1], [31, 34]]
test_list5 = [[14, 16], [12, 29], 3, [-3, 1], [31, 34]]

combinator = IntervalCombinator()

def test_number1():
    test_list = combinator.merge(test_list1)
    assert test_list == [[2, 23], [25, 30]]

def test_number2():
    test_list = combinator.merge(test_list2)
    assert test_list == [[-3, 29], [31, 34]]

def test_number3():
    test_list = combinator.merge(test_list3)
    assert test_list == [[3, 6]]

def test_number4():
    with pytest.raises(Exception):
        combinator.merge(test_list4)

def test_number5():
    with pytest.raises(Exception):
        combinator.merge(test_list5)

