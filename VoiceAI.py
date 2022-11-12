#pip install pyttsx3
import pyttsx3
#pip install SpeechRecognition
import speech_recognition as sr
#inbuilt module to access date and time
import datetime as dt
#pip install wikipedia
import wikipedia
#inbuilt module to open web browser
import webbrowser
#inbuilt modue to perform various os operations
import os
#pip install smtplib
import smtplib
#module to enable sql functionalities in python
import sqlite3
#inbuilt module to generate a random number
import random as r2
#inbuilt system module
import sys
#pip install wolframaplha (An API)
import wolframalpha
#pip install smtplib
import smtplib
#module used for GUI
from threading import *
#module used to create GUI
from tkinter import *
win=Tk()
win.title('Buddy')
win.geometry('630x700')
win.config(background="black")


usertext=StringVar()
comtext=StringVar()


conn = sqlite3.connect("contacts.db")


#defining a function that creates a GUI using tkinter
def new_GUI():

    root = Tk()
    root.geometry('650x750')
    root.title('Commands List')

    cmds="""                 

    1)Search Google keyword
        example: search google python or search google AI assistant
                
    2)Search Wikipedia keyword
        example: search Wikipedia python or search Wikipedia AI

    3)Send email -> To send an email  

    4)API services-> WOLF-RAM-ALPHA

    5)Google maps keyword
        example: google map delhi

    6)Open C Drive-> To Open C Drive   

    7)Play music-> To play Music

    8)Play video-> To play Video

    9)Search Youtube keyword
        example: search youtube python or search youtube AI assistant

    10)Open google, youtube, facebook, instagram, gmail, outlook, amazon,
        or stack-> To open google, youtube, facebook, instagram, gmail,
        outlook, amazon, or stackoverflow on browser

    11)The time-> To know the current time

    12)Go Offline/Nothing/Bye-> To close Application

    13)Shutdown-> To shutdown the Operating System

    14)Open 'Software Name'-> To open an installed software like word, etc.

    15)Open a file-> To search and open any file on the computer

    16)'any number'+'operator'+'any number'-> To calculate a simple
        mathematical operation. example: 2+5 

    """

    hpframe=LabelFrame(
        root,
        text="Commands:- ",
        font=('Black ops one',12,'bold'),
        highlightthickness=3)
    hpframe.pack(fill='both',expand='yes')

    hpmsg=Message(
        hpframe,
        text=cmds,
        bg='black',
        fg='#7adb1e'
        )
    hpmsg.config(font=('Comic Sans MS',10,'bold'),justify="left")
    hpmsg.pack(fill='both',expand='no')

    exitbtn = Button(
        root, 
        text='EXIT', 
        font=('#7adb1e', 11, 'bold'), 
        bg='red', 
        fg='white',
        borderwidth=5,
        command=root.destroy).pack(fill='x', expand='no')

    root.mainloop()


compframe=LabelFrame(
    win,
    text="Buddy ",
    font=('Lucida',10,'bold'),
    highlightthickness=2)
compframe.pack(fill='both',expand='yes')

left2=Message(
    compframe,
    textvariable=comtext,
    bg='#7adb1e',
    fg='black',
    justify='left'
    )

left2.config(font=('Lucida',12,'bold'),aspect=250)
left2.pack(fill='both',expand='yes')

userframe=LabelFrame(
    win,
    text="User",
    font=('Lucida',10,'bold'),
    highlightthickness=2,)
    
userframe.pack(fill='both',expand='yes')

left1=Message(
    userframe,
    textvariable=usertext,
    bg='black',
    fg='#7adb1e',
    justify='left'
    )
left1.config(font=('Lucida',12,'bold'),aspect=250)
left1.pack(fill='both',expand='yes')

#creating an engine for voice IO using sapi5
engine = pyttsx3.init('sapi5')

#connecting to wolframaplha API
client = wolframalpha.Client('497K74-LQ93WJ8229')

#giving a voice to the assistant
voices = engine.getProperty('voices')
#print(voices[1].id)
engine.setProperty('voice', voices[0].id)
comtext.set("""Hello! 
I am your Personal Assistant Buddy 

Click on Start button to give your Commands"""
            )
usertext.set(' ')


