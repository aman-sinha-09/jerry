import os
import keyboard
import pyautogui
import webbrowser
import random
import word2number
from time import sleep
from Body.Speak import Speak
from Body.Listen import MicExecution
import pywhatkit as wk
from keyboard import press
from keyboard import write
from pyautogui import click
from word2number import w2n

def email(name,subject,content):
    pyautogui.press('win')
    sleep(1)
    keyboard.write('chrome')
    sleep(1)
    keyboard.press('enter')
    sleep(2) 
    click(x=53, y=106)
    sleep(5)
    click(x=108, y=252)
    sleep(1)
    keyboard.write(name)
    sleep(1)
    keyboard.press('enter')
    sleep(0.5)
    keyboard.press('tab')
    sleep(0.5)
    keyboard.write(subject)
    sleep(1)
    keyboard.press('tab')
    sleep(0.5)
    keyboard.write(content)
    sleep(1)
    click(x=1205, y=989)
    Speak(f"Mail Sent To {name}")
    sleep(0.5)
    click(x=1880, y=22)
    sleep(0.5)

def alarm(hour, minute):
    hour=str(hour)
    minute=str(minute)
    pyautogui.press('win')
    sleep(1)
    keyboard.write('clock')
    sleep(1)
    keyboard.press('enter')
    sleep(2) 
    click(x=794, y=174)
    sleep(0.5)
    click(x=675, y=318)
    keyboard.write(hour)
    sleep(1)
    keyboard.press('tab')
    keyboard.write(minute)
    sleep(1)
    click(x=673, y=816)
    sleep(0.5)
    click(x=1360, y=23)
    Speak(f"Alarm set for {hour} hour and {minute} minute")
    sleep(1)

def game_play():
    Speak("Lets Play ROCK PAPER SCISSORS !!")
    print("LETS PLAYYYYYYYYYYYYYY")
    Me_score = 0
    Com_score = 0
    while(True):
        choose = ("rock","paper","scissors") #Tuple
        com_choose = random.choice(choose)
        query=MicExecution()
        query=str(query)

        if (query == "rock"):
            if (com_choose == "rock"):
                Speak("ROCK")
                print(f"Score:- ME :- {Me_score} : COM :- {Com_score}")
            elif (com_choose == "paper"):
                Speak("paper")
                Com_score += 1
                print(f"Score:- ME :- {Me_score} : COM :- {Com_score}")
            else:
                Speak("Scissors")
                Me_score += 1
                print(f"Score:- ME :- {Me_score} : COM :- {Com_score}")

        elif (query == "paper" ):
            if (com_choose == "rock"):
                Speak("ROCK")
                Me_score += 1
                print(f"Score:- ME :- {Me_score+1} : COM :- {Com_score}")

            elif (com_choose == "paper"):
                Speak("paper")
                print(f"Score:- ME :- {Me_score} : COM :- {Com_score}")
            else:
                Speak("Scissors")
                Com_score += 1
                print(f"Score:- ME :- {Me_score} : COM :- {Com_score}")

        elif (query == "scissors" or query == "scissor"):
            if (com_choose == "rock"):
                Speak("ROCK")
                Com_score += 1
                print(f"Score:- ME :- {Me_score} : COM :- {Com_score}")
            elif (com_choose == "paper"):
                Speak("paper")
                Me_score += 1
                print(f"Score:- ME :- {Me_score} : COM :- {Com_score}")
            else:
                Speak("Scissors")
                print(f"Score:- ME :- {Me_score} : COM :- {Com_score}")

        elif (query == "final score" or query =="score"):
             Speak(f"Final Score of yours is {Me_score} and mine is {Com_score}")
             break

def WhatsappMsg(name,message):
    pyautogui.press('win')
    sleep(1)
    keyboard.write('whatsapp')
    sleep(1)
    keyboard.press('enter')
    sleep(2) 
    click(x=1242, y=151)
    write(name)
    sleep(1)
    click(x=1270, y=227)
    # click(x=1279, y=284)
    sleep(0.5)
    click(x=1631, y=745)
    write(message)
    sleep(2)
    keyboard.press('enter')
    Speak('message sent') 

def WhatsappCall(name):
    pyautogui.press('win')
    sleep(1)
    keyboard.write('whatsapp')
    sleep(1)
    keyboard.press('enter')
    sleep(2) 
    click(x=1242, y=151)
    write(name)
    sleep(1)
    click(x=1270, y=227)
    # click(x=1279, y=284)
    sleep(1)
    click(x=1809, y=93)
    sleep(5)



