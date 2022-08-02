from tkinter import *
from tkinter import ttk
from tkinter.messagebox import showinfo

clickcount = 0

def showOrder():
    global clickcount
    clickcount+=1
    judgementLabel['text'] = 'The world watches you, with bated breath. What shall you order?'

    while(clickcount > 20):
        judgementLabel['text'] = "If only you had friends, maybe they could help you order."
        clickcount = 0

    if len(coffee.get()) > 0 and len(tea.get()) > 0:
        drink = "Yuan Yang"
    elif len(coffee.get()) > 0:
        drink = coffee.get()
    elif len(tea.get()) > 0:
        drink = tea.get()
    else:
        drink = ""
        
    if len(noMilk.get()) > 0 and len(eMilk.get()) > 0:
        milk = " [confused noises]"
    elif len(noMilk.get()) > 0:
        milk = noMilk.get()
    elif len(eMilk.get()) > 0:
        milk = eMilk.get()
    else:
        milk = ""
        
    if (len(noSugar.get()) > 0 and len(lSugar.get()) > 0) or (len(noSugar.get()) > 0 and len(mSugar.get()) > 0) or (len(lSugar.get()) > 0 and len(mSugar.get()) > 0):
        sugar = " [ambiguous mumbles]"
    elif len(noSugar.get()) > 0:
        sugar = noSugar.get()
    elif len(lSugar.get()) > 0:
        sugar = lSugar.get()
    elif len(mSugar.get()) > 0:
        sugar = mSugar.get()
    else:
        sugar = ""
    if (len(lStrength.get()) > 0 and len(mStrength.get()) > 0) or (len(lStrength.get()) > 0 and len(vmStrength.get()) > 0) or (len(mStrength.get()) > 0 and len(vmStrength.get()) > 0):
        strength = " [clear throat to buy time]"
    elif len(lStrength.get()) > 0:
        strength = lStrength.get()
    elif len(mStrength.get()) > 0:
        strength = mStrength.get()
    elif len(vmStrength.get()) > 0:
        strength = vmStrength.get()
    else:
        strength = ""
    if len(ice.get())>0:
        temperature = ice.get()
    else:
        temperature = ''
    if len(takeAway.get())>0:
        ordertype = takeAway.get()
    else:
        ordertype = ''
        
    orderLabel['text'] = "{0}{1}{2}{3}{4}{5}".format(drink,milk,sugar,strength,temperature,ordertype)

root = Tk()
root.geometry('700x450')
root.title('faster la.')

"""
Drink Section
"""

drinkFrame = Frame(root)
drinkFrame.pack(anchor = N, fill = X)

drinkLabel = Label(drinkFrame)
drinkLabel['text'] = 'Pick a drink. Know that the kopi auntie can sense fear.'
drinkLabel['font']=('Arial',14)
drinkLabel.pack(side = TOP, fill = X)


coffee = StringVar(drinkFrame)
ttk.Checkbutton(root,
                text = 'Coffee',
                command = showOrder,
                variable = coffee,
                onvalue = 'Kopi',
                offvalue = '').pack()

tea = StringVar(drinkFrame)
ttk.Checkbutton(root,
                text='Tea',
                command = showOrder,
                variable = tea,
                onvalue = 'Teh',
                offvalue = '').pack()

"""
Milk Specs
"""
milkFrame = Frame(root)
milkFrame.pack(anchor = N, fill = X)
milkLabel = Label(milkFrame)
milkLabel['text'] = 'Milk specs. Condensed milk is the default.'
milkLabel['font']=('Arial',14)
milkLabel.pack()

noMilk = StringVar(milkFrame)
ttk.Checkbutton(root,
                text = 'No Milk',
                command = showOrder,
                variable = noMilk,
                onvalue = ' O',
                offvalue = '').pack()

eMilk = StringVar(milkFrame)
ttk.Checkbutton(root,
                text = 'Evaporated Milk',
                command = showOrder,
                variable = eMilk,
                onvalue = ' C',
                offvalue = '').pack()

"""
Sugar Time
"""
sugarFrame = Frame(root)
sugarFrame.pack(anchor = N, fill = X)
sugarLabel = Label(sugarFrame)
sugarLabel['text'] = "Sugar Level, but this isn't gongcha."
sugarLabel['font']=('Arial',14)
sugarLabel.pack()

noSugar = StringVar(sugarFrame)
ttk.Checkbutton(root,
                text = 'No Sugar',
                command = showOrder,
                variable = noSugar,
                onvalue = ' Kosong',
                offvalue = '').pack()

lSugar = StringVar(sugarFrame)
ttk.Checkbutton(root,
                text = 'Less Sugar',
                command = showOrder,
                variable = lSugar,
                onvalue = ' Siew Dai',
                offvalue = '').pack()

mSugar = StringVar(sugarFrame)
ttk.Checkbutton(root,
                text = 'More Sugar',
                command = showOrder,
                variable = mSugar,
                onvalue = ' Gah Dai',
                offvalue = '').pack()

"""
Tastebud strength
"""
strengthFrame = Frame(root)
strengthFrame.pack(anchor = N, fill = X)
strengthLabel = Label(strengthFrame)
strengthLabel['text'] = "Drink Strength (It's not going to punch you. How much coffee powder do you want?)"
strengthLabel['font']=('Arial',14)
strengthLabel.pack()

lStrength = StringVar(strengthFrame)
ttk.Checkbutton(root,
                text = 'Weaker',
                command = showOrder,
                variable = lStrength,
                onvalue = ' Po',
                offvalue = '').pack()

mStrength = StringVar(strengthFrame)
ttk.Checkbutton(root,
                text='Stronger',
                command=showOrder,
                variable=mStrength,
                onvalue=' Gao',
                offvalue='').pack()

vmStrength = StringVar(strengthFrame)
ttk.Checkbutton(root,
                text='Very The Strong',
                command = showOrder,
                variable = vmStrength,
                onvalue = ' Di Lo',
                offvalue = '').pack()

"""
Ice time
"""
iceFrame = Frame(root)
iceFrame.pack(anchor = N, fill = X)
iceLabel = Label(iceFrame)
iceLabel['text'] = 'Do you want ice or are you normal?'
iceLabel['font']=('Arial',14)
iceLabel.pack()

ice = StringVar(iceFrame)
ttk.Checkbutton(root,
                text='Iced',
                command = showOrder,
                variable = ice,
                onvalue = ' Peng',
                offvalue = '').pack()

"""
Da Bao
"""
takeAwayFrame = Frame(root)
takeAwayFrame.pack(anchor = N, fill = X)
takeAwayLabel = Label(takeAwayFrame)
takeAwayLabel['text'] = 'Are you fleeing as soon as this is over?'
takeAwayLabel['font']=('Arial',14)
takeAwayLabel.pack()

takeAway = StringVar(takeAwayFrame)
ttk.Checkbutton(root,
                text='Take Away',
                command = showOrder,
                variable = takeAway,
                onvalue = ' Da Bao',
                offvalue = '').pack()

"""
Order return
"""
orderFrame = Frame(root)
judgementLabel = Label(orderFrame)
judgementLabel['text'] = 'The world watches you, with bated breath. What shall you order?'
judgementLabel['font']=('Arial',16, "italic")
judgementLabel.pack(fill = BOTH)

orderLabel = Label(orderFrame)
orderLabel['text'] = ''
orderLabel['font']=('Arial',16)
orderLabel.pack(side=BOTTOM, anchor=S, fill = X)
orderFrame.pack(side=BOTTOM, fill=X)
