from bs4 import BeautifulSoup
import requests
import pandas as pd

all_rashis = []

def knowrashi(tag):
    """Return a url tag """
    url = f'https://www.astrosage.com/nepali/rashifal/{tag}.asp'
    return url
    
#  Multi-dimensional array i.e. dimension=1*12(Rashi's)
rashi =[["mesh-rashifal"],["vrishabha-rashifal"],["mithun-rashifal"],["karkat-rashifal"],["simha-rashifal"],["kanya-rashifal"],["tula-rashifal"],["vrishchika-rashifal"],["dhanu-rashifal"],["makara-rashifal"],["kumbha-rashifal"],["meen-rashifal"]]

for x in rashi:
    
    b = x.pop()
    a=knowrashi(b)
    
    source = requests.get(a).text
    soup = BeautifulSoup(source, 'lxml')

    class WebScrapper():

        
        """First attempt to scrap"""

        def __init__(self,html_class1,html_class2):
            """Initializing class"""
            self.html_class1=html_class1
            self.html_class2=html_class2

        def date(self):
            """Return a date"""
            content_box1 = soup.find('div', class_=self.html_class1).text
            return content_box1 
        
        def body_part(self):
            """Return a rashifal for the day"""
            content_box2 = soup.find('div', class_=self.html_class2).text
            return content_box2
            
    scrapper = WebScrapper("ui-large-hdg","ui-large-content text-justify")

    details ={
    'Date' : scrapper.date(),
    'Rashifal' : scrapper.body_part()}
    
    all_rashis.append(details)
 

df = pd.DataFrame(all_rashis)
print(df.head())

df.to_excel('astroage_horoscope.xlsx', index=False)

print('Finished')




