from tkinter import*
import math 
import sre_parse
import tkinter.messagebox


root = Tk()
root.title("Calculadora cientifica")
root.resizable(width=False,height=False)
root.geometry("400x492+460+40")
Mainframe = Frame(root, pady=2, relief=RIDGE)
Mainframe.grid()
calc =Frame(Mainframe, bd=20, pady=2, relief=RIDGE)
calc.grid()

class Calculadora():
  def __init__(self):
      self.total = 0
      self.current = ""
      self.input_value = True
      self.check_sum = False
      self.op=""
      self.result = False

added_value = Calculadora

txtresult = Entry(calc, font =('arial',16,'bold'),bg="SpringGreen2", bd=30, width=26, justify=RIGHT)
txtresult.grid(row=0,column=0, columnspan=4, pady=1)
txtresult.insert(0, "0")

menubar = Menu(calc)
filemenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label ="Archivo", menu=filemenu)
filemenu.add_command(label ="Estandar")
filemenu.add_separator()
filemenu.add_command(label ="cientifica")
filemenu.add_separator()
filemenu.add_command(label ="Salir")

root.config(menu = menubar)
root.mainloop()
