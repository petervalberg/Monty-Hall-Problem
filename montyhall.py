# Created by Peter Valberg, November 2018
# ---------------------------------------

from tkinter import *
import random, time

# Color definitions

neutral_color = 'SystemButtonFace'
active_color = 'snow3'
button_color = 'lightgray'
active_button_color = 'snow3'

# Font definitions

font0 = ('Helvetica', 10, 'normal', 'roman')
font1 = ('Helvetica', 12, 'bold', 'roman')
font2 = ('Helvetica', 20, 'normal', 'roman')

# Variables and lists

changeOK = False
prizeDoor = 0
contestantChoice = 0
playerWinsMoney = 0
playerGetsGoat = 0
doorsLeft = [1,2,3]


# Functions

def choosePrizeDoor():
    # computer chooses a random door to conceal the moneyprize
    global prizeDoor, doorsLeft
    prizeDoor = random.choice([1,2,3])
    doorsLeft.remove(prizeDoor)

def OpenGoatDoor():
    # Opens the door not chosen by contestant and not the prizedoor
    global doorsLeft
    root.update_idletasks()
    time.sleep(3)
    doorsList = ['dummy', door1, door2, door3]
    blankList = ['dummy', blank1, blank2, blank3]
    noPrizeDoor = random.choice(doorsLeft)
    doorsLeft.remove(noPrizeDoor)
    canvas.itemconfig(doorsList[noPrizeDoor], image=doorOpenGoat)
    canvas.itemconfig(blankList[noPrizeDoor], state=DISABLED)
    canvas.itemconfig(speech, image=speechGoat)
    if len(doorsLeft) < 2:
        doorsLeft.append(prizeDoor)
        doorsLeft.sort()
    else:
        pass
    if contestantChoice not in doorsLeft:
        doorsLeft.append(contestantChoice)
        doorsLeft.sort()
    changeChoice()

def changeChoice():
    # When contestant can change choice of door
    global changeOK
    root.update_idletasks()
    time.sleep(3)
    canvas.itemconfig(speech, image=speechAlterChoice)
    for element in doorsLeft:
        if element == 1:
            canvas.itemconfig(door1, image=doorOneClosed)
        elif element == 2:
            canvas.itemconfig(door2, image=doorTwoClosed)
        elif element == 3:
            canvas.itemconfig(door3, image=doorThreeClosed)
    changeOK = True

def blockChoice():
    # Doors can no longer be chosen
    canvas.itemconfig(blank1, state=DISABLED)
    canvas.itemconfig(blank2, state=DISABLED)
    canvas.itemconfig(blank3, state=DISABLED)
    
def RevealThirdDoor():
    # Opens the second door not chosen by contestant
    canvas.itemconfig(speech, image=speechOpenThird)
    root.update_idletasks()
    time.sleep(2)
    if prizeDoor in doorsLeft:
        loose()
    else:
        for element in doorsLeft:
            if element == 1:
                canvas.itemconfig(door1, image=doorOpenGoat)
            elif element == 2:
                canvas.itemconfig(door2, image=doorOpenGoat)
            elif element == 3:
                canvas.itemconfig(door3, image=doorOpenGoat)
        win()

def win():
    # If contestant wins the game (moneyprize)
    globals()['playerWinsMoney'] += 1
    root.update_idletasks()
    time.sleep(1)
    canvas.itemconfig(speech, image=speechSecondGoat)
    root.update_idletasks()
    time.sleep(2)
    doorsList = ['dummy', door1, door2, door3]
    canvas.itemconfig(doorsList[prizeDoor], image=doorOpenMoney)
    canvas.itemconfig(speech, image=speechWin)
    moneyCountLabel.config(text=playerWinsMoney)

def loose():
    # If contestant loses the game (gets a goat)
    globals()['playerGetsGoat'] += 1
    doorsList = ['dummy', door1, door2, door3]
    canvas.itemconfig(doorsList[prizeDoor], image=doorOpenMoney)
    canvas.itemconfig(speech, image=speechLoose)
    root.update_idletasks()
    time.sleep(2)
    canvas.itemconfig(doorsList[contestantChoice], image=doorOpenGoat)
    canvas.itemconfig(speech, image=speechBetterLuck)
    goatCountLabel.config(text=playerGetsGoat)

