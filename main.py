import cv2
import pyttsx3
import speech_recognition as sr
import pyautogui
import time
import face_recognition
import matplotlib.pyplot as plt
import pygetwindow as gw
import datetime
import smtplib
import requests
from bs4 import BeautifulSoup
import webbrowser
import pywhatkit as kit
import wikipedia
import os
import sys
import time
import psutil
import subprocess
import pyjokes
import handtrackingmodule as ht
from time import sleep
from fbchat import Client
from fbchat.models import *
import os.path

def click():
    pyautogui.click()

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices');
# print(voices[0].id)
engine.setProperty('voices', voices[len(voices) - 1].id)

def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()

known_image = face_recognition.load_image_file("C:\\Users\\ybbha\\Pictures\\Camera Roll\\profile.jpg")
known_face_encoding = face_recognition.face_encodings(known_image)[0]

# Initialize the webcam
video_capture = cv2.VideoCapture(0)

match_found = False  # Flag to track if a match is found

while not match_found:
    # Capture a frame from the webcam
    ret, frame = video_capture.read()

    # Find all face locations in the current frame
    face_locations = face_recognition.face_locations(frame)
    if len(face_locations) > 0:
        # Encode the faces in the current frame
        face_encodings = face_recognition.face_encodings(frame, face_locations)

        for face_encoding in face_encodings:
            # Check if the current face matches the known face
            matches = face_recognition.compare_faces([known_face_encoding], face_encoding)

            if any(matches):
                

                match_found = True
                print("Face matched successfully!")
                speak("Face matched successfully")
                  # Set the flag to exit the loop
                break  # Exit the loop after a successful match

    # Display the frame using matplotlib
    plt.imshow(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
    plt.pause(0.01)

    # Clear the current plot to update the displaypython "C:\Assistant\script.py"
    
    plt.clf()


# Release the webcam and close all windows
video_capture.release()


def speak(audio):
    print(audio)
    engine = pyttsx3.init()
    engine.say(audio)
    engine.runAndWait()

def click():
    pyautogui.click()

def username():
    username = psutil.users()
    for user_name in username:
        first_name = user_name[0]
        speak(f"Sir, this computer is signed to {first_name} as a username.")
    
def screenshot():
    pyautogui.screenshot(f"C://Users//ybbha//Pictures//Screenshots//1.png")

def battery():
    battery = psutil.sensors_battery()
    battery_percentage = str(battery.percent)
    plugged = battery.power_plugged
    speak(f"Sir, it is {battery_percentage} percent.")
    if plugged:
        speak("and It is charging....")
    if not plugged:
        if battery_percentage <= "95%":
            speak("Sir, plug charger.")

def shutDown():
    speak(f'Ok Sir   ')
    speak('Initializing shutdown protocol ')
    click()
    pyautogui.keyDown('alt')
    pyautogui.press('f4')
    pyautogui.keyUp('alt')
    pyautogui.press('enter')
    sleep(3)
    pyautogui.press('enter')

def restart():
    speak("Ok Sir    ")
    speak("Restarting your computer")
    click()
    pyautogui.keyDown('alt')
    pyautogui.press('f4')
    pyautogui.keyUp('enter')
    sleep(3)
    pyautogui.press('r')
    pyautogui.press('enter')

def Sleep():
    speak('Ok sir    ')
    speak("Initializing sleep mode")
    pyautogui.keyDown('alt')
    pyautogui.press('f4')
    pyautogui.keyUp('alt')
    sleep(2)
    pyautogui.press('s')
    pyautogui.press('s')
    pyautogui.press('enter')

def time():
    time = datetime.datetime.now().strftime('%I:%M:%S')
    speak(f"Sir, the current time is {time}.")

def date():
    year = int(datetime.datetime.now().year)
    month = int(datetime.datetime.now().month)
    date = int(datetime.datetime.now().day)
    speak(f"Sir, the current year is {year}, current month is {month} and the current date is {date}")

def google_search(audio_data):
    url = "https://www.google.com/search?q=" + audio_data
    webbrowser.open(url)
    speak(f"Sir, getting the result for {audio_data} from google.com")

def youtube_search(audio_data):
    url = "https:www.youtube.com/search?q=" + audio_data
    webbrowser.open(url)
    speak(f"Sir, getting the result for {audio_data} from youtube.com")

def volume():
    import pyautogui
    import time
    import subprocess

    # Path to your Python script
    script_path = r"C:\Assistant\script.py"

    # Open the command prompt and run the script
    subprocess.Popen(["cmd", "/c", f"python {script_path}"], shell=True)

    # Wait for the script to run (you may need to adjust this time based on your script's execution time)
    time.sleep(10)

    # Minimize the command prompt window
    pyautogui.hotkey('winleft', 'd')  # Minimize all windows and show the desktop

def command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.energy_threshold = 400
        r.dynamic_energy_threshold = True
        r.adjust_for_ambient_noise(source, duration=1)
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"user said: {query}")
        
        if 'tell me date'.lower() in query.lower() or 'date'.lower() in query.lower():
            date()
        elif 'hi'.lower() in query.lower() or 'sparkle'.lower() in query.lower() or 'hello'.lower() in query.lower():
            speak("hi yash sir, how are you")
        elif 'volume'.lower() in query.lower():
            volume()        
        elif 'fine'.lower() in query.lower():
            speak("thats great, how may I help you yash sir")            
        elif 'time'.lower() in query.lower() or 'what time is it'.lower() in query.lower() or 'tell time'.lower() in query.lower():
            time()
        elif 'thank'.lower() in query.lower():
            speak('No problem sir')
        elif 'open Google'.lower() in query.lower():
            webbrowser.open("https://www.google.com")
            speak("Opening google...")
        elif "open command prompt".lower() in query.lower():
            os.system("start cmd")      
        elif 'Google search'.lower() in query.lower():
            speak('What do you want to search')
            audio_data = command()
            google_search(audio_data)
        elif 'open YouTube'.lower() in query.lower():
            webbrowser.open("https://www.youtube.com")
            speak("Opening Youtube....")
        elif 'open portfolio'.lower() in query.lower():
            os.system("file:///D:/HTML%20Language%20Website%20Projects/Yash%20Portfolio/iPortfolio/iPortfolio/index.html")
        elif 'YouTube search'.lower() in query.lower():
            speak('What do you want to search?')
            pyautogui.hotkey('win', 'm')
            x_coordinate = 508
            y_coordinate = 287
            pyautogui.moveTo(x_coordinate, y_coordinate)
            audio_data = command()
            youtube_search(audio_data)
        elif 'open Facebook'.lower() in query.lower():
            webbrowser.open_new_tab("https://www.facebook.com")
            speak("Opening Facebook")
        elif 'open Gmail'.lower() in query.lower():
            webbrowser.open("https://mail.google.com/mail/u/0/#inbox")
            speak("Opening Gmail..")
        elif 'open maps'.lower() in query.lower() or 'show my location'.lower() in query.lower():
            webbrowser.open("https://www.google.com/maps/@26.6235458,87.3614451,16z")
            speak("Opening Maps...")       
        elif 'touch'.lower() in query.lower() or 'tap'.lower() in query.lower() or 'click'.lower() in query.lower():
            click()
        elif 'take screenshot'.lower() in query.lower() or 'screenshot'.lower() in query.lower():
            screenshot()
        elif "wikipedia".lower() in query.lower():
            speak("searching wikipedia....")
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query, sentences=2)
            speak("according to wikipedia")
            speak(results)
        elif "message to Yash".lower() in query.lower() or "to Yash".lower() in query.lower():
           python_program_path = 'C:\\Users\\ybbha\\Desktop\\Python Programs\\whatsapp.py'
           subprocess.run(['python', python_program_path])
        elif 'close window'.lower() in query.lower():
            pyautogui.keyDown('alt')
            pyautogui.press('f4')
            pyautogui.keyUp('alt')
            speak('Current window is closed.')
        elif 'battery percentage'.lower() in query.lower() or 'percentage in battery'.lower() in query.lower() or 'percent in my pc'.lower() in query.lower():
            battery()
        elif 'shutdown'.lower() in query.lower() or 'shut down'.lower() in query.lower() or 'close my PC'.lower() in query.lower():
            shutDown()
        elif 'sleep'.lower() in query.lower() or 'sleep mode'.lower() in query.lower() or 'jarvis quit'.lower() in query.lower():
            Sleep()
        # elif 'check message' in query or 'check messages' in query or 'check new messages' in query or 'check new message' in query or 'any new messages' in query or 'any new messages' in query or 'any new message' in query or 'any messages' in query or 'any message' in query:
        #     message()
        elif 'username'.lower() in query.lower() or 'user'.lower() in query.lower() or 'user name'.lower() in query.lower():
            username()
        elif 'play favourite song'.lower() in query.lower():
            musicPath = r"C:\Users\ybbha\Downloads\AllenW.m4a"
            os.system(f" {musicPath}")
        elif "set alarm".lower() in query.lower():
            nn = int(datetime.datetime.now().hour)
            if nn==22: 
                music_dir = 'E:\\music'
                songs = os.listdir(music_dir)
                os.startfile(os.path.join(music_dir, songs[0]))
