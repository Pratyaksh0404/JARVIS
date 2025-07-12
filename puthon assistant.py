import pyttsx3
import speech_recognition as sr
import wikipedia
import datetime
import webbrowser
import os
import smtplib
import requests
import json

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishme():
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour < 12:
        speak('Good Morning')
    elif 12 <= hour < 18:
        speak('Good Afternoon')
    else:
        speak('Good evening')
    speak('How can i help you ?')


def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening to you ......')
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print('Recognizing your voice .....')
        query = r.recognize_google(audio, language='en-in')
        print(f'You said: {query}\n')
        return query
    except sr.UnknownValueError:
        print('Could not understand the audio')
        speak('Sorry, I could not understand what you said. Please say that again.')
        return 'None'
    except sr.RequestError as e:
        print(f'Could not request results; {e}')
        speak('Sorry, my speech service is down. Please try again later.')
        return 'None'
    except Exception as e:
        print(e)
        speak('Something went wrong. Please try again.')
        return 'None'


def sendEmail(to, content):
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.login('mail_id', 'your_key')
        server.sendmail('mail_id', to, content)
        server.close()
        speak('Your email has been sent successfully')
    except Exception as e:
        print(e)
        speak('Sorry, unable to send your email. Please address the error.')


if __name__ == '__main__':
    wishme()
    while True:
        query = takecommand().lower()
        if query == 'None':
            continue

        if 'wikipedia' in query:
            speak('Searching wikipedia ....')
            query = query.replace('wikipedia', "")
            results = wikipedia.summary(query, sentences=2)
            speak('According to wikipedia ')
            print(results)
            speak(results)

        elif 'notepad' in query:
            os.system('notepad.exe')

        elif 'youtube' in query:
            webbrowser.open('http://youtube.com')

        elif 'udemy' in query:
            webbrowser.open('http://www.udemy.com')

        elif 'google' in query:
            webbrowser.open('http://google.com')

        elif 'time' in query:
            curtime = datetime.datetime.now().strftime('%H:%M:%S')
            speak(f"The time is {curtime}")
            print(f"The time is {curtime}")

        elif 'linkedin' in query:
            webbrowser.open('http://www.linkedin.com')

        elif 'spotify' in query:
            os.system('spotify.exe')

        elif 'email to' in query:
            try:
                speak('What should I send?')
                content = takecommand()
                to = 'mail_id'
                sendEmail(to, content)
            except Exception as e:
                print(e)
                speak('Sorry, unable to send your email. Please address the error.')

        elif 'goodbye' in query or 'good bye' in query:
            speak('Goodbye! Have a great day!')
            break

