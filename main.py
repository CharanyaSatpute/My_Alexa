import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.setProperty('rate', 130)
engine.say('Hello, Im your Alexa')
engine.say('How can I help you?')
engine.runAndWait()


def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_command():
    command = ''
    try:
        while command == '' and 'alexa' not in command:
            with sr.Microphone() as source:
                print('listening...')
                listener.adjust_for_ambient_noise(source)
                voice = listener.listen(source, timeout=3)
                command = listener.recognize_google(voice)
                command = command.lower()
                print(command)
                if command == 'alexa':
                    talk('Yes, How can I help you?')
                elif 'alexa' in command:
                    command = command.replace('alexa', '')
                    print(command)
                else:
                    continue

    except Exception as e:
        print(e)
    return command


def run_alexa():
    command = take_command()
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing ' + song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk('Current time is ' + time)
    elif 'date' in command:
        date = datetime.date.today().strftime('%d-%m-%Y')
        print(date)
        talk('Todays date is ' + date)
    elif any(keyword in command for keyword in ('who is', 'what is', 'where is')):
        command = command.replace('who is', '').replace('what is', '').replace('where is', '')
        info = wikipedia.summary(command, 2)
        print(info)
        talk(info)
    elif 'are you single' in command:
        talk('I am in a relationship with wifi')
    elif 'joke' in command:
        talk(pyjokes.get_joke())
    elif command == '':
        command = take_command()
    else:
        talk('Please say the command again.')


while True:
    run_alexa()
