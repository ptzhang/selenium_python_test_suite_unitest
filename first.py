import unittest
from selenium import webdriver


class SearchText(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.implicitly_wait(5)
        cls.driver.maximize_window()
        cls.driver.get("https://www.google.com.au/")

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_search_by_text(self):
        self.search_field = self.driver.find_element_by_name("q")
        self.search_field.clear()
        self.search_field.send_keys("Selenium with Python")
        self.search_field.submit()

        lists = self.driver.find_elements_by_class_name("r")
        self.assertEqual(13, len(lists))

    def test_search_by_name(self):
        self.search_field = self.driver.find_element_by_name("q")
        self.search_field.clear()
        self.search_field.send_keys("Python Class")
        self.search_field.submit()
        lists = self.driver.find_elements_by_class_name("r")
        self.assertEqual(12, len(lists))


if __name__ == '__main__':
    unittest.main()
