#workspace allows users to get a hub to open files

#importing tkinter, messagebox, filedialog, tkcalander, time and OS
from tkinter import*
from tkinter import messagebox
from tkinter import filedialog
from tkcalendar import*
from tkinter import ttk
import tkinter as tk
import time
import os 

#Root congiguration
Root = Tk()
Root.title("Workspace for windows")
Root.configure(bg="Lightgreen")
Root.geometry("1325x600")
Root.iconbitmap("D:\Izu\python icon sets\icon_ws.ico")   

def commandrandom():
    Root.title("Workpsace for windows")
    my_menu = Menu(Root)
    Root.config(menu=my_menu)
    
    #Menubars
    my_menu = Menu(Root)
    Root.config(menu=my_menu)

    #filemenu
    file_menu = Menu(my_menu, tearoff=False)
    my_menu.add_cascade(label="Tools", menu=file_menu)
    file_menu.add_command(label="Search files", command=search_file)
    file_menu.add_command(label="Customize workpace", command=Settings_workspace)
    file_menu.add_command(label="Developer mode", command=developermode_command)
    file_menu.add_command(label="Show Calander", command=show_calander_command)
    file_menu.add_command(label="Hide Calander", command=hide_calander_command)
    file_menu.add_command(label="Exit program", command=Root.destroy)

    #textmenu
    text_menu = Menu(my_menu, tearoff=False)
    my_menu.add_cascade(label="Text editors", menu=text_menu)
    text_menu.add_command(label="Sublime text editor", command=launch_sublime_text_command)
    text_menu.add_command(label="Basic Text For Windows", command=launch_text_editor_command)
    text_menu.add_command(label="Basic Text 3.0", command=launch_basictext30_command)
    text_menu.add_command(label="Basic Text 2.0", command=launch_basictext20_command)
    text_menu.add_command(label="Basic Text 1.0", command=launch_basictext10_command)

    #paymeny menu
    paymeny_menu = Menu(my_menu, tearoff=False)
    my_menu.add_cascade(label="Simple payments", menu=paymeny_menu)
    paymeny_menu.add_command(label="Simple payment app", command=launch_simple_payments_app)
    paymeny_menu.add_command(label="Simple payment XA", command=launch_simple_payments_XA)

    #browsers
    browser_menu = Menu(my_menu, tearoff=False)
    my_menu.add_cascade(label="Browsers", menu=browser_menu)
    browser_menu.add_command(label="Microsoft edge", command=launch_edge_browser_command)
    browser_menu.add_command(label="Google chrome", command=launch_chrome_browser_command)

    #flashback
    fb_menu = Menu(my_menu, tearoff=False)
    my_menu.add_cascade(label="Flashback tools", menu=fb_menu)
    fb_menu.add_command(label="Flashback express recorder", command=launch_fbr_command)
    fb_menu.add_command(label="Flashback express player", command=launch_fbp_command)

    #all
    allapps_menu = Menu(my_menu, tearoff=False)
    my_menu.add_cascade(label="All apps", menu=allapps_menu)
    allapps_menu.add_command(label="Simple payment app", command=launch_simple_payments_app)
    allapps_menu.add_command(label="Simple payment XA", command=launch_simple_payments_XA)
    allapps_menu.add_separator()
    allapps_menu.add_command(label="Sublime text editor", command=launch_sublime_text_command)
    allapps_menu.add_command(label="Basic Text For Windows", command=launch_text_editor_command)
    allapps_menu.add_command(label="Basic Text 3.0", command=launch_basictext30_command)
    allapps_menu.add_command(label="Basic Text 2.0", command=launch_basictext20_command)
    allapps_menu.add_command(label="Basic Text 1.0", command=launch_basictext10_command)
    allapps_menu.add_separator()
    allapps_menu.add_command(label="Microsoft edge", command=launch_edge_browser_command)
    allapps_menu.add_command(label="Google chrome", command=launch_chrome_browser_command)

    #developer
    d_menu = Menu(my_menu, tearoff=False)
    my_menu.add_cascade(label="Modes", menu=d_menu)
    d_menu.add_command(label="Customize workpace", command=Settings_workspace)
    d_menu.add_command(label="Developer mode", command=developermode_command)

        #freeze program
    freeze_menu = Menu(my_menu, tearoff=False)
    my_menu.add_cascade(label="Lock workpsace", menu=freeze_menu)
    freeze_menu.add_command(label="05 sec", command=freez_5sec_command)
    freeze_menu.add_command(label="15 sec", command=freez_15sec_command)
    freeze_menu.add_command(label="30 sec", command=freez_30sec_command)
    freeze_menu.add_command(label="01 min", command=freez_60sec_command)
    freeze_menu.add_command(label="03 min", command=freez_3min_command)
    freeze_menu.add_command(label="05 min", command=freez_5min_command)

    #users
    users_menu = Menu(my_menu, tearoff=False)
    my_menu.add_cascade(label="Users", menu=users_menu)
    users_menu.add_command(label="Other user", command=other_workspae_command)

    #intepreter
    int_menu = Menu(my_menu, tearoff=False)
    my_menu.add_cascade(label="Help", menu=int_menu)
    int_menu.add_command(label="Help", command=show_help_command)
    int_menu.add_command(label="About", command=show_about_command)

