import pytest

from src.actions.actions import ActionsLib, ActionObj

def test_action_obj():
    action = ActionObj('name', 100)
    assert action.action == 'name'

def test_actions_lib():
    a = ActionsLib()
    a.addAction('{"action":"jump","time":200}')
    a.addAction('{"action":"run","time":75}')
    a.addAction('{"action":"jump","time":100}')

    assert len(a.getStats()) == 2
    assert a.getStats()[0]['action'] == 'jump'
    assert a.getStats()[0]['avg'] == 150

    assert a.getStats()[1]['action'] == 'run'
    assert a.getStats()[1]['avg'] == 75

def test_actions_lib_errors():
    a = ActionsLib()
    with pytest.raises(Exception):
        a.addAction('{"time":200}')
    with pytest.raises(Exception):
        a.addAction('{"action":"run","timer":75}')
    with pytest.raises(Exception):
        a.addAction('broken')




