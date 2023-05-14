from tkinter import*
from tkinter import messagebox
from tkinter import filedialog
from tkcalendar import*
from tkinter import ttk
import tkinter as tk
import tkinter as tilGUI
import time
import os

root = Tk()
root.title("Workspace for windows - BugFix 01 Beta")
root.configure(bg="Lightgreen")
root.geometry("1325x600")

# Time
timeONE = time.strftime('%X')
timeTWO = time.strftime('%X')

# Bindings
root.bind('<Escape>', lambda event: root.state('normal'))
root.bind('<F5>', lambda event: root.state('zoomed'))

# Making def's
def clock():
    global hms
    hms = time.strftime("%X")
    clock_label.config(text=hms+ " - Male")
    clock_label.after(500, clock)

def date():
    global day_time
    date_time = time.strftime("%x")
    day_time = time.strftime("%a")
    day_week = time.strftime("%a")
    day_label.configure(text="Date = " +date_time +" - " +day_week)
    day_label.after(199999, date)

def clockifycommand():
    bottom_lbl.after(500, clockifycommand)

def enter_fullscreen_command():
    root.state('zoomed')
    pass

def exit_fullscreen_command():
    root.resizable(1,1)
    root.state('normal')
    root.geometry("1325x600")

def hide_app_window_command():
    root.overrideredirect(1)

def show_app_window_command():
    root.overrideredirect(False)

def hide_calander_command():
    the_label.pack_forget()
    name.pack_forget()
    Cal.pack_forget()

def show_calander_command():
    global name
    global the_label
    the_label = Label(root, text='', bg="Lightgreen", font=('Comfortaa', 5))
    the_label.pack()
    name = Label(root, text='Calander', bg="Lightgreen", font=('Comfortaa', 18))
    name.pack()
    Cal.pack()

def exit_command():
    global timepro
    timepro = time.strftime("%X")
    root.destroy()

def show_about_command():
    messagebox.showinfo("About","# Workspace UI X2\n\nWorkspace BugFix 01\nBug fix 01\nCopyright (c) 2021 IPP.inc All Rights Reserved.\n\nThis product is made by ipp.inc, and all copyright goes to IPP.inc, do not disteribute this product without permision")

def show_help_command():
    messagebox.showinfo("Help","For help email izooizkaan@gmail.com")

# Def section - open apps
def link_open_command():
    e = input('Fille location:')
    os.popen('"%s"' % e)

def Laungceytictactoey():
    os.popen('"%s"' %'D:\Izu\Python\Tic-tac-toe.py')

def launch_text_editor_command():
    os.popen('"%s"' %'Basic Text\Basic Text for windows.py')

def launch_basictext30_command():
    os.popen('"%s"' %'Basic text\\basictext3.0.py')

def launch_basictext20_command():
    os.popen('"%s"' %'Basic text\BasicTextEditor2.0.py')

def launch_basictext5_command():
    os.popen('"%s"' %'Basic text\BasicTextEditor1.0.py')

def launch_simple_payments_app():
    os.popen('"%s"' %'D:\Izu\Python\Simple payment app.py')

def launch_simple_payments_XA():
    os.popen('"%s"' %'Extern\Simple payment XA.py')

def launch_sublime_text_command():
    os.popen('"%s"' %'C:\Program Files\Sublime Text 3\sublime_text.exe')

def launch_edge_browser_command():
    os.popen('"%s"' %'C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe')

def launch_chrome_browser_command():
    os.popen('"%s"' %'C:\Program Files\Google\Chrome\Application\chrome.exe')

def launch_fbr_command():
    os.popen('"%s"' %'C:\Program Files (x86)\Blueberry Software\FlashBack Express 5\FlashBack Recorder.exe')

def launch_fbp_command():
    os.popen('"%s"' %'C:\Program Files (x86)\Blueberry Software\FlashBack Express 5\FlashBack Player.exe')

def other_workspae_command():
    os.popen('"%s"' %'D:\Izu\Python\Workspace for windows - Workspace UI - Other user.py')

def search_file():
    my_program = filedialog.askopenfilename()
    os.popen('"%s"' % my_program)

# Def section - Color's, customize workspace
def grey_text_active_bg():
    launch_text_editor_btn.configure(activebackground="Lightgrey")
    exit_btn.configure(activebackground="Lightgrey")
    applist_btn. configure(activebackground="Lightgrey")
    launch_text_editor_btn.configure(activebackground="Lightgrey")
    Customize_btn.configure(activebackground="Lightgrey")
    edge_btn.configure(activebackground="Lightgrey")
    tkcopen_btn.configure(activebackground="Lightgrey")


