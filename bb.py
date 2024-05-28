from importlib.resources import path
from lib2to3.pgen2 import driver
from pathlib import Path
from re import search
from selenium import webdriver
from time import sleep, time
from selenium.webdriver.chrome.service import service
# service=service("C:\Program Files (x86)\chromedriver.exe")
Path ="C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(Path)
driver.maximize_window()
driver.get("https://cuchd.blackboard.com/")
print(driver.title)


driver.find_element_by_xpath("//*[@id='agree_button']").click()

sleep(2)
Username = "20BCS2920"
Password = "Manish@321"

driver.find_element_by_xpath("//*[@id='user_id']").send_keys(Username)
driver.find_element_by_xpath("//*[@id='password']").send_keys(Password)


driver.find_element_by_xpath("//*[@id='entry-login']").click()
sleep(2)


#search=driver.find_element_by_class_name("ng-pristine ng-valid ng-empty ng-touched")
search = driver.find_element_by_xpath('//*[@id="base-course-search"]/div/input')
search.send_keys("254")
search.send_keys("keys.RETURN")
time.sleep(5)  





















'''class login:
    def  __init__(self, username, password):
        
         self.opts = webdriver.ChromeOptions()
         self.opts.add_experimental_option("detach", True)
         self.driver  = webdriver.Chrome(options=self.opts)
        
         self.Username = username
         self.Password = password
        
         self.driver.get("https://cuchd.blackboard.com/")
         sleep(2)
        
         self.driver.find_element_by_xpath("//input[@name = 'Username']").send_keys(self.Username)
         self.driver.find_element_by_xpath("//input[@name = 'Password']").send_keys(self.Password)
        
         self.driver.find_element_by_xpath("//div[contains(text(), 'Sign In')]").click()
         sleep(2)
         login('20BCS2920','Manish@543')'''
         
         
