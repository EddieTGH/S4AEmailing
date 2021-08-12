import pyautogui as pyA
import time

def attachflier(pos1x, pos1y, pos2x, pos2y): #does not work yet
    #pos1x = 80
    #pos1y = 1006
    #pos2x = 1459
    #pos2y = 533
    #coordinate of the flier
    pyA.moveTo(pos1x, pos1y)
    time.sleep(1)
    print("getting ready to drag")
    #coordinate of the email text box
    pyA.dragTo(pos2x, pos2y,1,button="left")


#print(pyA.position())

pos1x, pos1y = pyA.position()
print("dont")
time.sleep(3)

pos2x, pos2y = pyA.position()
print(pos1x)
print(pos1y)
print(pos2x)
print(pos2y)
time.sleep(3)
for i in range(0,10):
    attachflier(pos1x, pos1y, pos2x, pos2y)