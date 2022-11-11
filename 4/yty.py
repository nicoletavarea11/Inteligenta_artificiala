import pyautogui
import keyboard
import time

def inapoi():#da pagina inapoi
    if pyautogui.locateOnScreen(r'C:\Users\nicol\OneDrive\Desktop\marina\an 3\inteligenta artificiala\sem\4\back.png', confidence=0.7) != None:
        back = pyautogui.locateOnScreen(r"C:\Users\nicol\OneDrive\Desktop\marina\an 3\inteligenta artificiala\sem\4\back.png", confidence=0.7)
        pyautogui.click(back) #dupa ce gaseste sageata de back, da click pe ea
    else:
        print('Imaginea back NU se afla pe ecran')
        
def cautare_google():#cauta bara de la google si introduce linkul spre un videoclip
    if pyautogui.locateOnScreen(r'C:\Users\nicol\OneDrive\Desktop\marina\an 3\inteligenta artificiala\sem\4\g.png', confidence=0.7) != None:
        camp_google = pyautogui.locateOnScreen(r"C:\Users\nicol\OneDrive\Desktop\marina\an 3\inteligenta artificiala\sem\4\g.png", confidence=0.7)
        pyautogui.click(camp_google)#da click pe bara
        time.sleep(2)#asteapta 2 secunde
        pyautogui.write("https://www.youtube.com/channel/UCdWmirD6MzuTFeUAtAv4TKQ/videos")#introduce linkul spre videoclip
        pyautogui.press('enter')#dupa ce introduce adresa, apasa enter
       
    else:
        print('Imaginea g NU se afla pe ecran')
              
# def cautare_googleabonare():#cauta imaginea cu aboneaza-te
#     if pyautogui.locateOnScreen(r'C:\Users\nicol\OneDrive\Desktop\marina\an 3\inteligenta artificiala\sem\4\a.png', confidence=0.7) != None:
#         abonare = pyautogui.locateOnScreen(r"C:\Users\nicol\OneDrive\Desktop\marina\an 3\inteligenta artificiala\sem\4\a.png", confidence=0.7)
#         pyautogui.click(abonare)#da click pe aboneaza-te dupa ce il gaseste 
#     else:
#         print('Imaginea a NU se afla pe ecran')
        
def cautare_googlevideo():#apasa pe videoclipuri
    while not keyboard.is_pressed('esc'):
        x=382
        y=585
        pyautogui.click(x,y)
        time.sleep(10)
        inapoi()
        time.sleep(10)
        x=x+268
        pyautogui.click(x,y)
        time.sleep(10)
        inapoi()
        time.sleep(10)
        x=x+268
        pyautogui.click(x,y)
        time.sleep(10)
        inapoi()
        time.sleep(10)
        x=x+268
        pyautogui.click(x,y)
        time.sleep(10)
        inapoi()
        time.sleep(10)
        i=0
        while i<7:
            pyautogui.press('down')
            i=i+1 
        
time.sleep(5)#asteapta 2 secunde
#cautare_google()#cauta bara de la google si deschide pagina de pe yt

# cautare_googleabonare()#apasa pe abonare
# time.sleep(7)#asteapta 7 secunde

cautare_googlevideo()#deschide videoclipurile de pe pagina


