import speech_recognition as sr
import webbrowser
import pyttsx3
import musicLibrary
import requests
from openai import OpenAI
from gtts import gTTS
import pygame
import os


r = sr.Recognizer()
engine= pyttsx3.init()
newsapi = " "



def speak_old(text):
     engine.say(text)
     engine.runAndWait()

def speak(text):
      tts = gTTS(text)
      tts.save('temp.mp3')
      pygame.mixer.init()
      pygame.mixer.music.load('temp.mp3')
      pygame.mixer.music.play()
      while pygame.mixer.music.get_busy():
           pygame.time.Clock().tick(10)
     
      pygame.mixer.music.unload()           
      os.remove("temp.mp3")
      
      
      
def aiprocess(command):
     client = OpenAI(api_key = "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",) 
     completion = client.chat.completions.create(
        model = "gpt-3.5-turbo",
        messages = [
      {"role":"system","content":"you are a virtual assistant named jarvis skilled in general like Alexa and Google Cloud.Give short responses please "},
      {"role":"user","content":command}
      
  ]
)    
     return completion.choices[0].message.content
def processcommand(c):
     if "open google" in c.lower():
          webbrowser.open("https://google.com")
     elif"open facebook" in c.lower():
          webbrowser.open("https://facebook.com")    
     elif"open youtube" in c.lower():
          webbrowser.open("https://youtube.com") 
     elif"open linkedin" in c.lower():
          webbrowser.open("https://linkedin.com")
     elif c.lower().startswith("play"):
           song =c.lower().split(" ")[1]
           link=musicLibrary.music[song]
           webbrowser.open(link)
     elif "news" in c.lower():
          r =requests.get(f"https://newsapi.org/v2/top-headlines?country=in&apiKey={newsapi}")
          if r.status_code == 200:
               
               data = r.json()
               
               
               articles = data.get('articles', [])
               
              
               for article in articles:
                    speak(article['title'])   
     else:
         output = aiprocess(c)
         speak(output)
          

         
          
if __name__ == "__main__":
     speak("Initializing Jarvis....   ")
     while True :

          # Listen for the wake word "jarivis"
          # obtain audio from the microphone
          r = sr.Recognizer()
        
        # recognize speech using sphinx
          print("recognizing ....")
          try:

               with sr.Microphone() as source:
                    print("Listening...")
                    r.adjust_for_ambient_noise(source, duration=1)
                    audio = r.listen(source, timeout=10,phrase_time_limit=8)
                              
               word = r.recognize_google(audio)
               if word.lower() == "jarvis":
                    speak("ya")
                    # listen for the command
                    with sr.Microphone() as source:
                         print("jarvis active")
                         audio = r.listen(source)
                         command = r.recognize_google(audio)
                         processcommand(command)
          except Exception as e:
               print("Error;{0}".format(e))     
                
      
     

