import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia as wp


import pyowm
owm = pyowm.OWM('657285c93eb1ca33d2e8f5764c9d84c7') # TODO: Replace <api_key> with your API key
mgr = owm.weather_manager()
sf = mgr.weather_at_place('kottayam')
temp=sf.weather.temperature('celsius')
hum=sf.weather.humidity


for key,value in temp.items():
    if 'temp_max' == key :
        max_temp=value
#wp.set_lang("hi") 

engine=pyttsx3.init()
voices=engine.getProperty('voices')

engine.setProperty('voice',voices[0].id)
engine.say('Iam jarvis ,what kind of help you want ')
engine.runAndWait()

def talk(text):
    engine.say(text)
    engine.runAndWait()

listner=sr.Recognizer()
def take():
     try :
         with sr.Microphone() as source:
             print('listening.....')
             voice=listner.listen(source)
             command=listner.recognize_google(voice)
             command=command.lower()
             

     except:
         pass
     return command

def runcommand():
    command=str(take())
    if 'jarvis' in command:
                 command=command.replace('jarvis','')
                 print(command)
                 if 'play' in command:
                      talk('playing')
                      song=command.replace('play','')
                      talk(song)
                      pywhatkit.playonyt(song)
                 elif 'time' in command :
                      time=datetime.datetime.now().strftime('%I:%M %p')
                      talk(time) 
                 elif 'temperature' in command :
                      talk('temperature is')
                      talk(max_temp)
                 elif 'humidity' in command :
                      talk('humidity is')
                      talk(hum)
                      #talk(hum)
                      #talk(max_temp) 
                 elif 'who is ' or 'what is ' in command:
                      person=command.replace('who is','')
                      
                      info=wp.summary(person,2)
                      print(info) 
                      talk('result'+info)
                 elif 'are you die' in command:
                      talk('ha'+''+''+''+'ha')
                      talk(' Iam still alive ') 
                 


                 
    else:
         talk('not recognisable')
      

runcommand()