def orange_text_active_bg():
    launch_text_editor_btn.configure(activebackground="#fed8b1")
    exit_btn.configure(activebackground="#fed8b1")
    applist_btn.configure(activebackground="#fed8b1")
    launch_text_editor_btn.configure(activebackground="#fed8b1")
    Customize_btn.configure(activebackground="#fed8b1")
    edge_btn.configure(activebackground="#fed8b1")
    tkcopen_btn.configure(activebackground="#fed8b1")

def pink_text_active_bg():
    launch_text_editor_btn.configure(activebackground="Pink")
    exit_btn.configure(activebackground="Pink")
    applist_btn.configure(activebackground="Pink")
    launch_text_editor_btn.configure(activebackground="Pink")
    Customize_btn.configure(activebackground="Pink")
    edge_btn.configure(activebackground="Pink")
    tkcopen_btn.configure(activebackground="Pink")

def purple_text_active_bg():
    launch_text_editor_btn.configure(activebackground="#e2d5e8")
    exit_btn.configure(activebackground="#e2d5e8")
    applist_btn.configure(activebackground="#e2d5e8")
    #note_btn.configure(activebackground="#e2d5e8")
    launch_text_editor_btn.configure(activebackground="#e2d5e8")
    Customize_btn.configure(activebackground="#e2d5e8")
    edge_btn.configure(activebackground="#e2d5e8")
    tkcopen_btn.configure(activebackground="#e2d5e8")

def blue_text_active_bg():
    launch_text_editor_btn.configure(activebackground="Light blue")
    exit_btn.configure(activebackground="Light blue")
    applist_btn.configure(activebackground="Light blue")
    #note_btn.configure(activebackground="Light blue")
    launch_text_editor_btn.configure(activebackground="Light blue")
    Customize_btn.configure(activebackground="Light blue")
    edge_btn.configure(activebackground="Light blue")
    tkcopen_btn.configure(activebackground="Light blue")

def green_text_active_bg():
    launch_text_editor_btn.configure(activebackground="Light green")
    exit_btn.configure(activebackground="Light green")
    applist_btn.configure(activebackground="Light green")
    #note_btn.configure(activebackground="Light green")
    launch_text_editor_btn.configure(activebackground="Light green")
    Customize_btn.configure(activebackground="Light green")
    edge_btn.configure(activebackground="Light green")
    tkcopen_btn.configure(activebackground="Light green")

def green_text_active():
    launch_text_editor_btn.configure(activeforeground="Dark green")
    applist_btn.configure(activeforeground="Dark green")
    #note_btn.configure(activeforeground="Dark green")
    launch_text_editor_btn.configure(activeforeground="Dark green")
    Customize_btn.configure(activeforeground="Dark green")
    edge_btn.configure(activeforeground="Dark green")
    tkcopen_btn.configure(activeforeground="Dark green")

def black_text_active():
    launch_text_editor_btn.configure(activeforeground="Black")
    applist_btn.configure(activeforeground="Black")
    #note_btn.configure(activeforeground="Black")
    launch_text_editor_btn.configure(activeforeground="Black")
    Customize_btn.configure(activeforeground="Black")
    edge_btn.configure(activeforeground="Black")
    tkcopen_btn.configure(activeforeground="Black")

def blue_text_active():
    launch_text_editor_btn.configure(activeforeground="Dark blue")
    applist_btn.configure(activeforeground="Dark blue")
    #note_btn.configure(activeforeground="Dark blue")
    launch_text_editor_btn.configure(activeforeground="Dark blue")
    Customize_btn.configure(activeforeground="Dark blue")
    edge_btn.configure(activeforeground="Dark blue")
    tkcopen_btn.configure(activeforeground="Dark blue")

def purple_text_active():
    launch_text_editor_btn.configure(activeforeground="Purple")
    applist_btn.configure(activeforeground="Purple")
    #note_btn.configure(activeforeground="Purple")
    launch_text_editor_btn.configure(activeforeground="Purple")
    Customize_btn.configure(activeforeground="Purple")
    edge_btn.configure(activeforeground="Purple")
    tkcopen_btn.configure(activeforeground="Purple")

def orange_text_active():
    launch_text_editor_btn.configure(activeforeground="#c4981d")
    applist_btn.configure(activeforeground="#c4981d")
    #note_btn.configure(activeforeground="#c4981d")
    launch_text_editor_btn.configure(activeforeground="#c4981d")
    Customize_btn.configure(activeforeground="#c4981d")
    edge_btn.configure(activeforeground="#c4981d")
    tkcopen_btn.configure(activeforeground="#c4981d")

def black_text_active():
    launch_text_editor_btn.configure(activeforeground="Black")
    applist_btn.configure(activeforeground="Black")
    #note_btn.configure(activeforeground="Black")
    launch_text_editor_btn.configure(activeforeground="Black")
    Customize_btn.configure(activeforeground="Black")
    tkcopen_btn.configure(activeforeground='Black')
    edge_btn.configure(activeforeground="Black")

