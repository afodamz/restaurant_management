from tkinter import*
import random
import time;

#================Frame and Name of Project=======================
root = Tk()
root.geometry("1600x800+0+0")
root.title("restaurant management system")

#=====================INTERNAL FRAME DESIGN==================================
text_Input = StringVar()
operator = ""

Tops = Frame(root, width=1600, height=50, bg="powder blue", relief=SUNKEN)
Tops.pack(side=TOP)

f1 = Frame(root, width=800, height=700, relief=SUNKEN)
f1.pack(side=LEFT)

f2 = Frame(root, width=300, height=700, relief=SUNKEN)
f2.pack(side=RIGHT)

#==================TIME AND DATE FUNCTION===============================
localtime = time.asctime(time.localtime(time.time()))

#==================INFO===============================
lblinfo = Label(Tops, font=('arial', 50, 'bold'), text="Restuarant Management Systems", fg="Steel Blue",
                bd=10, anchor='w')
lblinfo.grid(row=0, column=0)
lblDateTime = Label(Tops, font=('arial', 20, 'bold'), text=localtime, fg="Steel Blue", bd=10, anchor='w')
lblDateTime.grid(row=1, column=0)

#==================================================CALCULATOR=============================================
def btnClick(numbers):
    global operator
    operator = operator + str(numbers)
    text_Input.set(operator)

def btnclearDisplay():
    global operator
    operator = ""
    text_Input.set("")


def btnEqualsInput():
    global operator
    sumup = str(eval(operator))
    text_Input.set(sumup)
    operator = ""

def Ref():
    x = random.randint(10908, 500876)
    randomRef = str(x)
    rand.set(randomRef)   #THIS IS FOR THE RECEIPT NUMBER

    CoF = float(Fries.get())
    CoD = float(Drinks.get())
    CoFilet = float(Filet.get())
    CoBurger = float(Burger.get())
    CoChickenBurger = float(Chicken_Burger.get())
    CoCheese_Burger = float(Cheese_Burger.get())

    CostofFries = CoF * 0.99
    CostofDrinks = CoD * 1
    CostofFilet = CoFilet * 2.99
    CostofBurger= CoBurger * 2.87
    CostofChicken_Burger = CoChickenBurger * 2.89
    CostofCheese_Burger = CoCheese_Burger * 2.69

    CostofMeal = "$", str('%.2f' % (CostofFries + CostofDrinks + CostofFilet + CostofBurger
                                    + CostofChicken_Burger + CostofCheese_Burger))

    PayTax = ((CostofFries + CostofDrinks + CostofFilet + CostofBurger
                                    + CostofChicken_Burger + CostofCheese_Burger) * 0.2)

    TotalCost = (CostofFries + CostofDrinks + CostofFilet + CostofBurger
                                    + CostofChicken_Burger + CostofCheese_Burger)


    Ser_Charge = ((CostofFries + CostofDrinks + CostofFilet + CostofBurger
                                    + CostofChicken_Burger + CostofCheese_Burger) / 99)

    Service = "$", str('%.2f' % Ser_Charge)

    OverAllCost = "$", str('%.2f' % (PayTax + TotalCost + Ser_Charge))
    PaidTax =  "$", str('%.2f' % PayTax)

    Services_Charge.set(Service)
    Cost.set(CostofMeal)
    Tax.set(PaidTax)
    SubTotal.set(CostofMeal)
    Total.set(OverAllCost)


def qExit():
    root.destroy()

def Reset():
    rand.set("")
    Fries.set("")
    Burger.set("")
    Filet.set("")
    SubTotal.set("")
    Total.set("")
    Services_Charge.set("")
    Drinks.set("")
    Tax.set("")
    Cost.set("")
    Chicken_Burger.set("")
    Cheese_Burger.set("")


txtDisplay = Entry(f2, font=('arial', 20, 'bold'), textvariable=text_Input, bd=30, insertwidth=4,
                   bg="powder blue", justify='right')
txtDisplay.grid(columnspan=4)

btn7=Button(f2, padx=16, pady=16, bd=8, fg='black', font=('arial', 20, 'bold'),
            text='7', bg='powder blue', command=lambda: btnClick(7)).grid(row=2,column=0)
btn8=Button(f2, padx=16, pady=16, bd=8, fg='black', font=('arial', 20, 'bold'),
            text='8', bg='powder blue', command=lambda: btnClick(8)).grid(row=2,column=1)
