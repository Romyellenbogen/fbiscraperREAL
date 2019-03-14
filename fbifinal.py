from urllib.request import urlopen
from bs4 import BeautifulSoup
from selenium import webdriver
import time
import csv

file = open('fbi.csv', 'w', newline="", encoding="utf-8")
c = csv.writer(file)
c.writerow(['Name', 'Charges', 'Date', 'Birthplace', 'Sex', 'Race', 'Occupation', 'Nationality', 'Reward', 'Remarks', 'Summary'])

with open('fbi.txt') as f:
    content = f.readlines()

content = [x.strip() for x in content]

personInfo = []


def fugitive_detail(fugURL):
    driver = webdriver.Chrome('C:/Users/romyj/Documents/UF/Senior/webapps/python/scraping/chromedriver')
    driver.get(fugURL);
    html = driver.page_source
    bsObj = BeautifulSoup(html, "html.parser")
    name = bsObj.find("h1", {"class": "documentFirstHeading"})
    charges = bsObj.find("p", {"class": "summary"})
    try:
        table = bsObj.find("table", {"class" : "wanted-person-description"})
    except:
        dob = "N/A"
        bplace = "N/A"
        sex = "N/A"
        race = "N/A"
        job = "N/A"
        nat = "N/A"
    if table:
        dob = "N/A"
        bplace = "N/A"
        sex = "N/A"
        race = "N/A"
        job = "N/A"
        nat = "N/A"
        rowList = table.find_all("tr")
        for row in rowList:
            td = row.find("td")
            if td.get_text() == "Date(s) of Birth Used":
                dob = td.next_sibling.next_sibling.get_text()
            elif td.get_text() == "Place of Birth":
                bplace = td.next_sibling.next_sibling.get_text()
            elif td.get_text() == "Sex":
                sex = td.next_sibling.next_sibling.get_text()
            elif td.get_text() == "Race":
                race = td.next_sibling.next_sibling.get_text()
            elif td.get_text() == "Occupation":
                job = td.next_sibling.next_sibling.get_text()
            elif td.get_text() == "Nationality":
                nat = td.next_sibling.next_sibling.get_text()
    else:
        dob = "N/A"
        bplace = "N/A"
        sex = "N/A"
        race = "N/A"
        job = "N/A"
        nat = "N/A"

    try:
        rewardPath = bsObj.find("div", {"class" : "wanted-person-reward"})
        reward = rewardPath.find("p")
    except:
        reward = "N/A"

    try:
        remarkPath = bsObj.find("div", {"class": "wanted-person-remarks"})
        remark = remarkPath.find("p")
    except:
        remark = "N/A"

    strippedP = ""
    try:
        cautionPath = bsObj.find("div", {"class" : "wanted-person-caution"})
        caution = cautionPath.find_all("p")
        for p in caution:
            strippedP += p.get_text()
    except:
            try:
                detailPath = bsObj.find("div", {"class" : "wanted-person-details"})
                caution = detailPath.find_all("p")
                for p in caution:
                    strippedP += p.get_text()
            except:
                caution = "N/A"

    personInfo = [name, charges, dob, bplace, sex, race, job, nat, reward, remark, strippedP]
    row = []
    for item in personInfo:
        try:
            row.append(item.get_text())
        except:
            row.append(item)
    c.writerow(row)
    time.sleep(2)
    driver.quit()


for details in content:
    fd = fugitive_detail(details)

f.close()
file.close()
