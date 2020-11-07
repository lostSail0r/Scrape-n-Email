from bs4 import BeautifulSoup
import requests, io, csv, sys
import sciScraper, rcpScraper, clistScraper

def csvinit():
    with open('links.csv', 'a', newline='') as f:
            writer = csv.writer(f)
            writer.writerow( ('HEADLINE', 'URL') )
            writer.writerow( ('', '') )
            f.close()

def writer(title, link):
    with open('links.csv', 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow( (title, link) )
        f.close()

def scrape():

    i = 0
    n = 15

    drudge = requests.get("http://www.drudgereport.com/")
    soup = BeautifulSoup(drudge.content, 'html.parser')

    outputFile = open('headlines.txt', 'w+')

    outputFile.write('--------------\n--------------\nDrudge Headlines\n--------------\n--------------\n\n')
    try:
        for counter in range(1,n+1):
            for div in soup.findAll('div', {'id': 'app_topstories'}):
                a = div.findAll('a')[i]
                mainTitle = (a.text.strip())
                mainLink = (a.attrs['href'])
                outputFile.write(mainTitle + '\n' + mainLink + '\n\n')
                writer(mainTitle, mainLink)
                i += 1
    except IndexError:
        print("Scraping 'Da News...")

    # outputFile.write('--------------\nLeft Headlines\n--------------\n')
    i=0
    try:
        for counter in range(1,n+1):
            for div in soup.findAll('div', {'id': 'app_col1'}):
                a = div.findAll('a')[i]
                leftTitle = (a.text.strip())
                leftLink = (a.attrs['href'])
                outputFile.write(leftTitle + '\n' + leftLink + '\n\n')
                writer(leftTitle, leftLink)
                i += 1
    except IndexError:
        print("... Almost Done")

    # outputFile.write('--------------\nCenter Headlines\n--------------\n')
    i=0
    try:
        for counter in range(1,n+1):
            for div in soup.findAll('div', {'id': 'app_col2'}):
                a = div.findAll('a')[i]
                rightTitle = (a.text.strip())
                rightLink = (a.attrs['href'])
                outputFile.write(rightTitle + '\n' + rightLink + '\n\n')
                writer(rightTitle, rightLink)
                i += 1
    except IndexError:
        print("... Almost Done")

    # outputFile.write('--------------\nRight Headlines\n--------------\n')
    i=0
    try:
        for counter in range(1,n+1):
            for div in soup.findAll('div', {'id': 'app_col3'}):
                a = div.findAll('a')[i]
                rightTitle = (a.text.strip())
                rightLink = (a.attrs['href'])
                outputFile.write(rightTitle + '\n' + rightLink + '\n\n')
                writer(rightTitle, rightLink)
                i += 1
    except IndexError:
        print("... Almost Done")

    
    outputFile.close()

if __name__ == "__main__":
    csvinit()
    writer("~DRUDGE","  ~~~") 
    scrape()
    writer("~SCIENCEDAILY","  ~~~") 
    sciScraper.controller()
    writer("~REALCLEARPOLITICS","  ~~~") 
    rcpScraper.scrape()
    exit()

