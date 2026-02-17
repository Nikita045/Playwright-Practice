import os
from datetime import datetime
import pytest

@pytest.fixture(scope="session")
def authenticated_context(browser):
    context = browser.new_context(storage_state="auth.json")
    yield context
    context.close()

def pytest_configure(config):
    reports_dir = "reports"
    os.makedirs(reports_dir, exist_ok=True)

    if config.option.htmlpath:
        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        config.option.htmlpath = os.path.join(
            reports_dir, f"report_{timestamp}.html"
        )