def developermode_command():
    new_menu = Menu(Root)
    Root.config(menu=new_menu)
    Root.title("Developer mode - Workspace for windows")
    Root.geometry("1325x600")
    
    #filemenu
    file_menu = Menu(new_menu, tearoff=False)
    new_menu.add_cascade(label="Tools", menu=file_menu)
    file_menu.add_command(label="Setting mode", command=Settings_workspace)
    file_menu.add_command(label="Developer mode", command=developermode_command)
    file_menu.add_command(label="Show Calander", command=show_calander_command)
    file_menu.add_command(label="Hide Calander", command=hide_calander_command)
    file_menu.add_command(label="Exit program", command=Root.destroy)

    #textmenu
    text_menu = Menu(new_menu, tearoff=False)
    new_menu.add_cascade(label="Text editors", menu=text_menu)
    text_menu.add_command(label="Sublime text editor", command=launch_sublime_text_command)
    text_menu.add_command(label="Basic Text For Windows", command=launch_text_editor_command)
    text_menu.add_command(label="Basic Text 3.0", command=launch_basictext30_command)
    text_menu.add_command(label="Basic Text 2.0", command=launch_basictext20_command)
    text_menu.add_command(label="Basic Text 1.0", command=launch_basictext10_command)

    #paymeny menu
    paymeny_menu = Menu(new_menu, tearoff=False)
    new_menu.add_cascade(label="Simple payments", menu=paymeny_menu)
    paymeny_menu.add_command(label="Simple payment app", command=launch_simple_payments_app)
    paymeny_menu.add_command(label="Simple payment XA", command=launch_simple_payments_XA)

    #browsers
    browser_menu = Menu(new_menu, tearoff=False)
    new_menu.add_cascade(label="Browsers", menu=browser_menu)
    browser_menu.add_command(label="Microsoft edge", command=launch_edge_browser_command)
    browser_menu.add_command(label="Google chrome", command=launch_chrome_browser_command)

    #flashback
    fb_menu = Menu(new_menu, tearoff=False)
    new_menu.add_cascade(label="Flashback tools", menu=fb_menu)
    fb_menu.add_command(label="Flashback express recorder", command=launch_fbr_command)
    fb_menu.add_command(label="Flashback express player", command=launch_fbp_command)

    #all
    allapps_menu = Menu(new_menu, tearoff=False)
    new_menu.add_cascade(label="All apps", menu=allapps_menu)
    allapps_menu.add_command(label="Simple payment app", command=launch_simple_payments_app)
    allapps_menu.add_command(label="Simple payment XA", command=launch_simple_payments_XA)
    allapps_menu.add_separator()
    allapps_menu.add_command(label="Sublime text editor", command=launch_sublime_text_command)
    allapps_menu.add_command(label="Basic Text For Windows", command=launch_text_editor_command)
    allapps_menu.add_command(label="Basic Text 3.0", command=launch_basictext30_command)
    allapps_menu.add_command(label="Basic Text 2.0", command=launch_basictext20_command)
    allapps_menu.add_command(label="Basic Text 1.0", command=launch_basictext10_command)
    allapps_menu.add_separator()
    allapps_menu.add_command(label="Microsoft edge", command=launch_edge_browser_command)
    allapps_menu.add_command(label="Google chrome", command=launch_chrome_browser_command)

    #freeze program
    freeze_menu = Menu(new_menu, tearoff=False)
    new_menu.add_cascade(label="Lock workpsace", menu=freeze_menu)
    freeze_menu.add_command(label="05 sec", command=freez_5sec_command)
    freeze_menu.add_command(label="15 sec", command=freez_15sec_command)
    freeze_menu.add_command(label="30 sec", command=freez_30sec_command)
    freeze_menu.add_separator()
    freeze_menu.add_command(label="01 min", command=freez_60sec_command)
    freeze_menu.add_command(label="03 min", command=freez_3min_command)
    freeze_menu.add_command(label="05 min", command=freez_5min_command)

    #users
    users_menu = Menu(new_menu, tearoff=False)
    new_menu.add_cascade(label="Users", menu=users_menu)
    users_menu.add_command(label="Other user", command=other_workspae_command)

    #setting menu
    setting_menu = Menu(new_menu, tearoff=False)
    new_menu.add_cascade(label="Color", menu=setting_menu)
    setting_menu.add_command(label="Light green", command=greenBG)
    setting_menu.add_command(label="Light blue", command=blueBG)
    setting_menu.add_command(label="Light yellow", command=yellowBG)
    setting_menu.add_command(label="Light pink", command=pinkBG)
    setting_menu.add_command(label="Light purple", command=purpleBG)
    setting_menu.add_command(label="Light orange", command=orangeBG)

    #text menu
    text_menu = Menu(new_menu, tearoff=False)
    new_menu.add_cascade(label="Clock text color", menu=text_menu)
    text_menu.add_command(label="Dark green", command=greenFG)
    text_menu.add_command(label="Dark blue", command=blueFG)
    text_menu.add_command(label="Dark purple", command=purpleFG)
    text_menu.add_command(label="Dark orange", command=orangeFG)
    text_menu.add_command(label="Yellow", command=yellowFG)
    text_menu.add_command(label="Pink", command=pinkFG)

    #taskbar
    taskbar_menu = Menu(new_menu, tearoff=False)
    new_menu.add_cascade(label="Taskbar options", menu=taskbar_menu)
    taskbar_menu.add_command(label="Light green", command=greencolor)
    taskbar_menu.add_command(label="Light blue", command=bluecolor)
    taskbar_menu.add_command(label="Light yellow", command=yellowcolor)
    taskbar_menu.add_command(label="Light pink", command=pinkcolor)
    taskbar_menu.add_command(label="Light grey", command=greycolor)
    taskbar_menu.add_command(label="Light purple", command=purplecolor)
    taskbar_menu.add_command(label="Light orange", command=orangecolor)
    taskbar_menu.add_command(label="Hide taskbar", command=hide_taskbar_command)
    taskbar_menu.add_command(label="Show taskbar", command=show_taskbar_command)
    taskbar_menu.add_command(label="Center taskbar", command=center_taskbar_command)

    #tdate_menu
    date_menu = Menu(new_menu, tearoff=False)
    new_menu.add_cascade(label="Date and day text color", menu=date_menu)
    date_menu.add_command(label="Dark green", command=date_green)
    date_menu.add_command(label="Dark blue", command=date_blue)
    date_menu.add_command(label="Dark purple", command=date_purple)
    date_menu.add_command(label="Dark Orange", command=date_orange)
    date_menu.add_command(label="Yellow", command=date_yellow)
    date_menu.add_command(label="Pink", command=date_pink)

    #mormal
    normal_menu = Menu(new_menu, tearoff=False)
    new_menu.add_cascade(label="Exit developer", menu=normal_menu)
    normal_menu.add_command(label="Exit developer mode", command=commandrandom)

    Root.title('Developer mode - Workspace for windows')

