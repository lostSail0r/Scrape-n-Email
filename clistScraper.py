from bs4 import BeautifulSoup
import requests, io

def scrape():

    domain = "http://craigslist.com/"
    i = 0
    n = 10

    drudge = requests.get("https://atlanta.craigslist.org/search/web")
    soup = BeautifulSoup(drudge.content, 'html.parser')

    outputFile = open('jobs.txt', 'a')

    outputFile.write('---------------------\nWeb Dev Job Listings:\n---------------------\n')
    try:
        for counter in range(1,n+1):
            for job in soup.findAll('a', {'class': 'result-title hdrlnk'}):
                mainTitle = (job.text.strip())
                mainLink = (domain + job.attrs['href'])
                if (i < 10):
                    outputFile.write(mainTitle + '\n' + mainLink + '\n\n')
                i += 1
    except IndexError:
        print(i)

    
    outputFile.close()

if __name__ == "__main__":
    scrape()
    exit()
