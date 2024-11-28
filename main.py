from bs4 import BeautifulSoup
import requests #Sends requests to get url., and get responses back

url = requests.get('https://realpython.com/atom.xml') #Create the url
#print(url)#Prints http response code[200], meaning response request was successful

soup = BeautifulSoup(url.content,'xml')

#Loop through each entry in the feed and look for the title, link and summary

entries = soup.find_all('entry')

for entry in entries:
    title = entry.title.text
    summary = entry.summary.text
    link= entry.link['href']
    print(f"Title: {title}\n\nSummary: {summary}\n\nLink: {link}\n\n----------------------------------------------\n\n")