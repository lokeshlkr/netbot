from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

BROWSER = Chrome()
BROWSER.get("https://instagram.com")


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
        return True
    else:
        print("Could not find element to click on.")
        return False


def write_on(xpath, text):
    element = find_element(xpath)
    if element:
        element.send_keys(text)
        return True
    else:
        print("Could not find element to write on.")
        return False


class Operation():
    def __init__(self, xpath, text=None):
        self.xpath = xpath
        self.text = text if text else ""
        self.action = "write" if text else "click"

    def perform(self):
        result = False
        if self.action.lower() not in ["click", "write"]:
            print("Unknown action associated with the operation.")
            result = False
        elif self.action.lower() == "click":
            result = click_on(self.xpath)
        else:
            result = write_on(self.xpath, self.text)
        return result


OPERATIONS = [
    Operation("//span[contains(text(),'Log in with Facebook')]"),
    Operation("//input[@name='email']", "ggwellplayed@yoyomail.com"),
    Operation("//input[@name='pass']", "passwordsaresecrets"),
    Operation("//button[@id='loginbutton']"),
    Operation("//button[contains(text(),'Not Now')]"),
]

for op in OPERATIONS:
    if not op.perform():
        break

