'''
    This script was written in python 3.x.
    In order to run this script, please make sure your python version is 3.x or above.
    How to run:
        python Protos.py
    or if it doesn't work use this one:
        python3 Protos.py
    Author: Pedja <pedja.terzic@hotmail.com>
'''

from tkinter import *
import tkinter.messagebox
from tkinter.ttk import Frame, Label, Entry , Button , Style

class Protos(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.parent = parent
        self.initUI()

    def initUI(self):
        self.parent.title("Protos")
        self.pack(fill=BOTH, expand=True)
        global value
        value = 0
        global num
        num = StringVar()
        global res
        res = StringVar()

        frame1 = Frame(self,style='My.TFrame')
        frame1.pack(fill=X)

        lbl1 = Label(frame1, text="Enter the ordinal number n :", width=22,background='orange')
        lbl1.pack(side=LEFT, padx=5, pady=5)

        entry1 = Entry(frame1,textvariable=num,style='My.TEntry')
        entry1.pack(fill=X, padx=5, expand=True)

        
        frame2 = Frame(self,style='My.TFrame')
        frame2.pack(fill=X)

        lbl2 = Label(frame2, text="The nth prime number is :", width=22,background='orange')
        lbl2.pack(side=LEFT, padx=5, pady=5)

        result = Entry(frame2,textvariable=res,style='My.TEntry',state='readonly')
        result.pack(fill=X, padx=5, expand=True)

		
        frame3 = Frame(self,style='My.TFrame')
        frame3.pack(fill=X)

        btnnthprime = Button(frame3, text="Calculate", width=10, command=self.nthprime,style='My.TButton')
        btnnthprime.pack(side=LEFT, anchor=N, padx=5, pady=5)
		
        btnclear = Button(frame3, text="Clear", width=10, command=self.clear,style='My.TButton')
        btnclear.pack(side=LEFT, anchor=N, padx=5, pady=5)
		
        btnclose = Button(frame3, text="Close", width=10, command=self.quit,style='My.TButton')
        btnclose.pack(side=LEFT, anchor=N, padx=5, pady=5)

    def errorMsg(self,msg):
        if msg == 'error':
            tkinter.messagebox.showerror('Error!', 'Something went wrong! Maybe invalid entries')
        
    

    def nthprime(self):
        try:
            n = int(num.get())
            if n<1:
                self.errorMsg('error')
            else:
                def lcm(p,q):
	                p, q = abs(p), abs(q)
	                m = p * q
	                if not m: return 0
	                while True:
		                p %= q
		                if not p: return m // q
		                q %= p
		                if not q: return m // p
                b1=6
                b2=6
                b3=6
                if int(n)==1: 
                    value=2 
                else: 
                    value=3
                k=4
                m=3
                while m<=n:
                    b4=b1+lcm(k-2,b1)
                    a=b4/b1-1 
                    k=k+1
                    b1=b2 
                    b2=b3
                    b3=b4
                    if value<a:
                        value=a
                        m=m+1
                res.set(self.makeAsItIs(value))
        except:
            self.errorMsg('error')
			
    def clear(self):
        try:
            res.set('')
            num.set('')
        except:
            self.errorMsg('error')
			
    
    def makeAsItIs(self, value):
        if (value == int(value)):
            value = int(value)
        return value

def main():
    root = Tk()
    root.resizable(0,0)
    s = Style()
    s.configure('My.TFrame', background='orange')
    s.configure('My.TButton', background='light gray')
    s.configure('My.TEntry', fieldbackground='light gray')
    root.geometry("300x85")
    protos = Protos(root)
    root.mainloop()

if __name__ == '__main__':
    main()
