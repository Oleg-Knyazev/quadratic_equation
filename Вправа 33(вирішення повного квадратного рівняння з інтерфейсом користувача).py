from tkinter import *
from tkinter import messagebox as mb
from math import *

root = Tk()
root.title('Квадратне рівняння')
root.geometry('230x100')

labA = Label(root, width=1, text='A', font='Arial 16')
labA.grid(row=0, column=0, padx=10)

labB = Label(root, width=1, text='B', font='Arial 16')
labB.grid(row=0, column=1, padx=10)

labC = Label(root, width=1, text='C', font='Arial 16')
labC.grid(row=0, column=2, padx=10)

enA = Entry(root, width=5, font='Arial 14')
enA.grid(row=1, column=0, padx=10)

enB = Entry(root, width=5, font='Arial 14')
enB.grid(row=1, column=1, padx=10)

enC = Entry(root, width=5, font='Arial 14')
enC.grid(row=1, column=2, padx=10)

def btn_click():
    if enA.get() == '' or enB.get() == '' or enC.get() == '':
        mb.showinfo('Помилка', 'Заповніть всі поля!')
    else:
        a, b, c = map(float, [enA.get(), enB.get(), enC.get()])

        D = (b ** 2) - (4 * a * c)

        if D < 0:
            mb.showinfo('Коренів немає', 'Оскільки дискримінант від’ємний')
        elif D == 0:
            x = -b / (2 * a)
            mb.showinfo('Один корінь', 'x = ' + str(x))
        else:
            x1 = (-b + sqrt(D)) / (2 * a)
            x2 = (-b - sqrt(D)) / (2 * a)

            mb.showinfo(
                'Два корені',
                'Перший корінь = ' + str(x1) +
                '\nДругий корінь = ' + str(x2)
            )

btn1 = Button(
    root,
    text='Знайти корені',
    width=13,
    font='Arial 14',
    command=btn_click
)
btn1.grid(row=2, column=0, columnspan=3)

root.mainloop()
