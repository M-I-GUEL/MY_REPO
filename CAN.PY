import tkinter as tk
root = tk.Tk()

root.title('CALCULATOR')

ent = tk.Entry(root, width = '40', borderwidth='5')
ent.grid(row=0, column=0,columnspan=3,padx =10,pady=10)

def click(num):
   acc = ent.get()
   ent.delete(0, 'end')
   ent.insert(0, str(acc) + str(num))
    
def clear():

   ent.delete(0,'end')


def add():
   first = ent.get()
   global f_number
   global calc
   calc = 'adding'
   f_number = int(first)


   ent.delete(0,'end')


def equal():
   second = ent.get()
   
   ent.delete(0,'end')
   if calc == 'adding':
       ent.insert(0, f_number + int(second))

   if calc == 'subtracting':
       ent.insert(0, f_number - int(second))
   if calc == 'multiply':
       
       ent.insert(0, f_number * int(second))

   if calc == 'divide':
       ent.insert(0, f_number / int(second))
       


def subtract():
   first = ent.get()
   global f_number
   global calc
   calc = 'subtracting'
   f_number = int(first)


   ent.delete(0,'end')


def divide():
   first = ent.get()
   global f_number
   global calc
   calc = 'divide'
   f_number = int(first)


   ent.delete(0,'end')


def multiply():
   first = ent.get()
   global f_number
   global calc
   calc = 'multiply'
   f_number = int(first)


   ent.delete(0,'end')




button_1 = tk.Button(root,background='light blue',foreground='black',text='1',padx=40,pady=20,command=lambda : click(1))
button_2 = tk.Button(root,background='light blue',foreground='black',text='2',padx=40,pady=20,command=lambda : click(2))
button_3 = tk.Button(root,background='light blue',foreground='black',text='3',padx=40,pady=20,command=lambda : click(3))
button_4 = tk.Button(root,background='light blue',foreground='black',text='4',padx=40,pady=20,command=lambda : click(4))
button_5 = tk.Button(root,background='light blue',foreground='black',text='5',padx=40,pady=20,command=lambda : click(5))
button_6 = tk.Button(root,background='light blue',foreground='black',text='6',padx=40,pady=20,command=lambda : click(6))
button_7 = tk.Button(root,background='light blue',foreground='black',text='7',padx=40,pady=20,command=lambda : click(7))
button_8 = tk.Button(root,background='light blue',foreground='black',text='8',padx=40,pady=20,command=lambda : click(8))
button_9 = tk.Button(root,background='light blue',foreground='black',text='9',padx=40,pady=20,command=lambda : click(9))
button_0 = tk.Button(root,background='light blue',foreground='black',text='0',padx=40,pady=20,command=lambda : click(0))
button_add =tk.Button(root,background='light blue',foreground='black',text='+',padx=40,pady=20,command=lambda : add())
button_clear = tk.Button(root,background='light blue',foreground='black',text='clear',padx=80,pady=20,command=lambda : clear())
button_equal =tk.Button(root,background='pink',foreground='black',text='=',padx=87,pady=20,command=lambda : equal())
button_divide =tk.Button(root,background='light blue',foreground='black',text='/',padx=40,pady=20,command=lambda : divide())
button_multiply =tk.Button(root,background='light blue',foreground='black',text='*',padx=40,pady=20,command=lambda : multiply())
button_subtract=tk.Button(root,background='light blue',foreground='black',text='-',padx=40,pady=20,command=lambda : subtract())

button_7.grid(row=1,column=0)
button_8.grid(row=1,column=1)
button_9.grid(row=1,column=2)


button_4.grid(row=2,column=0)
button_5.grid(row=2,column=1)
button_6.grid(row=2,column=2)


button_1.grid(row=3,column=0)
button_2.grid(row=3,column=1)
button_3.grid(row=3,column=2)


button_0.grid(row=4,column=0)
button_clear.grid(row=4,column=1,columnspan=2)
button_equal.grid(row=5,column=1,columnspan=2)
button_add.grid(row=5,column=0)



button_multiply.grid(row=6, column=0)
button_subtract.grid(row=6,column=1)
button_divide.grid(row=6,column=2)






root.mainloop()