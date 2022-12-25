import requests
import json
f = open('studenti.txt', 'w')
API_KEY="7902fdd36701dc6dec8cefe73b86b7f3"
BASE_URL="http://api.openweathermap.org/data/2.5/weather"
city=input("introdu numele orasului: ")
request_url=f"{BASE_URL}?appid={API_KEY}&q={city}&units=metric"
response=requests.get(request_url)

if response.status_code==200:
    data=response.json()
    #print(data)
    vreme=data['weather'][0]['description']
    temperature=round(data["main"]["temp"],2)
    humidity=round(data["main"]['humidity'],2)
    # print("vremea: ", vreme)
    # print("temperatura: ",temperature)
    # print("umiditatea este de: ", humidity)
    f.write("Vremea este: "+ str(vreme)+"\n")
    f.write("Temperatura este: "+ str(temperature)+"\n")
    f.write("Umiditatea este: "+ str(humidity))
    f.close()
else:
    print("am intampinat o eroare")