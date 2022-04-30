# selenium 4
import time
from lib2to3.pgen2.token import NAME
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from soupsieve import select
from selenium.webdriver.support.color import Color

from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get("http://deyson20.pelisgoogledrivehd.xyz")
assert "Página principal" in driver.title
""""
##elem.clear()
elem.send_keys("jhgjjj")
elem.send_keys(Keys.RETURN)
"""
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
color = driver.find_element(by=By.NAME, value="color")
color.send_keys("value","#FF0000")
time.sleep(2)
driver.close()

