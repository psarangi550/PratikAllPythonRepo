from selenium import webdriver
import unittest
driver=None
class NGWFMT_Login(unittest.TestCase):
    def setUp(self):
        pass
    def test(self):
        global driver
        driver = webdriver.Firefox(executable_path="C:\\Users\\611903295\\Downloads\\Driver\\geckodriver.exe")
        driver.get("https://en-gb.facebook.com/")
        print(driver.find_element_by_xpath("//div[@id='reg_pages_msg']/a").text)
    def tearDown(self):
        driver.close()
