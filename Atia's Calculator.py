import customtkinter
import math
from tkinter import END
from tkinter import messagebox

# Functionality Part
def Allclear(): 
    entryField.delete(0, END) 

def Clear(): 
    pass

def buttonClick(number): 
    entryField.insert(END, number)

def buttonSin():
    expression = entryField.get()
    result = math.sin(math.radians(float(expression)))
    ans = round(result, 2)
    entryField.delete(0, END)
    entryField.insert(0, ans)

def buttonCos():
    expression = entryField.get()
    result = math.cos(math.radians(float(expression)))
    ans = round(result, 2)
    entryField.delete(0, END)
    entryField.insert(0, ans)

def buttonTan():
    expression = entryField.get()
    result = math.tan(math.radians(float(expression)))
    ans = round(result, 2)
    entryField.delete(0, END)
    entryField.insert(0, ans)

def buttonLog():
    expression = entryField.get()
    result = math.log2(float(expression))
    ans = round(result, 1)
    entryField.delete(0, END)
    entryField.insert(0, ans)

def buttonExp():
    expression = entryField.get()
    result = eval(f"{expression}**2")
    entryField.delete(0, END)
    entryField.insert(0, result)

def buttonSqRoot():
    expression = entryField.get()
    result = eval(f"{expression}**0.5")
    ans = round(result,1)
    entryField.delete(0, END)
    entryField.insert(0, ans)

def buttonCubeRoot():
    expression = entryField.get()
    result = eval(f"{expression}**(1/3)")
    ans = round(result, 1)
    entryField.delete(0, END)
    entryField.insert(0, ans)

def buttonBack(): 
    current_text = entryField.get()
    if len(current_text) > 0:
        entryField.delete(len(current_text) - 1, END)

def answer():
    expression = entryField.get() 
    try:
        result = eval(expression)
        ans = round(result, 2) 
        entryField.delete(0, END) 
        entryField.insert(0, ans) 
    except SyntaxError:
        messagebox.showerror('Error', 'Wrong Input! Please Try Again')
    except ZeroDivisionError:
        messagebox.showerror('Error', 'A number cannot be divided by Zero')

# GUI Part
root = customtkinter.CTk() 
root.title('Calculator By Attia') 
root.geometry('290x290') 
root.config(bg='black') 

entryField = customtkinter.CTkEntry(root, font=('arial', 20, 'bold'), text_color='white', fg_color='limegreen',
                                    border_color='white', width=280, height=50, bg_color='black')
entryField.grid(row=0, column=0, padx=5, pady=5, columnspan=4) 

# Row 1 = 7,8,9,+ 
b7 = customtkinter.CTkButton(root, text='7', font=('arial', 20, 'bold'), width=60, bg_color='black', cursor='hand2',
                            fg_color='grey16', hover_color='grey50', command=lambda: buttonClick('7'))
b7.grid(row=1, column=0, padx=1, pady=1)
b8 = customtkinter.CTkButton(root, text='8', font=('arial', 20, 'bold'), width=60, bg_color='black', cursor='hand2',
                            fg_color='grey16', hover_color='grey50', command=lambda: buttonClick('8'))
b8.grid(row=1, column=1, padx=1, pady=1)
b9 = customtkinter.CTkButton(root, text='9', font=('arial', 20, 'bold'), width=60, bg_color='black', cursor='hand2',
                            fg_color='grey16', hover_color='grey50', command=lambda: buttonClick('9'))
b9.grid(row=1, column=2, padx=1, pady=1)
b_add = customtkinter.CTkButton(root, text='+', font=('arial', 20, 'bold'), width=60, bg_color='black', cursor='hand2',
                                fg_color="DarkGoldenrod1", hover_color='goldenrod4', command=lambda: buttonClick('+'))
b_add.grid(row=1, column=3, padx=1, pady=1)

# Row 2 = 4,5,6,-
b4 = customtkinter.CTkButton(root, text='4', font=('arial', 20, 'bold'), width=60, bg_color='black', cursor='hand2',
                            fg_color='grey16', hover_color='grey50', command=lambda: buttonClick('4'))
b4.grid(row=2, column=0, padx=1, pady=1)
b5 = customtkinter.CTkButton(root, text='5', font=('arial', 20, 'bold'), width=60, bg_color='black', cursor='hand2',
                            fg_color='grey16', hover_color='grey50', command=lambda: buttonClick('5'))
b5.grid(row=2, column=1, padx=1, pady=1)
b6 = customtkinter.CTkButton(root, text='6', font=('arial', 20, 'bold'), width=60, bg_color='black', cursor='hand2',
                            fg_color='grey16', hover_color='grey50', command=lambda: buttonClick('6'))
b6.grid(row=2, column=2, padx=1, pady=1)
b_sub = customtkinter.CTkButton(root, text='-', font=('arial', 20, 'bold'), width=60, bg_color='black', cursor='hand2',
                                fg_color="DarkGoldenrod1", hover_color='goldenrod4', command=lambda: buttonClick('-'))
b_sub.grid(row=2, column=3, padx=1, pady=1)

# Row 3 = 1,2,3,*
b1 = customtkinter.CTkButton(root, text='1', font=('arial', 20, 'bold'), width=60, bg_color='black', cursor='hand2',
                            fg_color='grey16', hover_color='grey50', command=lambda: buttonClick('1'))
