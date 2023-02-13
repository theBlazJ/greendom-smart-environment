#Del kode napisan po navodilih vodiča: 
    #PiMyLifeUp 
    #https://pimylifeup.com/raspberry-pi-humidity-sensor-dht22/ 

 
#vstamimo modul za senzor in cas 
import Adafruit_DHT 
from datetime import datetime 

 
#definiramo senzor in pine 
DHT_SENSOR = Adafruit_DHT.DHT22 
DHT_PIN = 4 


#kadar senzor prebira temperaturo in vlago 
while True: 

    humidity, temperature = Adafruit_DHT.read_retry(DHT_SENSOR, DHT_PIN) 
    #Če je vlaga in temperatura znana 

    if humidity is not None and temperature is not None: 

        #program odpre datoteko vlaga in dejanje definira z besedo podatki 
        with open('vlaga.txt', "a") as podatki: 


            #V datoteko zapiše formatiran čas in parametre 
            podatki.write("Cas in datum: {0} Temperatura: {1:0.1f}*C  Vlaga: {2:0.1f}% \n".format(datetime.now(), temperature, humidity)) 


            #zapre datoteko 
            podatki.close() 

             
    #če dejanje spodleti izpiše sporočilo 
    else: 

        print("NAPAKA: Ni bilo mogoče pridobiti podatka o temperaturi ali vlagi") 