from bs4 import BeautifulSoup
import requests, io, os
import drudgeScraper, rcpScraper, sciScraper, clistScraper

def main():
    drudgeScraper.scrape()
    rcpScraper.scrape()
    sciScraper.controller()
    clistScraper.scrape()

if __name__ == "__main__":
    main()
    os.system("email.bat")
    quit()
