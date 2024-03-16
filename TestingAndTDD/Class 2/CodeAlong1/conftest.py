import pytest


@pytest.fixture
def mock_file():
    return "mock.csv"


@pytest.fixture
def test_list_42():
    return [
        {
            "id": "1",
            "first_name": "Idaline",
            "last_name": "Murrell",
            "email": "imurrell0@yale.edu",
            "gender": "Female",
            "age": "42"
        }
    ]


@pytest.fixture
def test_list_13():
    return [
        {
            "id": "1",
            "first_name": "Idaline",
            "last_name": "Murrell",
            "email": "imurrell0@yale.edu",
            "gender": "Female",
            "age": "13"
        }
    ]