#to find a joke
        elif "tell me a joke".lower() in query.lower():
            joke = pyjokes.get_joke()
            speak(joke)

        elif "shut down".lower() in query.lower():
            os.system("shutdown /s /t 5")

        elif "restart the system".lower() in query.lower():
            os.system("shutdown /r /t 5")

        elif "sleep the system".lower() in query.lower():
            os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")



        elif 'switch the window'.lower() in query.lower():
            pyautogui.keyDown("alt")
            pyautogui.press("tab")
            time.sleep(1)
            pyautogui.keyUp("alt")
                   
           

        elif "reset chat".lower() in query.lower():
            chatStr = ""
        elif "open camera".lower() in query.lower():
            cap = cv2.VideoCapture(0)
            while True:
                ret, img = cap.read()
                cv2.imshow('webcam', img)
                k = cv2.waitKey(50)
                if k==27:
                    break;
            cap.release()
            cv2.destroyAllWindows()
        elif 'open chat GPT'.lower() in query.lower():
            webbrowser.open("https://chat.openai.com/")

        elif 'open insta'.lower() in query.lower():
            webbrowser.open("https://www.instagram.com/")
            x_coordinate = 508
            y_coordinate = 287
            pyautogui.moveTo(x_coordinate, y_coordinate)
        elif 'open story'.lower() in query.lower():
            x_coordinate = 508
            y_coordinate = 287
            pyautogui.moveTo(x_coordinate, y_coordinate)
            click()
        elif 'back'.lower() in query.lower():
            x_coordinate = 1855
            y_coordinate = 172
            pyautogui.moveTo(x_coordinate, y_coordinate)
            click()
            click()
        elif 'video'.lower() in query.lower() or 'open reel'.lower() in query.lower():
            x_coordinate = 97
            y_coordinate = 500
            pyautogui.moveTo(x_coordinate, y_coordinate)
            click()
        elif 'reel Unmute'.lower() in query.lower() or 'Unmute'.lower() in query.lower():
            x_coordinate = 1326
            y_coordinate = 191
            pyautogui.moveTo(x_coordinate, y_coordinate)
            click()
        elif 'next'.lower() in query.lower():
            x_coordinate = 1248
            y_coordinate = 199
            pyautogui.moveTo(x_coordinate, y_coordinate)
            pyautogui.press('down')
        elif 'down'.lower() in query.lower():
            x_coordinate = 599
            y_coordinate = 498
            pyautogui.moveTo(x_coordinate, y_coordinate)
            pyautogui.press('down')
        elif "open whatsapp".lower() in query.lower():
            os.system(r"C:\Users\ybbha\Desktop\WhatsApp.lnk")
        elif 'who created you'.lower() in query.lower():
            speak("I have been created by sir yash bhaskar")

    except:
        return None
    return query

def greeting():
    
    x_coordinate = 1472
    y_coordinate = 438
    pyautogui.moveTo(x_coordinate, y_coordinate)
    click()
    speak('Welcome back yash sir i am Sparkle')
    time()
    date()

if __name__ == '__main__':
    greeting()
   
    speak("Getting battery information....")
    battery()

    while True:
        command()