def chooseDoorOne(event):
    # Function to control choice of door 1
    global contestantChoice, doorsLeft
    if contestantChoice == 0:
        contestantChoice = 1
        if contestantChoice in doorsLeft:
            doorsLeft.remove(contestantChoice)
        else:
            pass
        canvas.itemconfig(speech, image=speechRevealFirstDoor)
        canvas.itemconfig(door1, image=doorOneChosen)
        OpenGoatDoor()
    else:
        if changeOK == True:
            contestantChoice = 1
            doorsLeft.remove(contestantChoice)
            canvas.itemconfig(door1, image=doorOneChosen)
            blockChoice()
            RevealThirdDoor()
        else:
            pass

def chooseDoorTwo(event):
    # Function to control choice of door 2
    global contestantChoice, doorsLeft
    if contestantChoice == 0:
        contestantChoice = 2
        if contestantChoice in doorsLeft:
            doorsLeft.remove(contestantChoice)
        else:
            pass
        canvas.itemconfig(speech, image=speechRevealFirstDoor)
        canvas.itemconfig(door2, image=doorTwoChosen)
        OpenGoatDoor()
    else:
        if changeOK == True:
            contestantChoice = 2
            doorsLeft.remove(contestantChoice)
            canvas.itemconfig(door2, image=doorTwoChosen)
            blockChoice()
            RevealThirdDoor()
        else:
            pass

def chooseDoorThree(event):
    # Function to control choice of door 3
    global contestantChoice, doorsLeft
    if contestantChoice == 0:
        contestantChoice = 3
        if contestantChoice in doorsLeft:
            doorsLeft.remove(contestantChoice)
        else:
            pass
        canvas.itemconfig(speech, image=speechRevealFirstDoor)
        canvas.itemconfig(door3, image=doorThreeChosen)
        OpenGoatDoor()
    else:
        if changeOK == True:
            contestantChoice = 3
            doorsLeft.remove(contestantChoice)
            canvas.itemconfig(door3, image=doorThreeChosen)
            blockChoice()
            RevealThirdDoor()
        else:
            pass

def newGame():
    # Creates a new game an resets variables, lists etc.
    global prizeDoor, contestantChoice, doorsToChoose, doorsLeft, doorsChosen, changeOK
    prizeDoor = 0
    contestantChoice = 0
    changeOK = False
    doorsLeft = [1,2,3]
    canvas.itemconfig(speech, image=speechFirstChoice)
    canvas.itemconfig(blank1, state=NORMAL)
    canvas.itemconfig(blank2, state=NORMAL)
    canvas.itemconfig(blank3, state=NORMAL)
    canvas.itemconfig(door1, image=doorOneClosed)
    canvas.itemconfig(door2, image=doorTwoClosed)
    canvas.itemconfig(door3, image=doorThreeClosed)
    choosePrizeDoor()

def Exit():
    # Terminates the program
    root.destroy()

# GUI definitions

root = Tk()
root.title('The Monty Hall problem')
root.resizable(width=False, height=False)
root.geometry('+350+150')
root.geometry('1000x800')
root.iconbitmap('graphics/door.ico')
root.configure(bg=neutral_color)

# Graphics

doorOneClosed = PhotoImage(file='graphics/doorOneClosed.png')
doorOneChosen = PhotoImage(file='graphics/doorOneChosen.png')
doorTwoClosed = PhotoImage(file='graphics/doorTwoClosed.png')
doorTwoChosen = PhotoImage(file='graphics/doorTwoChosen.png')
doorThreeClosed = PhotoImage(file='graphics/doorThreeClosed.png')
doorThreeChosen = PhotoImage(file='graphics/doorThreeChosen.png')
doorOpenGoat = PhotoImage(file='graphics/doorOpenGoat.png')
doorOpenMoney = PhotoImage(file='graphics/doorOpenMoney.png')
blank = PhotoImage(file='graphics/blankImage.png')   # used as invisible "buttons"

