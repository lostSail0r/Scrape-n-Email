#!/usr/bin/python
from bs4 import BeautifulSoup
import requests, io
import drudgeScraper

outputFile = open('altheadlines.txt', 'w+')

def offbeatScraper(): 
    a = 0
    xml = requests.get("https://www.sciencedaily.com/rss/strange_offbeat.xml")

    website = BeautifulSoup(xml.content,"xml")

    for article in website.find_all("item"):
        rawTitle = str(article.findAll("title"))
        rawLink = str(article.findAll("link"))
        rawDesc = str(article.findAll("description"))

        # Cleaning / formatting imported data
        title = rawTitle.replace("[<title>", "")
        title = title.replace("</title>]", "")
        
        link = rawLink.replace("[<link>", "URL: ")
        link = link.replace("</link>]", "")
        csvLink = link.replace("URL: ", "")

        desc = rawDesc.replace("[<description>", "Summary: ")
        desc = desc.replace(" <!-- more --></description>]", "")
        
        if (a < 5):
            outputFile.write(title + "\n" + desc + "\n" + link + "\n\n")
            drudgeScraper.writer(title, csvLink)
            a += 1


def mainScraper():
    a = 0
    xml = requests.get("https://www.sciencedaily.com/rss/all.xml")

    website = BeautifulSoup(xml.content,"xml")

    for article in website.find_all("item"):
        rawTitle = str(article.findAll("title"))
        rawLink = str(article.findAll("link"))
        rawDesc = str(article.findAll("description"))

        # Cleaning / formatting imported data
        title = rawTitle.replace("[<title>", "")
        title = title.replace("</title>]", "")
        
        link = rawLink.replace("[<link>", "URL: ")
        link = link.replace("</link>]", "")
        csvLink = link.replace("URL: ", "")

        desc = rawDesc.replace("[<description>", "SUMMARY: ")
        desc = desc.replace(" <!-- more --></description>]", "")

        if (a < 25):
            if (a == 0):
                outputFile.write("---\n\n")
            outputFile.write(title + "\n" + desc + "\n" + link + "\n\n")
            drudgeScraper.writer(title, csvLink)
            a += 1

def controller():
    offbeatScraper()
    mainScraper()
    outputFile.close()

if __name__ == "__main__":
    controller()
    exit()
