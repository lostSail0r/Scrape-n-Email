Headline and URL Scraper with built-in automatic email reporting - Python/Tkinter and Windows .bat<br><br>

<hr><img src="http://cgfixit.com/img/scrapeNemail.png"><hr>

***DOUBLE CLICK MAIN.PY to start program***<hr>You will notice if you change nothing cmd will give you path errors; just update the paths to where the unzipped Scrape-n-Email folder is located and it should work<br><br>

scrapes news headlines/urls,craigslist job posts, and exports RCP news into CSV file - Then sends them all (2 text files and 1 excel spreadsheet) as an email attachment<br>

*Please note even slight changes to website code will break the scrape if it is expecting objects that have been removed/re-named, but they are usually pretty easy to fix. 
<br>It looks like the RCP scrape may already be broken but the clistScraper still works wonders (love you craiglists for never changing) and the rest can be used as a template (Works on multiple versions but I recently confirmed still works on Python 3.7, although you will need dependencies like beautifulsoup installed<br><br>

sendEmail.exe credit goes to:<br>
sendEmail - Send email from a console near you!<br>
Written by: Brandon Zehm <caspian@dotconf.net><br>
http://caspian.dotconf.net/<br>
<br>

^^Python and Batch files are my original code, but I downloaded and integrated the sendEmail tool into the batch script - Just wanted to make sure he receives credit for the program that actually sends the email^^
