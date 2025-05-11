from tkinter import *
from math import *
from time import *

#funcs
def update_text(lang):
    #z = btnClicked
    #entryBox.delete(0, END)
    entryBox.insert(END, lang)
def clear():
    entryBox.delete(0, END)
def evaluate():
    exp = entryBox.get()
    #print(exp)

    #square tree root
    findSQRT = exp.find("√")
    while findSQRT != -1:

#       x=exp.split("√")
        expL = exp[:findSQRT+1]
        #print("expL: " + expL)
        startFind=exp[findSQRT+1:]
        #print("startFind: " + startFind)
        findOper = startFind.find("+" or "-" or "*" or "/" or "%" or "(" or ")" or "**" or "^" or "[" or "]" or "{" or "}" or " " or "")
        #print("findOPER: ", findOper)
        if findOper != -1:
            findOper = findSQRT + findOper + 1
            expMid = exp[findSQRT+1:findOper]
            expR = exp[findOper:]
        elif findOper == -1:
            expMid = exp[findSQRT+1:]
            expR=""

        #print("findOPER modified: ", findOper)
        #print("expMid: " + expMid)
        #print("expR: " + expR)

        expL = expL.replace("√", "sqrt(")
        concatinationEXP = expL + expMid + ")" + expR
        #print("concat: " + concatinationEXP)
        exp = concatinationEXP

        findSQRT = exp.find("√")    #+10
        #print("findSQRT: ", findSQRT)

    findFACT = exp.find("!")
    expL=""
    expMid=""
    expR=""
    while findFACT != -1:


#       x=exp.split("√")
        expL = exp[:findFACT+1]
        #print("expL: " + expL)

        digits=""
        i=1
        while expL[findFACT-i].isdigit():
            #print("loop")
            digits=expL[findFACT-i]+digits[1:]
            i+=1
            #print(digits)
        expL = expL[:findFACT-i+1] + "factorial(" + digits + ")"
        #print(expL)

        exp = expL + exp[findFACT+1:]
        #print("Fact exp " + exp)

        findFACT = exp.find("!")    #+10
        #print("findFACT: ", findFACT)

    #pie
    findPIE = exp.find("π")
    #print("|-|-|-|")
    #print("where da pie? ", findPIE)
    while findPIE != -1:
       # if findPIE == len(exp)-1:
       #     print("Any more pie check? ", findPIE)
       #     exp = exp.replace("π", "*pi")
#        print("in da while: "+exp[findPIE] + " " + exp[findPIE-1] + " " + exp[findPIE+1])
        if findPIE == 0 and len(exp) == 1: #just pie(not on list)
#            print("only π")
            exp =  "pi"
#            print("inter-exp:", exp)
        elif findPIE == 0 and exp[findPIE+1].isdigit():
#            print("first π followed by numeric")
            exp = "pi*" + exp[findPIE+1:]
#            print("inter-exp:", exp)
        elif findPIE == 0 and not exp[findPIE+1].isdigit(): #first
#            print("first π followed by not numeric")
            exp = "pi" + exp[findPIE+1:]
#            print("inter-exp:", exp)
        elif findPIE == (len(exp)-1) and exp[findPIE-1].isdigit():
#            print("last π and numeric before it")
            exp = exp[:findPIE] + "*pi"
#            print("inter-exp:", exp)
        elif findPIE == (len(exp)-1) and not exp[findPIE-1].isdigit():
#            print("last π and not numeric before it")
            exp = exp[:findPIE] + "pi"
#            print("inter-exp:", exp)
        elif findPIE == findPIE and exp[findPIE-1].isdigit() and not exp[findPIE+1].isdigit():
#            print("left of π is numeric and right of π is not numeric")
            exp = exp[:findPIE] + "*pi" + exp[findPIE+1:]
#            print("inter-exp:", exp)
        elif findPIE == findPIE and not exp[findPIE-1].isdigit() and exp[findPIE+1].isdigit():
#            print("left of π is not numeric and right of π is numeric")
            exp = exp[:findPIE] + "pi*" + exp[findPIE+1:]
#            print("inter-exp:", exp)
        elif findPIE == findPIE and exp[findPIE-1].isdigit() and exp[findPIE+1].isdigit():
#            print("left of π is numeric and right of π is numeric")
            exp = exp[:findPIE] + "*pi*" + exp[findPIE+1:]
#            print("inter-exp:", exp)
        else: # both non-numeric
#            print("both left and right of π are numeric")
            exp = exp[:findPIE] + "pi" + exp[findPIE+1:]
#            print("inter-exp:", exp)
        findPIE = exp.find("π")
#        print("Any more pie? ", findPIE)
#    print("final-exp:", exp)
    try:
        result = eval(exp)
#        print(eval(exp))
        entryBox.delete(0, END)
        entryBox.insert(0, eval(exp))
    except SyntaxError or NameError or TypeError or Exception or ValueError or ZeroDivisionError or ArithmeticError:
#        print("Error")
        entryBox.delete(0, END)
        entryBox.insert(0, "Error")


#window setup
root = Tk()
root.title("Scientific Calculator PRO MAX")
root.geometry("350x400")

#box thing
entryBox=Entry(root, bg='White', width=45)
entryBox.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

#btns
c=0 #column
r=1 #row
btnsList = [
    "(", ")", "%", "AC","7","8","9", "/", "4","5","6", "*", "1","2","3", "-", "0", ".", "=", "+", "^","√", "π", "!"
]
#btnClicked = ""
btns = {}
message = ""
for anything in btnsList:
#    print(anything)
#    print(btns)

    #btns for loop
    #new function(not going to put into funcs.py for now!)
    def act(t=anything):
        if t == "^":
            t = "**"

        if t == "AC":
            return clear()
#        elif t == "√":
#            sqrt(int(entryBox.get()))
            #for sqrts in entryBox.get()
#            entryGet = entryBox.get()
#            print(entryGet)
#            num = t.rstrip(entryGet)
#            print(num)
        elif t == "=":
            return evaluate()
        else:
            return update_text(t)
    btns[anything]=Button(root, text = anything, padx=20, pady=10, command=act)
#    btnClicked = btnsList[i]
    btns[anything].grid(row=r, column=c)
    c+=1
    if c>3:
        c=0
        r+=1
