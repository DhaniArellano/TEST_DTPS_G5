# selenium 4
import time
import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.color import Color
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.alert import Alert
import pathlib

test_path = pathlib.Path(__file__).parent.absolute()

class DtpsTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        unittest.TestLoader.sortTestMethodsUsing = None

    def test010_register(self):
        driver = self.driver
        driver.get("http://deyson20.pelisgoogledrivehd.xyz")
        self.assertIn("Página principal", driver.title)
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
        photo.send_keys(str(test_path)+'\images\\test.jpg')
        sl_ft = Select(driver.find_element(by=By.XPATH, value="//*[@id='RegistrarVehiculo']/div/div/form/div[1]/div/div[7]/select"))
        sl_ft.select_by_value("electricidad")
        reg_btn = driver.find_element(by=By.NAME, value="save_vehicle")
        reg_btn.click()
        time.sleep(3)
        assert "Se ha ingresado un nuevo vehículo al sistema" in driver.page_source

    def test020_edit(self):
        driver = self.driver
        driver.get("http://deyson20.pelisgoogledrivehd.xyz")
        self.assertIn("Página principal", driver.title)
        elem = driver.find_element(by=By.XPATH, value="/html/body/div[2]/section/div[2]/div[2]/div/table/tbody/tr[last()]/td[8]/a")
        elem.click()
        assert "update" in driver.page_source
        sl_veh = Select(driver.find_element(by=By.NAME, value="type"))
        sl_veh.select_by_value("Autobus")
        model = driver.find_element(by=By.NAME, value="model")
        model.clear()
        model.send_keys("ModelTestEdit")
        plate = driver.find_element(by=By.NAME, value="license_plate")
        plate.clear()
        plate.send_keys("PlateTestEdit")
        color = driver.find_element(by=By.NAME, value="color")
        color.send_keys("#FF00BB")
        seats = driver.find_element(by=By.NAME, value="num_passengers")
        seats.clear()
        seats.send_keys("1")
        sl_ft = Select(driver.find_element(by=By.NAME, value="fuel_type"))
        sl_ft.select_by_value("GLP")
        photo = driver.find_element(by=By.NAME, value="imgVehicle")
        photo.send_keys(str(test_path)+'\images\\testEdit.jpg')
        upd_btn = driver.find_element(by=By.NAME, value="update")
        upd_btn.click()
        assert "Vehicle Updated Successfully" in driver.page_source

    def test030_delete(self):
        driver = self.driver
        driver.get("http://deyson20.pelisgoogledrivehd.xyz")
        self.assertIn("Página principal", driver.title)
        elem = driver.find_element(by=By.XPATH, value="/html/body/div[2]/section/div[2]/div[2]/div/table/tbody/tr[last()]/td[8]/form/button")
        elem.click()
        alertText = Alert(driver).text
        assert("El vehiculo se eliminara permanentemente" in alertText)
        Alert(driver).accept()
        ##Alert(driver).dismiss()
        time.sleep(2)
        assert "http://deyson20.pelisgoogledrivehd.xyz/index.php" in driver.current_url
        assert "Task Removed Successfully" in driver.page_source

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()
