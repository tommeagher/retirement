import requests
from lxml import html

def mega():
    url = 'http://www.megamillions.com/'
    r = requests.get(url)
    tree = html.fromstring(r.content)
    dollars = tree.find_class('home-next-drawing-estimated-jackpot-dollar-amount')[0].text
    zeroes = tree.find_class('home-next-drawing-estimated-jackpot-million')[0].text
    cash = tree.find_class('home-next-drawing-estimated-jackpot-cash-option visible-desktop visible-tablet')[0].text.split(':')[1].strip()[1:]
    next = tree.find_class('home-next-drawing-date-top-day')[1].text.strip()
    record = {}
    record['dollars']=dollars
    record['zeroes']=zeroes
    record['cash']=cash
    record['next']=next
    return record

def power():
    url = 'http://www.powerball.com/pb_home.asp'
    r = requests.get(url)
    tree = html.fromstring(r.content)
    jackpot = tree.xpath('//*[@id="mainContent"]/div[3]/table[1]/tr[2]/td[14]/font/strong')[0].text
    dollars = jackpot.split()[0][1:]
    zeroes = jackpot.split()[1]
    cash = tree.xpath('//*[@id="mainContent"]/div[3]/table[1]/tr[4]/td[14]/font')[0].text.split('Cash')[0]
    record={}
    record['dollars']=dollars
    record['zeroes']=zeroes
    record['cash']=cash.strip()
    return record

if __name__=='__main__':

