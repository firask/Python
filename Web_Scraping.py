import requests
from bs4 import BeautifulSoup
import csv

date = input("Enter rge date of the game in the the following formay MM/DD/YYYY: ")

page = requests.get(f"https://www.yallakora.com/match-center/?date={date}")

def main(page):
#Within the context of the pattern.web.Element class, .content is employed to retrieve the inner HTML content of an HTML element. This attribute allows you to extract the actual content encapsulated within the HTML tags.
    src = page.content
    #BeautifullSoup is the parser for the content of src variable that
    #convert the byte-code to readable format
    #lxml is a paraser
    soup = BeautifulSoup(src, "lxml")
    
    
main(page)