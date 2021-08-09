import requests
import json
import bs4
import smtplib
import time
import os
import pandas as pd
from columnar import columnar
from email.message import EmailMessage
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

res = pd.DataFrame()

# key function used for sorting by price column
def sort_by_price(val):
    return val[3]

def soup_listing_call():
    base_url="https://search.mlslistings.com"
    property_uri=f"/Matrix/Public/Portal.aspx?ID=0-886769211-10&eml=YXBlZXIwMDdAZ21haWwuY29t&L=1#1"
    property_listing_request = requests.post(url=f"{base_url}{property_uri}")
    soup = bs4.BeautifulSoup(property_listing_request.content, 'lxml')
    return soup

def parse_soup_houses():
    houses_data = []

    # capture all divs in HTML that match house listing square with details about the house in it
    divs = soup.find_all("div", {'class':'d1347m_show'})
    for div in divs:
        address = div.find('div', {'class':'d-color--brandDark'}).text
        city = div.find_all('span', {'class':'J_formula'})
        beds = div.find_all('span', {'class':'d-textStrong d-paddingRight--4'})[0].text
        baths = div.find_all('span', {'class':'d-textStrong'})[1].text
        price = div.find('span', {'class':'d-fontSize--largest'}).text
        status_badge = div.find('span', {'class':'mtx-subheader-badge'}).text
        open_house = div.find_all("div", {'class':'d1385m_show'})
        for row in open_house:
            if "Open House Date / Time" in row.text:
                open_house = row.text.strip().replace('Type\nOpen House Date / Time\n\n\nIn Person\n','')
                break
        for c in city:
            if "california" in c.text.lower():
                city = c.text
                break
        # add final prop info to data array
        if len(open_house) == 0:
            open_house = "Not available for viewing"
        houses_data.append([address + city, beds, baths, price, status_badge, open_house])

    # sort house list by price
    houses_data.sort(key=sort_by_price)
    return houses_data

def print_house_table(houses, prev_houses, email_address, email_password, receiver):
    # print the data out in a nice view
    headers = ['Property', 'Beds', 'Baths', 'price','status','open house']
    table = columnar(houses, headers, no_borders=False)
    print(table)

    if len(houses) != len(prev_houses):
        houses_msg = ""
        for house in houses:
            house_msg = ""
            for item in house:
                houses_msg += f"{item} "
            houses_msg += f'{house_msg}\n'

        with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
            smtp.ehlo()
            smtp.starttls()
            smtp.ehlo()

            smtp.login(email_address, email_password)

            msg = MIMEMultipart('alternative')
            msg['Subject'] = "New Listing Found in San Jose"
            msg['From'] = email_address
            msg['To'] = receiver
            part1 = MIMEText(str(houses_msg), 'plain')
            msg.attach(part1)
            smtp.sendmail(email_address, receiver, msg.as_string())
    else:
        print("Not Sending out email because there are no new changes!")
    prev_houses = houses
    return prev_houses

    
if __name__ == "__main__":
    EMAIL_ADDRESS = os.getenv("EMAIL_ADDRESS")
    EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")
    RECEIVER = os.getenv("RECEIVER_EMAIL_ADDRESS")

    prev_houses = []
    while True:
        houses_data = parse_soup_houses(soup_listing_call())
        prev_houses = print_house_table(houses_data, prev_houses, EMAIL_ADDRESS, EMAIL_PASSWORD, RECEIVER)
        time.sleep(60*60*4)
        print("4 hour has passed. Checking to see if there are new updates in San Jose Houses")
