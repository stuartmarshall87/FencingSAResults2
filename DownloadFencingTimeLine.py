import urllib.request
from bs4 import BeautifulSoup
import re
from datetime import datetime
import json

year = 2023
url = 'https://fencingsa.org.au/' + str(year) + '-Results'
tournamentIndex = urllib.request.urlopen(url).read()

soup = BeautifulSoup(tournamentIndex, 'html.parser')
links = soup.find_all('a')
urls = []
for link in links:
    href = str(link['href'])
    if 'fencingtimelive' in href:
        urls.append(href)

for url in urls:
    tournamentIndex = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(tournamentIndex, 'html.parser')

    date = soup.find('h5')

    date_format = '%A %B %d, %Y'
    date = datetime.strptime(date.text, date_format)
    date = date.strftime('%Y%m%d')

    def getCategory(compName: str):
        if 'Open B' in compName:
            return 'OB'
        if 'Opeb B' in compName:
            return 'OB'
        if 'Kingsley B ' in compName:
            return 'O'
        if 'Open' in compName:
            return 'O'
        if 'Veteran' in compName:
            return 'V'
        if 'U17/U20' in compName:
            return 'U1720'
        if 'U20' in compName:
            return 'U20'
        if 'U17' in compName:
            return 'U17'
        if 'U15' in compName:
            return 'U15'
        if 'U13' in compName:
            return 'U13'
        if 'U11' in compName:
            return 'U11'
        if 'U9' in compName:
            return 'U9'
    
    def getGender(compName: str):
        if 'Mens' in compName:
            return 'M'
        if 'Men\'s' in compName:
            return 'M'
        if 'Womens' in compName:
            return 'W'
        if 'Women\'s' in compName:
            return 'W'
        if 'Boys' in compName:
            return 'B'
        if 'Boy\'s' in compName:
            return 'B'
        if 'Girls' in compName:
            return 'G'
        if 'Girl\'s' in compName:
            return 'G'
        if 'Mixed' in compName:
            return ''
        if 'Meredith Coleman' in compName:
            return ''
        
    def getWeapon(compName: str):        
        if 'Foil' in compName:
            return 'F'
        if 'Epee' in compName:
            return 'E'
        if 'Sabre' in compName:
            return 'S'
    
    soup = soup.find('table', {"class":"scheduleTable"})
    links = soup.find_all('a')
    for link in links:
        href = str(link['href'])
        compName = str(link.text).strip()
        if 'Team' in compName:
            continue
        category = getCategory(compName)
        gender = getGender(compName)
        weapon = getWeapon(compName)
        fileName = date + category + gender + weapon        
        
        compHome = urllib.request.urlopen('https://fencingtimelive.com' + href).read()
        soup = BeautifulSoup(compHome, 'html.parser')
        compLinks = soup.find_all('a', {"class":['nav-link', 'waves-light','waves-effect','waves-light']})
        for compLink in compLinks:
            if 'tableaus' in compLink['href']:
                tableauInfo = urllib.request.urlopen('https://fencingtimelive.com' + compLink['href'] + '/trees/').read()
                tableauInfo = json.loads(tableauInfo)
                tableau = urllib.request.urlopen('https://fencingtimelive.com' + compLink['href'] + '/trees/' + tableauInfo[0]['guid'] + '/tables/0/5').read()
                f = open(str(year) + '\\'+fileName + '.html', "a")
                f.write(str(tableau))
                f.close()
                break