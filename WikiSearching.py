from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By



class info():
    def __init__(self):
        self.driver_service = Service(executable_path="C:\Program Files (x86)\Google\Chrome\chromedriver.exe")
        self.driver = webdriver.Chrome(service=self.driver_service)

    def get_info(self,query):
        self.query = query
        self.driver.get(url ="https://www.wikipedia.org/")
        search = self.driver.find_element(by=By.XPATH, value='//*[@id="searchInput"]')
        search.click()
        search.send_keys(query)
        enter = self.driver.find_element(by=By.XPATH, value='//*[@id="search-form"]/fieldset/button/i')
        enter.click()

        #speak = self.driver.find_element(by=By.XPATH, value='// *[ @ id = "siteSub"]')
        #speak.click()
