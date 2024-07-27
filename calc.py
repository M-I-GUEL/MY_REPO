import tkinter
import customtkinter


customtkinter.set_appearance_mode('dark')
customtkinter.set_default_color_theme('blue')



root = customtkinter.CTk()



root.title('BMI CALCULATOR')
root.geometry('900x900')


enter = customtkinter.CTkEntry(root, corner_radius=5,placeholder_text='Enter you height',width=200,)


enter.pack(pady=20)
enter2 = customtkinter.CTkEntry(root, corner_radius=5,placeholder_text='Enter you weight',width=200,)

enter2.pack(pady=20)

def clear():
    enter.delete(0, 'end')
    enter2.delete(0, 'end')
    results.configure(text ='YOUR BMI IS:')
def result():
    calc = int(enter.get()) * int(enter.get())
    calc1 = int(enter2.get()) / calc
    calc2 = calc1 * 10000
    calc3 = round(calc2, 1)
    
    results.configure(text= str(calc3))

    if calc3 < 18:
        results.configure(text= f'{str(calc3)} : SEVERELY UNDERWEIGHT', text_color='red')
    elif calc3 > 18 and calc3 < 24:
        results.configure(text= f'{str(calc3)} : HEALTHY',text_color='yellow')
    elif calc3 > 24 and calc3 < 28:
        results.configure(text= f'{str(calc3)} :  NORMAL',text_color='blue')
    elif calc3 > 28 and calc3 < 30:
        results.configure(text= f'{str(calc3)} : OVERWEIGHT',text_color='cyan')
    elif calc3 > 30:
        results.configure(text= f'{str(calc3)} : OBESE',text_color='brown')
    else:
        pass
create = customtkinter.CTkButton(root, text='calculate bmi',corner_radius=10,height=20,width=202,command = result)

create.pack(pady=20)
create1 = customtkinter.CTkButton(root, text='clear bmi',corner_radius=10,height=20,width=202,command =clear)
create1.pack(pady=20)

results = customtkinter.CTkLabel(root, text='YOUR BMI IS:')
bug = customtkinter.CTkLabel(root, text= 'SEVERELY UNDERWEIGHT < 18', text_color='red')
bug1 = customtkinter.CTkLabel(root, text= 'HEALTHY > 18 and < 24',text_color='yellow')
bug2 = customtkinter.CTkLabel(root, text= 'NORMAL > 24 and < 28',text_color='blue')
bug3 = customtkinter.CTkLabel(root, text= 'OVERWEIGHT > 28 and < 30',text_color='cyan')
bug4 = customtkinter.CTkLabel(root, text= 'OBESE > 30',text_color='brown')

bug.pack(pady=10)
bug1.pack(pady=10)
bug2.pack(pady=10)
bug3.pack(pady=10)
bug4.pack(pady=10)

results.pack(pady = 50)

root.mainloop()