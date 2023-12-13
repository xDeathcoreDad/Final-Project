#Importing the packages

import tkinter as tk

from tkinter import *

from tkinter import messagebox

#Creating the root window

root = tk.Tk()

root.minsize(700, 500)

#Main window

root.title("Pizza and Subs")

#Displaying a menu for pizza using a label

tk.Label(root, text="Pizza: Supreme, Meat Lovers, Chicken Bacon Ranch, Buffalo", font=("Arial", 15)).place(x=50, y=200)

#Displaying a menu for subs using a label

tk.Label(root, text="Subs: Pizza, Ham & Cheese, Steak, Chicken Bacon Ranch", font=("Arial", 15)).place(x=50, y=230)

tk.Label(root, text="Enter pizza names (using comma)", font=("Arial", 15)).place(x=50, y=280)

#Entry box with font and size

t1 = tk.Entry(root, font=("Arial", 15))

t1.place(x=380, y=280)

tk.Label(root, text="Enter sub names (using comma)", font=("Arial", 15)).place(x=50, y=310)

t2 = tk.Entry(root, font=("Arial", 15))

t2.place(x=380, y=310)

#Function to calculate price of pizza and subs seperately

def calc():
    s1 = t1.get()
    s2 = t2.get()
    pizza = s1.split(sep=', ')
    subs = s2.split(sep=', ')
    len1 = len(pizza)
    len2 = len(subs)
    priceofPizza = len1 * 20.00
    priceofSubs = len2 * 8.99
    s = 'Price of pizza: {} \nPrice of subs: {}'.format(priceofPizza, priceofSubs)
    messagebox.showinfo('Price of Pizza and Subs', s)
    return priceofPizza, priceofSubs, pizza, subs

#Function to calculate price of pizza and subs altogether

def total():
    pr_pizza, pr_subs, pizza, subs = calc()
    total_price = pr_pizza + pr_subs
    s = 'Total price: {:5.2f}'.format(total_price)
    child_w = Toplevel(root)
    child_w.geometry("350x350")
    child_w.title("Total Price")
    label_child = Label(child_w, text=s, font=('Helvetica', 15))
    label_child.place(x=20, y=50)

    s2 = '\n'.join(pizza) + "\n" + ' '.join(subs)
    Label(child_w, text=s2, font=('Helvetica', 15)).place(x=20, y=150)

#Creating label widgets

    label_child= Label(child_w, text= s, font=('Helvetica 15'))

    label_child.place(x=20,y=50) #positioning the label

    l2= Label(child_w, text="You have ordered", font=('Helvetica 15'))

    l2.place(x=20,y=100) #positioning the label

    s2=' '.join(pizza)+" "+' '.join(subs)

    l3= Label(child_w, text=s2, font=('Helvetica 15'))

    l3.place(x=20,y=150) #positioning the label

#Creating the buttons which calculate the totals of each as well as altogether

b1 = tk.Button(root, text="Calculate price of pizza and subs", command=calc, font=("Arial", 15))

b1.place(x=100, y=380)

b2 = tk.Button(root, text="Calculate total price", command=total, font=("Arial", 15))

b2.place(x=100, y=420)

#Creating the button that exits from the program

b3 = tk.Button(root, text="Exit", command=root.destroy, font=("Arial", 15))

b3.place(x=100,y=460)

#Starting the main menu

root.mainloop()