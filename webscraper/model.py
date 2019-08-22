class Company:
    def __init__ (self, link, price, change, latestUpdate, ticker, company, earningsTime):
        self.link = link
        self.price = price
        self.change = change
        self.latestUpdate = latestUpdate
        self.ticker = ticker
        self.company = company
        self.earningsTime = earningsTime
        
    def printAllInfo(self):
        print("%s\t%s\t%s\t%s\t%s\t%s\t%s" % (self.link, self.ticker, self.company, self.earningsTime, self.price, self.change, self.latestUpdate))

    def printCompanyInfo(self):
        print("%s\t%s\t%s" % (self.ticker, self.company, self.price))
        