#this function prints output on GUI window
def printo(shan):
    global comtext
    comtext.set(shan)


#this function lets the assistant speak 
def speak(audio):
    
    printo(audio+"\n")
    engine.say(audio)
    engine.runAndWait()


#function to wish the user according to time
def wishMe():
    hour = int(dt.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning! " +name)

    elif hour>=12 and hour<18:
        speak("Good Afternoon! " +name)   

    else:
        speak("Good Evening! " +name)
        
    speak("""Hello {} 
How can I help you?""".format(name))
    speak("Click start speaking button to give Commands")
    usertext.set('''  Click start speaking button to give Commands''')


def Name():
    #It takes microphone input from the user and returns string output
    global r,source,audio,query,name
    name=" "
    r = sr.Recognizer()
    with sr.Microphone() as source:
        speak("What is your name")
        printo("Please tell me Your name\n")
        printo("Listening...\n")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        printo("Recognizing...\n")    
        name = r.recognize_google(audio, language='en-in') 
        

    except Exception as e:
        printo(e)    
        printo("Say that again please...\n") 
        speak("Say that again please...")
        Name() 
        return None
    return name
    wishMe()


#function to take commands form the user
def Commands():
    global r,source,audio,query,usertext
    r = sr.Recognizer()
    r.energy_threshold=2500
    with sr.Microphone() as source:
        printo("Listening...\n")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        printo("Recognizing...\n")
        query = r.recognize_google(audio, language='en-in') 
        usertext.set("User said:"+query+"\n")

    except Exception as e:
        # print(e)    
        printo("Say that again please...\n") 
        speak("Say that again please...")
        Commands() 
        return query
    return query


#function to search anything on google
def srch_google():
    speak("Seaching on Google.....\n")
    printo("Seaching on Google.....\n")
    try:
        text=r.recognize_google(audio)
        keywords=(text.split(" "))
        printo(keywords)
        del keywords[0]
        del keywords[0]
        printo(keywords)
        
        def listosrting(s):
            str1=" "
            new=str1.join(s)
            return new
        printo(listosrting(keywords))
        keyword=listosrting(keywords)

        printo("You said : {}\n".format(keyword))
        url='https://www.google.co.in/search?q='
        search_url=f'https://www.google.co.in/search?q='+keyword
        speak('searching on google' +" "+ keyword)
        webbrowser.open(search_url)
    except:
        printo("Can't recognize\n")


#function to search a place on google maps 
def srch_google_map():
    speak(" Searching on Google Map.....")
    printo("Searching on Google Map.....\n")
    try:
        text2=r.recognize_google(audio)
        keywords=(text2.split(" "))
        print(keywords)
        del keywords[0]
        del keywords[0]
        print(keywords)
        
        def listosrting(s):
            str1=" "
            new=str1.join(s)
            return new
        printo(listosrting(keywords))
        keyword=listosrting(keywords)

        print("You said : {}\n".format(keyword))
        search_url=f'http://maps.google.com/?q='+keyword
        speak('searching on google map' +" "+ keyword)
        webbrowser.open(search_url)
    except:
        printo("Can't recognize\n")


#function to search a video on youtube
def search_yt():
    speak("searching on youtube.....\n")
    printo("searching on youtube.....\n")
    try:
        text=r.recognize_google(audio)
        key=(text.split(" "))
        #print(keywords)
        del key[0]
        del key[0]
        #print(keywords)
        
        def lis(s):
            str1=" "
            new=str1.join(s)
            return new
    
        key=lis(key)

        print("You said : {}".format(key))
        url='http://www.youtube.com/results?search_query='
        search_url=f'http://www.youtube.com/results?search_query='+key
        speak('searching on youtube ' +" "+ key)
        webbrowser.open(search_url)
    except:
        print("Can't recognize")

#defining a function to send emails
def sendemail(to, content):
    #using smtplib module
     server = smtplib.SMTP('64.233.184.108', 587)
     server.ehlo()
     server.starttls()
     cursor = conn.execute("SELECT EMAIL, PASSWORD FROM CONTACTS WHERE SNO=1")
     uid = cursor[0]
     upass = cursor[1]
     server.login(uid, upass)
     server.sendmail(uid, to, content)
     server.close()


#function to search any file stored on this pc
def find_files(filename, search_path):
    for root, dir, files in os.walk(search_path):
        if filename in files:
            result = os.path.join(root, filename)
    return result


#The Main Function    
def mainfn():
    global query
    if __name__ == "__main__":
        Name()
        wishMe()
    #while True:


#function that recognizes the users command
def reco():   
    query = Commands().lower()
    print(query)
    # Logic for executing tasks based on query

    #if the user wants to search something on google
    if 'search google' in query:
        srch_google()

    #if the user wants to search something on youtube
    elif 'search youtube' in query:
            search_yt()

    #if the user wants to search something on wikipedia
    elif 'wikipedia' in query:
        speak('Searching Wikipedia...')
        query = query.replace("wikipedia", "")
        results = wikipedia.summary(query, sentences=3)
        speak("According to Wikipedia")
        printo(results+"\n")
        speak(results)

    #if the user wants to open youtube
    elif 'open youtube' in query:
        speak("opening youtube ")
        url='http://www.youtube.com'
        webbrowser.open(url)

    #if the user wants to open facebook
    elif 'open facebook' in query:
        speak("opening facebook ")
        url='http://www.facebook.com'
        webbrowser.open(url)

    #if the user wants to open instagram
    elif 'open instagram' in query:
        speak("opening instagram ")
        url='http://www.instagram.com'
        webbrowser.open(url)

    #if the user wants to open gmail
    elif 'open gmail' in query:
        speak("opening gmail ")
        url='http://www.gmail.com'
        webbrowser.open(url)

    #if the user wants to open outlook
    elif 'open outlook' in query:
        speak("opening outlook ")
        url='http://www.outlook.com'
        webbrowser.open(url)

    #if the user wants to open amazon
    elif 'open amazon' in query:
        speak("opening amazon ")
        url='http://www.amazon.com'
        webbrowser.open(url)

    #if the user wants to open stackoverflow
    elif 'open stack' in query:
        speak("opening stack over flow ")
        url='http://www.stackoverflow.com'
        webbrowser.open(url)

    #if the user wants to open google
    elif 'open google' in query:
        speak('opening google')
        webbrowser.open("google.com")
    
    #if the user wants to search a place on map
    elif 'google map' in query:
        srch_google_map()

    #if the user wants to know the time
    elif 'the time' in query:
        strTime = dt.datetime.now().strftime("%H:%M:%S")
        speak(f"Sir, The time is {strTime}")

    #if the user wants to open VS Code
    elif 'open code' in query:
        code_path = "C:\\Users\\vskus\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
        os.startfile(code_path)

    #if the user wants to open word
    elif 'open word' in query:
        word_path = "C:\\Program Files\\Microsoft Office\\root\\Office16\\WINWORD.EXE"
        os.startfile(word_path)

    #if the user wants to open access
    elif 'open access' in query:
        access_path = "C:\\Program Files\\Microsoft Office\\root\\Office16\\MSACCESS.EXE"
        os.startfile(access_path)

    #if the user wants to open acrobat
    elif 'open acrobat' in query:
        acro_path = "C:\\Program Files\\Adobe\\Acrobat DC\\Acrobat\\Acrobat.exe"
        os.startfile(acro_path)

    #if the user wants to open browser
    elif 'open browser' in query:
        br_path = "C:\\Program Files\\BraveSoftware\\Brave-Browser\\Application\\brave.exe"
        os.startfile(br_path)
            
    #if the user wants to open excel
    elif 'open excel' in query:
        excel_path = "C:\\Program Files\\Microsoft Office\\root\\Office16\\EXCEL.EXE"
        os.startfile(excel_path)

    #if the user wants to open powerpoint
    elif 'open powerpoint' in query:
        p_path = "C:\\Program Files\\Microsoft Office\\root\\Office16\\POWERPNT.EXE"
        os.startfile(p_path)

    #if the user wants to quit the assistant
    elif 'go offline' in query:
        speak('ok '+name)
        quit()
        win.destroy()

    #if the user wants to shutdown the pc
    elif 'shutdown' in query:
        #self.compText.set('okay')
        speak('okay')
        os.system('shutdown -s')


    elif "what\'s up" in query or 'how are you' in query:
        stMsgs = ['Just doing my thing!', 'I am fine!', 'Nice!', 'I am nice and full of energy']
        speak(r2.choice(stMsgs))

    #if the user wants to play some music   
    elif 'play music' in query:
        music_folder = "music path "
        music = ['music1','music2','music3','music4','music5']
        random_music = music_folder + r2.choice(music) + '.mp3'
        os.system(random_music)
        speak('Okay, here is your music! Enjoy!')

    #if the user wants to play some video
    elif 'play video' in query:
            video_folder = "video path"
            video = ['video1','video2','video3','video4','video5']
            random_video = video_folder + r2.choice(video) + '.mp4'
            os.system(random_video)
            speak('Okay, here is your video! Enjoy!')

    #if the user wants to open C Drive     
    elif 'open c drive' in query:
        cdrive = "C:"
        speak("openning C Drive....")
        os.startfile(cdrive)

    #if the user wants to send an email
    elif 'send email' in query:
        speak("Please tell me the secret code:")
        p = Commands().lower()
        if p=="ok":
            #using exception handeling
            try:
                #speak("To whom should i send this email?")
                #too = Commands().lower()
                cursor3 = conn.execute("SELECT EMAIL FROM CONTACTS WHERE UNAME='ME'")
                to = cursor3
                speak("What should i say?")
                content = Commands()
                sendemail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry, I am unable to send this email.")
        else:
            speak("Wrong passcode!")
    
    #if the user wants to open a file
    elif 'open a file' in query:
        speak("Please tell me the name of file")
        name = Commands().lower()
        speak("Please tell me the extension of file")
        ext = Commands().lower()
        file_name = name + "." + ext
        try:
            path = find_files(file_name, "C:")
            os.startfile(path)
        except Exception as e:
            print(e)
            speak("Sorry, I am unable to find the file")

    #when user wants nothing       
    elif 'nothing' in query or 'abort' in query or 'stop' in query:
        speak('okay')
        speak('Bye'+name+', have a good day.')
        win.destroy()
        quit()

    #if the user wishes hello          
    elif 'hello' in query:
        speak('Hello '+name)

    #if the user wants to go
    elif 'bye' in query:
        speak('Bye'+name+', have a good day.')
        win.destroy()
        quit()

    #if the assistant cannot understand the command then if takes help form the API
    else:
        query = query
        try:
            speak('Searching in API...')
            res = client.query(query)
            results = next(res.results).text
            speak('API says - ')
            speak('please wait.')
            speak(results)
                
        except Exception as e:
                #print(e)
            #if the command is not in API then it can search it on goolge
            speak("sorry sir. i can't recognize your command maybe google can handle this should i open google for you?")
            ans=Commands()
            if 'yes' in str(ans) or 'yeah' in str(ans):
                webbrowser.open('www.google.com')
            elif 'no' in str(ans) or 'nah' in str(ans):
                speak("ok disconnecting")
                sys.exit()
            else:
                speak("no respnse i am disconnecting")
                sys.exit()

#function to ecit the window
def exit():
    win.destroy()
    sys.exit()
    #pass

#function to call main function
def start():
    Thread(target=mainfn).start()

def speakingbtn():
    Thread(target=reco).start()

#defining some buttons of the GUI
btn = Button(
    win, 
    text='Start!', 
    font=('#7adb1e', 11, 'bold'), 
    bg='black', 
    fg='#7adb1e',
    borderwidth=5,
    command=start).pack(fill='x', expand='no')
btn1 = Button(
    win, 
    text='Start Speaking!', 
    font=('#7adb1e', 11, 'bold'), 
    bg='black', fg='#7adb1e',
    borderwidth=5,
    command=speakingbtn).pack(fill='x', expand='no')
btn2 = Button(
    win, text='Command List', 
    font=('#7adb1e', 11, 'bold'), 
    bg='black', fg='#7adb1e',
    borderwidth=5,
    command=new_GUI).pack(fill='x', expand='no')
btn3 = Button(
    win, 
    text='EXIT', 
    font=('#7adb1e', 11, 'bold'), 
    bg='red', 
    fg='white',
    borderwidth=5,
    command=exit).pack(fill='x', expand='no')

conn.close()

#a loop so that the assistant does not stop afert completing a task
win.mainloop()