def pink_text_active():
    launch_text_editor_btn.configure(activeforeground="pink")
    applist_btn.configure(activeforeground="Pink")
    #note_btn.configure(activeforeground="pink")
    launch_text_editor_btn.configure(activeforeground="Pink")
    Customize_btn.configure(activeforeground="Pink")
    tkcopen_btn.configure(activeforeground='Pink')
    edge_btn.configure(activeforeground="Pink")

def green_text():
    launch_text_editor_btn.configure(fg="Dark green")
    exit_btn.configure(fg="Dark green")
    applist_btn.configure(fg="Dark green")
    #note_btn.configure(fg="Dark green")
    launch_text_editor_btn.configure(fg="Dark green")
    Customize_btn.configure(fg="Dark green")
    edge_btn.configure(fg="Dark green")
    tkcopen_btn.configure(fg="Dark green")

def blue_text():
    launch_text_editor_btn.configure(fg="Dark blue")
    exit_btn.configure(fg="Dark blue")
    applist_btn.configure(fg="Dark blue")
    #note_btn.configure(fg="Dark blue")
    launch_text_editor_btn.configure(fg="Dark blue")
    Customize_btn.configure(fg="Dark blue")
    edge_btn.configure(fg="Dark blue")
    tkcopen_btn.configure(fg="Dark blue")

def purple_text():
    launch_text_editor_btn.configure(fg="Purple")
    exit_btn.configure(fg="Purple")
    applist_btn.configure(fg="Purple")
    #note_btn.configure(fg="Purple")
    launch_text_editor_btn.configure(fg="Purple")
    Customize_btn.configure(fg="Purple")
    edge_btn.configure(fg="Purple")
    tkcopen_btn.configure(fg="Purple")

def orange_text():
    launch_text_editor_btn.configure(fg="#c4981d")
    exit_btn.configure(fg="#c4981d")
    applist_btn.configure(fg="#c4981d")
    #note_btn.configure(fg="#c4981d")
    launch_text_editor_btn.configure(fg="#c4981d")
    Customize_btn.configure(fg="#c4981d")
    edge_btn.configure(fg="#c4981d")
    tkcopen_btn.configure(fg="#c4981d")

def black_text():
    launch_text_editor_btn.configure(fg="Black")
    exit_btn.configure(fg="Black")
    applist_btn.configure(fg="Black")
    #note_btn.configure(fg="Black")
    launch_text_editor_btn.configure(fg="Black")
    Customize_btn.configure(fg="Black")
    tkcopen_btn.configure(fg='Black')
    edge_btn.configure(fg="Black")

def pink_text():
    launch_text_editor_btn.configure(fg="pink")
    exit_btn.configure(fg="Pink")
    applist_btn.configure(fg="Pink")
    #note_btn.configure(fg="Pink")
    launch_text_editor_btn.configure(fg="Pink")
    Customize_btn.configure(fg="Pink")
    tkcopen_btn.configure(fg='Pink')
    edge_btn.configure(fg="Pink")

def date_black():
    day_label.configure(fg='Black')

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

def orangeBG():
    random.configure(bg="#fed8b1")
    root.configure(bg="#fed8b1")
    clock_label.configure(bg="#fed8b1")
    day_label.configure(bg="#fed8b1")
    bottom_lbl.configure(bg="#fed8b1")
    #add menu MENU
    thanxuey.configure(bg="#fed8b1")
    kawamath.configure(bg="#fed8b1")
    xux_label.configure(bg="#fed8b1")
    xaq_label.configure(bg="#fed8b1")
    #the_frame.configure(bg='#fed8b1')
    app_frame.configure(bg='#fed8b1')
    random_label.configure(bg='#fed8b1')

def purpleBG():
    random.configure(bg="#e2d5e8")
    root.configure(bg="#e2d5e8")
    clock_label.configure(bg="#e2d5e8")
    day_label.configure(bg="#e2d5e8")
    bottom_lbl.configure(bg="#e2d5e8")
    #add menu MENU
    thanxuey.configure(bg="#e2d5e8")
    kawamath.configure(bg="#e2d5e8")
    xux_label.configure(bg="#e2d5e8")
    xaq_label.configure(bg="#e2d5e8")
    #the_frame.configure(bg='#e2d5e8')
    app_frame.configure(bg='#e2d5e8')
    random_label.configure(bg='#e2d5e8')

def greenBG():
    random.configure(bg="Light green")
    root.configure(bg="Light green")
    clock_label.configure(bg="Light green")
    day_label.configure(bg="Light green")
    bottom_lbl.configure(bg="Light green")
    #add menu MENU
    thanxuey.configure(bg="Lightgreen")
    kawamath.configure(bg="Lightgreen")
    xux_label.configure(bg="Lightgreen")
    xaq_label.configure(bg="Lightgreen")
    #the_frame.configure(bg='Lightgreen')
    app_frame.configure(bg='Lightgreen')
    random_label.configure(bg='Lightgreen')

