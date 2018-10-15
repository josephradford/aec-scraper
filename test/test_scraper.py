#!/usr/bin/env python3

"""Tests for scraper project"""
import unittest
from scraper.scraper import SiteParser
import os
from bs4 import BeautifulSoup

class Test(unittest.TestCase):

    def setUp(self):
        self.test_dir = os.path.dirname(os.path.realpath(__file__))
        pass


    def tearDown(self):
        pass


    def testComboBoxParsed(self):
        with open(self.test_dir + "\\data\\Home - Annual Returns.html") as fp:
            soup = BeautifulSoup(fp, "html.parser")
        
        sp = SiteParser(soup)
        results = sp.get_combo_box("dropDownListPeriod")
        
        self.assertEqual(results[0]["value"], "1998-1999")
        self.assertEqual(results[0]["id"], "1")
        

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main(exit=False)