btn9=Button(f2, padx=16, pady=16, bd=8, fg='black', font=('arial', 20, 'bold'),
            text='9', bg='powder blue', command=lambda: btnClick(9)).grid(row=2,column=2)
addition=Button(f2, padx=16, pady=16, bd=8, fg='black', font=('arial', 20, 'bold'),
            text='+', bg='powder blue', command=lambda: btnClick('+')).grid(row=2,column=3)

#============================================================================================
btn4=Button(f2, padx=16, pady=16, bd=8, fg='black', font=('arial', 20, 'bold'),
            text='4', bg='powder blue', command=lambda: btnClick(4)).grid(row=3,column=0)
btn5=Button(f2, padx=16, pady=16, bd=8, fg='black', font=('arial', 20, 'bold'),
            text='8', bg='powder blue', command=lambda: btnClick(5)).grid(row=3,column=1)
btn6=Button(f2, padx=16, pady=16, bd=8, fg='black', font=('arial', 20, 'bold'),
            text='9', bg='powder blue', command=lambda: btnClick(6)).grid(row=3,column=2)
subtraction=Button(f2, padx=16, pady=16, bd=8, fg='black', font=('arial', 20, 'bold'),
            text='-', bg='powder blue', command=lambda: btnClick('-')).grid(row=3,column=3)

#===========================================================================================
btn3=Button(f2, padx=16, pady=16, bd=8, fg='black', font=('arial', 20, 'bold'),
            text='3', bg='powder blue', command=lambda: btnClick(3)).grid(row=4,column=0)
btn2=Button(f2, padx=16, pady=16, bd=8, fg='black', font=('arial', 20, 'bold'),
            text='2', bg='powder blue', command=lambda: btnClick(2)).grid(row=4,column=1)
btn1=Button(f2, padx=16, pady=16, bd=8, fg='black', font=('arial', 20, 'bold'),
            text='1', bg='powder blue', command=lambda: btnClick(1)).grid(row=4,column=2)
multiplication=Button(f2, padx=16, pady=16, bd=8, fg='black', font=('arial', 20, 'bold'),
            text='*', bg='powder blue', command=lambda: btnClick('*')).grid(row=4,column=3)

#===========================================================================================
btn0=Button(f2, padx=16, pady=16, bd=8, fg='black', font=('arial', 20, 'bold'),
            text='0', bg='powder blue', command=lambda: btnClick('0')).grid(row=5,column=0)
btnclear=Button(f2, padx=16, pady=16, bd=8, fg='black', font=('arial', 20, 'bold'),
            text='C', bg='powder blue', command=btnclearDisplay).grid(row=5,column=1)
btnEquals=Button(f2, padx=16, pady=16, bd=8, fg='black', font=('arial', 20, 'bold'),
            text='=', bg='powder blue', command=btnEqualsInput).grid(row=5,column=2)
Division=Button(f2, padx=16, pady=16, bd=8, fg='black', font=('arial', 20, 'bold'),
            text='/', bg='powder blue', command=lambda: btnClick('/')).grid(row=5,column=3)

#=====================================Restaurant Info 1======================================================
rand = StringVar()
Fries = StringVar()
Burger = StringVar()
Filet = StringVar()
SubTotal = StringVar()
Total = StringVar()
Services_Charge = StringVar()
Drinks = StringVar()
Tax = StringVar()
Cost = StringVar()
Chicken_Burger = StringVar()
Cheese_Burger = StringVar()


lblReference = Label(f1, font=('arial', 16, 'bold'), text="Reference", bd=16, anchor='w',)
lblReference.grid(row=0, column=0)
txtReference = Entry(f1, font=('arial', 16, 'bold'), textvariable=rand, bd=10,insertwidth=4,
                     bg="powder blue", justify = "right")
txtReference.grid(row=0, column=1)


lblFries= Label(f1, font=('arial', 16, 'bold'), text="Large Fries", bd=16, anchor='w',)
lblFries.grid(row=1, column=0)
txtFries = Entry(f1, font=('arial', 16, 'bold'), textvariable=Fries, bd=10,insertwidth=4,
                     bg="powder blue", justify = "right")
txtFries.grid(row=1, column=1)


lblBurger= Label(f1, font=('arial', 16, 'bold'), text="Burger_Meal", bd=16, anchor='w',)
lblBurger.grid(row=2, column=0)
txtBurger = Entry(f1, font=('arial', 16, 'bold'), textvariable=Burger, bd=10,insertwidth=4,
                     bg="powder blue", justify = "right")
