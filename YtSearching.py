from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

class music():
    def __init__(self):
        self.driver_service = Service(executable_path="C:\Program Files (x86)\Google\Chrome\chromedriver.exe")
        self.driver = webdriver.Chrome(service=self.driver_service)

    def play(self,query):
        self.query = query
        self.driver.get(url ="https://www.youtube.com/results?search_query="+query)
        search = self.driver.find_element(by=By.XPATH, value='//*[@id="video-title"]/yt-formatted-string')
        search.click()
