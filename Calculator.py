from tkinter import *
import math
import tkinter.messagebox



root = Tk()
root.title("Calculadora cientifica")
root.resizable(width=False,height=False)
root.geometry("400x492+460+40")
Mainframe = Frame(root, pady=2, relief=RIDGE)
Mainframe.grid()
calc =Frame(Mainframe, bd=20, pady=2, relief=RIDGE)
calc.grid()

class Calc():
	def __init__(self):
		self.total=0
		self.current=''
		self.input_value=True
		self.check_sum=False
		self.op=''
		self.result=False
    
    
    
	def numberEnter(self, num):
		self.result=False
		firstnum=txtDisplay.get()
		secondnum=str(num)
		if self.input_value:
			self.current = secondnum
			self.input_value=False
		else:
			if secondnum == '.':
				if secondnum in firstnum:
					return
			self.current = firstnum+secondnum
		self.display(self.current)

	def sum_of_total(self):
		self.result=True
		self.current=float(self.current)
		if self.check_sum==True:
			self.valid_function()
		else:
			self.total=float(txtDisplay.get())

	def display(self, value):
		txtDisplay.delete(0, END)
		txtDisplay.insert(0, value)

	def valid_function(self):
		if self.op == "add":
			self.total += self.current
		if self.op == "sub":
			self.total -= self.current
		if self.op == "multi":
			self.total *= self.current
		if self.op == "divide":
			self.total /= self.current
		if self.op == "mod":
			self.total %= self.current
		self.input_value=True
		self.check_sum=False
		self.display(self.total)

	def operation(self, op):
		self.current = float(self.current)
		if self.check_sum:
			self.valid_function()
		elif not self.result:
			self.total=self.current
			self.input_value=True
		self.check_sum=True
		self.op=op
		self.result=False

	def Clear_Entry(self):
		self.result = False
		self.current = "0"
		self.display(0)
		self.input_value=True

	def All_Clear_Entry(self):
		self.Clear_Entry()
		self.total=0

	def pi(self):
		self.result = False
		self.current = math.pi
		self.display(self.current)

	def tau(self):
		self.result = False
		self.current = math.tau
		self.display(self.current)

	def e(self):
		self.result = False
		self.current = math.e
		self.display(self.current)

	def mathPM(self):
		self.result = False
		self.current = -(float(txtDisplay.get()))
		self.display(self.current)

	def squared(self):
		self.result = False
		self.current = math.sqrt(float(txtDisplay.get()))
		self.display(self.current)

	def cos(self):
		self.result = False
		self.current = math.cos(math.radians(float(txtDisplay.get())))
		self.display(self.current)

	def cosh(self):
		self.result = False
		self.current = math.cosh(math.radians(float(txtDisplay.get())))
		self.display(self.current)

	def tan(self):
		self.result = False
		self.current = math.tan(math.radians(float(txtDisplay.get())))
		self.display(self.current)

	def tanh(self):
		self.result = False
		self.current = math.tanh(math.radians(float(txtDisplay.get())))
		self.display(self.current)

	def sin(self):
		self.result = False
		self.current = math.sin(math.radians(float(txtDisplay.get())))
		self.display(self.current)

	def sinh(self):
		self.result = False
		self.current = math.sinh(math.radians(float(txtDisplay.get())))
		self.display(self.current)

	def log(self):
		self.result = False
		self.current = math.log(float(txtDisplay.get()))
		self.display(self.current)

	def exp(self):
		self.result = False
		self.current = math.exp(float(txtDisplay.get()))
		self.display(self.current)

	def acosh(self):
		self.result = False
		self.current = math.acosh(float(txtDisplay.get()))
		self.display(self.current)

	def asinh(self):
		self.result = False
		self.current = math.asinh(float(txtDisplay.get()))
		self.display(self.current)
 

	def expm1(self):
		self.result = False
		self.current = math.expm1(float(txtDisplay.get()))
		self.display(self.current)

	def lgamma(self):
		self.result = False
		self.current = math.lgamma(float(txtDisplay.get()))
		self.display(self.current)

	def degrees(self):
		self.result = False
		self.current = math.degrees(float(txtDisplay.get()))
		self.display(self.current)

	def log2(self):
		self.result = False
		self.current = math.log2(float(txtDisplay.get()))
		self.display(self.current)

	def log10(self):
		self.result = False
		self.current = math.log10(float(txtDisplay.get()))
		self.display(self.current)

	def log1p(self):
		self.result = False
		self.current = math.log1p(float(txtDisplay.get()))
		self.display(self.current)
    



