import json

from bus_factor import __version__
from bus_factor.executor.executor import Executor
from util.testformatter import TestFormatter
from util.testclient import TestClient


def test_version():
    assert __version__ == '0.1.0'

def _execute_test_bus_factor(filename):
    github_client = TestClient()
    formatter = TestFormatter()

    current_test_data = json.loads(filename)

    github_client.load_results(current_test_data["client"])
    formatter.load_expected(current_test_data["expected"])

    executor = Executor(github_client, formatter)
    executor.execute(current_test_data.query_parameters)

def test_bus_factor():
    _execute_test_bus_factor("data/test_basic_case_returns_data.json")