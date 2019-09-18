from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

BROWSER = Chrome()


def find_element(xpath, waittime=10, all=False):
    try:
        res = WebDriverWait(BROWSER, waittime).until(
            ec.presence_of_all_elements_located((By.XPATH, xpath))
        )
    except:
        return None
    if all:
        return res
    else:
        return res[0]


def click_on(xpath):
    element = find_element(xpath)
    if element:
        element.click()
    else:
        print("Could not find element to click on.")


def write_on(xpath, text):
    element = find_element(xpath)
    if element:
        element.send_keys(text)
    else:
        print("Could not find element to write on.")


BROWSER.get("https://instagram.com")

OPERATIONS = [
    {
        "xpath": "//button[contains(text(),'Log in with Facebook')]",
        "action": "click",
        "text": "",
    },
    {
        "xpath": "//input[@name='email']",
        "action": "write",
        "text": "username@email.com",
    },
    {
        "xpath": "//input[@name='pass']",
        "action": "write",
        "text": "passwordsaresecrets",
    },
    {"xpath": "//button[@value='Log In']", "action": "click", "text": ""},
    {"xpath": "//button[contains(text(),'Not Now')]", "action": "click", "text": ""},
]

for operation in OPERATIONS:
    if operation["action"].lower() == "write":
        write_on(operation["xpath"], operation["text"])
    elif operation["action"].lower() == "click":
        click_on(operation["xpath"])

