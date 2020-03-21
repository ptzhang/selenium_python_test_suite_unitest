import unittest
from first import SearchText
from second import HomePageTest

search_text_test = unittest.TestLoader().loadTestsFromTestCase(SearchText)
home_page_test = unittest.TestLoader().loadTestsFromTestCase(HomePageTest)

test_suite = unittest.TestSuite([search_text_test, home_page_test])

unittest.TextTestRunner(verbosity=2).run(test_suite)