def date_orange():
    day_label.configure(fg="#c4981d")

def date_green():
    day_label.configure(fg="Dark green")

def date_blue():
    day_label.configure(fg="Dark Blue")

def date_yellow():
    day_label.configure(fg="Yellow")

def date_pink():
    day_label.configure(fg="Pink")

def date_purple():
    day_label.configure(fg="Purple")

def greencolor():
    launch_text_editor_btn.configure(bg="Light green")
    exit_btn.configure(bg="Light green")
    chrome_btn.configure(bg="Light green")
    launch_payment_btn.configure(bg="Light green")
    launch_text_editor_btn.configure(bg="Light green")
    sublime_button.configure(bg="Light green")
    edge_btn.configure(bg="Light green")
    taskbar.configure(bg='Lightgreen')


def purplecolor():
    launch_text_editor_btn.configure(bg="#e2d5e8")
    exit_btn.configure(bg="#e2d5e8")
    chrome_btn.configure(bg="#e2d5e8")
    launch_payment_btn.configure(bg="#e2d5e8")
    launch_text_editor_btn.configure(bg="#e2d5e8")
    sublime_button.configure(bg="#e2d5e8")
    edge_btn.configure(bg="#e2d5e8")
    taskbar.configure(bg='#e2d5e8')

def bluecolor():
    launch_text_editor_btn.configure(bg="Light blue")
    exit_btn.configure(bg="Light blue")
    chrome_btn.configure(bg="Light blue")
    launch_payment_btn.configure(bg="Light blue")
    launch_text_editor_btn.configure(bg="Light blue")
    sublime_button.configure(bg="Light blue")
    edge_btn.configure(bg="Light blue")
    taskbar.configure(bg="Light blue")
    clock_label.configure(fg="Dark green")

