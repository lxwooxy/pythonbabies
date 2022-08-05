from tkinter import *

res = []
n = 0
binaryStr = ""
userStr = ""
stepStr = ""

def convert():
    global n, binaryList, userStr
    userStr = inputBox.get()
    if userStr != '':
        n = int(float(inputBox.get()))
        inputBox.delete(0,END)
        if n<0 or n>512:
            n=0
            userStr = "{0} is out of range. Enter a DMX Address between 0-512.".format(userStr)
        binaryList = fixed(binary(n))
        updateSwitch()
    
def binary(n):
    if n > 1:
        binary(n//2)
    res.append(n%2)
    return(res)

def fixed(res):   
    while(len(res)<10):
        res.insert(0,0)
    return(res)
    
def decimal(a,b,c,d,e,f,g,h,i,j):
    return(a+b*2+c*4+d*8+e*16+f*32+g*64+h*128+i*256+j*512)

def flip(v):
    if v9.get() == 1:
        v9.set(0)
    addressLabel['text'] = 'Address: {0}'.format(getAddress())
    updateBinary()

def increment():
    global binaryList
    stepStr = stepBox.get()
    n = getAddress()
    if stepStr != "":
        step = int(float(stepStr))
        n+=step
        if n>=0 and n <=512:
            binaryList = fixed(binary(n))
            updateBinary()
            updateSwitch()
            updateAddress()

def decrement():
    global binaryList
    stepStr = stepBox.get()
    n = getAddress()
    if stepStr != "":
        step = int(float(stepStr))
        n-=step
        if n>=0 and n <=512:
            binaryList = fixed(binary(n))
            updateBinary()
            updateSwitch()
            updateAddress()

def test512(v):
    if v9.get()==1:
        addressLabel['text'] = 'Address: 512'
        v0.set(0)
        v1.set(0)
        v2.set(0)
        v3.set(0)
        v4.set(0)
        v5.set(0)
        v6.set(0)
        v7.set(0)
        v8.set(0)
        updateBinary()
    else:
        addressLabel['text'] = 'Address: 0'

def updateSwitch():
    global res, binaryStr, binaryList
    for num in binaryList:
        binaryStr+=str(num)
    addressLabel['text'] = 'Address: {0}'.format(n)
    binaryLabel['text'] = 'Binary: {0}'.format(binaryStr)
    binaryStr = ''
    res = []
    if v9.get()==1:
        v9.set(0)
    v0.set(binaryList[9])
    v1.set(binaryList[8])
    v2.set(binaryList[7])
    v3.set(binaryList[6])
    v4.set(binaryList[5])
    v5.set(binaryList[4])
    v6.set(binaryList[3])
    v7.set(binaryList[2])
    v8.set(binaryList[1])
    v9.set(binaryList[0])

def updateBinary():
    binaryStr = "{0}{1}{2}{3}{4}{5}{6}{7}{8}{9}".format(v9.get(),v8.get(),v7.get(),v6.get(),v5.get(),v4.get(),v3.get(),v2.get(),v1.get(),v0.get())
    binaryLabel['text'] = 'Binary: {0}'.format(binaryStr)

def getAddress():
    return(decimal(v0.get(),v1.get(),v2.get(),v3.get(),v4.get(),v5.get(),v6.get(),v7.get(),v8.get(),v9.get()))

def updateAddress():
    addressLabel['text'] = 'Address: {0}'.format(getAddress())

def clear():
    global binaryList
    binaryList = [0,0,0,0,0,0,0,0,0,0]
    updateSwitch()
    updateBinary()
    updateAddress()
    if len(stepBox.get())>0:
        stepBox.delete(0,END)

"""
User Input
"""
root = Tk()
root.geometry('550x270')
root.title("So you found a light/hazer with a DIP Switch panel. Yikes.")
root.resizable(False,False)

inputFrame = Frame(root)
inputFrame.pack(fill = X)

inputBoxLabel = Label(inputFrame)
inputBoxLabel['text'] = 'Enter first DMX Address(0-512):'
inputBoxLabel.pack(side=LEFT, fill=X)

inputBox = Entry(inputFrame)
inputBox.pack(side=LEFT, fill=X)

buttonCon = Button(inputFrame)
buttonCon['text'] = 'Convert'
buttonCon['command'] = convert
buttonCon.pack(side=LEFT, fill=X)

buttonClr = Button(inputFrame)
buttonClr['text'] = 'Clear'
buttonClr['command'] = clear
buttonClr.pack(side=LEFT, fill=X)

stepFrame = Frame(root)
stepFrame.pack(fill = X)

stepLabel = Label(stepFrame)
stepLabel['text'] = 'Enter step size:'
stepLabel.pack(side=LEFT, fill=X)

stepBox = Entry(stepFrame)
stepBox.pack(side=LEFT, fill=X)

buttonInc = Button(stepFrame)
buttonInc['text'] = 'Increment'
buttonInc['command'] = increment
buttonInc.pack(side=LEFT, fill=X)

buttonDec = Button(stepFrame)
buttonDec['text'] = 'Decrement'
buttonDec['command'] = decrement
buttonDec.pack(side=LEFT)

"""
DMX Address, Binary representation, and DIP Switch header
"""
addressFrame = Frame(root)
addressFrame.pack(fill = X)
addressLabel = Label(addressFrame)
addressLabel['text'] = 'Address: {0}'.format(userStr)
addressLabel.pack(side = LEFT)

binaryFrame = Frame(root)
binaryFrame.pack(fill = X)
binaryLabel = Label(binaryFrame)
binaryLabel['text'] = 'Binary: {0}'.format(binaryStr)
binaryLabel.pack(side = LEFT, fill = X)

sLabelFrame = Frame(root)
sLabelFrame.pack(fill = X)
switchLabel = Label(sLabelFrame)
switchLabel['text'] = "DIP Switch Configuration: "
switchLabel.pack(side = LEFT, fill = X)

"""
ON/OFF labels
"""
onFrame = Frame(root)
onFrame.pack(side = LEFT, fill = Y)
onLabel = Label(onFrame)
onLabel['text'] = 'ON'
onLabel.pack()

offLabel = Label(onFrame)
offLabel['text'] = 'OFF'
offLabel.pack(side = BOTTOM)

"""
Switches 1-10
"""
switchFrame = Frame(root)
switchFrame.pack(fill = X)

v0 = IntVar()
s0 = Scale(switchFrame, from_=1, to=0, variable = v0, command = flip)
s0.pack(padx=5, pady=5, side = LEFT)

v1 = IntVar()
s1 = Scale(switchFrame, from_=1, to=0, variable = v1, command = flip)
s1.pack(padx=5, pady=5, side = LEFT)

v2 = IntVar()
s2 = Scale(switchFrame, from_=1, to=0, variable = v2, command = flip)
s2.pack(padx=5, pady=5, side = LEFT)

v3 = IntVar()
s3 = Scale(switchFrame, from_=1, to=0, variable = v3, command = flip)
s3.pack(padx=5, pady=5, side = LEFT)

v4= IntVar()
s4 = Scale(switchFrame, from_=1, to=0, variable = v4, command = flip)
s4.pack(padx=5, pady=5, side = LEFT)

v5 = IntVar()
s5 = Scale(switchFrame, from_=1, to=0, variable = v5, command = flip)
s5.pack(padx=5, pady=5, side = LEFT)

v6 = IntVar()
s6= Scale(switchFrame, from_=1, to=0, variable = v6, command = flip)
s6.pack(padx=5, pady=5, side = LEFT)

v7 = IntVar()
s7 = Scale(switchFrame, from_=1, to=0, variable = v7, command = flip)
s7.pack(padx=5, pady=5, side = LEFT)

v8 = IntVar()
s8 = Scale(switchFrame, from_=1, to=0, variable = v8, command = flip)
s8.pack(padx=5, pady=5, side = LEFT)

v9 = IntVar()
s9 = Scale(switchFrame, from_=1, to=0, variable = v9, command = test512)
s9.pack(padx=5, pady=5, side = LEFT)

"""
Switch Labels
"""
numFrame = Frame(root)
numFrame.pack(fill = X)
numLabel = Label(numFrame)
numLabel['text'] = "    1           2          3          4          5          6         7         8          9       Test"   
numLabel.pack(side =  LEFT)