def pinkBG():
    random.configure(bg="Light pink")
    root.configure(bg="Light pink")
    clock_label.configure(bg="Light pink")
    day_label.configure(bg="Light pink")
    bottom_lbl.configure(bg="Light pink")
    #add menu MENU
    thanxuey.configure(bg="Lightpink")
    kawamath.configure(bg="Lightpink")
    xux_label.configure(bg="Lightpink")
    xaq_label.configure(bg="Lightpink")
    #the_frame.configure(bg='Lightpink')
    app_frame.configure(bg='Lightpink')
    random_label.configure(bg='Lightpink')

def blueBG():
    random.configure(bg="Light blue")
    root.configure(bg="Light blue")
    clock_label.configure(bg="Light blue")
    day_label.configure(bg="Light blue")
    bottom_lbl.configure(bg="Light blue")
    #add menu MENU
    thanxuey.configure(bg="Lightblue")
    kawamath.configure(bg="Lightblue")
    xux_label.configure(bg="Lightblue")
    xaq_label.configure(bg="Lightblue")
    #the_frame.configure(bg='Lightblue')
    app_frame.configure(bg='Lightblue')
    random_label.configure(bg='Lightblue')

def yellowBG():
    random.configure(bg="Light yellow")
    root.configure(bg="Light yellow")
    clock_label.configure(bg="Light yellow")
    day_label.configure(bg="Light yellow")
    bottom_lbl.configure(bg="Light yellow")
    #add menu MENU
    thanxuey.configure(bg="Lightyellow")
    kawamath.configure(bg="Lightyellow")
    xux_label.configure(bg="Lightyellow")
    xaq_label.configure(bg="Lightyellow")
    #the_frame.configure(bg='Lightyellow')
    app_frame.configure(bg='Lightyellow')
    random_label.configure(bg='Lightyellow')


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

def blackFG():
    clock_label.configure(fg="Black")

#def section in section (customize workspace and colors) #taskbar options
def center_taskbar_command():
    bottom_lbl.pack_forget()
    taskbar.pack_forget()
    taskbar.pack(side=BOTTOM)
    bottom_lbl.pack(side=BOTTOM)

def show_taskbar_command():
    bottom_lbl.pack_forget()
    taskbar.pack(side=BOTTOM, fill=X)
    bottom_lbl.pack(side=BOTTOM)

def hide_taskbar_command():
    taskbar.pack_forget()

def greencolor():
    launch_text_editor_btn.configure(bg="Light green")
    exit_btn.configure(bg="Light green")
    applist_btn.configure(bg="Light green")
    #note_btn.configure(bg="Light green")
    launch_text_editor_btn.configure(bg="Light green")
    Customize_btn.configure(bg="Light green")
    edge_btn.configure(bg="Light green")
    tkcopen_btn.configure(bg="Lightgreen")
    taskbar.configure(bg='Lightgreen')

def purplecolor():
    launch_text_editor_btn.configure(bg="#e2d5e8")
    exit_btn.configure(bg="#e2d5e8")
    applist_btn.configure(bg="#e2d5e8")
    #note_btn.configure(bg="#e2d5e8")
    launch_text_editor_btn.configure(bg="#e2d5e8")
    Customize_btn.configure(bg="#e2d5e8")
    tkcopen_btn.configure(bg="#e2d5e8")
    edge_btn.configure(bg="#e2d5e8")
    taskbar.configure(bg='#e2d5e8')

def bluecolor():
    launch_text_editor_btn.configure(bg="Light blue")
    exit_btn.configure(bg="Light blue")
    applist_btn.configure(bg="Light blue")
    #note_btn.configure(bg="Light blue")
    launch_text_editor_btn.configure(bg="Light blue")
    Customize_btn.configure(bg="Light blue")
    tkcopen_btn.configure(bg="Light blue")
    edge_btn.configure(bg="Light blue")
    taskbar.configure(bg="Light blue")
    clock_label.configure(fg="Dark green")

def yellowcolor():
    launch_text_editor_btn.configure(bg="Light yellow")
    exit_btn.configure(bg="Light yellow")
    applist_btn.configure(bg="Light yellow")
    #note_btn.configure(bg="Light yellow")
    launch_text_editor_btn.configure(bg="Light yellow")
    Customize_btn.configure(bg="Light yellow")
    tkcopen_btn.configure(bg="Light yellow")
    edge_btn.configure(bg="Light yellow")
    taskbar.configure(bg='Light yellow')

def pinkcolor():
    launch_text_editor_btn.configure(bg="Light pink")
    exit_btn.configure(bg="Light pink")
    applist_btn.configure(bg="Light pink")
    #note_btn.configure(bg="Light pink")
    launch_text_editor_btn.configure(bg="Light pink")
    Customize_btn.configure(bg="Light pink")
    tkcopen_btn.configure(bg="Lightpink")
    edge_btn.configure(bg="Light pink")
    taskbar.configure(bg='Light pink')

