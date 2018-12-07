import bs4, requests

def getEbayPrice(productUrl):
    res = requests.get(productUrl)
    res.raise_for_status()

    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    elems = soup.select('#prcIsum')
    elems[0].text.strip()
    return elems[0].text.strip()





price = getEbayPrice('https://www.ebay.com/itm/GF07-Magnetic-Car-Vehicle-GSM-GPRS-GPS-Tracker-Real-Time-Tracking-Locator-Device-/173533145447')
print('The price is ' + price)
