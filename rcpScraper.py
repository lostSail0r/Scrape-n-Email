from bs4 import BeautifulSoup
import requests, io
import drudgeScraper

def scrape():

    i = 0
    n = 25

    drudge = requests.get("https://www.realclearpolitics.com/")
    soup = BeautifulSoup(drudge.content, 'html.parser')

    outputFile = open('RCPheadlines.txt', 'w+')

    outputFile.write('--------------\n--------------\nRCP Headlines\n--------------\n--------------\n\n')
    try:
        for counter in range(1,n+1):
            for div in soup.findAll('div', {'class': 'story'}):
                a = div.findAll('a')[i]
                mainTitle = (a.text.strip())
                mainLink = (a.attrs['href'])
                if (i != 18): 
                    outputFile.write(mainTitle + '\n' + mainLink + '\n\n')
                    drudgeScraper.writer(mainTitle, mainLink)
                i += 1
    except IndexError:
        print(i)

    
    outputFile.close()

if __name__ == "__main__":
    scrape()
    exit()