txtBurger.grid(row=2, column=1)


lblFilet= Label(f1, font=('arial', 16, 'bold'), text="Filet_o_Meal", bd=16, anchor='w',)
lblFilet.grid(row=3, column=0)
txtFilet = Entry(f1, font=('arial', 16, 'bold'), textvariable=Filet, bd=10,insertwidth=4,
                     bg="powder blue", justify = "right")
txtFilet.grid(row=3, column=1)


lblChicken= Label(f1, font=('arial', 16, 'bold'), text="Chicken Meal", bd=16, anchor='w',)
lblChicken.grid(row=4, column=0)
txtChicken = Entry(f1, font=('arial', 16, 'bold'), textvariable=Chicken_Burger, bd=10,insertwidth=4,
                     bg="powder blue", justify = "right")
txtChicken.grid(row=4, column=1)


lblBurger= Label(f1, font=('arial', 16, 'bold'), text="Burger", bd=16, anchor='w',)
lblBurger.grid(row=5, column=0)
txtBurger = Entry(f1, font=('arial', 16, 'bold'), textvariable=Cheese_Burger, bd=10,insertwidth=4,
                     bg="powder blue", justify = "right")
txtBurger.grid(row=5, column=1)

#=====================================restaurant Info 2==========================================

lblDrinks = Label(f1, font=('arial', 16, 'bold'), text="Drinks", bd=16, anchor='w',)
lblDrinks.grid(row=0, column=2)
txtDrinks = Entry(f1, font=('arial', 16, 'bold'), textvariable=Drinks, bd=10,insertwidth=4,
                     bg="#ffffff", justify = "right")
txtDrinks.grid(row=0, column=3)


lblCost = Label(f1, font=('arial', 16, 'bold'), text="Cost Of Meal", bd=16, anchor='w',)
lblCost.grid(row=1, column=2)
txtCost = Entry(f1, font=('arial', 16, 'bold'), textvariable=Cost, bd=10,insertwidth=4,
                     bg="#ffffff", justify = "right")
txtCost.grid(row=1, column=3)


lblService = Label(f1, font=('arial', 16, 'bold'), text="Service Charge", bd=16, anchor='w',)
lblService.grid(row=2, column=2)
txtService = Entry(f1, font=('arial', 16, 'bold'), textvariable=Services_Charge, bd=10,insertwidth=4,
                     bg="#ffffff", justify = "right")
txtService.grid(row=2, column=3)


lblStateTax = Label(f1, font=('arial', 16, 'bold'), text="State Tax", bd=16, anchor='w',)
lblStateTax.grid(row=3, column=2)
txtStateTax = Entry(f1, font=('arial', 16, 'bold'), textvariable=Tax, bd=10,insertwidth=4,
                     bg="#ffffff", justify = "right")
txtStateTax.grid(row=3, column=3)


lblSubTotal= Label(f1, font=('arial', 16, 'bold'), text="Sub Total", bd=16, anchor='w',)
lblSubTotal.grid(row=4, column=2)
txtSubTotal = Entry(f1, font=('arial', 16, 'bold'), textvariable=SubTotal, bd=10,insertwidth=4,
                     bg="#ffffff", justify = "right")
txtSubTotal.grid(row=4, column=3)


lblTotal= Label(f1, font=('arial', 16, 'bold'), text="Total", bd=16, anchor='w',)
lblTotal.grid(row=5, column=2)
txtTotal = Entry(f1, font=('arial', 16, 'bold'), textvariable=Total, bd=10,insertwidth=4,
                     bg="#ffffff", justify = "right")
txtTotal.grid(row=5, column=3)

#========================================Buttons======================================================

btnTotal = Button(f1, padx=16, pady=8, bd=16, fg="black", font=('arial', 16, 'bold'), width=10,
                  text="Total", bg="powder blue", command = Ref).grid(row=7, column=1)

btnReset = Button(f1, padx=16, pady=8, bd=16, fg="black", font=('arial', 16, 'bold'), width=10,
                  text="Reset", bg="powder blue", command = Reset).grid(row=7, column=2)

btnExit = Button(f1, padx=16, pady=8, bd=16, fg="black", font=('arial', 16, 'bold'), width=10,
                  text="Exit", bg="powder blue", command = qExit).grid(row=7, column=3)







root.mainloop()