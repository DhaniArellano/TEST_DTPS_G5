# It's importing the libraries that are going to be used in the test.
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

# It's getting the path of the file that is running the test.
test_path = pathlib.Path(__file__).parent.absolute()

# It's a class that inherits from the unittest.TestCase class
class DtpsTest(unittest.TestCase):

    def setUp(self):
        """
        The above function will install the latest version of ChromeDriver and then use it to launch a
        Chrome browser
        """
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        unittest.TestLoader.sortTestMethodsUsing = None

    def test010_register(self):
        """
        It opens a web page, clicks a button, fills out a form, and then checks if the form was
        submitted successfully
        """
        driver = self.driver
        driver.get("http://deyson20.pelisgoogledrivehd.xyz")
        self.assertIn("Página principal", driver.title)
        elem = driver.find_element(by=By.XPATH, value="//button[@class='btn btn-primary']")
        elem.click()
        mod = driver.find_element(by=By.XPATH, value="//*[@id='RegistrarVehiculo']")
        # It's checking if the text "Seleccionar el tipo de vehículo" is in the page source.
        assert "Seleccionar el tipo de vehículo" in driver.page_source
        sl_veh = Select(driver.find_element(by=By.XPATH, value="//*[@id='RegistrarVehiculo']/div/div/form/div[1]/div/div[1]/select"))
        sl_veh.select_by_value("Motocicleta")
        model = driver.find_element(by=By.NAME, value="model")
        model.send_keys("ModelTest")
        plate = driver.find_element(by=By.NAME, value="license_plate")
        plate.send_keys("PlateTest")
        # It's finding the element by XPATH and assigning it to the variable color.
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
        # It's checking if the text "Se ha ingresado un nuevo vehículo al sistema" is in the page
        # source.
        assert "Se ha ingresado un nuevo vehículo al sistema" in driver.page_source

    def test020_edit(self):
        """
        It goes to the website, clicks on the last edit button, fills the form with new data and clicks
        on the update button.
        """
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
        """
        It clicks on the delete button of the last row of the table, accepts the alert, and then checks
        that the page has been redirected to the index page and that the task has been removed
        successfully
        """
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
        """
        The function closes the browser window that the driver has focus of
        """
        self.driver.close()

# It's a way to run the test from the command line.
if __name__ == "__main__":
    unittest.main()
