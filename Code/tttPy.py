from os import system as cmd
from time import sleep
import paho.mqtt.client as paho

text = { 958 : "a", 900 : "3",847 : "h",797 : "e",747 : "l",697 : "o",644 : "f",
         588 : "Please help me",526 : "Hi there",372 : "I want water",
         276 : "I am hungry",154 : "ok"} 
prev = ""
delay = 0.5
QoS = 1
client = paho.Client()
client.on_message = on_message  
client.connect("iot.eclipse.org", 1883)
client.subscribe(topic = "teethSensor", qos = QoS)
client.loop_start()

def on_message(client, userdata, msg):              
    inText = str(msg.payload.decode("utf-8"))
    print(intext)
    outText = inText[3:len(inText)]
    inText = inText[0:3]
    text[inText] = outText
    
try:
    while 1:
        i = 0
        file = open("at.txt","r")
        receive = file.read()
        file.close()
        file = open("at.txt","w")
        file.write("")
        file.close()
        if(len(receive) < 1):
            sleep(delay)
            continue
        receive = receive[4:len(receive)]
        receive = int(receive)
        print(receive)
        if(receive > 1000):
            sleep(delay)
            continue
        for i in text:
            if( receive >= i - 10 and receive <= i + 10 ):
                break
        if(len(text[i]) > 1):
            prev = text[i]
            txt = "espeak \""+prev+"\" -s 120 -p 44 -a 200"
            print(prev)
            cmd(txt)
            prev = ""
            sleep(delay)
            continue
        if(text[i] == "3"):
            print(prev)
            txt = "espeak \""+prev+"\" -s 120 -p 44 -a 200"
            cmd(txt)
            prev = ""
            sleep(delay)
            continue
        prev = prev + text[i]
        sleep(delay)
except KeyboardInterrupt:
    exit (0)