b1.grid(row=3, column=0, padx=1, pady=1)
b2 = customtkinter.CTkButton(root, text='2', font=('arial', 20, 'bold'), width=60, bg_color='black', cursor='hand2',
                            fg_color='grey16', hover_color='grey50', command=lambda: buttonClick('2'))
b2.grid(row=3, column=1, padx=1, pady=1)
b3 = customtkinter.CTkButton(root, text='3', font=('arial', 20, 'bold'), width=60, bg_color='black', cursor='hand2',
                            fg_color='grey16', hover_color='grey50', command=lambda: buttonClick('3'))
b3.grid(row=3, column=2, padx=1, pady=1)
b_mul = customtkinter.CTkButton(root, text='x', font=('arial', 20, 'bold'), width=60, bg_color='black', cursor='hand2',
                                fg_color="DarkGoldenrod1", hover_color='goldenrod4', command=lambda: buttonClick('*'))
b_mul.grid(row=3, column=3, padx=1, pady=1)

# Row 4 = 0,.,C,/
b0 = customtkinter.CTkButton(root, text='0', font=('arial', 20, 'bold'), width=60, bg_color='black', cursor='hand2',
                            fg_color='grey16', hover_color='grey50', command=lambda: buttonClick('0'))
b0.grid(row=4, column=0, padx=1, pady=1)
b_back = customtkinter.CTkButton(root, text='←', font=('arial', 20, 'bold'), width=60, bg_color='black', cursor='hand2',
                                 fg_color="firebrick1", hover_color='red3', command=buttonBack)
b_back.grid(row=4, column=1, padx=1, pady=1)
b_Clear = customtkinter.CTkButton(root, text='C', font=('arial', 20, 'bold'), width=60, bg_color='black', cursor='hand2',
                                  fg_color="firebrick1", hover_color='red3', command=Allclear)
b_Clear.grid(row=4, column=2, padx=1, pady=1)
b_div = customtkinter.CTkButton(root, text='/', font=('arial', 20, 'bold'), width=60, bg_color='black', cursor='hand2',
                                fg_color="DarkGoldenrod1", hover_color='goldenrod4', command=lambda: buttonClick('/'))
b_div.grid(row=4, column=3, padx=1, pady=1)

# Row 5 = exp, sqrt, cuberoot, pi
b_exp = customtkinter.CTkButton(root, text='x²', font=('arial', 20, 'bold'), width=60, bg_color='black', cursor='hand2',
                                fg_color="DarkGoldenrod1", hover_color='goldenrod4', command=buttonExp)
b_exp.grid(row=5, column=0, padx=1, pady=1)
b_sqroot = customtkinter.CTkButton(root, text='√', font=('arial', 20, 'bold'), width=60, bg_color='black', cursor='hand2',
                                   fg_color="DarkGoldenrod1", hover_color='goldenrod4', command=buttonSqRoot)
b_sqroot.grid(row=5, column=1, padx=1, pady=1)
b_cuberoot = customtkinter.CTkButton(root, text='³√', font=('arial', 20, 'bold'), width=60, bg_color='black', cursor='hand2',
                                     fg_color="DarkGoldenrod1", hover_color='goldenrod4', command=buttonCubeRoot)
b_cuberoot.grid(row=5, column=2, padx=1, pady=1)
bdot = customtkinter.CTkButton(root, text='.', font=('arial', 20, 'bold'), width=60, bg_color='black', cursor='hand2',
                              fg_color="DarkGoldenrod1", hover_color='goldenrod4', command=lambda: buttonClick('.'))
bdot.grid(row=5, column=3, padx=1, pady=1)

# Row 6 = sin, cos, tan, log2
b_sin = customtkinter.CTkButton(root, text='sin(θ)', font=('arial', 20), width=60, bg_color='black', cursor='hand2',
                                fg_color="DarkGoldenrod1", hover_color='goldenrod4', command=buttonSin)
b_sin.grid(row=6, column=0, padx=1, pady=1)
b_cos = customtkinter.CTkButton(root, text='cos(θ)', font=('arial', 20), width=60, bg_color='black', cursor='hand2',
                                fg_color="DarkGoldenrod1", hover_color='goldenrod4', command=buttonCos)
b_cos.grid(row=6, column=1, padx=1, pady=1)
b_tan = customtkinter.CTkButton(root, text='tan(θ)', font=('arial', 20), width=60, bg_color='black', cursor='hand2',
                                fg_color="DarkGoldenrod1", hover_color='goldenrod4', command=buttonTan)
b_tan.grid(row=6, column=2, padx=1, pady=1)
b_log = customtkinter.CTkButton(root, text='log2', font=('arial', 20), width=60, bg_color='black', cursor='hand2',
                                fg_color="DarkGoldenrod1", hover_color='goldenrod4', command=buttonLog)
b_log.grid(row=6, column=3, padx=1, pady=1)

# Row 7 = Equal To Sign
bequal = customtkinter.CTkButton(root, text='=', font=('arial', 20, 'bold'), width=280, bg_color='black',
                                 cursor='hand2', fg_color="steel blue", hover_color='sky blue', command=answer)
bequal.grid(row=7, column=0, columnspan=4, padx=5, pady=5)

root.mainloop()
