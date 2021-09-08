import pyautogui as pyA
import time
import webbrowser
import re
import cv2
from datetime import datetime
from twilio.rest import Client
import os

#notes: make sure u are on 100 percent zoom.
global links, libraries
links = []
libraries = []
#Opens the file and extracts the links,edmond.niu@gmail.com returned in a list format,
def openFile():
    f = open('emails.txt','r') #opens the text file
   
    for line in f: #iterates through the text file
        line = line.rstrip()
        x = re.findall('.*E:\s*(\S+)', line) #regular expressions function designed to extract just the link
        y = re.findall('.*L:\s*(.+)', line)
        if (len(x)>0):
            links.append(x)
            libraries.append(y)


def findEmails(): #search on google and compile a list of emails
    pass



#before, open gmail, make sure emails.txt is filled, and copy paste the email body. make sure a new email is composed and the cursor is on the to: window ready to type the adresseees
def sendEmails():
    openFile()

    i=0
    for link in links:
        address = str(link[0])

        #press compose
        pic1 = pyA.locateOnScreen('ImagesD/compose2D.PNG', confidence = 0.75)
        if pic1 != None:
            pic1 = pyA.center(pic1)
            pic1X, pic1Y = pic1
            time.sleep(1)
            pyA.moveTo(pic1X, pic1Y) 
            time.sleep(1)
            #pyA.click(pic1X, pic1Y) 
            pyA.click(pic1X, pic1Y) 
            print("found compose")

        time.sleep(1)

        #type s, then enter (select satwika)
        #pyA.typewrite('sa')
        #time.sleep(1)
        #pyA.hotkey('enter')
        
        time.sleep(1)

        #paste the email
        pyA.typewrite(address)
        pyA.hotkey('enter')

        time.sleep(1)

        #select edmond1, then edmond2
        pic2 = pyA.locateOnScreen('ImagesD/edmond1D.PNG', confidence = 0.75)
        if pic2 != None:
        #print("Pic found!")
            pic2 = pyA.center(pic2)
            pic2X, pic2Y = pic2
            time.sleep(1)
            pyA.moveTo(pic2X, pic2Y)
            time.sleep(1)
            time.sleep(2)
            pyA.click(pic2X, pic2Y)
            #pyA.click(pic2X, pic2Y)
        
        time.sleep(1)

        pic3 = pyA.locateOnScreen('ImagesD/edmond2D.PNG', confidence = 0.75)
        if pic3 != None:
        #print("Pic found!")
            pic3 = pyA.center(pic3)
            pic3X, pic3Y = pic3
            time.sleep(1)
            pyA.moveTo(pic3X, pic3Y)
            time.sleep(1)
            pyA.click(pic3X, pic3Y)
            #pyA.click(pic3X, pic3Y)

        time.sleep(1)

        #select subject window
        pic4 = pyA.locateOnScreen('ImagesD/subjectD.PNG', confidence = 0.75)
        if pic4 != None:
        #print("Pic found!")
            pic4 = pyA.center(pic4)
            pic4X, pic4Y = pic4
            time.sleep(1)
            pyA.moveTo(pic4X, pic4Y)
            time.sleep(1)
            pyA.click(pic4X, pic4X)
            pyA.click(pic4X, pic4Y)
    
        time.sleep(1)

        #type the subject
        pyA.typewrite('Red Bank Business Alliance')

        time.sleep(1)

        #select body window
        pyA.click(1347,636)

        time.sleep(1)

        library = str(libraries[i][0])
        pyA.typewrite('Good evening, librarian at ' + library + '!')

        pyA.hotkey('enter')

        time.sleep(1)

        pyA.hotkey('enter')

        time.sleep(1)

        #past the body ctrl v
        pyA.hotkey('ctrl', 'shift', 'v')

        time.sleep(1)

        #attach flier
        pyA.hotkey('enter')

        pyA.moveTo(81,1003)
        pyA.dragTo(1538,735,2,button="left")
        time.sleep(1)
        pyA.mouseUp()

        time.sleep(1)

        #press send
        pic5 = pyA.locateOnScreen('ImagesD/sendD.PNG', confidence = 0.75)
        if pic5 != None:
        #print("Pic found!")
            pic5 = pyA.center(pic5)
            pic5X, pic5Y = pic5
            time.sleep(1)
            pyA.moveTo(pic5X, pic5Y)
            time.sleep(1)
            pyA.click(pic5X, pic5Y)
            #pyA.click(pic5X, pic5Y)

        time.sleep(1)
        print('one done')
        #end of function
        i+=1

sendEmails()

def findpos():
    print(pyA.position())

#findpos()
