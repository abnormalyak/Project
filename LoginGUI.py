import tkinter as tk

class LoginSystem(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        
        self.geometry("400x400")
        self.title("Login")
        
        self.ulabel = tk.Label(self, text="Username").place(x=20, y=20)
        self.uinput = tk.Entry(self)
        self.uinput.place(x=20, y=40)

        self.plabel = tk.Label(self, text="Password").place(x=20, y=70)
        self.pinput = tk.Entry(self)
        self.pinput.place(x=20, y=90)
        
        self.login = tk.Button(self, text = "Login", command = self.login_clicked).place(x=20, y=120)

    def login_clicked(self):
        ucontent = self.uinput.get()
        pcontent = self.pinput.get()
        ufile = open('%s\%s_details.txt' % (ucontent, ucontent), 'r+')
        for line in ufile.readlines():
            check = line.split()
            if ucontent == check[0] and pcontent == check[1]:
                print("Login successful. \n Welcome back, %s!" % (ucontent))
            else:
                print("Login failed")
                
window = LoginSystem()
window.mainloop()