def orangecolor():
    launch_text_editor_btn.configure(bg="#fed8b1")
    exit_btn.configure(bg="#fed8b1")
    #note_btn.configure(bg="#fed8b1")
    launch_text_editor_btn.configure(bg="#fed8b1")
    Customize_btn.configure(bg="#fed8b1")
    tkcopen_btn.configure(bg="#fed8b1")
    edge_btn.configure(bg="#fed8b1")
    taskbar.configure(bg='#fed8b1')

def greycolor():
    launch_text_editor_btn.configure(bg="Light grey")
    exit_btn.configure(bg="Light grey")
    #note_btn.configure(bg="Light grey")
    launch_text_editor_btn.configure(bg="Light grey")
    tkcopen_btn.configure(bg="Lightgrey")
    Customize_btn.configure(bg="Light grey")
    edge_btn.configure(bg="Light grey")
    taskbar.configure(bg='Light grey')

#def section -modes

header_font = ('Comfortaa', 21)
grey = 'Lightgrey'
size = ('500x400')
the_font = ('Comfortaa', 16)

def Settings_workspace():
    root.geometry("1325x600")
    bottom_lbl.configure(text='Customize workspace homescreen - Workspace BugFix 01')

    the_menu = Menu(root)
    root.config(menu=the_menu)

    #background color
    setting_menu = Menu(the_menu, tearoff=False)
    the_menu.add_cascade(label="Background color", menu=setting_menu)
    setting_menu.add_command(label="Light green", command=greenBG)
    setting_menu.add_command(label="Light blue", command=blueBG)
    setting_menu.add_command(label="Light pink", command=pinkBG)
    setting_menu.add_command(label="Light purple", command=purpleBG)
    setting_menu.add_command(label="Light orange", command=orangeBG)

    #clock label color
    clock_label_color = Menu(the_menu, tearoff=False)
    the_menu.add_cascade(label="Clock text color", menu=clock_label_color)
    clock_label_color.add_command(label="Dark green", command=greenFG)
    clock_label_color.add_command(label="Dark blue", command=blueFG)
    clock_label_color.add_command(label="Light pink", command=pinkFG)
    clock_label_color.add_command(label="Dark purple", command=purpleFG)
    clock_label_color.add_command(label="Brown", command=orangeFG)
    clock_label_color.add_command(label="Black", command=blackFG)

    #taskbar
    taskbar_menu = Menu(the_menu, tearoff=False)
    the_menu.add_cascade(label="Taskbar options", menu=taskbar_menu)
    taskbar_menu.add_command(label="Light green", command=greencolor)
    taskbar_menu.add_command(label="Light blue", command=bluecolor)
    taskbar_menu.add_command(label="Light grey", command=greycolor)
    taskbar_menu.add_command(label="Light purple", command=purplecolor)
    taskbar_menu.add_command(label="Light orange", command=orangecolor)
    taskbar_menu.add_command(label="Pink", command=pinkcolor)
    taskbar_menu.add_separator()
    taskbar_menu.add_command(label="Hide taskbar", command=hide_taskbar_command)
    taskbar_menu.add_command(label="Show taskbar", command=show_taskbar_command)
    taskbar_menu.add_command(label="Center taskbar", command=center_taskbar_command)

    #tdate_menu
    date_menu = Menu(the_menu, tearoff=False)
    the_menu.add_cascade(label="Date and day text color", menu=date_menu)
    date_menu.add_command(label="Dark green", command=date_green)
    date_menu.add_command(label="Dark blue", command=date_blue)
    date_menu.add_command(label="Dark purple", command=date_purple)
    date_menu.add_command(label="Brown", command=date_orange)
    date_menu.add_command(label="Black", command=date_black)
    date_menu.add_command(label="Pink", command=date_pink)

    #tdate_menu
    SEARCH_MENU_CUS = Menu(the_menu, tearoff=False)
    the_menu.add_cascade(label="Button text color", menu=SEARCH_MENU_CUS)
    SEARCH_MENU_CUS.add_command(label="Dark green", command=green_text)
    SEARCH_MENU_CUS.add_command(label="Dark blue", command=blue_text)
    SEARCH_MENU_CUS.add_command(label="Dark purple", command=purple_text)
    SEARCH_MENU_CUS.add_command(label="Brown", command=orange_text)
    SEARCH_MENU_CUS.add_command(label="Black", command=black_text)
    SEARCH_MENU_CUS.add_command(label="Pink", command=pink_text)

    #tdate_menu
    ABC_menu = Menu(the_menu, tearoff=False)
    the_menu.add_cascade(label="Active button text color", menu=ABC_menu)
    ABC_menu.add_command(label="Dark green", command=green_text_active)
    ABC_menu.add_command(label="Dark blue", command=blue_text_active)
    ABC_menu.add_command(label="Dark purple", command=purple_text_active)
    ABC_menu.add_command(label="Brown", command=orange_text_active)
    ABC_menu.add_command(label="Black", command=black_text_active)
    ABC_menu.add_command(label="Pink", command=pink_text_active)

    #tdate_menu
    menu_menu = Menu(the_menu, tearoff=False)
    the_menu.add_cascade(label="Active button background color", menu=menu_menu)
    menu_menu.add_command(label="Light green", command=green_text_active_bg)
    menu_menu.add_command(label="Light blue", command=blue_text_active_bg)
    menu_menu.add_command(label="Light purple", command=purple_text_active_bg)
    menu_menu.add_command(label="light orange", command=orange_text_active_bg)
    menu_menu.add_command(label="Light grey", command=grey_text_active_bg)
    menu_menu.add_command(label="Pink", command=pink_text_active_bg)

    #lakure menu
    lakure_menu = Menu(the_menu, tearoff=False)
    the_menu.add_cascade(label="Exit modes", menu=lakure_menu)
    lakure_menu.add_command(label="Exit customize workspace mode", command=commandrandom)

    #break ----
    Customize_btn.configure(text='Normal mode', command=commandrandom)

    root.title("Workspace for windows - Workspace BugFix 01 - Customize workspace")

