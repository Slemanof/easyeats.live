import pytest

@pytest.fixture(autouse=True)
def _mock_db_connection(mocker, db_connection):
    mocker.patch('db.database.dbc', db_connection)
    return True




