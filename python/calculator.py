#calculator using tkinter
#import everything from tkinter module
import tkinter

#globally declare the expression variable
expression = ""

#function to update expression variable in the text entry box
def press(num):
    #point out the global expression variable
    global expression 

    #concatenation of string 
    expression = expression + str(num)

    #update the expression by using set method 
    equation.set(expression)

def equalpress():
    #Try and except statement is used for handling 
    #the errors like zero division error etc. 
    
    #Put the code in the try block which may generate
    #the error.
    try:
        global expression 

        # eval function evaluate the expression 
        # and str function convert the result 
        # into string 
        total = str(eval(expression))

        equation.set(total)

        # initialze the expression variable 
        # by empty string 
        expression = ""

        #if error is generated then handle
        # by the except 

    except:
            equation.set(" error ")
            expression = ""

#Function to clear the content 
# of text except block
def clear():
    global expression 
    expression =  ""
    equation.set("")

# Driver code
if __name__ == "__main__":
    #creta a gui window
    gui = tkinter.Tk()

    gui.title("Calculator")
    # Set the background colour of the GUI window
    gui.configure(background="linen")

    #set the confiuration of the gui window
    gui.geometry('435x230')

    #stringvar is a variable class 
    #an instance of this class is created here
    equation = tkinter.StringVar()
    
    #create the entry box for showing the expression
    expression_field = tkinter.Entry(gui,textvariable = equation)
    #grid method is used for placing the widget at respective positions 
    #in the table like structure
    expression_field.grid(columnspan=4,ipadx = 70) 
    #ipadx ,ipady -how many pixel to pad widget ,horizontally and vertically,inside widget's borders.
    
    equation.set('enter your expression')

    #create a button and place at a perticular location inside the root window.
    #when user press a button command of function affiliated to the button is executed
    button1 = tkinter.Button(gui, text=' 1 ',fg ='black',bg ='light cyan',command = lambda: press(1),height= 2, width = 14)
    button1.grid(row=3,column=0)
    button2 = tkinter.Button(gui, text=' 2 ',fg ='black',bg ='light cyan',command = lambda: press(2),height= 2, width = 14)
    button2.grid(row=3,column=1)
    button3 = tkinter.Button(gui, text=' 3 ',fg ='black',bg ='light cyan',command = lambda: press(3),height= 2, width = 14)
    button3.grid(row=3,column=2)
    button4 = tkinter.Button(gui, text=' 4 ',fg ='black',bg ='light cyan',command = lambda: press(4),height= 2, width = 14)
    button4.grid(row=4,column=0)
    button5 = tkinter.Button(gui, text=' 5 ',fg ='black',bg ='light cyan',command = lambda: press(5),height= 2, width = 14)
    button5.grid(row=4,column=1)
    button6 = tkinter.Button(gui, text=' 6 ',fg ='black',bg ='light cyan',command = lambda: press(6),height= 2, width = 14)
    button6.grid(row=4,column=2)
    button7 = tkinter.Button(gui, text=' 7 ',fg ='black',bg ='light cyan',command = lambda: press(7),height= 2, width = 14)
    button7.grid(row=5,column=0)
    button8 = tkinter.Button(gui, text=' 8 ',fg ='black',bg ='light cyan',command = lambda: press(8),height= 2, width = 14)
    button8.grid(row=5,column=1)
    button9 = tkinter.Button(gui, text=' 9 ',fg ='black',bg ='light cyan',command = lambda: press(9),height= 2, width = 14)
    button9.grid(row=5,column=2)
    button0 = tkinter.Button(gui, text=' 0 ',fg ='black',bg ='light cyan',command = lambda: press(0),height= 2, width = 14)
    button0.grid(row=6,column=0)
    plus = tkinter.Button(gui, text=' + ',fg ='black',bg ='light cyan',command = lambda: press('+'),height= 2, width = 14)
    plus.grid(row=3,column=3)
    minus = tkinter.Button(gui, text=' - ',fg ='black',bg ='light cyan',command = lambda: press('-'),height= 2, width = 14)
    minus.grid(row=4,column=3)
    multiply = tkinter.Button(gui, text=' * ',fg ='black',bg ='light cyan',command = lambda: press('*'),height= 2, width = 14)
    multiply.grid(row=5,column=3)
    divide = tkinter.Button(gui, text=' / ',fg ='black',bg ='light cyan',command = lambda: press('/'),height= 2, width = 14)
    divide.grid(row=6,column=3)
    equal = tkinter.Button(gui, text=' = ',fg ='black',bg ='light cyan',command = lambda: equalpress,height= 2, width = 14)
    equal.grid(row=6,column=2)
    clear = tkinter.Button(gui, text=' C ',fg ='black',bg ='light cyan',command = lambda: clear,height= 2, width = 14)
    clear.grid(row=2,column=0)
    decimal = tkinter.Button(gui, text=' . ',fg ='black',bg ='light cyan',command = lambda: press('.'),height= 2, width = 14)
    decimal.grid(row=6,column=1)
    #start the gui
    gui.mainloop()