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
elem = driver.find_element(by=By.XPATH, value="//button[@class='btn btn-primary']")
elem.click()
mod = driver.find_element(by=By.XPATH, value="//*[@id='RegistrarVehiculo']")
assert "Seleccionar el tipo de vehículo" in driver.page_source
sl_veh = Select(driver.find_element(by=By.XPATH, value="//*[@id='RegistrarVehiculo']/div/div/form/div[1]/div/div[1]/select"))
sl_veh.select_by_value("Motocicleta")
model = driver.find_element(by=By.NAME, value="model")
model.send_keys("ModelTest")
plate = driver.find_element(by=By.NAME, value="license_plate")
plate.send_keys("PlateTest")
##color = driver.find_element(by=By.NAME, value="color").execute_script('color.value = arguments[0]', "#000")
color = driver.find_element(by=By.XPATH, value="//*[@id='RegistrarVehiculo']/div/div/form/div[1]/div/div[4]/input")
color.send_keys("#FF0000")
seats = driver.find_element(by=By.NAME, value="num_passengers")
seats.send_keys("4")
photo = driver.find_element(by=By.NAME, value="photoVehicle")
photo.send_keys('C:\image_ds\\test.jpg')
sl_ft = Select(driver.find_element(by=By.XPATH, value="//*[@id='RegistrarVehiculo']/div/div/form/div[1]/div/div[7]/select"))
sl_ft.select_by_value("electricidad")
reg_btn = driver.find_element(by=By.NAME, value="save_vehicle")
reg_btn.click()
time.sleep(3)
assert "Se ha ingresado un nuevo vehículo al sistema" in driver.page_source
driver.close()

