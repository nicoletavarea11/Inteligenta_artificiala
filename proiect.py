from bs4 import BeautifulSoup
import pyautogui
import keyboard
import time
from selenium import webdriver
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup
import requests

ser = Service(r"C:/Users/Asus/Downloads/chromedriver_win32/chromedriver.exe")
driver = webdriver.Chrome(service=ser)
driver.get("https://www.emag.ro/search/telefoane?ref=effective_search")

def data_scraping ():
    f = open('date.txt', 'a')
    req=requests.get(driver.current_url)
    soup=BeautifulSoup(req.text,"html.parser")
    pret=soup.find('p', attrs={'class': 'product-new-price'}).text
    nume=soup.find('p', attrs={'class': 'page-title-mobile'}).text
    print("numele este: ", nume)
    print("pretul este: ", pret)
    f.write("Numele este: "+ str(nume))
    f.write("Pretul este: "+ str(pret)+"\n")
    f.close()    

def inapoi():#da pagina inapoi
    if pyautogui.locateOnScreen(r'C:\Users\nicol\OneDrive\Desktop\marina\an 3\inteligenta artificiala\sem\proiect\back.png', confidence=0.7) != None:
        back = pyautogui.locateOnScreen(r"C:\Users\nicol\OneDrive\Desktop\marina\an 3\inteligenta artificiala\sem\proiect\back.png", confidence=0.7)
        pyautogui.click(back) #dupa ce gaseste sageata de back, da click pe ea
    else:
        print('Imaginea back NU se afla pe ecran')
                 
def cautare_oferta():#apasa pe videoclipuri
    j=0
    while j<4:
        while not keyboard.is_pressed('esc'):
            x=382
            y=585
            pyautogui.click(x,y)
            data_scraping()
            time.sleep(10)
            inapoi()
            time.sleep(10)
            x=x+268
            pyautogui.click(x,y)
            data_scraping()
            time.sleep(10)
            inapoi()
            time.sleep(10)
            x=x+268
            pyautogui.click(x,y)
            data_scraping()
            time.sleep(10)
            inapoi()
            time.sleep(10)
            x=x+268
            pyautogui.click(x,y)
            data_scraping()
            time.sleep(10)
            inapoi()
            time.sleep(10)
            i=0
            while i<11:
              pyautogui.press('down')
              i=i+1 
    j=j+4 
    time.sleep(2) 
time.sleep(5)

cautare_oferta()