def yellowcolor():
    launch_text_editor_btn.configure(bg="Light yellow")
    exit_btn.configure(bg="Light yellow")
    chrome_btn.configure(bg="Light yellow")
    launch_payment_btn.configure(bg="Light yellow")
    launch_text_editor_btn.configure(bg="Light yellow")
    sublime_button.configure(bg="Light yellow")
    edge_btn.configure(bg="Light yellow")
    taskbar.configure(bg='Light yellow')

def pinkcolor():
    launch_text_editor_btn.configure(bg="Light pink")
    exit_btn.configure(bg="Light pink")
    chrome_btn.configure(bg="Light pink")
    launch_payment_btn.configure(bg="Light pink")
    launch_text_editor_btn.configure(bg="Light pink")
    sublime_button.configure(bg="Light pink")
    edge_btn.configure(bg="Light pink")
    taskbar.configure(bg='Light pink')

def orangecolor():
    launch_text_editor_btn.configure(bg="#fed8b1")
    exit_btn.configure(bg="#fed8b1")
    chrome_btn.configure(bg="#fed8b1")
    launch_payment_btn.configure(bg="#fed8b1")
    launch_text_editor_btn.configure(bg="#fed8b1")
    sublime_button.configure(bg="#fed8b1")
    edge_btn.configure(bg="#fed8b1")
    taskbar.configure(bg='#fed8b1')

def greycolor():
    launch_text_editor_btn.configure(bg="Light grey")
    exit_btn.configure(bg="Light grey")
    chrome_btn.configure(bg="Light grey")
    launch_payment_btn.configure(bg="Light grey")
    launch_text_editor_btn.configure(bg="Light grey")
    sublime_button.configure(bg="Light grey")
    edge_btn.configure(bg="Light grey")
    taskbar.configure(bg='Light grey')

def orangeFG():
    clock_label.configure(fg="#c4981d")

def purpleFG():
    clock_label.configure(fg="Purple")

def greenFG():
    clock_label.configure(fg="Dark green")

def blueFG():
    clock_label.configure(fg="Dark blue")

def yellowFG():
    clock_label.configure(fg="Yellow")