def OpenExe(Query):
    Query = str(Query).lower()

    if "visit" in Query:
        Nameofweb = Query.replace("visit ","")
        Link = f"https://www.{Nameofweb}.com"
        webbrowser.open(Link)
        return True

    elif "launch" in Query:
        Nameofweb = Query.replace("launch ","")
        Link = f"https://www.{Nameofweb}.com"
        webbrowser.open(Link)
        return True
    
    elif "goto" in Query:
        Nameofweb = Query.replace("goto ","")
        Link = f"https://www.{Nameofweb}.com"
        webbrowser.open(Link)
        return True

    elif "open" in Query:
        Nameoftheapp = Query.replace("open ","")
        pyautogui.press('win')
        sleep(1)
        keyboard.write(Nameoftheapp)
        sleep(1)
        keyboard.press('enter')
        sleep(0.5)  
        return True

    elif "start" in Query:
        Nameoftheapp = Query.replace("start ","")
        pyautogui.press('win')
        sleep(1)
        keyboard.write(Nameoftheapp)
        sleep(1)
        keyboard.press('enter')
        sleep(0.5)  
        return True
    
    elif 'youtube' in Query:
        Speak('opening youtube')
        Speak("what would you like to watch ?")
        qry= MicExecution().lower()
        wk.playonyt(f'{qry}')
        sleep(5)
        return True
    
    elif 'full' in Query:
        keyboard.press('f')
        return True
    
    elif 'pause' in Query:
        keyboard.press('space bar')
        return True
    
    elif 'whatsapp' in Query:
        Speak("to whom you want to send message to")
        name=MicExecution()
        name=str(name)
        Speak(f"Preparing To Send a Message To {name}")
        Speak("What's The Message By The Way?")
        msg = MicExecution()
        msg=str(msg)
        WhatsappMsg(name,msg)
        return True
    
    elif 'call' in Query:
        Speak("to whom you want to call")
        name=MicExecution()
        name=str(name)
        Speak(f"calling {name} ")
        WhatsappCall(name)
        return True
    
    elif 'close' in Query:
        Speak('closing whatsapp')
        click(x=1880, y=22)
        return True
    
    elif 'terminate' in Query:
        Speak('closing youtube')
        click(x=1880, y=22)
        return True
    
    elif 'cut' in Query:
        Speak('terminating the call')
        click(x=1076, y=817)
        sleep(1)
        click(x=1880, y=22)
        return True
    
    elif 'slide show' in Query:
        click(x=632, y=53)
        sleep(0.5)
        click(x=42, y=109)
        while True:
            data=MicExecution()
            data=str(data)
            if 'next' in data:
                keyboard.press('n')
            elif 'next slide' in data:
                keyboard.press('n')
            elif 'goto next slide' in data:
                keyboard.press('n')
            elif 'previous' in data:
                keyboard.press('p')   
            elif 'previous slide' in data:
                keyboard.press('p') 
            elif 'goto previous slide' in data:
                keyboard.press('p')  
            elif 'exit' in data:
                keyboard.press('esc')
            elif 'exit slide' in data:
                keyboard.press('esc')
            elif 'close powerpoint' in data:
                Speak('closing powerpoint')
                break
            elif 'close slide' in data:
                Speak('closing slide')
                break
        click(x=1901, y=18)
        return True
    
    elif "game" in Query:
        game_play()
        return True
    
    elif "alarm" in Query:
        Speak("Please tell me the hour")
        hour=MicExecution()
        hour= w2n.word_to_num(hour)
        print(hour)
        Speak("Please tell me the minute")
        minute=MicExecution()
        minute= w2n.word_to_num(minute)
        print(minute)
        Speak(f"Setting alarm for {hour} hour and {minute} minute")
        alarm(hour,minute)
        return True
    
    elif 'mail' in Query:
        Speak("To whom do you want to send mail to")
        name=MicExecution()
        name=str(name)
        Speak(f"Preparing To Send Mail To {name}")
        Speak("What's The Subject By The Way?")
        subject=MicExecution()
        subject=str(subject)
        Speak("Please specify the content")
        content=MicExecution()
        content=str(content)
        Speak(f"Sending mail to {name} ")
        email(name,subject,content)
        return True
 
    
    return False