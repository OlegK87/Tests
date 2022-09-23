from main2 import folder_creation
import pytest

class TestYandex:
    fixture = [("test", 201), ("test", 409)]

    @pytest.mark.parametrize("argument, expected_result", fixture)
    def test_folder_creation(self, argument, expected_result):
        assert folder_creation(argument) == expected_result


