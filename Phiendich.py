#%% 
from tkinter import *
anh = {'cat':'meo', 
       'dog':'cho', 
       'leaf':'chiec la',
       'fish':'ca',
       'bird':'chim'}

viet = {'meo':'cat', 
       'cho':'dog', 
       'chiec la':'leaf',
       'ca':'fish',
       'chim':'bird'}

def phiendich():
    global X
    x = input.get()
    output.delete(0,END)
    if var.get() == 1:
        for y in anh:
            if x == y:
                z = anh.get(y)
                output.insert(0, z)
    elif var.get() == 2:
        for y in viet:
            if x == y:
                z = viet.get(y)
                output.insert(0, z)


rt = Tk()

rt.title('Trinh phien dich')
rt.geometry('800x600')

var = IntVar()

l1 = Label(text=(''), font=('Verdana', 15))
l2 = Label(text=(''), font=('Verdana', 15))
l3 = Label(text=('->'), font=('Verdana', 15))

input = Entry(font=('Verdana', 15), width=10)
output = Entry(font=('Verdana', 15), width=10)

anhviet = Radiobutton(text=('Anh - Viet'), font=('Verdana',10), variable=var, value=1, 
                      command=lambda: (l1.config(text=('Tieng Anh'), font=('Verdana', 15)), 
                                       (l2.config(text=('Tieng Viet'), font=('Verdana', 15)))))
vietanh = Radiobutton(text=('Viet - Anh'), font=('Verdana',10), variable=var, value=2, 
                      command=lambda: (l1.config(text=('Tieng Viet'), font=('Verdana', 15)), 
                                       (l2.config(text=('Tieng Anh'), font=('Verdana', 15)))))

dich = Button(text=('Dich'), font=('Verdana', 15), width=10, bg='light green', command=phiendich)

anhviet.grid(column=1, row=0)
vietanh.grid(column=1, row=1)

l1.grid(column=1, row=2)
l2.grid(column=3, row=2)
l3.grid(column=2, row=3)

input.grid(column=1, row=3)
output.grid(column=3, row=3)

dich.grid(column=2, row=4)

mainloop()
# %%
