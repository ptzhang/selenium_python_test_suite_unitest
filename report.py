import unittest
import HtmlTestRunner
import os
from first import SearchText
from second import HomePageTest

directory = os.getcwd()

search_text_test = unittest.TestLoader().loadTestsFromTestCase(SearchText)
home_page_test = unittest.TestLoader().loadTestsFromTestCase(HomePageTest)

test_suite = unittest.TestSuite([search_text_test, home_page_test])

outfile = open(directory + "\\SeleniumPythonTestSummary.html", "w")

runner = HtmlTestRunner.HTMLTestRunner(stream=outfile, report_title="Test Report", descriptions=True, combine_reports=True)

runner.run(test_suite)