#===================================================================================================================#

added_value = Calc()
txtDisplay= Entry(calc, font =('arial',16,'bold'),bg="SpringGreen2", bd=30, width=26, justify=RIGHT)
txtDisplay.grid(row=0,column=0, columnspan=4, pady=1)
txtDisplay.insert(0, "0")

numericbutton = "789456123"
i =0
btn=[]
for j in range(2,5):
    for q in range(3):
      btn.append(Button(calc, width=6, height=2, font=('arial',16,'bold'),bd=4,
      text=numericbutton[i]))
      btn[i].grid(row =j, column=q,pady=1)
      btn[i]["command"]=lambda x=numericbutton[i]:added_value.numberEnter(x)
      i +=1
 #===================================================================================================================#
btn0=Button(calc, text="0", width=6, height=2, font=('arial',16,'bold'),bd=4,
 bg="SpringGreen2", command=lambda:added_value.numberEnter(".")).grid(row=5, column=0, pady=1)

btndiv=Button(calc, text=chr(247), width=6, height=2, font=('arial',16,'bold'),bd=4,
 bg="SpringGreen2",command=lambda:added_value.operation("dividie")).grid(row=5, column=3, pady=1)

btnmult=Button(calc, text=chr(42), width=6, height=2, font=('arial',16,'bold'),bd=4,
 bg="SpringGreen2",command=lambda:added_value.operation("multi")).grid(row=4, column=3, pady=1)

btnres=Button(calc, text=chr(45), width=6, height=2, font=('arial',16,'bold'),bd=4,
 bg="SpringGreen2", command=lambda:added_value.operation("sub")).grid(row=3, column=3, pady=1)

btndot=Button(calc, text=chr(183), width=6, height=2, font=('arial',16,'bold'),bd=4,
 bg="SpringGreen2",command=lambda:added_value.numberEnter(".")).grid(row=5, column=1, pady=1)

btnadd=Button(calc, text=chr(43), width=6, height=2, font=('arial',16,'bold'),bd=4,
 bg="SpringGreen2",command=lambda:added_value.operation("add")).grid(row=2, column=3, pady=1)

btnpm=Button(calc, text=chr(177), width=6, height=2, font=('arial',16,'bold'),bd=4,
 bg="SpringGreen2",command=added_value.mathPM).grid(row=1, column=3, pady=1)
 

btnclearentry=Button(calc, text= chr(67) + chr(69), width=6, height=2, font=('arial',16,'bold'),bd=4,
 bg="SpringGreen2",
 command= added_value.Clear_Entry ).grid(row=1, column=1, pady=1)

btnclear=Button(calc, text=chr(67), width=6, height=2, font=('arial',16,'bold'),bd=4,
 bg="SpringGreen2",
 command= added_value.All_Clear_Entry ).grid(row=1, column=2, pady=1)

btnequals=Button(calc, text=chr(61), width=6, height=2, font=('arial',16,'bold'),bd=4,
 bg="SpringGreen2",command=added_value.sum_of_total).grid(row=5, column=2, pady=1)
#===================================================================================================================#
btnsin=Button(calc, text="sin", width=6, height=2, font=('arial',16,'bold'),bd=4,
 bg="SpringGreen2",command=added_value.sin).grid(row=1, column=4, padx=5,pady=1 )

btntan=Button(calc, text="tan", width=6, height=2, font=('arial',16,'bold'),bd=4,
 bg="SpringGreen2",command=added_value.tan).grid(row=1, column=5,pady=1 )

btncos=Button(calc, text="cos", width=6, height=2, font=('arial',16,'bold'),bd=4,
 bg="SpringGreen2").grid(row=1, column=6,pady=1 )

btnpi=Button(calc, text="π", width=6, height=2, font=('arial',16,'bold'),bd=4,
 bg="SpringGreen2",command=added_value.pi).grid(row=1, column=7,pady=1 )
