# selenium 4
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.color import Color
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.alert import Alert

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("http://deyson20.pelisgoogledrivehd.xyz")
assert "Página principal" in driver.title
elem = driver.find_element(by=By.XPATH, value="/html/body/div[2]/section/div[2]/div[2]/div/table/tbody/tr[last()]/td[8]/form/button")
elem.click()
alertText = Alert(driver).text
assert("El vehiculo se eliminara permanentemente" in alertText)
Alert(driver).accept()
##Alert(driver).dismiss()
time.sleep(2)
assert "http://deyson20.pelisgoogledrivehd.xyz/index.php" in driver.current_url
assert "Task Removed Successfully" in driver.page_source
driver.close()