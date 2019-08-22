# earnings_whiteRow and earnings_greyRow have the contents for the default max number of viewable companies. May need to move to next page to see rest of companies.
# Each element of these two containers contains the html code for each row. The company ticker, earnings release time, and other information can be found within 
# the rows html code. 
#
# Add conditions when filtering through data


import model
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

class WebScraperHandle:
    def testingPrint(self):
        print("Printing from WebScraperHandle")

    def pageToPageSoup(self, url):
        # opening up connection, grabbing page
        uClient = uReq(url)
        page_html = uClient.read()
        uClient.close()

        # html parsing
        page_soup = soup(page_html, 'html.parser') 
        return page_soup


    # Implement try except when inspecting spans
    def inspectTicker(self, link):
        url_Ticker_Page = 'https://finance.yahoo.com'+link
        page_soup = self.pageToPageSoup(url_Ticker_Page)
        market_Quote_html = page_soup.find("div", {"class" :"My(6px) Pos(r) smartphone_Mt(6px)"}) # Start of HTML section that contains price, change and latestUpdate time
        all_spans = market_Quote_html.findAll("span")

        price = all_spans[0].string
        change = all_spans[1].string
        latestUpdate = all_spans[2].string

        return price, change, latestUpdate
    


    def analyzeData(self, dataSet):
        listOfCompanies = []
        for row in dataSet:
                link = row.td.a["href"]
                price, change, latestUpdate = self.inspectTicker(link)
                # Conditions to filter data 
                if(float(price) <= 10.0):
                        company = row.find('td', {'aria-label': 'Company'}).text
                        earningsTime = row.find('td', {'aria-label': 'Earnings Call Time'}).text
                        ticker = row.td.string
                
                        listOfCompanies.append(model.Company(link, price, change, latestUpdate, ticker, company, earningsTime))
                        print("Adding", ticker , price)
                else: 
                        print("Price above $10")
        
        return listOfCompanies


    def scrapeYahooEarningsCalander(self): 
        listOfCompanies = []
        url_Yahoo_Earnings_Calander = 'https://finance.yahoo.com/calendar/earnings/'
        page_soup = self.pageToPageSoup(url_Yahoo_Earnings_Calander)

        # Grabs rows of earnings report table
        earnings_whiteRow = page_soup.findAll("tr", {"class":"simpTblRow Bgc($extraLightBlue):h BdB Bdbc($finLightGrayAlt) Bdbc($tableBorderBlue):h H(32px) Bgc(white)"})
        earnings_greyRow = page_soup.findAll("tr", {"class":"simpTblRow Bgc($extraLightBlue):h BdB Bdbc($finLightGrayAlt) Bdbc($tableBorderBlue):h H(32px) Bgc($altRowColor)"})
        dataSet = earnings_whiteRow + earnings_greyRow
        
        listOfCompanies = self.analyzeData(dataSet)
        
        return listOfCompanies

        

def main():
    webscraper = WebScraperHandle()
    listOfCompanies = webscraper.scrapeYahooEarningsCalander()
    print("Size:", len(listOfCompanies))
    for company in listOfCompanies:
            company.printCompanyInfo()

if __name__ == '__main__':
    main()