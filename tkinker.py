import tkinter as tk
import  tkinter.ttk as ttk
#with out oop
# root = tk.Tk()
# root.title("hy my frist app")
# label = tk.Label (root , text= " hy brother it good to program and write code  ", font ="Arial 15").pack()
# root.mainloop()
class App:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("My Frist App")
        self.label =tk.Label(self.root , text ="Hy . user my name  Ituze agacyo ebedi meleck" , font = "consolas 23").pack()
        self.button = tk.Button(self.root , text ="click here "  ).pack()
        self.label2 = ttk.Label(self.root , text = "here is label of python ttk " , font="Consolas ").pack()
        self.button2 = ttk.Button(self.root , text = "click on button" ).pack()
    def run(self):
        self.root.mainloop()
App().run()

