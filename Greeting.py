from datetime import datetime
import pyttsx3

hour = datetime.now() # Current hour in 24 hr format
grt=""
def welcome(): # welcome function which greets the user based on the current time.
    name=input("May i know your good name please? ")
    h = hour.hour
    if h<12:
        grt="Good Morning!" # If the current time is less than 12pm
    elif h>=12 and h<17:
        grt="Good Afternoon!" # If the current time is less than 5pm
    else:
        grt="Good Evening!" 
    voice_msg(grt+name) # Passing the Greeting and name of the user to convert it into Voice message
    print("\n I am your codeforces chatbot I hope you are coding regularly \n I can help you in providing the programms in the area which you want to master it")

def voice_msg(var): # Converts the given text into Voice message
    speak = pyttsx3.init() # Initalizes the pyttsx3 package
    voices = speak.getProperty('voices')
    speak.setProperty('rate',170) # Making the speech rate less for more audibulity
    speak.setProperty('voice', voices[1].id) # Selecting a voice type 
    speak.say(var) # Converts text in the variable var into Voice Message
    speak.runAndWait()
