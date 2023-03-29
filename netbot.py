from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from time import sleep

BROWSER = Firefox(executable_path="D:\Stranger\Downloads\geckodriver-v0.32.2-win64\geckodriver.exe")

BROWSER.get("http://192.168.1.1/status/device-info")


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

def read_text(xpath):
    element = find_element(xpath)
    if element:
        return element.text
    else:
        print("Could not find element to read.")
        return False


class Operation():
    def __init__(self, xpath):
        self.xpath = xpath
    def click(self):
        self.action = "click"
        return self
    def write(self,text):
        self.action = "write"
        self.text = text
        return self
    def read(self,retry_text=""):
        self.action = "read"
        self.retry_text = retry_text
        return self
        
    def perform(self):
        result = False
        if self.action.lower() == "click":
            result = click_on(self.xpath)
        elif self.action.lower() == "write":
            result = write_on(self.xpath, self.text)
        elif self.action.lower() == "read":
            result = read_text(self.xpath)
            # while(len(self.retry_text)>0 and self.retry_text in result):
            #     sleep(0.2)
            #     result = read_text(self.xpath)
            # print(result)
        else:
            if not bool(self.action): 
                print("No action associated with operation.")
            else:
                print("Unknown action associated with operation.")
        return result


setup = [
    Operation("//input[@name='username']").write("admin"),
    Operation("//input[@name='password']").write("apples"),
    Operation("//button/span[contains(text(),'Login')]").click(),
]
for op in setup:
    res = op.perform()
    if not res:
        break
    else:
        print(f"Completed {op.action} on <{op.xpath}>, Result: {res}")

uptime = Operation("/html/body/div/div/div[2]/div/div[2]/section/div/div[2]/div[1]/div/div/div/form/div[2]/div[5]/div[contains(text(),'seconds')]").read()
temp = Operation("/html/body/div/div/div[2]/div/div[2]/section/div/div[2]/div[1]/div/div/div/form/div[2]/div[8]/div[contains(text(),'.')]").read()

print("Uptime:",uptime.perform())
print("Temperature:",temp.perform())
