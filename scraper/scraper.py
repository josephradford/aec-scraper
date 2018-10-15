#!/usr/bin/env python3

""""Classes used to scrape the AEC website"""

import mechanicalsoup

class AecSite(object):
    '''
    Access to the AEC website
    '''
    

    def __init__(self, typeString):
        '''
        Connect to AecSite
        '''
        self.baseAecUrl = "http://periodicdisclosures.aec.gov.au/"
        self.completeUrl = self.baseAecUrl + typeString + ".aspx"

        self.periods = []
        
        
        self.br = mechanicalsoup.StatefulBrowser()
        self.response = self.br.open(self.completeUrl)
        
        
    def is_connected(self):
        return self.response.status_code == 200
    
        
    def get_year_range(self):
        for option in self.br.get_current_page().find(id="dropDownListPeriod").find_all('option'):
            self.periods.append({"year":option.text,"id":option['value']})
        
            

class PartyScraper(object):
    '''
    Scraping party donation disclosure information
    '''


    def __init__(self, params):
        '''
        Constructor
        '''
        aec = AecSite("name")
        
        
    def read_data(self):
        '''
        import everything
        '''
        
