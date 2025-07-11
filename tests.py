import pytest
from function import get_tallest_hero

class TestFunction:

    param_list =[
        ['male', 'yes'],
        ['male', 'no'],
        ['female', 'yes'],
        ['female', 'no']
    ]

    @pytest.mark.parametrize('gender, job', param_list)
    def test_get_tallest_hero_correct_input_return_hero(self, gender, job):
        assert get_tallest_hero(gender, job) is not None

    param_list_negative = [
        ['Male', 'yes'],
        ['male', 'No'],
        ['', 'yes'],
        ['male', ''],
        [' ', 'yes'],
        ['male', ' '],
        [1, 'no'],
        ['female', 1],
        ['@male', 'yes'],
        ['male', '@no'],
        ['мужчина', 'yes'],
        ['male', 'да']
    ]

    @pytest.mark.parametrize('gender, job', param_list_negative)
    def test_get_tallest_hero_wrong_input_return_none(self, gender, job):
        assert get_tallest_hero(gender, job) is None