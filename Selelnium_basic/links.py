# handlink link:
# click on link :


from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(5)
driver.get("https://www.google.com")
exception=driver.find_element(By.XPATH,"//textarea[@id='APjFqb']")
exception.send_keys("selinium")
driver.implicitly_wait(5)
exception.submit()
clickonoption1=driver.find_element(By.XPATH,'//h3[text()="Selenium"]')
driver.implicitly_wait(5)
clickonoption1.click()

