@echo off

for /f "tokens=2 delims==" %%a in ('wmic OS Get localdatetime /value') do set "dt=%%a"
set "YY=%dt:~2,2%" & set "YYYY=%dt:~0,4%" & set "MM=%dt:~4,2%" & set "DD=%dt:~6,2%"
set "HH=%dt:~8,2%" & set "Min=%dt:~10,2%" & set "Sec=%dt:~12,2%"
set "datestamp=%MM%-%DD%-%YYYY%"

sendEmail -f EMAILADDRESSYOUARESENDINGFROM@EMAIL.COM -u Daily News:  %datestamp% -m Attached is today's headlines! (RCP,Drudge,MORE) -a C:\\PATH\TO\SCRAPERPROGRAM\headlines.txt -a C:\\PATH\TO\SCRAPERPROGRAM\altheadlines.txt -t EMAILADDRESSYOUARESENDINGTO@EMAIL.COM -s smtp.gmail.com:587 -xu EMAILSENDINGFROM@EMAIL.COM -xp EMAILPASSWORDGOESHERE -o tls=yes

Timeout /t 002 /NOBREAK

sendEmail -f EMAILADDRESSYOUARESENDINGFROM@EMAIL.COM -u Daily Jobs:  %datestamp% -m Attached is today's Craigslist job listings! -a C:\\PATH\TO\SCRAPERPROGRAM\jobs.txt -t EMAILADDRESSYOUARESENDINGTO@EMAIL.COM -s smtp.gmail.com:587 -xu EMAILSENDINGFROM@EMAIL.COM -xp EMAILPASSWORDGOESHERE -o tls=yes

Timeout /t 002 /NOBREAK

sendEmail -f EMAILADDRESSYOUARESENDINGFROM@EMAIL.COM -u Daily Spreadsheet:  %datestamp% -m Attached is today's News Excel Spreadsheet! -a C:\\PATH\TO\SCRAPERPROGRAM\links.csv -t EMAILADDRESSYOUARESENDINGTO@EMAIL.COM -s smtp.gmail.com:587 -xu EMAILSENDINGFROM@EMAIL.COM -xp EMAILPASSWORDGOESHERE -o tls=yes

Timeout /t 010 && exit