def pinkFG():
    clock_label.configure(fg="Pink")

def orangeBG():
    Root.configure(bg="#fed8b1")
    clock_label.configure(bg="#fed8b1")
    name.configure(bg="#fed8b1")
    day_label.configure(bg="#fed8b1")

def purpleBG():
    Root.configure(bg="#e2d5e8")
    clock_label.configure(bg="#e2d5e8")
    name.configure(bg="#e2d5e8")
    day_label.configure(bg="#e2d5e8")

def greenBG():
    Root.configure(bg="Lightgreen")
    clock_label.configure(bg="Lightgreen")
    name.configure(bg="Lightgreen")
    day_label.configure(bg="Lightgreen")

def pinkBG():
    Root.configure(bg="Light pink")
    clock_label.configure(bg="Light pink")
    name.configure(bg="Light Pink")
    day_label.configure(bg="Light pink")

def blueBG():
    Root.configure(bg="Lightblue")
    clock_label.configure(bg="Lightblue")
    name.configure(bg="Lightblue")
    day_label.configure(bg="Light blue")


def yellowBG():
    Root.configure(bg="Light yellow")
    clock_label.configure(bg="Light yellow")
    name.configure(bg="Light yellow")
    day_label.configure(bg="Light yellow")

def date():
    date_time = time.strftime("%x")
    day_time = time.strftime("%a")
    day_week = time.strftime("%a")
    day_label.configure(text="Date = " +date_time +" - " +day_week)
    day_label.after(1620000, date)

def hide_calander_command():
    Cal.pack_forget()

def show_calander_command():
    Cal.pack(pady=5)

def clock():
    hms = time.strftime("%X")    
    clock_label.config(text=hms+ " - Male")
    clock_label.after(1000, clock)

def center_taskbar_command():
    messagebox.showwarning("Warning","You have to hide the taskbar before centering the taskbar")
    taskbar.pack(side=BOTTOM)

def show_taskbar_command():
    taskbar.pack(side=BOTTOM, fill=X)

def hide_taskbar_command():
    taskbar.pack_forget()

def show_help():
    messagebox.showinfo("Help", "If you need any help email izooizkaan@gmail.com")

def search_file():
    my_program = filedialog.askopenfilename()
    os.system('"%s"' % my_program)

def Settings_workspace():
    #menu 
    the_menu = Menu(Root)
    Root.config(menu=the_menu)
    Root.title("Customize workpace - Workspace for windows")
    Root.geometry("1325x600")

    #setting menu
    setting_menu = Menu(the_menu, tearoff=False)
    the_menu.add_cascade(label="Color", menu=setting_menu)
    setting_menu.add_command(label="Light green", command=greenBG)
    setting_menu.add_command(label="Light blue", command=blueBG)
    setting_menu.add_command(label="Light yellow", command=yellowBG)
    setting_menu.add_command(label="Light pink", command=pinkBG)
    setting_menu.add_command(label="Light purple", command=purpleBG)
    setting_menu.add_command(label="Light orange", command=orangeBG)

    #text menu
    text_menu = Menu(the_menu, tearoff=False)
    the_menu.add_cascade(label="Clock text color", menu=text_menu)
    text_menu.add_command(label="Dark green", command=greenFG)
    text_menu.add_command(label="Dark blue", command=blueFG)
    text_menu.add_command(label="Dark purple", command=purpleFG)
    text_menu.add_command(label="Dark orange", command=orangeFG)
    text_menu.add_command(label="Yellow", command=yellowFG)
    text_menu.add_command(label="Pink", command=pinkFG)

    #taskbar
    taskbar_menu = Menu(the_menu, tearoff=False)
    the_menu.add_cascade(label="Taskbar options", menu=taskbar_menu)
    taskbar_menu.add_command(label="Light green", command=greencolor)
    taskbar_menu.add_command(label="Light blue", command=bluecolor)
    taskbar_menu.add_command(label="Light yellow", command=yellowcolor)
    taskbar_menu.add_command(label="Light pink", command=pinkcolor)
    taskbar_menu.add_command(label="Light grey", command=greycolor)
    taskbar_menu.add_command(label="Light purple", command=purplecolor)
    taskbar_menu.add_command(label="Light orange", command=orangecolor)
    taskbar_menu.add_command(label="Hide taskbar", command=hide_taskbar_command)
    taskbar_menu.add_command(label="Show taskbar", command=show_taskbar_command)
    taskbar_menu.add_command(label="Center taskbar", command=center_taskbar_command)

    #tdate_menu
    date_menu = Menu(the_menu, tearoff=False)
    the_menu.add_cascade(label="Date and day text color", menu=date_menu)
    date_menu.add_command(label="Dark green", command=date_green)
    date_menu.add_command(label="Dark blue", command=date_blue)
    date_menu.add_command(label="Dark purple", command=date_purple)
    date_menu.add_command(label="Dark Orange", command=date_orange)
    date_menu.add_command(label="Yellow", command=date_yellow)
    date_menu.add_command(label="Pink", command=date_pink)

    #mormal
    normal_menu = Menu(the_menu, tearoff=False)
    the_menu.add_cascade(label="Exit Customize workpsace mode", menu=normal_menu)
    normal_menu.add_command(label="Exit Customize workpsace mode", command=commandrandom)

