import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import csv
options = Options()
options.add_argument("--headless")
options.add_argument("--window-size=1920x1080")
driver = webdriver.Chrome(options=options, executable_path= r"chromedriver.exe")
driver.get("https://www.4icu.org/us/a-z/")
time.sleep(15)
print("\n\n\nPage loading...\n\n\n")
data = driver.execute_script('data = []; for(i=1; i<document.getElementsByClassName("table")[0].childNodes[3].childNodes.length - 2; i += 2) { data.push(document.getElementsByClassName("table")[0].childNodes[3].childNodes[i].childNodes[3].innerText);  }; return data;')
with open('data.csv', mode="r+") as file: 
    reader = csv.reader(file)
    oldData = [] 
    for line in reader: 
    	oldData.extend(line)
file.close() 
newData = []
for college in data: 
	if college not in oldData: 
		newData.append(college)
with open('data.csv', 'a+') as file:
    csv.writer(file).writerow(newData)
file.close()
category = [] 
categories = ["Print with name", "Print with abbreviations or acronyms", "Print with mascot or associated symbols", "Print with departments or area of study", "Print with physical landmark", "Print with niche or general cultural references"]
for college in newData: 
	for cat in categories: 
		category.append(college + " " + cat)
with open('category.csv', 'a+') as file:
    csv.writer(file).writerow(category)
file.close()
print(str(len(newData)) + " new colleges added to database")
driver.quit()