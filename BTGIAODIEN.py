#%% Bai 1
from tkinter import *
def calculate():
    try:
        sotien = int(input.get())
        sotien = sotien*cost.get()
        value.configure(text = 'GIÁ TRỊ QUY ĐỔI: {:.0f} VNĐ'.format(sotien))
        #input.delete(0,END)
        if cost.get() == 22000:
            donvi.configure(text= 'USD', font=('Verdana', 12))
        elif cost.get() == 26000:
            donvi.configure(text= 'EUR', font=('Verdana', 12))
        elif cost.get() == 200:
            donvi.configure(text= 'JYP', font=('Verdana', 12))

    except:
        value.configure(text = 'MỜI NHẬP GIÁ TRỊ NGOẠI TỆ',font=('Verdana', 15))

    
rt = Tk()

rt.title('MONEY EXCHANGE')
rt.geometry('800x600')

cost = IntVar()
usdbutton = Radiobutton(text='USD: 22 000', font= ('Verdana', 12),variable=cost, value=22000)
eurbutton = Radiobutton(text='EUR: 26 000', font= ('Verdana', 12),variable=cost, value=26000)
jypbutton = Radiobutton(text='JYP:    200', font= ('Verdana', 12),variable=cost, value=200)

input = Entry(font=('Verdana', 12), width=10)
exbutton = Button(text='EXCHANGE', font=('Verdana', 12), command=calculate)

value = Label(text=('GIÁ TRỊ QUY ĐỔI:   VNĐ'), font=('Verdana', 15))
donvi = Label(text=('USD/EUR/JYP'),font=('Verdana', 12))


usdbutton.grid(column=1, row=1)
eurbutton.grid(column=1, row=3)
jypbutton.grid(column=1, row=5)
input.grid(column=3,row=1)
exbutton.grid(column=3, row=3)
value.grid(column=1, row=6, columnspan = 3)
donvi.grid(column=4,row=1)

mainloop()
# %% Bai 2
from Tkinter import *
def bt():
    global bmi
    chieucao = float(input1.get())
    cannang = float(input2.get())
    #print(chieucao)
    if var.get() == 1:
        bmi = cannang/((chieucao*0.01)**2)
        l3.configure(text='BMI= {:.5f}'.format(bmi),font=('Verdana', 12),fg=('green'))
        
    elif var.get() == 2:
        bmi = cannang/(chieucao**2)*703
        l3.configure(text='BMI= {:.0f}'.format(bmi),font=('Verdana', 12),fg=('green'))

rt = Tk()

rt.title('BMI CALCULATOR')
rt.geometry('800x600')

var = IntVar()

l1 = Label(font=('Verdana', 12))
l2 = Label(font=('Verdana', 12))
l3 = Label(text='BMI=',font=('Verdana', 12),fg=('green'))
l4 = Label(font=('Verdana', 12))
l5 = Label(font=('Verdana', 12))

input1 = Entry(font=('Verdana', 15), width=10)
input2 = Entry(font=('Verdana', 15), width=10)

metricbutton = Radiobutton(text='Metric', font= ('Verdana', 12),variable=var, value=1,
                           command=lambda: (l1.config(text="CHIỀU CAO (cm)"),
                                                      l2.config(text="CÂN NẶNG (kg)")))
englishbutton = Radiobutton(text='English', font= ('Verdana', 12),variable=var, value=2,
                            command=lambda: (l1.config(text="HEIGHT (Inches)"),
                                                       l2.config(text="WEIGHT (Pounds)")))

calbutton = Button(text=('CALCULATE'), font= ('Verdana', 12), width=15, command=bt)

l1.grid(column=1,row=1,columnspan=1)
l2.grid(column=1,row=3,columnspan=1)
l3.grid(column=2,row=8)
l4.grid(column=2,row=5)
l5.grid(column=2,row=7)
input1.grid(column=1,row=2,columnspan=1)
input2.grid(column=1,row=4,columnspan=1)
metricbutton.grid(column=3, row=2, columnspan=2)
englishbutton.grid(column=3,row=3, columnspan=3)
calbutton.grid(column=2, row=6)

mainloop()

# %%
