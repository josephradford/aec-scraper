#!/usr/bin/env python3

""""Classes used to scrape the AEC website"""

import mechanize

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
        
        
        self.br = mechanize.Browser()
        self.response = self.br.open(self.completeUrl)
        
        
    def is_connected(self):
        return self.response.code == 200
    
        
    def get_year_range(self):
        try:
            self.br.select_form(nr=2)
        except:
            print ('Expected forms did not return')
            return False
                    
                    
        for ddItem in self.br.form.controls[3].items:
            self.periods.append({"year":ddItem.attrs["contents"],"id":ddItem.name})
        
        
            

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
        
