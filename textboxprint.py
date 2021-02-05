from tkinter import *
#from tkinter.ttk import 
from tkinter import messagebox 
import os

os.chdir("D:\\QP\\python\\practice")

root=Tk() 
root.title("Add Item")

canvas1 = Canvas(root, width = 800, height = 400) 
canvas1['bg']= "light green"
root.resizable(0,0)
canvas1.pack()

txtinp={"product":"","category":"","variant":"","units":"","priceOfUnit":""}
global product,category,variant,units,priceOfUnit

def take_input():
    product = txtinp["product"].get("1.0", "end-1c")
    category=txtinp["category"].get("1.0", "end-1c")
    variant=txtinp["variant"].get("1.0", "end-1c")
    units=txtinp["units"].get("1.0", "end-1c")
    priceOfUnit=txtinp["priceOfUnit"].get("1.0", "end-1c") 
    if len(product)<3 or len(product)>20 or not product.isalnum():
        print("Product name should be within 3 to 20 chars and must not contain special chars")
    elif len(category)<3 or len(category)>10 or not category.isalpha():
        print("Category name should be within 3 to 10 chars and must be alpha")
    elif len(variant)<3 or len(variant)>5 or not variant.isalnum():
        print("Variant name should be within 3 to 5 chars and must not contain special chars ")
    elif len(units)<3 or len(units)>10 or not units.isalnum():
        print("Units should be within 3 to 10 chars and  must not contain special chars")
    elif len(priceOfUnit)<0 or len(priceOfUnit)>7 or not priceOfUnit.isdigit():
        print("Price should be within 1 to 7 chars and must be digit")
    else:
        prod_ID = (product[0:5]+"_"+category[0:4]+"_"+variant+"_"+units).upper()
        print(prod_ID)
        print(priceOfUnit)
        full_details=product+"\n"+category+"\n"+variant+"\n"+units+"\n"+priceOfUnit+"\n"+prod_ID+"\n"+"\n"
        create_stock_file(full_details)
        quit()

def quit():
    root.destroy()

#create stock file
def create_stock_file(full_details):
    stock_file=open('stock.txt',"a")
    stock_file.write(full_details)
    stock_file.close()

btn1 = Button (root, text='Submit',command=take_input, height =1, width = 12,font = "Verdana 12 bold")
canvas1.create_window(300, 300, window=btn1)

btn2 = Button (root, text='Cancel',command=quit, height =1, width = 12,font = "Verdana 12 bold")
canvas1.create_window(500, 300, window=btn2)



txtinp["product"] = Text(root, height = 2,width = 20,bg = "white",font="Arial 10 bold")
canvas1.create_window(450,50, window=txtinp["product"])

txtinp["category"]= Text(root, height = 2,width = 20,bg = "white",font="Arial 10 bold")
canvas1.create_window(450,100, window=txtinp["category"])

txtinp["variant"]= Text(root, height = 2,width = 20,bg = "white",font="Arial 10 bold")
canvas1.create_window(450,150, window=txtinp["variant"])

txtinp["units"]= Text(root, height = 2,width = 20,bg = "white",font="Arial 10 bold")
canvas1.create_window(450,200, window=txtinp["units"])

txtinp["priceOfUnit"]= Text(root, height = 2,width = 20,bg = "white",font="Arial 10 bold")
canvas1.create_window(450,250, window=txtinp["priceOfUnit"])

#Labels
canvas1.create_text(300,50,text="Product :",font = "Verdana 14 bold")
canvas1.create_text(300,100,text="Category :",font = "Verdana 14 bold")
canvas1.create_text(300,150,text="Variant :",font = "Verdana 14 bold")
canvas1.create_text(300,200,text="Units :",font = "Verdana 14 bold")
canvas1.create_text(300,250,text="Price : ",font = "Verdana 14 bold")




root.mainloop()
