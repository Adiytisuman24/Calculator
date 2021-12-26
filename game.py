from tkinter import *
root=Tk()
expression=""

def press(num):
    global expression
    express=expression+str(num)
    equation.set(expression)


def equalpress():
 try:
    global expression
    total=str(eval(expression))
    equation.set(total)
    expression=""
 except:
     equation.set(" error ")
     expression=""

def clear():
    global expression
    expression=""
    equation.set("")  

if __name__ == "___main___":
   root=Tk()
   root.configure(background="white")
   root.title("calculator")
   root.geometry("900*600")
   equation=StringVar()
   expression_field=Entry(root,textVariable=equation)
   expression_field.grid(columnspan=6,ipadx=10)



button1 = Button(root,text='1',height='1',width='6',command=lambda: press(1))
button1.grid(row=2,column=0)

button2=Button(root,text='2',height='1',width='6',command=lambda:press(2))
button2.grid(row=2,column=1)

button3=Button(root,text='3',height='1',width='6')
button3.grid(row=2,column=2)

button4=Button(root,text='4',height='1',width='6')
button4.grid(row=3,column=0)

button5=Button(root,text='5',height='1',width='6')
button5.grid(row=3,column=1)

button6=Button(root,text='6',height='1',width='6')
button6.grid(row=3,column=2)

button7=Button(root,text='7',height='1',width='6')
button7.grid(row=4,column=0)

button8=Button(root,text='8',height='1',width='6')
button8.grid(row=4,column=1)

button9=Button(root,text='9',height='1',width='6')
button9.grid(row=4,column=2)

button0=Button(root,text='0',height='1',width='6')
button0.grid(row=5,column=1)

buttonadd=Button(root,text='+',height='1',width='6')
buttonadd.grid(row=3,column=3)

buttonsubtract=Button(root,text='-',height='1',width='6')
buttonsubtract.grid(row=4,column=3)

buttonmultiply=Button(root,text='*',height='1',width='6')
buttonmultiply.grid(row=5,column=2)

buttondivide=Button(root,text='÷',height='1',width='6')
buttondivide.grid(row=5,column=3)

buttondecimal=Button(root,text='.',height='1',width='6')
buttondecimal.grid(row=5,column=0)

buttonclear=Button(root,text='C',height='1',width='6')
buttonclear.grid(row=2,column=3)

mainloop()
 