def hide_lock():
    lock_label.pack_forget()

def freez_5min_command():
    messagebox.showwarning("Warning", "Do you want to lock workpsace, until 5 minuetes you cant do anything with workpsace")
    time.sleep(300)

def freez_3min_command():
    messagebox.showwarning("Warning", "Do you want to lock workpsace, until 03 minuetes you cant do anything with workpsace")
    time.sleep(180)

def freez_60sec_command():
    messagebox.showwarning("Warning", "Do you want to lock workpsace, until 01 minuetes you cant do anything with workpsace")
    time.sleep(60)

def freez_30sec_command():
    messagebox.showwarning("Warning", "Do you want to lock workpsace, until 30 seconds you cant do anything with workpsace")
    time.sleep(30)

def freez_15sec_command():
    messagebox.showwarning("Warning", "Do you want to lock workpsace, until 15 seconds you cant do anything with workpsace")
    time.sleep(15)

def freez_5sec_command():
    messagebox.showwarning("Warning", "Do you want to lock workpsace, until 05 seconds you cant do anything with workpsace")
    time.sleep(5)

def show_about_command():
    messagebox.showinfo("About","Workspace for windows is a GUI workpsace designed to give users a neat, simple and clean GUI to do all the basic tasks you will on windows")

def show_help_command():
    messagebox.showinfo("Help","For help email izooizkaan@gmail.com")

def launch_text_editor_command():
	os.system('"%s"' %'D:\Izu\Python\Basic Text for windows.py')

def launch_simple_payment_command():
	os.system('"%s"' %'D:\Izu\Python\Simple payment XA.py')

def launch_basictext30_command():
    os.system('"%s"' %'D:\Izu\Python/basictext3.0.py')

def launch_basictext20_command():
    os.system('"%s"' %'D:\Izu\Python\BasicTextEditor2.0.py')

def launch_basictext10_command():
    os.system('"%s"' %'D:\Izu\Python\BasicTextEditor1.0.py')

def launch_simple_payments_app():
    os.system('"%s"' %'D:\Izu\Python\Simple payment app.py')

def launch_simple_payments_XA():
    os.system('"%s"' %'D:\Izu\Python\Simple payment XA.py')

def launch_sublime_text_command():
    os.system('"%s"' %'C:\Program Files\Sublime Text 3\sublime_text.exe')

def launch_edge_browser_command():
    os.system('"%s"' %'C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe')

def launch_chrome_browser_command():
    os.system('"%s"' %'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe')

def launch_fbr_command():
    os.system('"%s"' %'C:\Program Files (x86)\Blueberry Software\FlashBack Express 5\FlashBack Recorder.exe')

def launch_fbp_command():
    os.system('"%s"' %'C:\Program Files (x86)\Blueberry Software\FlashBack Express 5\FlashBack Player.exe')

