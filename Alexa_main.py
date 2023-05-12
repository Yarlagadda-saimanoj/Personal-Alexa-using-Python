import speech_recognition as sr
import os
import pyttsx3
import pywhatkit
import datetime
import warnings
import calendar
import random
import wikipedia

# ignore any warnings messages
warnings.filterwarnings('ignore')

# Record audio and return it as text
def recordAudio():
    # Record the audio
    r = sr.Recognizer()
    # Open microphone& start recording
    with sr.Microphone() as source:
        print('Listening...')
        audio = r.listen(source)

    # Use google speech recognition
    try:
        text = r.recognize_google(audio)
        print('You said: ' + text)
        return text
    except sr.UnknownValueError:
        print('Sorry, could not understand audio')
    # In case if service is disconnected
    except sr.RequestError as e:
        print('Service error: ' + str(e))

    return ''

def speak(text):
    # Initialize the text-to-speech engine
    engine = pyttsx3.init()
    # Set voice rate and volume
    engine.setProperty('rate', 150)
    engine.setProperty('volume', 1.0)
    # Speak the text
    engine.say(text)
    engine.runAndWait()

def iceBreakingWords(text):
    words = ['hey Alexa, how may I help you', 'okay Alexa', 'Alexa welcomes you']

    for w in words:
        if text in w.lower():
            return True

    return False

def getDate():
    now = datetime.datetime.now()
    current_date = datetime.datetime.today()
    current_day = calendar.day_name[current_date.weekday()]
    month = now.month
    day = now.day

    month_list = ['January', 'February', 'March', 'April', 'May', 'June', 'July','August', 'September', 'October', 'November', 'December']
    ordinal = lambda n: "%d%s" % (n, "tsnrhtdd"[(n // 10 % 10 != 1) * (n % 10 < 4) * n % 10::4])
    ordinal_list = [ordinal(n) for n in range(1,32)]

    return 'Today is '+current_day+' '+month_list[month-1]+' '+ordinal_list[day-1]

def greet(text):
    inputGreetWords = ['hi', 'hello', 'hey', 'hiya', 'sup']
    outputGreetWords = ['Hello, how can I help you?', 'Hey, what\'s up?', 'Hi there!', 'Hi, how can I assist you today?']

    for word in text.split():
        if word in inputGreetWords:
            return random.choice(outputGreetWords)

    return ''

def getPersonData(text):
    text_list = text.split()
    for i in range(0,len(text_list)):
        if i <= len(text_list) - 2 and text_list[i].lower() == 'who' and text_list[i+1].lower() == 'is':
            person = ' '.join(text_list[i+2:])
            return person

    return ''

while True:
    # Record audio and get text
    text = recordAudio()
    response = ''

    # If icebreaking words are detected, respond with a greeting
    if iceBreakingWords(text):
        response += greet(text)

    # If 'date' is in the command, get the current date
    if 'date' in text.lower():
        response += getDate()

    # If 'who is' is in the command, get information from Wikipedia
    if 'who is'
