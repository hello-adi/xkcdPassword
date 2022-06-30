import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

PATH = "C:\Program Files (x86)\chromedriver.exe"

driver = webdriver.Chrome(PATH)

driver.get("https://www.craiyon.com/")

search = driver.find_element(By.ID, "prompt")

# try catch block for entering string into the prompt

search.send_keys("kanye best album")
search.send_keys(Keys.RETURN)

# print(driver.page_source)

time.sleep(120)

driver.close()
