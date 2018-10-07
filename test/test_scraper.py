#!/usr/bin/env python3

"""Tests for scraper project"""
import unittest

from scraper import AecSite

class Test(unittest.TestCase):


    def setUp(self):
        pass


    def tearDown(self):
        pass


    def testYearRangeFetched(self):
        aec = AecSite("AnalysisParty")
        self.assertTrue(aec.is_connected())
        
        aec.get_year_range()
        
        self.assertEqual(aec.periods[0]["year"], "1998-1999")
        self.assertEqual(aec.periods[0]["id"], "1")
        

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
