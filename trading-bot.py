'https://finance.yahoo.com/gainers'
from selenium import webdriver
import time
import bs4 as bs
import urllib.request

class GetStockNum:
    def __init__(self):
        self.stock_data = []
        self.browser = webdriver.Chrome("C:\Program Files (x86)\chromedriver.exe")
        self.url = 'https://finance.yahoo.com/gainers'
        self.browser.get(self.url)
        time.sleep(3)
        
    def get_data(self):
        return self.stock_data
    
    def quit_browser(self):
        time.sleep(2)
        self.browser.quit()
        
    def Get_names(self):
        for x in range(1,25):
            self.symb = self.browser.find_element_by_xpath('//*[@id="scr-res-table"]/div[1]/table/tbody/tr['+str(x)+']/td[1]/a').text
            self.name = self.browser.find_element_by_xpath('//*[@id="scr-res-table"]/div[1]/table/tbody/tr['+str(x)+']/td[2]').text
            self.price = self.browser.find_element_by_xpath('//*[@id="scr-res-table"]/div[1]/table/tbody/tr['+str(x)+']/td[3]/span').text
            self.change = self.browser.find_element_by_xpath('//*[@id="scr-res-table"]/div[1]/table/tbody/tr['+str(x)+']/td[4]/span').text
            #adds to a list
            self.stock_data.append([self.symb, self.name, self.price, self.change])

    def print_data(self):
        print('-'*87)
        print(': SYMB       : NAME                                         : PRICE       : CHANGE    :')
        print('-'*87)
        for i in self.stock_data:
            print(":", i[0]," "*(9-len(i[0])),":",\
                  i[1]," "*(48-len(i[1])),":",\
                  i[2]," "*(10-len(str(i[2]))),":",\
                  i[3]," "*(8-len(str(i[3]))),":")
        print('-'*87)

class Single:
    def __init__(self, data):
        self.browser = webdriver.Chrome("C:\Program Files (x86)\chromedriver.exe")
        self.data = data
        self.stats = [] # list of the symbs
        self.single_stats = []         # for https://finance.yahoo.com/quote/WTCZF/history?p=WTCZF data
        self.all_single_stats = {}
        for syms in self.data:
            self.stats.append([syms[0]])
            self.all_single_stats[str(syms[0])]=[]
            
    def quit_browser(self):
        time.sleep(2)
        self.browser.quit()
        
    def add_data(self, stock):
        self.url = 'https://finance.yahoo.com/quote/'+stock+'/history?p='+stock
        self.browser.get(self.url)
        time.sleep(1)
        for x in range(1,10):# the 1,10 is howmane days to check 
            try:
                self.date = self.browser.find_element_by_xpath('//*[@id="Col1-1-HistoricalDataTable-Proxy"]/section/div[2]/table/tbody/tr['+str(x)+']/td[1]/span').text
                self.opened = self.browser.find_element_by_xpath('//*[@id="Col1-1-HistoricalDataTable-Proxy"]/section/div[2]/table/tbody/tr['+str(x)+']/td[2]/span').text
                self.high = self.browser.find_element_by_xpath('//*[@id="Col1-1-HistoricalDataTable-Proxy"]/section/div[2]/table/tbody/tr['+str(x)+']/td[3]/span').text
                self.low = self.browser.find_element_by_xpath('//*[@id="Col1-1-HistoricalDataTable-Proxy"]/section/div[2]/table/tbody/tr['+str(x)+']/td[4]/span').text
                self.closed = self.browser.find_element_by_xpath('//*[@id="Col1-1-HistoricalDataTable-Proxy"]/section/div[2]/table/tbody/tr['+str(x)+']/td[5]/span').text
            except Exception:
                pass
            self.single_stats.append([self.date, self.opened, self.high, self.low, self.closed])#stats[stock[0]].append([self.date, self.opened, self.high, self.low, self.closed])
            self.all_single_stats[stock].append([self.date, self.opened, self.high, self.low, self.closed])
        print('-'*84)
        print(':Date              :Opened         :High           :Low            :Closed         :')
        print('-'*84)
        
        for i in self.all_single_stats[stock]:
            print(":", i[0]," "*(15-len(i[0])),":",\
                  i[1]," "*(12-len(i[1])),":",\
                  i[2]," "*(12-len(str(i[2]))),":",\
                  i[3]," "*(12-len(str(i[3]))),":",\
                  i[4]," "*(12-len(str(i[4]))),":")
        print('-'*84)
        
        #time.sleep(1)
            

    
        
        
        


t = GetStockNum()
t.Get_names()
t.quit_browser()
t.print_data()

s = Single(t.stock_data)

for x in s.stats:
    print(x[0])
    s.add_data(x[0])

#s.add_data('ITRO')
s.quit_browser()