#def -- BREAKLINE
app_frame = Frame(root, bg='Lightgreen')
random_label = Label(root, text='Application list', font=('Comfortaa', 27), bg='Lightgreen')

username = 'izkaan DEVELOPER'
job_name = 'izkaan and dad python productions'

def end_session_command_msg():
    data_end = str( username+ '' + ' has ended a session on '+ time.strftime("%a") + ' '+ time.strftime('%X') + ' for ' + job_name + ' company')
    messagebox.showinfo("Sessions" ,data_end)

def Start_session_command_msg():
    data_start = str( username+ '' + ' has started a new session on '+ time.strftime("%a") + ' '+ time.strftime('%X') + ' for ' + job_name+ ' company')
    messagebox.showinfo("Sessions" ,data_start)

def AppList_ShowCommand():
    #clear the screen and edit the title
    random.pack_forget()
    clock_label.pack_forget()
    day_label.pack_forget()
    bottom_lbl.configure(text='App list - Workspace BugFix 01')
    #the_frame.pack_forget()

    #configure
    applist_btn.configure(text='Normal mode', command=commandrandom)
    root.title('Workspace for windows - BugFix 01 Beta - App list')
    random_label.pack(side=TOP, pady=5)

    #frame
    app_frame.pack(side=TOP, fill=X)

    b1 = Button(app_frame, text=" Sublime text editor ", bg="Lightgrey" ,font=("Comfortaa", "17"), borderwidth=0 ,activebackground="Lightgrey",activeforeground="Darkgreen", width=20,command=launch_sublime_text_command)
    b1.grid(row=0, column=0, padx=5)

    b2 = Button(app_frame, text=" Basic text for windows ", bg="Lightgrey" ,font=("Comfortaa", "17"), borderwidth=0 ,activebackground="Lightgrey",activeforeground="Darkgreen", width=20,command=launch_text_editor_command)
    b2.grid(row=0, column=1, padx=5)

    b3 = Button(app_frame, text=" Basic text editor 3.0 ", bg="Lightgrey" ,font=("Comfortaa", "17"), borderwidth=0 ,activebackground="Lightgrey",activeforeground="Darkgreen", width=20,command=launch_basictext30_command)
    b3.grid(row=0, column=2, padx=5)

    b4 = Button(app_frame, text=" Basic text editor 2.0 ", bg="Lightgrey" ,font=("Comfortaa", "17"), borderwidth=0 ,activebackground="Lightgrey",activeforeground="Darkgreen", width=20,command=launch_basictext20_command)
    b4.grid(row=0, column=3, padx=5)

    b8 = Button(app_frame, text=" Tic Tac Toe ", bg="Lightgrey" ,font=("Comfortaa", "17"), borderwidth=0 ,activebackground="Lightgrey",activeforeground="Darkgreen", width=15,command=Laungceytictactoey)
    b8.grid(row=0, column=4, padx=5)

    b5 = Button(app_frame, text=" Basic text editor 1.0 ", bg="Lightgrey" ,font=("Comfortaa", "17"), borderwidth=0 ,activebackground="Lightgrey",activeforeground="Darkgreen", width=20,command=launch_basictext5_command)
    b5.grid(row=1, column=0, padx=5, pady=5)

    b6 = Button(app_frame, text=" Simple payment app ", bg="Lightgrey" ,font=("Comfortaa", "17"), borderwidth=0 ,activebackground="Lightgrey",activeforeground="Darkgreen", width=20,command=launch_simple_payments_app)
    b6.grid(row=1, column=1, padx=5, pady=5)

    b7 = Button(app_frame, text=" Simple payment XA ", bg="Lightgrey" ,font=("Comfortaa", "17"), borderwidth=0 ,activebackground="Lightgrey",activeforeground="Darkgreen", width=20,command=launch_simple_payments_XA)
    b7.grid(row=1, column=2, padx=5, pady=5)

    b9= Button(app_frame, text=" Microsoft edge ", bg="Lightgrey" ,font=("Comfortaa", "17"), borderwidth=0 ,activebackground="Lightgrey",activeforeground="Darkgreen", width=20,command=launch_edge_browser_command)
    b9.grid(row=1, column=3, padx=5, pady=5)

    b10 = Button(app_frame, text=" Google chrome ", bg="Lightgrey" ,font=("Comfortaa", "17"), borderwidth=0 ,activebackground="Lightgrey",activeforeground="Darkgreen", width=15,command=launch_chrome_browser_command)
    b10.grid(row=1, column=4, padx=5, pady=5)

    b11= Button(app_frame, text=" Flashback player ", bg="Lightgrey" ,font=("Comfortaa", "17"), borderwidth=0 ,activebackground="Lightgrey",activeforeground="Darkgreen", width=20,command=launch_fbp_command)
    b11.grid(row=2, column=0, padx=5, pady=5)

    b12= Button(app_frame, text=" Flashback recorder ", bg="Lightgrey" ,font=("Comfortaa", "17"), borderwidth=0 ,activebackground="Lightgrey",activeforeground="Darkgreen", width=20,command=launch_fbr_command)
    b12.grid(row=2, column=1, padx=5, pady=5)

