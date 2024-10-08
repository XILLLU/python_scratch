from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService

url = "https://www.betclic.pl/-super-kursy-s99"


chrome_path = r'C:\Users\milos\OneDrive\Pulpit\Coding\web_scraping\chromedriver.exe'

driver = webdriver.Chrome(executable_path=chrome_path)

driver.get(url)

driver.implicitly_wait(10)

html_text = driver.page_source


driver.quit()

soup = BeautifulSoup(html_text, 'html.parser')

target_element = soup.find_all('div', {'bc-gb-buttonspinner': True, 'class': 'oddButtonWrapper'})

type_of_bet = [element.find_all('span', class_="oddMatchName") for element in target_element]


for bets in type_of_bet:
    for bet in bets:
        print(bet.text.strip())
