from tkinter import*
from tkinter import messagebox
root = Tk()

#root configuration 
root.configure(bg="#82edba")
root.title("Simple payment XA")
root.geometry("600x600")
root.iconbitmap("D:\Izu\python icon sets\SPL.ico")

#labels
labely = Label(root, text="Simple payment", bg="#82edba", font=("Comfortaa", "40"))
labely.pack()
Label(root,text="XA edition version 1.0", bg="#82edba", font=("Comfortaa", "22")).pack()

#fnx
def submit_payment_action():
    messagebox.showinfo("Payment", "Your payment has been submitd")

#Transfer
def Transfer_command():
    Window = Toplevel()
    Window.title("Simple payment XA - Transfer")
    Window.configure(bg='#82edba')
    Window.geometry("500x500")
    Window.iconbitmap("D:\Izu\python icon sets\SPL.ico")
    
    global tox
    global From
    global Amount
    global OTP_Method
    global OTP
    global Resend_OTP
    
    Label(Window, text="Transfer", bg="#82edba", font="Comfortaa 24 bold underline").pack() #Name
    Label(Window, text="To:", bg="#82edba", font="Comfortaa 15").pack() # to:
    tox = Entry(Window, bg="#82edba", font="calibri 14").pack() #input for to:
    Label(Window, text="From:", bg="#82edba", font="Comfortaa 15").pack() # From:
    From = Entry(Window, bg="#82edba", font="calibri 14").pack() #input for from
    Label(Window, text="Amount:", bg="#82edba", font="Comfortaa 15").pack() # Amount:
    Amount = Entry(Window, bg="#82edba", font="calibri 14").pack()  # input for ammount
    Label(Window, text="OTP Method:", bg="#82edba", font="Comfopairtaa 15").pack()  #Input OTP
    OTP_Method = Entry(Window, bg="#82edba", font=("calibri 14")).pack()  # input for SendOTP
    Label(Window, text="OTP:", bg="#82edba", font="Comfopairtaa 15").pack()  #OTP
    OTP = Entry(Window, bg="#82edba", font=("calibri 14")).pack()  # input for OTP
    Label(Window, text="Resend OTP:", bg="#82edba", font="Comfopairtaa 15").pack()  #OTP
    Resend_OTP = Entry(Window, bg="#82edba", font=("calibri 14")).pack()  # input for resent OTP
    submit_payment_btn= Button(Window, text="Submit payment", font=("Comfortaa", "17"), command=submit_payment_action)
    submit_payment_btn.pack(pady=20)

#buttons
Make_transfer_button = Button(root, text="Make a transfer", font=("Comfortaa", "17"), command=Transfer_command)
Make_transfer_button.pack(pady=10)
Make_transfer_button.configure(background="#b9fac9")

end= Button(root, text="Quit program",  font=("Comfortaa", "17"), command=root.destroy)
end.pack(pady=10)
end.configure(background="#b9fac9")

root.mainloop()