gameShowHost = PhotoImage(file='graphics/gameshowhost.png')
background = PhotoImage(file='graphics/background.png')

speechWelcome = PhotoImage(file='graphics/speechWelcome.png')
speechFirstChoice = PhotoImage(file='graphics/speechFirstChoice.png')
speechRevealFirstDoor = PhotoImage(file='graphics/speechRevealFirst.png')
speechAlterChoice = PhotoImage(file='graphics/speechAlterDoor.png')
speechGoat = PhotoImage(file='graphics/speechGoat.png')
speechOpenThird = PhotoImage(file='graphics/speechOpenThird.png')
speechLoose = PhotoImage(file='graphics/speechLoose.png')
speechBetterLuck = PhotoImage(file='graphics/speechBetterLuck.png')
speechWin = PhotoImage(file='graphics/speechWin.png')
speechSecondGoat = PhotoImage(file='graphics/speechSecondGoat.png')

# Buttons and labels

topFrame = Frame(root, bg=neutral_color)
topFrame.config(borderwidth=0, relief=FLAT)
topFrame.pack(padx=10, pady=10, fill=BOTH)
newButton = Button(topFrame, text='New', font=font1, bg=button_color, \
                   activebackground=active_button_color, width=10, command=lambda:newGame()).pack(side=LEFT, expand=0)
exitButton = Button(topFrame, text='Exit', font=font1, bg=button_color, \
                    activebackground=active_button_color, width=10, command=lambda:Exit()).pack(side=LEFT, expand=0)

blankLabel1 = Label(topFrame, text='', width=10, font=font2).pack(side=LEFT, expand=1)
moneyLabel = Label(topFrame, fg='black', text='Money', font=font2).pack(side=LEFT, expand=1)
moneyCountLabel = Label(topFrame, text='0', font=font2)
moneyCountLabel.pack(side=LEFT, expand=1)
blankLabel2 = Label(topFrame, text='', width=1, font=font2).pack(side=LEFT, expand=1)
goatCountLabel = Label(topFrame, text='0', font=font2)
goatCountLabel.pack(side=LEFT, expand=1)
goatLabel = Label(topFrame, fg='black', text='Goat', font=font2).pack(side=LEFT, expand=1)
blankLabel3 = Label(topFrame, text='', width=10, font=font2).pack(side=LEFT, expand=1)

# Canvas
canvas = Canvas(root, width=1000, height=700)
canvas.pack()
bg = canvas.create_image(0, 0, anchor=NW, image=background)

door1 = canvas.create_image(120, 50, anchor=NW, image=doorOneClosed)
door2 = canvas.create_image(380, 50, anchor=NW, image=doorTwoClosed)
door3 = canvas.create_image(640, 50, anchor=NW, image=doorThreeClosed)

blank1 = canvas.create_image(120, 50, anchor=NW, image=blank, state=DISABLED)
blank2 = canvas.create_image(380, 50, anchor=NW, image=blank, state=DISABLED)
blank3 = canvas.create_image(640, 50, anchor=NW, image=blank, state=DISABLED)

canvas.tag_bind(blank1, "<Button-1>", chooseDoorOne)
canvas.tag_bind(blank2, "<Button-1>", chooseDoorTwo)
canvas.tag_bind(blank3, "<Button-1>", chooseDoorThree)

monty = canvas.create_image(50, 690, anchor=SW, image=gameShowHost)
speech = canvas.create_image(300, 680, anchor=SW, image=speechWelcome)

# Author
authorFrame = Frame(root, bg=neutral_color)
authorFrame.config(borderwidth=0, relief=FLAT)
Label(authorFrame, text='Peter Valberg 2018', bg=neutral_color, fg='gray', font=font0).pack(side=RIGHT, expand=0)
authorFrame.pack(padx=10, pady=10, fill=BOTH)


root.mainloop()

