from pyhubitat import RuleMachineAPI

from tests.testutils import rule_machine_obj, mock_list_rules, RULES_LIST

def test_list_rules(rule_machine_obj, mock_list_rules):
    rules = rule_machine_obj.list_rules()
    assert rules == RULES_LIST
    