def other_workspae_command():
    os.system('"%s"' %'D:\Izu\Python\Workspace for windows - Workspace UI - Other user.py')

#Lables or buttons meant to look like labels
clock_label = Label(Root, text="Activating clock", bg="Lightgreen", font=("Comfortaa", "60"))
clock_label.pack(pady=10, side=TOP)

day_label = Label(Root, text="Finding date and day", font=("Comfortaa", "30"), bg="Lightgreen")
day_label.pack()

name = Label(Root, text="Workspace for windows - Workpsace UI", font=("Comfortaa", "25"), bg="Lightgreen")
name.pack(pady=13)

style = ttk.Style(Root)
style.theme_use('clam')   # change theme, you can use style.theme_names() to list themes
Cal = Calendar(Root, background="Light green", disabledbackground="Light green", bordercolor="Light green", 
               headersbackground="Light green", normalbackground="Light green", foreground='Black', 
               normalforeground='Black', headersforeground='Black')
Cal.config(background = "Light green")

lock_label = Label(Root, text="Workpsace is locked", font=("Comfortaa", 24))

day_label.after(1000, date)
clock_label.after(1000, clock)

#random

# Gets the requested values of the height and widht.
windowWidth = Root.winfo_reqwidth()
windowHeight = Root.winfo_reqheight()
print("Width",windowWidth,"Height",windowHeight)
 
# Gets both half the screen width/height and window width/height
positionRight = int(Root.winfo_screenwidth()/2 - windowWidth/2)
positionDown = int(Root.winfo_screenheight()/2 - windowHeight/2)
 
# Positions the window in the center of the page.
Root.geometry("+{}+{}".format(positionRight, positionDown))

global taskbar
taskbar = Frame(Root)
taskbar.pack(fill=X, side=BOTTOM)
taskbar.configure(bg="Lightgrey")

#launch text editor
search = Button(taskbar, bg="#e4f0e7" ,text=" Search files ", font=("Comfortaa", "18"), borderwidth=0 ,command=search_file)
search.grid(row=0, column=0)

sublime_button = Button(taskbar, text=" Sublime text ", bg="Lightgrey" ,font=("Comfortaa", "18"), borderwidth=0 ,command=launch_sublime_text_command)
sublime_button.grid(row=0, column=1)
        
launch_text_editor_btn = Button(taskbar, text=" Text editor ", bg="Lightgrey" ,font=("Comfortaa", "18"), borderwidth=0 ,command=launch_text_editor_command)
launch_text_editor_btn.grid(row=0, column=2)

launch_payment_btn = Button(taskbar, text=" Simple payment XA ", bg="Lightgrey" ,font=("Comfortaa", "18"), borderwidth=0 ,command=launch_simple_payment_command)
launch_payment_btn.grid(row=0, column=3)

edge_btn = Button(taskbar, text=" Microsoft edge ", bg="Lightgrey" ,font=("Comfortaa", "18"), borderwidth=0 ,command=launch_edge_browser_command)
edge_btn.grid(row=0, column=5)

chrome_btn = Button(taskbar, text=" Google chrome ", bg="Lightgrey" ,font=("Comfortaa", "18"), borderwidth=0 ,command=launch_chrome_browser_command)
chrome_btn.grid(row=0, column=6)

exit_btn = Button(taskbar, text=" Exit program ", bg="Lightgrey" ,font=("Comfortaa", "18"), borderwidth=0 ,command=Root.destroy)
exit_btn.grid(row=0, column=7)

#Menubars
my_menu = Menu(Root)
Root.config(menu=my_menu)
    
#filemenu
file_menu = Menu(my_menu, tearoff=False)
my_menu.add_cascade(label="Tools", menu=file_menu)
file_menu.add_command(label="Search files", command=search_file)
file_menu.add_command(label="Customize workpace", command=Settings_workspace)
file_menu.add_command(label="Developer mode", command=developermode_command)
file_menu.add_command(label="Show Calander", command=show_calander_command)
file_menu.add_command(label="Hide Calander", command=hide_calander_command)
file_menu.add_command(label="Exit program", command=Root.destroy)

