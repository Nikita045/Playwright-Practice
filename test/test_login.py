from pom.LoginPage import LoginPlayground
from playwright.sync_api import Page,expect
import pytest,json,os
from utils.data_loader import load_csv_data
#pytestmark = pytest.mark.smoke - all test in that file will be executed as part of smoke test
#multiple user data using parametrize fixture

@pytest.mark.smoke
@pytest.mark.parametrize("username,password,expected_message",
[("nikita","pwd","Welcome, nikita!"),("shivangi","pwd","Welcome, shivangi!"),
 ("simran","pwd","Welcome, simran!"),("manisha", "wrongpwd", "Invalid username/password"),])

def test_param_multiple_users_login(page:Page,username,password,expected_message):
    login_page=LoginPlayground(page)
    login_page.Login(username,password)
    expect(login_page.label_val).to_have_text(expected_message)

#user data load using json
"""""with open("test_data/users_data.json") as f:
    test_data=json.load(f)
@pytest.mark.parametrize("data", test_data)
def test_json_multiple_users_login(page:Page,data):
    login_page=LoginPlayground(page)
    login_page.Login(data["username1"],data["password1"])
    expect(login_page.label_val).to_have_text(data["expected"])
"""""
#user data load using csv
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
file_path = os.path.join(BASE_DIR, "test_data", "login_data.csv")

login_test_data = load_csv_data(file_path)

@pytest.mark.regression
@pytest.mark.parametrize("username2,password2,expected_message2", login_test_data)
def test_csv_login_data(page: Page, username2, password2, expected_message2):
    login_page=LoginPlayground(page)
    login_page.Login(username2,password2)
    expect(login_page.label_val).to_have_text(expected_message2)