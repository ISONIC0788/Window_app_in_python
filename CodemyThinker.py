from  tkinter import  *
root = Tk()
root.title("My Frist App")
input = Entry (root ,width= 70 )
input.pack()
input.insert(0,"Enter your name ...")
def myclick():
    label = Label(root , text= "Hellow my"+input.get())
    label.pack()

button = Button(root , text = "click me !!!" ,padx= 30, pady= 5 , command= myclick , fg= "white" ,bg= "green").pack()
root.mainloop()