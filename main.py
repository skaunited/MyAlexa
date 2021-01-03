import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[17].id)

def talck(text):
    engine.say(text)
    engine.runAndWait()

talck("Hello, I am Elodie. How I can help you?")

def get_command():
    try:
        with sr.Microphone() as source:
            print('I am listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'elodie' in command:
                command = command.replace('alexa', '')
                print(command)
    except:
        pass
    return command


def execute_command():
    order = get_command()
    print("here the command without Alexa===> " + order)
    if 'play' in order:
        song = order.replace('play', '')
        print("here the order without Play===> " + song)
        talck('Okay I will playing' + song)
        print("I am playing...")
        pywhatkit.playonyt(song)
    elif 'time' in order:
        time = datetime.datetime.now().strftime('%I:%M %p')
        print("The time now is ====> "+ time)
        talck("Based on my watch right now is:" + time)
    elif 'tell me' in order:
        person = order.replace('tell me', '')
        personResult = wikipedia.summary(person,1)
        print("Here the person Result ===> "+ personResult)
        talck(personResult)
    elif 'do you love me' in order:
        talck("Sorry I do not")
    elif 'are you single' in order:
        talck("No I am in a relationship with the wifi")
    elif 'joke' in order:
        talck(pyjokes.get_joke())
    else:
        talck("Sorry I do not understand you, Could you say it again ?" )

while True:
     execute_command()
