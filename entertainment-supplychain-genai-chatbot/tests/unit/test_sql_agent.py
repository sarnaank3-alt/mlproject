import pytest
from app.backend.sql_agent.agent import SQLAgent

@pytest.fixture
def sql_agent():
    return SQLAgent()

def test_safe_query_execution(sql_agent):
    query = "SELECT * FROM users WHERE id = %s"
    params = (1,)
    result = sql_agent.execute_query(query, params)
    assert result is not None
    assert isinstance(result, list)

def test_unsafe_query_execution(sql_agent):
    query = "SELECT * FROM users WHERE id = 1; DROP TABLE users;"
    params = ()
    with pytest.raises(ValueError, match="Unsafe query detected"):
        sql_agent.execute_query(query, params)

def test_parameterized_query(sql_agent):
    query = "SELECT * FROM users WHERE email = %s"
    params = ("test@example.com",)
    result = sql_agent.execute_query(query, params)
    assert result is not None
    assert isinstance(result, list)

def test_empty_query(sql_agent):
    query = ""
    params = ()
    with pytest.raises(ValueError, match="Query cannot be empty"):
        sql_agent.execute_query(query, params)