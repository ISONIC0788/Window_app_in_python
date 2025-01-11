import  tkinter as tk
import  tkinter.ttk as ttk

class App:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("My frist App")
        tk.Label(self.root , text = " Hy user this my frist App in thinker GUi " , font= "Arial 15").pack() # grid() or pack are the same
        ttk.Label(self.root , text = " My name is Ituze Agacy Ebedi melecki " , font= "consolas ").pack()

        tk.Button (self.root , text="This tk button clic here ").pack()
        ttk.Button (self.root , text= "this ttk button click here " ).pack()



    def run (self):
        self.root.mainloop()
App().run()

