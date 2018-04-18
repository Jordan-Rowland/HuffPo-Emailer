import bs4
import os
import requests
import smtplib

url = 'http://huffingtonpost.com/'

email = ## EMAIL GOES HERE
password = ## PASSWORD GOES HERE

os.chdir(r'd:\downloads\python')

# Establish connection with email server

smtpObj = smtplib.SMTP('smtp.gmail.com', 587)
smtpObj.ehlo()
smtpObj.starttls()
smtpObj.login(email, password)

# Request URL, parst HTML for article text and link
res = requests.get(url)
res.raise_for_status()
soup = bs4.BeautifulSoup(res.text, 'html.parser')
articles = soup.select(".card__link")[0:10]

headlines = []

# Write to file read around Unicode
with open('HuffPo.txt', 'w+', encoding='utf-8') as f:
    for article in articles:
        f.write(f'{article.get_text()[:-2]}\n')
        f.write(f'{url}{article["href"]}\n')
        f.write('--------------------------------------\n')

# Read from file, append to list, strip unicode
with open('HuffPo.txt', 'rb') as f:
    for line in f.readlines():
        headlines.append(str(line.strip())[2:-1])


# Send email, then quit
smtpObj.sendmail(email, ##EMAIL GOES HERE,
                 f'Subject: HuffPo top 10 stories\n' + '\n'.join(headlines))

smtpObj.quit()
