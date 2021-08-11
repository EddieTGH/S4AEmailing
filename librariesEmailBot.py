import pyautogui as pyA
import time
import re
from datetime import datetime
from twilio.rest import Client

#create a instructions panel and different versions of this     
global emails, names, cclist
emails = []
names = []
cclist = []
global subject, coemails, personalizerlevel, use
#Opens the file and extracts the links,edmond.niu@gmail.com returned in a list format,

def askForInputs():
    global use, subject, ccs
    print("welcome.")
    loop = False
    yesno = input("Do you have an emails of any partners/people that you want to send all these emails to (not LIBRARY EMAIL)? Type y for yes, n for no: ")
    if yesno.lower() == "y":
        loop = True
    while loop:
        ccs = input("Type the email address of any partners/people that you want to send all these emails to (not LIBRARY EMAIL): ")
        cclist.append(ccs)
        yesno = input("Type y if you are done and want to move on, type n if you have more email addresses of partners/people to add (not LIBRARY EMAIL): ")
        if yesno.lower() == "y":
            loop = False
    print("cclist: " + str(cclist))

    #use = input("What are you using this bot for? Type libraries, seniorcenters, or hackathon: ")
    subject = input("What is the subject of the email message? Type exactly as you want it: ")
    print("thank you. please switch back to your email tab. starting sending in 5 seconds.")
    time.sleep(5)
 
def openFile():
    f = open('emails.txt','r') #opens the text file
   
    for line in f: #iterates through the text file
        line = line.rstrip()
        x = re.findall('.*E:\s*(\S+)', line) #regular expressions function designed to extract just the link
        y = re.findall('.*L:\s*(.+)', line)
        if (len(x)>0):
            emails.append(x)
            names.append(y)
    print("library emails: " + str(emails))
    print("library names: " + str(names))

def findEmails(): #search on google and compile a list of emails
    pass

def selectcorrectmailingaddress():
    #select edmond1, then edmond2
    pic2 = pyA.locateOnScreen('Images/edmond1.PNG', confidence = 0.75)
    if pic2 != None:
    #print("Pic found!")
        pic2 = pyA.center(pic2)
        pic2X, pic2Y = pic2
        time.sleep(1)
        pyA.moveTo(pic2X, pic2Y)
        time.sleep(1)
        pyA.click(pic2X, pic2Y)
        #pyA.click(pic2X, pic2Y)
    
    time.sleep(1)

    pic3 = pyA.locateOnScreen('Images/edmond2.PNG', confidence = 0.75)
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


def attachflier(): #does not work yet
    #coordinate of the flier
    pyA.moveTo(182,1005)
    #coordinate of the email text box
    pyA.dragTo(1431,736,1,button="left")

#before, open gmail, make sure emails.txt is filled, and copy paste the email body. make sure a new email is composed and the cursor is on the to: window ready to type the adresseees
def sendEmails():
    askForInputs()
    openFile()

    i=0
    for email in emails:
        address = str(email[0])

        #press compose
        pic1 = pyA.locateOnScreen('Images/compose.PNG', confidence = 0.75)
        if pic1 != None:
            pic1 = pyA.center(pic1)
            pic1X, pic1Y = pic1
            time.sleep(1)
            pyA.moveTo(pic1X, pic1Y) 
            time.sleep(1)
            #pyA.click(pic1X, pic1Y) 
            pyA.click(pic1X, pic1Y) 

        time.sleep(1)

        #choosesenderemail()

        # paste partner emails
        if len(cclist) != 0:
            for cc in cclist:
                pyA.typewrite(str(cc))
                time.sleep(1)
                pyA.hotkey('enter')
        
        time.sleep(1)

        #library email paste
        pyA.typewrite(address)
        pyA.hotkey('enter')

        time.sleep(1)


        #select subject window
        pic4 = pyA.locateOnScreen('Images/subject.PNG', confidence = 0.75)
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
        pyA.typewrite(subject)

        time.sleep(1)

        #select body window
        pyA.hotkey("tab")

        time.sleep(1)

        #type personalized greeting
        library = str(names[i][0])
        pyA.typewrite('Good evening, librarian at ' + library + '!')

        pyA.hotkey('enter')

        time.sleep(1)

        pyA.hotkey('enter')

        time.sleep(1)

        #past the body ctrl v
        pyA.hotkey('ctrl', 'shift', 'v')

        time.sleep(1)

        pyA.hotkey('enter')

        #attach flyer()

        time.sleep(1)

        #press send
        pic5 = pyA.locateOnScreen('Images/send.PNG', confidence = 0.75)
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

        """ #click on compose again to start new one
        pic1 = pyA.locateOnScreen('Images/compose.PNG', confidence = 0.75)
        if pic1 != None:
            pic1 = pyA.center(pic1)
            pic1X, pic1Y = pic1
            time.sleep(1)
            pyA.moveTo(pic1X, pic1Y) 
            time.sleep(1)
            #pyA.click(pic1X, pic1Y) 
            pyA.click(pic1X, pic1Y)  """

        print('one done')
        #end of function
        i+=1
    print(str(i)+" emails sent")

sendEmails()

def findpos():
    print(pyA.position())
