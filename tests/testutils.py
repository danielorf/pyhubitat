import pytest
import httpx

from pyhubitat import RuleMachineAPI

RULES_LIST = [{"1": "rule_number_1"}, {"5": "rule_number_5"}, {"99": "rule_number_99"}]

@pytest.fixture
def rule_machine_obj():
    HUB_TOKEN = 'fake_token'
    HUB_URL_EXAMPLE = 'http://hubitat.local/apps/api/123/trigger'  # Follow the generic format of 'https://[hub-ip-address-or-hostname]/apps/api/[app-id]/trigger'
    rm = RuleMachineAPI(HUB_TOKEN, HUB_URL_EXAMPLE)
    yield rm
    del rm
    

# custom class to be the mock return value of requests.get()
class MockListRulesResponse:
    @staticmethod
    def json():
        return RULES_LIST


# monkeypatched requests.get moved to a fixture
@pytest.fixture
def mock_list_rules(monkeypatch):
    """httpx.get() mocked to return {'mock_key':'mock_response'}."""

    def mock_get(*args, **kwargs):
        return MockListRulesResponse()

    monkeypatch.setattr(httpx, "get", mock_get)
