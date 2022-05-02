# selenium 4
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.color import Color
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("http://deyson20.pelisgoogledrivehd.xyz")
assert "Página principal" in driver.title
elem = driver.find_element(by=By.XPATH, value="/html/body/div[2]/section/div[2]/div[2]/div/table/tbody/tr[last()]/td[8]/a")
elem.click()
assert "update" in driver.page_source
sl_veh = Select(driver.find_element(by=By.NAME, value="type"))
sl_veh.select_by_value("Autobus")
model = driver.find_element(by=By.NAME, value="model")
model.send_keys("ModelTestEdit")
plate = driver.find_element(by=By.NAME, value="license_plate")
plate.send_keys("PlateTestEdit")
color = driver.find_element(by=By.NAME, value="color")
color.send_keys("#FF00BB")
seats = driver.find_element(by=By.NAME, value="num_passengers")
seats.send_keys("1")
sl_ft = Select(driver.find_element(by=By.NAME, value="fuel_type"))
sl_ft.select_by_value("GLP")
photo = driver.find_element(by=By.NAME, value="imgVehicle")
photo.send_keys('C:\image_ds\\testEdit.jpg')
upd_btn = driver.find_element(by=By.NAME, value="update")
upd_btn.click()
assert "Vehicle Updated Successfully" in driver.page_source
##time.sleep(6)
driver.close()