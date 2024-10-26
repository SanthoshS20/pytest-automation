import constants, pytest

def pytest_addoption(parser):
    parser.addoption("--url", action="store")


@pytest.fixture(scope="session", autouse=True)
def set_env_variables(request):
    constants.BASE_URL = request.config.getoption("--url")


def pytest_sessionfinish(session, exitstatus):
    if exitstatus == 0:
        print("Test executed successfully")
    else:
        print("Test failed.")
