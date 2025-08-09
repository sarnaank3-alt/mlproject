import pytest
from app.backend.tool_call.accounting import ToolCallAccounting

@pytest.fixture
def tool_call_accounting():
    return ToolCallAccounting()

def test_initial_tool_call_count(tool_call_accounting):
    assert tool_call_accounting.get_tool_call_count() == 0

def test_increment_tool_call_count(tool_call_accounting):
    tool_call_accounting.increment_tool_call()
    assert tool_call_accounting.get_tool_call_count() == 1

def test_tool_call_limit_enforcement(tool_call_accounting):
    tool_call_accounting.set_tool_call_limit(5)
    for _ in range(5):
        tool_call_accounting.increment_tool_call()
    assert tool_call_accounting.get_tool_call_count() == 5
    with pytest.raises(Exception, match="Tool call limit exceeded"):
        tool_call_accounting.increment_tool_call()

def test_reset_tool_call_count(tool_call_accounting):
    tool_call_accounting.increment_tool_call()
    tool_call_accounting.reset_tool_call_count()
    assert tool_call_accounting.get_tool_call_count() == 0

def test_tool_call_budget_exceeded_message(tool_call_accounting):
    tool_call_accounting.set_tool_call_limit(3)
    for _ in range(3):
        tool_call_accounting.increment_tool_call()
    message = tool_call_accounting.check_tool_call_budget()
    assert message == "You have reached your tool call limit. Please refine your query."