#taskabr
#making a taskbar (smaller than before!)
taskbar = Frame(root)
taskbar.pack(fill=X, side=BOTTOM)
taskbar.configure(bg="Lightgrey")

#LABELS
random = Label(root, text="", bg="Lightgreen")
random.pack(fill=X)

clock_label = Label(root, text="Activating clock", bg="Lightgreen", font=("Comfortaa", "65"))
clock_label.pack(pady=5, side=TOP)

day_label = Label(root, text="Finding date and day", font=("Comfortaa", "37"), bg="Lightgreen")
day_label.pack(side=TOP)

day_label.after(500, date)
clock_label.after(500, clock)

#making a taskbar (smaller than before!)
taskbar = Frame(root)
taskbar.pack(fill=X, side=BOTTOM)
taskbar.configure(bg="Lightgrey")

search = Button(taskbar, bg="#e4f0e7" ,text=" Search files ", font=("Comfortaa", "17"), borderwidth=0 ,activebackground="#e4f0e7",activeforeground="Darkblue" ,command=search_file)
search.grid(row=0, column=0)

applist_btn = Button(taskbar, bg="#e4f0e7" ,text=" Application list ", font=("Comfortaa", "17"), borderwidth=0 ,activebackground="#e4f0e7",activeforeground="Darkblue" ,command=AppList_ShowCommand)
applist_btn.grid(row=0, column=1)

launch_text_editor_btn = Button(taskbar, text=" Text editor ", bg="Lightgrey" ,font=("Comfortaa", "17"), borderwidth=0 ,activebackground="Lightgrey",activeforeground="Darkgreen" ,command=launch_text_editor_command)
launch_text_editor_btn.grid(row=0, column=2)

tkcopen_btn = Button(taskbar, text=" Tic tac toe ", bg="Lightgrey" ,font=("Comfortaa", "17"), borderwidth=0 ,activebackground="Lightgrey",activeforeground="Darkgreen" ,command=Laungceytictactoey)
tkcopen_btn.grid(row=0, column=3)

edge_btn = Button(taskbar, text=" Microsoft edge ", bg="Lightgrey" ,font=("Comfortaa", "17"), borderwidth=0 ,activebackground="Lightgrey",activeforeground="Darkgreen" ,command=launch_edge_browser_command)
edge_btn.grid(row=0, column=4)

Customize_btn = Button(taskbar, text=" Customize mode ", bg="Lightgrey" ,font=("Comfortaa", "17"), borderwidth=0 ,activebackground="Lightgrey",activeforeground="Darkgreen",command=Settings_workspace)
Customize_btn.grid(row=0, column=7)

exit_btn = Button(taskbar, text=" Exit workspace ", bg="Lightgrey" ,font=("Comfortaa", "17"), borderwidth=0 ,activebackground="Lightgrey",activeforeground="Darkred" ,command=exit_command)
exit_btn.grid(row=0, column=8)

#-- Labels
bottom_lbl = Label(root, text="Homescreen - Workspace BugFix 01", font=("Comfortaa", "14"), bg="Lightgreen")
bottom_lbl.pack(side=BOTTOM)

