import unittest
from selenium import webdriver


class GoogleSearch(unittest.TestCase):
    # must have function called setUp to instantiate web driver, original function is overridden
    def setUp(self):
        # setting up the driver here makes it so you don't have to instantiate a new web driver for every test function
        # now when a function is tested, it will automatically instantiate a web driver
        self.driver = webdriver.Chrome()

    # naming convention of having 'test' as first word in functions that you want to test
    def test_search_in_google(self):
        driver = self.driver
        # command get for opening the following website, will wait until page is fully loaded
        driver.get("https://www.google.com")
        # maximizes window
        driver.maximize_window()
        search_box = driver.find_element_by_name("q")
        # clears any potential pre-typed things inside the search_box
        search_box.clear()
        # types in the following string into the search box
        search_box.send_keys('FaceBook')
        search_box.submit()
        # found first link that showed up by class name
        link = driver.find_element_by_class_name("LC20lb")
        # click that link
        link.click()

    # must have method called tearDown to close, original function is overridden
    def tearDown(self):
        # quit method closes entire browser window, you can use .close() instead if you want to only kill one tab
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