#textmenu
text_menu = Menu(my_menu, tearoff=False)
my_menu.add_cascade(label="Text editors", menu=text_menu)
text_menu.add_command(label="Sublime text editor", command=launch_sublime_text_command)
text_menu.add_command(label="Basic Text For Windows", command=launch_text_editor_command)
text_menu.add_command(label="Basic Text 3.0", command=launch_basictext30_command)
text_menu.add_command(label="Basic Text 2.0", command=launch_basictext20_command)
text_menu.add_command(label="Basic Text 1.0", command=launch_basictext10_command)

#paymeny menu
paymeny_menu = Menu(my_menu, tearoff=False)
my_menu.add_cascade(label="Simple payments", menu=paymeny_menu)
paymeny_menu.add_command(label="Simple payment app", command=launch_simple_payments_app)
paymeny_menu.add_command(label="Simple payment XA", command=launch_simple_payments_XA)

#browsers
browser_menu = Menu(my_menu, tearoff=False)
my_menu.add_cascade(label="Browsers", menu=browser_menu)
browser_menu.add_command(label="Microsoft edge", command=launch_edge_browser_command)
browser_menu.add_command(label="Google chrome", command=launch_chrome_browser_command)

#flashback
fb_menu = Menu(my_menu, tearoff=False)
my_menu.add_cascade(label="Flashback tools", menu=fb_menu)
fb_menu.add_command(label="Flashback express recorder", command=launch_fbr_command)
fb_menu.add_command(label="Flashback express player", command=launch_fbp_command)

#all
allapps_menu = Menu(my_menu, tearoff=False)
my_menu.add_cascade(label="All apps", menu=allapps_menu)
allapps_menu.add_command(label="Simple payment app", command=launch_simple_payments_app)
allapps_menu.add_command(label="Simple payment XA", command=launch_simple_payments_XA)
allapps_menu.add_separator()
allapps_menu.add_command(label="Sublime text editor", command=launch_sublime_text_command)
allapps_menu.add_command(label="Basic Text For Windows", command=launch_text_editor_command)
allapps_menu.add_command(label="Basic Text 3.0", command=launch_basictext30_command)
allapps_menu.add_command(label="Basic Text 2.0", command=launch_basictext20_command)
allapps_menu.add_command(label="Basic Text 1.0", command=launch_basictext10_command)
allapps_menu.add_separator()
allapps_menu.add_command(label="Microsoft edge", command=launch_edge_browser_command)
allapps_menu.add_command(label="Google chrome", command=launch_chrome_browser_command)

#deZloper
mode_menu = Menu(my_menu, tearoff=False)
my_menu.add_cascade(label="Modes", menu=mode_menu)
mode_menu.add_command(label="Customize workpace", command=Settings_workspace)
mode_menu.add_command(label="Developer mode", command=developermode_command)

#freeze program
freeze_menu = Menu(my_menu, tearoff=False)
my_menu.add_cascade(label="Lock workpsace", menu=freeze_menu)
freeze_menu.add_command(label="05 sec", command=freez_5sec_command)
freeze_menu.add_command(label="15 sec", command=freez_15sec_command)
freeze_menu.add_command(label="30 sec", command=freez_30sec_command)
freeze_menu.add_separator()
freeze_menu.add_command(label="01 min", command=freez_60sec_command)
freeze_menu.add_command(label="03 min", command=freez_3min_command)
freeze_menu.add_command(label="05 min", command=freez_5min_command)

#users
users_menu = Menu(my_menu, tearoff=False)
my_menu.add_cascade(label="Users", menu=users_menu)
users_menu.add_command(label="Other user", command=other_workspae_command)

#intepretern
int_menu = Menu(my_menu, tearoff=False)
my_menu.add_cascade(label="Help", menu=int_menu)
int_menu.add_command(label="Help", command=show_help_command)
int_menu.add_command(label="About", command=show_about_command)

Root.mainloop() #this is 680 lines!!!