#making a calander
style = ttk.Style(root)
style.theme_use('clam')
Cal = Calendar(root, background="Light green", disabledbackground="Light green", bordercolor="Light green",
               headersbackground="Light green", normalbackground="Light green", foreground='Black',
               normalforeground='Black', headersforeground='Black')
Cal.config(background = "Light green")

def commandrandom():
    #repack
    random.pack()
    clock_label.pack(side=TOP)
    day_label.pack(side=TOP)

    #configure text
    Customize_btn.configure(text=" Customize mode ", command=Settings_workspace)
    root.title("Workspace for windows - BugFix 01 Beta")
    Homescreen = bottom_lbl.configure(text="Homescreen - Workspace BugFix 01")
    bottom_lbl.config(font=("Comfortaa", "14"))
    #the_frame.pack_forget()
    random_label.pack_forget()
    app_frame.pack_forget()

    applist_btn.configure(text=" Application list ", command=AppList_ShowCommand)

    #Menubars help navigate
    global my_menu
    my_menu = Menu(root)
    root.config(menu=my_menu)
    random.configure(text=' ')

    #filemenu
    BE_external_M = Menu(my_menu, tearoff=False)
    my_menu.add_cascade(label=" Workspace  tools ", menu=BE_external_M)
    BE_external_M.add_command(label="Search files",command=search_file)
    BE_external_M.add_command(label="Customize workpace", command=Settings_workspace)
    BE_external_M.add_separator()
    BE_external_M.add_command(label="Start session", command=Start_session_command_msg)
    BE_external_M.add_command(label="End session", command=end_session_command_msg)
    BE_external_M.add_separator()
    BE_external_M.add_command(label="Show Calande", command=show_calander_command)
    BE_external_M.add_command(label="Hide Calander", command=hide_calander_command)
    BE_external_M.add_command(label="Exit Workspace", command=exit_command)

    #text editors menu
    #textmenu
    text_menu = Menu(my_menu, tearoff=False)
    my_menu.add_cascade(label="Text editors", menu=text_menu)
    text_menu.add_command(label="Sublime text editor", command=launch_sublime_text_command)
    text_menu.add_command(label="Basic Text For Windows", command=launch_text_editor_command)
    text_menu.add_command(label="Basic Text 3.0", command=launch_basictext30_command)
    text_menu.add_command(label="Basic Text 2.0", command=launch_basictext20_command)
    text_menu.add_command(label="Basic Text 1.0", command=launch_basictext5_command)

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

    #all apps
    allapps_menu = Menu(my_menu, tearoff=False)
    my_menu.add_cascade(label="All apps", menu=allapps_menu)
    allapps_menu.add_command(label="Simple payment app", command=launch_simple_payments_app)
    allapps_menu.add_command(label="Simple payment XA", command=launch_simple_payments_XA)
    allapps_menu.add_command(label='Tic tac toe', command=Laungceytictactoey)
    allapps_menu.add_separator()
    allapps_menu.add_command(label="Sublime text editor", command=launch_sublime_text_command)
    allapps_menu.add_command(label="Basic Text For Windows", command=launch_text_editor_command)
    allapps_menu.add_command(label="Basic Text 3.0", command=launch_basictext30_command)
    allapps_menu.add_command(label="Basic Text 2.0", command=launch_basictext20_command)
    allapps_menu.add_command(label="Basic Text 1.0", command=launch_basictext5_command)
    allapps_menu.add_separator()
    allapps_menu.add_command(label="Microsoft edge", command=launch_edge_browser_command)
    allapps_menu.add_command(label="Google chrome", command=launch_chrome_browser_command)
    allapps_menu.add_separator()
    allapps_menu.add_command(label="Flashback express recorder", command=launch_fbr_command)
    allapps_menu.add_command(label="Flashback express player", command=launch_fbp_command)

    #freeze program
    v_menu = Menu(my_menu, tearoff=False)
    my_menu.add_cascade(label="View options", menu=v_menu)
    v_menu.add_command(label="Fullscreen", command=enter_fullscreen_command)
    v_menu.add_command(label="Exit Fullscreen", command=exit_fullscreen_command)
    v_menu.add_separator()
    v_menu.add_command(label="Hide window title", command=hide_app_window_command)
    v_menu.add_command(label="Show window title", command=show_app_window_command)

    #intepretern
    c_menu = Menu(my_menu, tearoff=False)
    my_menu.add_cascade(label="Modes", menu=c_menu)
    c_menu.add_command(label="Customize workspace", command=Settings_workspace)

    #intepretern
    int_menu = Menu(my_menu, tearoff=False)
    my_menu.add_cascade(label="Help", menu=int_menu)
    int_menu.add_command(label="Help", command=show_help_command)
    int_menu.add_command(label="About", command=show_about_command)

commandrandom() #command random is the deafult main winword

hrminssec = time.strftime("%X")
root.mainloop()
