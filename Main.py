
import pandas as pd
import requests
from bs4 import BeautifulSoup
print("Matthew was here  :D")
 
url = "https://www.dell.com/en-us/shop/dell-laptops/sr/laptops/alienware-laptops"
page = requests.get(url)
page = page.text
 
soup = BeautifulSoup(page, 'html.parser')
def findtitles(mainPage):
    pc_titles = []
    #names of pc
    title =print(soup.title.text)
    mainPage = soup.find_all("article")
    for articale in mainPage:
        pc_title=articale.find("h3",class_ ="ps-title")
        if pc_title == None:
            break
        pc_titles.append(pc_title.text)
    return(pc_titles)
 
#price of pc
def find_prices(mainPage):
    computer_prices = []
    for article in mainPage:
        price = article.find('div', class_ = 'ps-dell-price ps-simplified')
        computer_prices.append(price)

    return(computer_prices)



df = pd.DataFrame(columns=['name', 'price'])
names = ['Alienware', 'Dell', 'Mac']
price =  [300,275,250]

df['name'] = names
df['price'] = price

print(df['name'])