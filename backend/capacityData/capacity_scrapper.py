import requests
from bs4 import BeautifulSoup
import pandas as pd

# Set the URL of the ASPX form
url = 'https://josaa.admissions.nic.in/applicant/seatmatrix/seatmatrixinfo.aspx'

#start session
session = requests.Session()

#get response
response = session.get(url)

#parsse html
soup=BeautifulSoup(response.text,'html.parser')

#get hidden attributes
viewstate=soup.find('input',attrs={'name':'__VIEWSTATE'})['value']
viewstategen=soup.find('input',attrs={'name':'__VIEWSTATEGENERATOR'})['value']
eventvalidaton=soup.find('input',attrs={'name':'__EVENTVALIDATION'})['value']

# Set the form data/payload
data = {
    '__EVENTTARGET':'ctl00$ContentPlaceHolder1$ddlInstType',
    '__EVENTARGUMENT':'',
    '__LASTFOCUS':'',
    '__VIEWSTATE':viewstate,
    '__VIEWSTATEGENERATOR':viewstategen,
    '__EVENTVALIDATION':eventvalidaton,
    'ctl00$ContentPlaceHolder1$ddlInstType': 'IIT',
    'ctl00$ContentPlaceHolder1$ddlInstitute': '0',
    'ctl00$ContentPlaceHolder1$ddlBranch':'0',
    'ctl00$ContentPlaceHolder1$btnSubmit':'Submit'
}

# Send the POST request
response = session.post(url, data=data)



# Check the response
if response.status_code == 200:
    # Request successful
    print('POST request sent successfully')
    # soup=BeautifulSoup(response.text,'html-parser')
    soup=BeautifulSoup(response.text,'html.parser')
    table=soup.find("table")

    df=pd.read_html(str(table))[0]
    df.to_csv("backend/capacityData/seat_capacity_current.csv",index=False)
    # get result and convert to HTML file
    # with open('seat_capacity_current.csv', 'w') as file:
    #     file.write(response.json())

else:
    # Request failed
    print('POST request failed')
    print('Status Code:', response.status_code)