#===================================================================================================================#
btnsinh=Button(calc, text="sinh", width=6, height=2, font=('arial',16,'bold'),bd=4,
command=added_value.sinh).grid(row=2, column=4, padx=5,pady=1 )

btntanh=Button(calc, text="tanh", width=6, height=2, font=('arial',16,'bold'),bd=4,
command=added_value.tanh).grid(row=2, column=5,pady=1 )

btncosh=Button(calc, text="cosh", width=6, height=2, font=('arial',16,'bold'),bd=4,
               command=added_value.cosh).grid(row=2, column=6,pady=1 )

btn2pi=Button(calc, text="2π", width=6, height=2, font=('arial',16,'bold'),bd=4,
 bg="SpringGreen2",command=added_value.tau).grid(row=2, column=7,pady=1 )
#===================================================================================================================#
btne=Button(calc, text="e", width=6, height=2, font=('arial',16,'bold'),bd=4,
command=added_value.e
).grid(row=3, column=4, padx=5,pady=1 )

btnmod=Button(calc, text="mod", width=6, height=2, font=('arial',16,'bold'),bd=4,
command=lambda:added_value.operation("mod")).grid(row=3, column=5,pady=1 )

btnexp=Button(calc, text="exp", width=6, height=2, font=('arial',16,'bold'),bd=4,
command=added_value.exp).grid(row=3, column=6,pady=1 )

btnlog=Button(calc, text="log", width=6, height=2, font=('arial',16,'bold'),bd=4,
 bg="SpringGreen2",command=added_value.log).grid(row=3, column=7,pady=1 )
#===================================================================================================================#
btnasinh=Button(calc, text="asinh", width=6, height=2, font=('arial',16,'bold'),bd=4,
command=added_value.asinh).grid(row=4, column=4, padx=5,pady=1 )

btnacosh=Button(calc, text="acosh", width=6, height=2, font=('arial',16,'bold'),bd=4,
command=added_value.acosh).grid(row=4, column=5,pady=1 )

btndeg=Button(calc, text="deg", width=6, height=2, font=('arial',16,'bold'),bd=4,
command=added_value.degrees).grid(row=4, column=6,pady=1 )

btnlog2=Button(calc, text="log2", width=6, height=2, font=('arial',16,'bold'),bd=4,
 bg="SpringGreen2",command=added_value.log2).grid(row=4, column=7,pady=1 )
 #===================================================================================================================#
btnlgamma=Button(calc, text="lgamma", width=6, height=2, font=('arial',16,'bold'),bd=4,
command=added_value.lgamma).grid(row=5, column=4, padx=5,pady=1 )

btnexpm1=Button(calc, text="expm1", width=6, height=2, font=('arial',16,'bold'),bd=4,
command=added_value.expm1).grid(row=5, column=5,pady=1 )

btnlog1p=Button(calc, text="log1p", width=6, height=2, font=('arial',16,'bold'),bd=4,
command=added_value.log1p).grid(row=5, column=6,pady=1 )

btnlog10=Button(calc, text="log10", width=6, height=2, font=('arial',16,'bold'),bd=4,
 bg="SpringGreen2",command=added_value.log10).grid(row=5, column=7,pady=1 )
 #===================================================================================================================#
def iExit():
  iExit = tkinter.messagebox.askyesno("Calculadora cientifica","Confirma si quieres salir")
  if iExit > 0:
    root.destroy()
    return

def cientifica():
    root.geometry("796x492+460+40")
    root.resizable(width=False,height=False)
    txtDisplay.delete(0, END)
    txtDisplay.delete(0, "0")
    lblDispaly =Label(calc,text="Calculadora Cientifica",font=('arial',20,'bold'),padx=9,
    bg="SpringGreen2",justify=CENTER)
    lblDispaly.grid(row =0, column= 4, columnspan=4)



def estandar():
    root.geometry("400x492+460+40")
    root.resizable(width=False,height=False)
    txtDisplay.delete(0, END)
    txtDisplay.delete(0, "0")




menubar = Menu(calc)
filemenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label ="Archivo", menu=filemenu)
filemenu.add_command(label ="Estandar", command=estandar)
filemenu.add_separator()
filemenu.add_command(label ="cientifica", command =cientifica)
filemenu.add_separator()
filemenu.add_command(label ="Salir", command =iExit)

root.config(menu = menubar)
root.mainloop()
