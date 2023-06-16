import tkinter as tk
from tkinter import CENTER,LEFT,RIGHT,Text,INSERT
import subprocess
import sys
from tkinter import messagebox
from tkinter.messagebox import askyesno
import tkinter.font as tkFont
import time
PyPath = '.\env\Scripts\python.exe'

def button1_click():
    answer = askyesno("Увага", "Якщо Ви вперше користуєтесь додатком рекомендуєм спочатику навчити програму під вас, Бажаєте виконати навчання?")
    if answer == True:
        button2_click()
        time.sleep(60)
        subprocess.call([PyPath, '.\\first_part\gui.py'])
    elif answer == False:
        messagebox.showinfo("INFO","Для того щоб додати букву у речення натисніть Enter, щоб додати пропуск у речення натисність пробіл, щоб стерти останній символ, натисніть BackSpace, Esc для виходу")
        subprocess.call([PyPath, '.\\first_part\gui.py'])
        
def button2_click():
    #root.withdraw()  # Приховати головне вікно
    msg=messagebox.askokcancel(title="Навчання моделі", message="Зараз відкриється вікно з вашим зображення, при натисканні вказаної кнопки, почнеться считування вашої руки протягом декількох секунд, змінюйте положення руки, ближче і дальше від камери, повторіть цей процес для кожної букви вказаної на зобреженні, считування йде алфавітному порядку!Щоб вийти натисніть декілька разів ESC")
    if msg == True:
        subprocess.call([PyPath,'.\\first_part\\test2.py'])
        
    #     process1.wait()  # Очікувати завершення першого процесу
    #     messagebox.showinfo("INFO","Зчитування завершено!")
    #     process2 = subprocess.Popen([PyPath,'D:\DZ\S6\diploma\\first_part\create_dataset.py'], stdout=subprocess.PIPE)
    #     process2.wait()  # Очікувати завершення другого процесу
    #     messagebox.showinfo("INFO","Створення датасету завершено!")
    #     process3 = subprocess.Popen([PyPath,'D:\DZ\S6\diploma\\first_part\\train_classifier.py'], stdout=subprocess.PIPE)
    #     process3.wait()  # Очікувати завершення другого процесу
    #     messagebox.showinfo("INFO","Створення моделі завершено!")
    else:
        root.update()
    #root.deiconify()  # Відновити головне вікно після завершення виконання всіх файлів
def button3_click():
    #root.withdraw()  # Приховати головне вікно
    subprocess.call([PyPath,'.\\seccond_part\SignToSignLanguage.py'])
    #root.deiconify()  # Відновити головне вікно після завершення виконання всіх файлів
def button4_click():
    info=tk.Tk()
    info.title("Інструкція")
    info.geometry("900x600")
    label1= tk.Label(info,text="Інструкції")
    fontExample = tkFont.Font(family="Arial", size=16, weight="bold", slant="italic")
    label1.configure(font=fontExample)
    label1.pack(pady=5)
    
    label2= tk.Label(info,text="Інструкція для використання 'Переклад мови жестів у текст.")
    fontExample = tkFont.Font(family="Arial", size=16, weight="bold", slant="italic")
    label2.configure(font=fontExample)
    label2.place(x=20,y=40)
    
    label3= tk.Label(info,justify=LEFT,text="Для використання цього додатку потрібна відеокамера. Програма виконує розпізнавання букви яку ви показуєте мовою жестів.\nПрограма розпізнає букви англійскої мови жестів, тому речення потрібно формувати з букв англійського алфавіту. \nДля того щоб додати букву у речення натисніть Enter, щоб додати пропуск у речення натисність Space, \nщоб стерти останній символ, натисніть BackSpace, Esc для виходу")
    label3.place(x=20,y=75)
    
    label4= tk.Label(info,text="Інструкція для частини навчання нового користувача")
    fontExample = tkFont.Font(family="Arial", size=16, weight="bold", slant="italic")
    label4.configure(font=fontExample)
    label4.place(x=20,y=150)
    
    label5= tk.Label(info,justify=LEFT,text="Після натискання на кнопку 'Новий користувач' відкриється вікно з вашим зображення, на екрані буде написано\n яку кнопку на клавіатурі потрібно натиснути щоб почати навчання. Після натискання кнопку вам буде дано декілька секунд\n на те щоб показати букву мовою жестів. Після початку зчитування, напис на екрані камери зникне, це означатиме що запис почався,\n коли напис зявиться знову це означатиме що запис букви завершено, цю операції потібно зробити для кожної букви алфавіту,\n в алфавітному порядку, додатково разом з програмою відкриється зображення з алфавітом. \nЗВЕРНІТЬ УВАГУ!\n Для кожної букви потрібно що разу натискати на вказану кнопку. Якщо ви помилитесь на якомусь етапі, \nпотрібно буде починати спочатку, тому приготуйтесь перед натисканням на кнопку, щоб ваша рука уже була на екрані при натисканні кнопки. \nПісля завершення считування всіх букв, вікно з камерою закриється,\n потібно зачекати декілька хвилини, поки не зявиться напис 'Створення моделі завершено!'. Для дострокового завершення декілька разів натисніть ESC")
    label5.place(x=20,y=180) 
    
    label6= tk.Label(info,text="Інструкція для використання 'Переклад тексту у мову жестів")
    fontExample = tkFont.Font(family="Arial", size=16, weight="bold", slant="italic")
    label6.configure(font=fontExample)
    label6.place(x=20,y=340)
    
    label7= tk.Label(info,justify=LEFT,text="Після натискання кнопки відкриється меню програми,кнопка Показати відео покаже останнє змонтоване програмою відео, \nв полі тексту потрібно написати текст який ви хочете перекласти на мову жестів, ТЕКСТ МАЄ БУТИ АНГЛІЙСЬКОЮ МОВОЮ, \nПісля чого натиснути кнопку згенерувати відео, почнеться процес під час якого програма буде перевіряти чи є в неї в базі таке слово, \nякшо всі слова вона уже має, \nто вона змонтує відео і покаже його вам, після чого воно буде збережно у папку з програмою, якщо ж у програмі немає потрібного слова, \nпрограма відкриє вам сайт на тому слові якого немає у базі, на сторонці буде відео, Вам потрібного його завантажити, \nнаписнувши правою кнопкою миші по відео->Save as та вибрати загрузки, \nна це все вам буде дано 20 секунд, решту зробить програма")
    label7.place(x=20,y=370)   
    
root = tk.Tk()
root.title("Сурдоперекладач")
root.geometry("900x500")
label1= tk.Label(root,text="Програма перекладу мови жесті на англійську та навпаки.")
fontExample = tkFont.Font(family="Arial", size=16, weight="bold", slant="italic")
label1.place(x=150,y=15)

label1.configure(font=fontExample)

button1 = tk.Button(root, text="Переклад мови жестів у текст", command=button1_click, height=5, width=28, bg='#567', fg='White', justify=CENTER)
button1.place(x=50,y=80)

button2 = tk.Button(root, text="Новий користувач", command=button2_click,height=5, width=28, bg='#567', fg='White',justify=CENTER)
button2.place(x=50,y=180)

button3 = tk.Button(root, text="Переклад тексту на мову жестів", command=button3_click,height=5, width=28, bg='#567', fg='White', justify=CENTER)
button3.place(x=50,y=280)

button4 = tk.Button(root, text="Інструкція \nпо використанню", command=button4_click,height=4, width=20, bg='#567', fg='White', justify=CENTER)
button4.place(x=690,y=400)
root.mainloop()
