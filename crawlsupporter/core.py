class StaticCrawler:
    def __init__(self, header):
        self.headers = {"user-agent" : header}
        self.soup = None
        
    def get_header_soup(self, url, parser="html.parser"):
        req = requests.get(url, headers=self.headers)
        
        if req.status_code == 200:
            soup = BeautifulSoup(req.content, parser)
            return soup
        else:
            return req.status_code
            
    
    def get_soup(self, url, parser="html.parser"):
        req = requests.get(url)
        
        if req.status_code == 200:
            soup = BeautifulSoup(req.content, parser)
            return soup
        else:
            return req.status_code
    
    def set_soup(self, soup):
        self.soup = soup
        
    def find_css_selector(self, selector, is_all=False):
        if is_all == True:
            return self.soup.select(selector)
        else:
            return self.soup.select(selector)[0]
        
        
    def find_pattern_from_script(self, pat):
    
        pattern = re.compile(pat, re.MULTILINE | re.DOTALL)
        script = self.soup.find("script", text=pattern) 


        return pattern.search(script.text)
