# -*- coding: utf-8 -*-
from tkinter import *
from tkinter import ttk
from tkcalendar import *
import tkinter.ttk as tkk
from PIL import ImageTk, Image
from tkinter import filedialog
from tkinter import messagebox
from tkinter import colorchooser
import os, center_tk_window, sys, pygame, webbrowser

# Window
root = Tk()
root.title("Workspace NT for windows")
root.geometry('1020x500')
root.config(bg='lightgreen')

# Startup sound
def playStartupSound():
    try:
        sound_file = open(f"Config\Sounds\logonSound.cnf")
        sound_file = sound_file.read()

        # Play sound
        pygame.mixer.init()
        pygame.mixer.music.load(f'Sounds\{sound_file}')
        pygame.mixer.music.play(loops=0)
    except Exception:
        messagebox.showerror('Error', f"The file {sound_file} does not exist.")

# If activeSound.cnf is set to true
activeSound = open(f"Config\soundName.cnf")
activeSound = activeSound.read()

if activeSound == "TRUE": playStartupSound()

# Variables
font_size = 13

# Center window
center_tk_window.center_on_screen(root)

# Get image name from ImageName.cnf
SPECM = open('Config\ImageName.cnf')
SPECM = SPECM.read()

people_str ="""- Izkaan ahmed shareef (Lead developer)

All credits of the UI and application developemenent goes to izkaan while some suggestions and bugs were found by ahmed shareef, and kayan was the contributor of the advertisement video.

The contribution numbers will be Izkaan 100%
Concept of workspace was also developed by izkaan, founder of IPP, This is a minor fix and a special version of workspace.

Workspace NT is made to celebrate "IPP's half aniversary". It is a minor new build, but recomended to download instead.
"""

if SPECM == "$IPP_HALF_BEYOND.REAL":
    messagebox.showinfo(r"Credits", people_str)

# Set background image
if (SPECM != ""):
    try:
        image_tk = f"Images\{SPECM}"
        SPECM = PhotoImage(file=image_tk)

        background_label = Label(root, image=SPECM)
        background_label.place(x=0, y=0, relwidth=1, relheight=1)

    except Exception as err:
        print("The following image is not found in the \Images directory. Please add the following image")

# Variables
about_txt = """\nIPP Workspace
    -------------------------------------------------------------------------------------------

    Version NT (Build NT-DEV-7121Rm)
    Milestone 1.0x Build, offical milestone update
    IPP Workspace ® Codename ® Halfes

    © 2021 Izkaan Python Productions. All rights reserved

    The code for "Workspace" shall NOT be distributed ileagally.
    This product is licensed under the MIT license OFFICALLY.
    This is also a developement build, not for public.
"""

# About workspace
def about_cmd():
    # About window
    about_win = Toplevel()
    about_win.title("About - Workspace NT for windows")
    about_win.geometry('600x350')
    about_win.config(bg='#f0f0f0')
    about_win.resizable(0, 0)
    center_tk_window.center_on_screen(about_win)

    # Display about text
    about_label = Text(about_win, font=('Monospace', 13), selectbackground='#f0f0f0', selectforeground='black', bd=0, wrap=WORD, bg='#f0f0f0')
    about_label.insert('1.0', about_txt)
    about_label.pack(expand=1, fill='both', pady=2, padx=2)
    about_label.config(state="disabled")

    # Tag
    about_label.tag_add("start", "2.0", "2.30")
    about_label.tag_config("start", font=('ubuntu', 20), justify='center', foreground='#0077c8')

# Open file
def openfile():
    filename = filedialog.askopenfilename(initialdir='C:\\', title='Select file to open')
    filename = ''.join(filename)
    os.popen(filename)

# View source code
def view_source_code():
    # Source code window
    srcwin = Toplevel()
    srcwin.title("Workspace NT for windows - Source code (Application.py)")
    srcwin.geometry('500x265')
    srcwin.config(bg='black')
    center_tk_window.center_on_screen(srcwin)

    # Get source code
    src_code = open("Application.pyw", "r")
    src_code = src_code.read()

    # Define scrollbar
    scrollbar = Scrollbar(srcwin)
    scrollbar.pack(side=RIGHT, fill=Y)

    # Display source Recorder
    src_code_label = Text(srcwin, font=('Consolas', 12), selectbackground='black', selectforeground='green', fg='lightgreen', bg='black', bd=0)
    src_code_label.insert('1.0', src_code)
    src_code_label.pack(expand=1, fill='both', pady=2, padx=2)
    src_code_label.config(state="disabled")

    # Add scrollbar
    src_code_label.config(yscrollcommand=scrollbar.set)
    scrollbar.config(command=src_code_label.yview)

# Activate widgets
def activ_widgets():
    file = open(r"Config\activeWidgets.cnf", 'w')
    file.write("TRUE")
    tkcalendar.pack(anchor='nw', pady=15, padx=15)

# Activateee widgets
def active_widgets():
    file = open(r"Config\activeWidgets.cnf", 'w')
    file.write("TRUE")

# Disable widgets
def disl_widget():
    file = open(r"Config\activeWidgets.cnf", 'w')
    file.write("FALSE")
    tkcalendar.pack_forget()

# Taskbar color customize
def taskbar_color_change(colorname):
    Taskbar.config(bg=str(colorname))
    chrome_btn.config(bg=str(colorname))
    atom_btn.config(bg=str(colorname))
    setting_btn.config(bg=str(colorname))
    text_btn.config(bg=str(colorname))
    py_btn.config(bg=str(colorname))
    terminal_btn.config(bg=str(colorname))
    explorer_btn.config(bg=str(colorname))
    fnx.config(bg=str(colorname))
    twd.config(bg=str(colorname))

# Bright mode
def bright_mode():
    taskbar_color_change(colorname='white')
    tkcalendar.config (
        background="lightgrey", disabledbackground="lightgrey", bordercolor="lightgrey",
        headersbackground="lightgrey", normalbackground="lightgrey", foreground='Black',
        normalforeground='Black', headersforeground='Black'
    )

# Deafult mode
def deafult_mode():
    taskbar_color_change(colorname='lightgrey')
    tkcalendar.config (
        background="lightblue", disabledbackground="lightblue", bordercolor='lightblue',
        headersbackground="lightblue", normalbackground="lightblue", foreground='Black',
        normalforeground='Black', headersforeground='Black'
    )

# Dark mode
def dark_mode():
    taskbar_color_change(colorname='grey')
    tkcalendar.config (
        background="grey", disabledbackground="grey", bordercolor="grey",
        headersbackground="grey", normalbackground="grey", foreground='white',
        normalforeground='white', headersforeground='white'
    )

# Exit Basic text application
def cexits():
    cwin.pack_forget()
    Taskbar.pack(side='bottom')
    text_btn.config(state='active')
    activ_widgets()
    normal_menu()


def stb_func():
    content = open(r"Config\soundName.cnf", 'w')
    content.write("TRUE")

def stbf_func():
    content = open(r"Config\soundName.cnf", 'w')
    content.write("FALSE")

def fUnC(output):
    content = open(r"Config\imageName.cnf", 'w')
    content.write(output)

# Paint exit
def exitPaint():
    pwin.pack_forget()
    Taskbar.pack(side='bottom')
    text_btn.config(state='active')
    activ_widgets()
    normal_menu()

# Paint app
def PaintApp():
    global pwin, lbar, bext, textele

    disl_widget()

    # Main frame
    pwin = Frame(bd=0)
    pwin.pack(fill='both', expand=1, pady=35, padx=35)

    # Toolbar
    lbar = Frame(pwin, bd=0, bg='lightgrey')
    lbar.pack(fill='x', side='top')

    # Exit button
    bext = Button(lbar, text=' X ', font=('ubuntu', 14), bg='lightgrey', fg='red', bd=0, activebackground='red', activeforeground='lightgrey', command=lambda:exitPaint())
    bext.pack(side='right')

    textele = Label(lbar, text='Paint App', justify='center', fg='black', font=("ubuntu", 14), bg='lightgrey')
    textele.pack(pady=(2, 0))

    #variables section
    w = 600
    h = 400

    #def section
    brush_color = 'Black'
    def pain(e):
        #brush paramaters
        brush_width = '%0.0f' % float(my_slider.get())
        #brush_color = 'Dark green'
        brush_type2 = brush_type.get()
        #starting position
        x1 = e.x -1
        y1 = e.y -1
        #ending postion
        x2 = e.x +1
        y2 = e.y +1
        #draw on the canvas
        my_canvas.create_line(x1, y1, x2, y2, fill=brush_color, width=brush_width, capstyle=brush_type2, smooth=True)

    def change_brush_size(thing):
        slider_label.config(text='%0.0f' % float(my_slider.get()))

    def change_brush_color():
        messagebox.showerror("Error", "We are expeiencing some technical issues with brush colors. ")

        brush_color = 'Black'
        brush_color = colorchooser.askcolor(color=brush_color)[1]

    def change_canvas_color():
        global bg_color
        bg_color = 'Black'
        bg_color = colorchooser.askcolor(color=bg_color)[1]
        my_canvas.config(bg=bg_color)

    def clear_screen():
        my_canvas.delete(ALL)
        my_canvas.config(bg='white')

    def save_as_PNG():
        global result
        result = filedialog.asksaveasfilename(initialdir='D:\Izu\python icon sets', filetypes=(('PNG files', '*.png'), ('All files', '*.png')))

        #else
        if result.endswith('.png'):
            return
        else:
            result = result + '.png'    

        if result:
            #Pup up cgood message
            messagebox.showinfo("Message", 'Your image has been saved!')

        my_var = root.title("Paint program " + result)
        print(result)

    def help_show():
        messagebox.showinfo("Help", 'For help and support email izooizkaan@gmail.com')

    def about_show():
        messagebox.showinfo('About', 'Paint for windows Version 1.0, made on Thursday.\nCredit for codemy.com for the concept. Made by izkaan and dad python productions')

    #bursh options frame
    brush_options_frame = Frame(pwin, bg='lightgrey')
    brush_options_frame.pack(fill='x', side='top')

    brush_type = StringVar()
    brush_type.set('round')

    #brush size
    brush_size_frame = Frame(brush_options_frame, bg='lightgrey')
    brush_size_frame.grid(row=0, column=0)

    my_slider = tkk.Scale(brush_size_frame, from_=1, to=100, command=change_brush_size, orient=HORIZONTAL, value=10)
    my_slider.grid(row=0, column=0, pady=10, padx=10)

    #bursh slider label
    slider_label = Label(brush_size_frame, text=my_slider.get(), bg='lightgrey')
    slider_label.grid(row=0, column=1)

    #brush type
    brush_type_frame = Frame(brush_options_frame, height=200, bg='lightgrey')
    brush_type_frame.grid(row=0, column=1, padx=10)

    #create radio buttons for brush type
    brush_type_radio1 = Radiobutton(brush_type_frame, text='Slash', variable=brush_type, value='butt', bg='lightgrey', activebackground='lightgrey')
    brush_type_radio2 = Radiobutton(brush_type_frame, text='Round', variable=brush_type, value='round', bg='lightgrey', activebackground='lightgrey')
    brush_type_radio3 = Radiobutton(brush_type_frame, text='Diamond', variable=brush_type, value='projecting', bg='lightgrey', activebackground='lightgrey')

    #pack radio buttons
    brush_type_radio1.grid(row=0, column=0)
    brush_type_radio2.grid(row=0, column=1)
    brush_type_radio3.grid(row=0, column=2)

    #change colors
    change_colors_frame = Frame(brush_options_frame, bg='lightgrey')
    change_colors_frame.grid(row=0, column=2)

    #change bursh color button
    brush_color_button = Button(change_colors_frame, text='Brush color', bg='lightblue', bd=0, font=('Ubuntu', 11), command=change_brush_color)
    brush_color_button.config(activebackground='#6f97a3', activeforeground='white')
    brush_color_button.grid(row=0, column=0)

    #change background color 
    canvas_color_button = Button(change_colors_frame, text='Canvas color', bg='lightblue', bd=0, font=('Ubuntu', 11), command=change_canvas_color)
    canvas_color_button.config(activebackground='#6f97a3', activeforeground='white')
    canvas_color_button.grid(row=0, column=1)

    #clear screen button
    clear_button = Button(change_colors_frame, text='Clear screen', bg='lightblue', bd=0, font=('Ubuntu', 11), command=clear_screen)
    clear_button.config(activebackground='#6f97a3', activeforeground='white')
    clear_button.grid(row=0, column=2)

    #get help
    help_frame = Frame(brush_options_frame, bg='lightgrey')
    help_frame.grid(row=0, column=4)

    #help button
    help_button = Button(help_frame, text='Help',  bg='lightblue', bd=0, font=('Ubuntu', 11), activebackground='#6f97a3', activeforeground='white', command=help_show)
    help_button.grid(row=0, column=0)

    #about button
    about_button = Button(help_frame, text='About',  bg='lightblue', bd=0, font=('Ubuntu', 11), activebackground='#6f97a3', activeforeground='white', command=about_show)
    about_button.grid(row=0, column=1)

    #canvas
    my_canvas = Canvas(pwin, width=w, height=h, bg='white')
    my_canvas.pack(fill='both', expand=1)

    #bind a mouse to a canvas
    my_canvas.bind('<B1-Motion>', pain)

# TIC TAC TOE
def texits():
    ticroot.pack_forget()
    toolbar.pack_forget()
    root_window.pack_forget()

    Taskbar.pack(side='bottom')
    text_btn.config(state='active')
    activ_widgets()
    normal_menu()

def tictock():
    # Fullscreen window
    def full():
        tkcalendar.pack_forget()
        root_window.pack(expand=1, fill='both', padx=0, pady=0)
        full_btn.config(command=min)
        Taskbar.pack_forget()

    def min():
        window.pacK()
        full_btn.config(command=full)
        Taskbar.pack(side='bottom')

    global clicked, count, root_window, toolbar, ticroot
    global b1, b2, b3, b4, b5, b6, b7, b8, b9

    text_btn.config(state='disabled')

    # Main window
    text_btn.config(state='disabled')
    root_window = Frame(bg='white', bd=0, height=200, width=200)
    tkcalendar.pack_forget()
    root_window.pack(padx=35, pady=35, anchor='w')

    # Generate toolbar
    toolbar = Frame(root_window, bd=0, bg='lightgrey')
    toolbar.pack(fill='x', side='top', anchor='e')

    ticroot = Frame(root_window, bg='#daeced')
    ticroot.pack(fill='both', expand=1)

    # Grid Icons
    exit_btn = Button(toolbar, bg='lightgrey', activeforeground='white', fg='red', text=' X ', bd=0, font=('Helvetica', 13), activebackground='red', command=texits)
    exit_btn.grid(row=0, column=0, ipadx=5, ipady=5)

    # xm starts so true
    clicked = True
    count = 0

    def Reset():
        global b1, b2, b3, b4, b5, b6, b7, b8, b9
        global clicked, count, ticroot, toolbar
        clicked = True
        count = 0

        #confuring a bg
        b1.configure(text=" ")
        b2.configure(text=" ")
        b3.configure(text=" ")
        b4.configure(text=" ")
        b5.configure(text=" ")
        b6.configure(text=" ")
        b7.configure(text=" ")
        b8.configure(text=" ")
        b9.configure(text=" ")

        #confuring a bg
        b1.configure(bg="#daeced", bd=0)
        b2.configure(bg="#daeced", bd=0)
        b3.configure(bg="#daeced", bd=0)
        b4.configure(bg="#daeced", bd=0)
        b5.configure(bg="#daeced", bd=0)
        b6.configure(bg="#daeced", bd=0)
        b7.configure(bg="#daeced", bd=0)
        b8.configure(bg="#daeced", bd=0)
        b9.configure(bg="#daeced", bd=0)

        b1.config(state=ACTIVE)
        b2.config(state=ACTIVE)
        b3.config(state=ACTIVE)
        b4.config(state=ACTIVE)
        b5.config(state=ACTIVE)
        b6.config(state=ACTIVE)
        b7.config(state=ACTIVE)
        b8.config(state=ACTIVE)
        b9.config(state=ACTIVE)


    def disable_all_buttons():
        b1.config(state=DISABLED)
        b2.config(state=DISABLED)
        b3.config(state=DISABLED)
        b4.config(state=DISABLED)
        b5.config(state=DISABLED)
        b6.config(state=DISABLED)
        b7.config(state=DISABLED)
        b8.config(state=DISABLED)
        b9.config(state=DISABLED)

    #check to see if somone won
    def checkifwon():
        global winner
        winner = False

        if b1['text'] == "X" and b4['text'] == 'X' and b7 ['text'] == 'X':
            b1.config(bg="Light green")
            b4.config(bg="Light green")
            b7.config(bg="Light green")
            winner = True
            messagebox.showinfo("Winner", "CONGRATULATIONS!, X wins!")
            disable_all_buttons()

        elif b2['text'] == "X" and b5['text'] == 'X' and b8 ['text'] == 'X':
            b2.config(bg="Light green")
            b5.config(bg="Light green")
            b8.config(bg="Light green")
            winner = True
            messagebox.showinfo("Winner", "CONGRATULATIONS!, X wins!")
            disable_all_buttons()

        elif b3['text'] == "X" and b6['text'] == 'X' and b9 ['text'] == 'X':
            b3.config(bg="Light green")
            b6.config(bg="Light green")
            b9.config(bg="Light green")
            winner = True
            messagebox.showinfo("Winner", "CONGRATULATIONS!, X wins!")
            disable_all_buttons()

        elif b1['text'] == "X" and b5['text'] == 'X' and b9 ['text'] == 'X':
            b1.config(bg="Light green")
            b5.config(bg="Light green")
            b9.config(bg="Light green")
            winner = True
            messagebox.showinfo("Winner", "CONGRATULATIONS!, X wins!")
            disable_all_buttons()

        elif b3['text'] == "X" and b5['text'] == 'X' and b7 ['text'] == 'X':
            b3.config(bg="Light green")
            b5.config(bg="Light green")
            b7.config(bg="Light green")
            winner = True
            messagebox.showinfo("Winner", "CONGRATULATIONS!, X wins!")
            disable_all_buttons()

        elif b1['text'] == "X" and b2['text'] == 'X' and b3 ['text'] == 'X':
            b1.config(bg="Light green")
            b2.config(bg="Light green")
            b3.config(bg="Light green")
            winner = True
            messagebox.showinfo("Winner", "CONGRATULATIONS!, X wins!")
            disable_all_buttons()

        elif b4['text'] == "X" and b5['text'] == 'X' and b6['text'] == 'X':
            b4.config(bg="Light green")
            b5.config(bg="Light green")
            b6.config(bg="Light green")
            winner = True
            messagebox.showinfo("Winner", "CONGRATULATIONS!, X wins!")
            disable_all_buttons()

        elif b7['text'] == "X" and b8['text'] == 'X' and b9['text'] == 'X':
            b7.config(bg="Light green")
            b8.config(bg="Light green")
            b9.config(bg="Light green")
            winner = True
            messagebox.showinfo("Winner", "CONGRATULATIONS!, X wins!")
            disable_all_buttons()

        elif b1['text'] == "O" and b4['text'] == 'O' and b7 ['text'] == 'O':
            b1.config(bg="Light green")
            b4.config(bg="Light green")
            b7.config(bg="Light green")
            winner = True
            messagebox.showinfo("Winner", "CONGRATULATIONS!, O wins!")
            disable_all_buttons()

        elif b2['text'] == "O" and b5['text'] == 'O' and b8 ['text'] == 'O':
            b2.config(bg="Light green")
            b5.config(bg="Light green")
            b8.config(bg="Light green")
            winner = True
            messagebox.showinfo("Winner", "CONGRATULATIONS!, O wins!")
            disable_all_buttons()

        elif b3['text'] == "O" and b6['text'] == 'O' and b9 ['text'] == 'O':
            b3.config(bg="Light green")
            b6.config(bg="Light green")
            b9.config(bg="Light green")
            winner = True
            messagebox.showinfo("Winner", "CONGRATULATIONS!, O wins!")
            disable_all_buttons()

        elif b1['text'] == "O" and b5['text'] == 'O' and b9 ['text'] == 'O':
            b1.config(bg="Light green")
            b5.config(bg="Light green")
            b9.config(bg="Light green")
            winner = True
            messagebox.showinfo("Winner", "CONGRATULATIONS!, O wins!")
            disable_all_buttons()

        elif b3['text'] == "O" and b5['text'] == 'O' and b7 ['text'] == 'O':
            b3.config(bg="Light green")
            b5.config(bg="Light green")
            b7.config(bg="Light green")
            winner = True
            messagebox.showinfo("Winner", "CONGRATULATIONS!, O wins!")
            disable_all_buttons()

        elif b1['text'] == "O" and b2['text'] == 'O' and b3 ['text'] == 'O':
            b1.config(bg="Light green")
            b2.config(bg="Light green")
            b3.config(bg="Light green")
            winner = True
            messagebox.showinfo("Winner", "CONGRATULATIONS!, O wins!")
            disable_all_buttons()

        elif b4['text'] == "O" and b5['text'] == 'O' and b6['text'] == 'O':
            b4.config(bg="Light green")
            b5.config(bg="Light green")
            b6.config(bg="Light green")
            winner = True
            messagebox.showinfo("Winner", "CONGRATULATIONS!, O wins!")
            disable_all_buttons()

        elif b7['text'] == "O" and b8['text'] == 'O' and b9['text'] == 'O`':
            b7.config(bg="Light green")
            b8.config(bg="Light green")
            b9.config(bg="Light green")
            winner = True
            messagebox.showinfo("Winner", "CONGRATULATIONS!, O wins!")
            disable_all_buttons()

        elif count == 9 and winner == False:
            messagebox.showinfo("Winner", "It is a tie!\nno one wins, try starting a new match")
            disable_all_buttons()

    def b_click(b):
        global clicked, count

        if b["text"] == " " and clicked == True:
            b["text"] = 'X'
            clicked = False
            count += 1
            checkifwon()
        elif b["text"] == " " and clicked == False:
            b["text"] = 'O'
            clicked = True
            count += 1
            checkifwon()
        else:
            messagebox.showerror("Error", "That box has already been used \nUse another box")

    #buttons
    b1 = Button(ticroot, text=" ", font=("Arial", 20), height=3, width=6, bg="#daeced",command= lambda: b_click(b1))
    b2 = Button(ticroot, text=" ", font=("Arial", 20), height=3, width=6, bg="#daeced",command= lambda: b_click(b2))
    b3 = Button(ticroot, text=" ", font=("Arial", 20), height=3, width=6, bg="#daeced",command= lambda: b_click(b3))

    b4 = Button(ticroot, text=" ", font=("Arial", 20), height=3, width=6, bg="#daeced",command= lambda: b_click(b4))
    b5 = Button(ticroot, text=" ", font=("Arial", 20), height=3, width=6, bg="#daeced",command= lambda: b_click(b5))
    b6 = Button(ticroot, text=" ", font=("Arial", 20), height=3, width=6, bg="#daeced",command= lambda: b_click(b6))

    b7 = Button(ticroot, text=" ", font=("Arial", 20), height=3, width=6, bg="#daeced",command= lambda: b_click(b7))
    b8 = Button(ticroot, text=" ", font=("Arial", 20), height=3, width=6, bg="#daeced",command= lambda: b_click(b8))
    b9 = Button(ticroot, text=" ", font=("Arial", 20), height=3, width=6, bg="#daeced",command= lambda: b_click(b9))

    def about_command():
        messagebox.showinfo("About", 'tic tac toe is a simple tic tac toe game made by izkaan and dad python productions®')

    def show_help_command():
        messagebox.showinfo('Help', "Mail izooizkaan@gmail.com for help")

    #grid buttons
    b1.grid(row=0, column=0)
    b2.grid(row=0, column=1)
    b3.grid(row=0, column=2)

    b4.grid(row=1, column=0)
    b5.grid(row=1, column=1)
    b6.grid(row=1, column=2)

    b7.grid(row=2, column=0)
    b8.grid(row=2, column=1)
    b9.grid(row=2, column=2)

    #confuring a bg
    b1.configure(bg="#daeced", bd=0)
    b2.configure(bg="#daeced", bd=0)
    b3.configure(bg="#daeced", bd=0)
    b4.configure(bg="#daeced", bd=0)
    b5.configure(bg="#daeced", bd=0)
    b6.configure(bg="#daeced", bd=0)
    b7.configure(bg="#daeced", bd=0)
    b8.configure(bg="#daeced", bd=0)
    b9.configure(bg="#daeced", bd=0)

    # Reload button
    res_btn = Button(toolbar, bg='lightgrey', fg='black', text='Tic Tac Toe', bd=0, font=('Helvetica', 13), activebackground='lightgrey', command=Reset)
    res_btn.grid(row=0, column=2, padx=5, pady=5)

# Menu bar
def normal_menu():
    global normalMenubar, main_menu
    # Normal menubar
    normalMenubar = Menu(root)
    root.config(menu=normalMenubar)

    # Options
    main_menu = Menu(normalMenubar, tearoff=0, activebackground='lightblue', activeforeground='black')
    normalMenubar.add_cascade(label="Workspace", menu=main_menu)
    main_menu.add_command(label="Open file", command=openfile)
    main_menu.add_command(label="View source code", command=view_source_code)
    main_menu.add_separator()
    main_menu.add_command(label="Activate Widgets", command=activ_widgets)
    main_menu.add_command(label="Disable Widgets", command=disl_widget)
    main_menu.add_separator()
    main_menu.add_command(label="Bright theme", command=bright_mode)
    main_menu.add_command(label="Deafult theme", command=deafult_mode)
    main_menu.add_command(label="Dark theme", command=dark_mode)
    main_menu.add_separator()
    main_menu.add_command(label="Exit workspace", command=exit_app)

    # Program
    program_menu = Menu(normalMenubar, tearoff=0, activebackground='lightblue', activeforeground='black')
    normalMenubar.add_cascade(label="Programs", menu=program_menu)
    program_menu.add_command(label="Windows settings", command=lambda:os.popen('start ms-settings:'))
    program_menu.add_command(label="Microsoft Edge", command=lambda:os.popen('start msedge'))
    program_menu.add_command(label="Google Chrome", command=lambda:os.popen("start chrome"))
    program_menu.add_separator()
    program_menu.add_command(label="Github Atom", command=lambda:os.popen("start atom"))
    program_menu.add_command(label="Sublime Text", command=lambda:os.popen("\"C:\Program Files\Sublime Text 3\sublime_text.exe\""))
    program_menu.add_separator()
    program_menu.add_command(label="Windows Terminal", command=lambda:os.popen("start wt"))
    program_menu.add_command(label="Command Prompt", command=lambda:os.popen("start cmd.exe"))
    program_menu.add_command(label="Python Intepreter", command=lambda:os.popen("start py"))
    program_menu.add_separator()
    program_menu.add_command(label="Windows PowerShell", command=lambda:os.popen("start powershell.exe"))
    program_menu.add_command(label="Windows PowerShell ISE", command=lambda:os.popen("start powershell_ise.exe"))
    program_menu.add_command(label="Windows PowerShell 7", command=lambda:os.popen("start pwsh.exe"))

    # Amazing
    software_menu = Menu(normalMenubar, tearoff=0, activebackground='lightblue', activeforeground='black')
    normalMenubar.add_cascade(label="Workspace Software", menu=software_menu)
    software_menu.add_command(label="Basic Text", command=lambda:Text_editor())
    software_menu.add_command(label="Tic Tac Toe", command=lambda:tictock())
    software_menu.add_command(label='Paint App', command=lambda:PaintApp())

    # Short cut menu
    short_menu = Menu(normalMenubar, tearoff=0, activebackground='lightblue', activeforeground='black')
    normalMenubar.add_cascade(label="Shortucts", menu=short_menu)
    short_menu.add_command(label="Google", command=lambda:os.system(r'start https:\\google.com'))
    short_menu.add_command(label="Gmail", command=lambda:os.system(r'start https:\\gmail.com'))
    short_menu.add_command(label="Meet", command=lambda:os.system(r'start https:\\meet.google.com'))
    short_menu.add_command(label="Youtube", command=lambda:os.system(r'start https:\\Youtube.com'))
    short_menu.add_command(label="Google Drive", command=lambda:os.system(r'start https:\\drive.google.com'))

    # View menu
    view_menu = Menu(normalMenubar, tearoff=0, activebackground='lightblue', activeforeground='black')
    normalMenubar.add_cascade(label="View", menu=view_menu)
    view_menu.add_command(label="Fullscreen", command=lambda:root.attributes('-fullscreen', True))
    view_menu.add_command(label="Exit fullscreen", command=lambda:root.attributes('-fullscreen', False))
    view_menu.add_separator()
    view_menu.add_command(label="Mazimize window", command=lambda:root.state('zoomed'))
    view_menu.add_command(label="Minimize window", command=root.iconify)
    view_menu.add_separator()
    view_menu.add_command(label="Hide dock", command=lambda:Taskbar.pack_forget())
    view_menu.add_command(label="Show dock", command=lambda:Taskbar.pack(side='bottom'))

    # Help menu
    help_menu = Menu(normalMenubar, tearoff=0, activebackground='lightblue', activeforeground='black')
    normalMenubar.add_cascade(label="Help", menu=help_menu)
    help_menu.add_command(label="About workspace", command=about_cmd)
    help_menu.add_command(label="Report bug", command=lambda:webbrowser.open("mailto:pycodes.10@gmail.com", new=1))

# Widgets
activewidgets = open(r"Config\activeWidgets.cnf")
activewidgets = activewidgets.read()

# calendar
root.style = ttk.Style()
root.style.theme_use("clam")

tkcalendar = Calendar(root, background="lightblue", disabledbackground="lightblue", bordercolor="lightblue", bd=0,
               headersbackground="lightblue", normalbackground="lightblue", foreground='Black',
               normalforeground='Black', headersforeground='Black')

#if (tkcalendar.get_date())

# Display if ALLOWED
if (activewidgets == "FALSE"):
    tkcalendar.pack_forget()

if (activewidgets == "TRUE"):
    tkcalendar.pack(anchor='nw', pady=15, padx=15)

# Exit Basic text application
def exits():
    ROOT.pack_forget()
    Taskbar.pack(side='bottom')
    text_btn.config(state='active')
    activ_widgets()
    normal_menu()

# Size window
def mixode():
    ROOT.pack(fill='both', expand=1, padx=35, pady=35)
    Taskbar.pack(side='bottom')
    txtel.config(command=mazow)

# Basic text new file
def new_txt():
    ask1 = messagebox.askyesno("Warning", "Save current changes?", icon='warning')

    if (ask1 == True):
        Textbox.delete(1.0, END)
        details.pack(side='left', ipady=3, ipadx=3, fill='x')
        details.config(text='New file')
# Open file
def open_txt():

    global filename
    # Get file
    filename = filedialog.askopenfilename(title='Select file to open', initialdir='C:\\')
    filename = ''.join(filename)

    # Open file
    try:
        if (filename != ""):
            content = open(filename, encoding='utf8')
            content_txt = content.read()
            Textbox.delete(1.0, END)
            Textbox.insert(1.0, content_txt)

            # Update details panel
            details.pack(side='left', ipady=3, ipadx=3, fill='x')
            details.config(text=f'Opened "{filename}"')

    except Exception as err:
        messagebox.showerror("Error", f'The following error occoured in PROCESS_OPEN:\n{err}')

# Basic text application
def Text_editor():
    # Save file
    def save_txt():
        try:
            # Get text and filename
            global content_str
            content_str = Textbox.get(1.0, END)

            # Write to filename
            open_filename = open(filename, mode='w', encoding='utf8')
            open_filename.write(content_str)
            open_filename.close()

            # Update details panel
            details.pack(side='left', ipady=3, ipadx=3, fill='x')
            details.config(text=f'Saved {filename} sucsessfully')
            details.after(5000, lambda:details.pack_forget())

        except NameError:
            messagebox.showinfo("Error", "Please open a file before attempting to save it.")
        except Exception as exceptiontk:
            messagebox.showerror('Error', f"We ran into the following error:\n{exceptiontk}")

    # Save as file
    def save_as_txt():
        # Get file name, directory
        savefilemsg = filedialog.asksaveasfilename(title='Type filename to save', initialdir='C:\\')
        savefilemsg = ''.join(savefilemsg)

        # Make file
        try:
            if (savefilemsg != ""):
                os.system(f'touch "{savefilemsg}"')

                with open(savefilemsg, 'w') as file:
                    # Write to file
                    file.write(Textbox.get(1.0, END))
                    file.close()

        except Exception as err__:
            print(err__)
            messagebox.showerror("Error", f'The following error occoured in PROCESS_SAVE_AS:\n{err__}')

    # Increase font size
    def increasefont():
        global font_size
        font_size += 3
        Textbox.config(font=("ubuntu", font_size))

    # Less font Size
    def lesssfont():
        global font_size
        font_size -= 3
        Textbox.config(font=("ubuntu", font_size))

    # Contact developer
    def contanct(): webbrowser.open("mailto:pycodes.10@gmail.com")

    global ROOT, txtel, Textbox, details, content_str, toolbar
    # Hide <widgets> and the <dock>
    tkcalendar.pack_forget()

    # Disbale MORE window openings
    text_btn.config(state='disabled')

    # Main root
    ROOT = Frame(bg='white', bd=0)
    ROOT.pack(fill='both', expand=1, padx=35, pady=35)

    # Exit application
    toolbar = Frame(ROOT, bd=0, bg='lightgrey')
    toolbar.pack(fill='x', side='top')

    # Exit button
    exit_btn = Button(toolbar, text=' X ', font=('ubuntu', 14), bg='lightgrey', fg='red', bd=0, activebackground='red', activeforeground='lightgrey', command=lambda:exits())
    exit_btn.pack(side='right')

    txtel = Label(toolbar, text='  Basic text', justify='center', fg='black', font=("ubuntu", 14), bg='lightgrey')
    txtel.pack(pady=(2, 0))

    # Basic text menubar
    basicMenu = Menu(root)
    root.config(menu=basicMenu)

    # File menu
    text_menu = Menu(basicMenu, tearoff=0, activebackground='lightblue', activeforeground='black')
    basicMenu.add_cascade(label="File", menu=text_menu)
    text_menu.add_command(label="New", command=new_txt)
    text_menu.add_command(label="Open", command=open_txt)
    text_menu.add_command(label="Save", command=save_txt)
    text_menu.add_command(label="Save As", command=save_as_txt)
    text_menu.add_separator()
    text_menu.add_command(label="Exit", command=exits)

    # Editor menu
    edit_menu = Menu(basicMenu, tearoff=0, activebackground='lightblue', activeforeground='black')
    basicMenu.add_cascade(label="Edit", menu=edit_menu)
    edit_menu.add_command(label="Undo", command=lambda:Textbox.event_generate("<<Undo>>"), accelerator='Ctrl+z')
    edit_menu.add_command(label="Redo", command=lambda:Textbox.event_generate("<<Redo>>"), accelerator='Ctrl+y')
    edit_menu.add_separator()
    edit_menu.add_command(label="Cut", command=lambda:Text(False), accelerator="Ctrl+x")
    edit_menu.add_command(label="Copy", command=lambda:Textbox.event_generate("<<Copy>>"), accelerator='Ctrl+c')
    edit_menu.add_command(label="Paste", command=lambda:Textbox.event_generate("<<Paste>>"), accelerator='Ctrl+v')
    edit_menu.add_command(label="Select all", command=lambda:Textbox.tag_add('sel', '1.0', 'end-1c'), accelerator='Ctrl+a')

    # View menu
    view_menu = Menu(basicMenu, tearoff=0, activebackground='lightblue', activeforeground='black')
    basicMenu.add_cascade(label="View", menu=view_menu)

    view_menu.add_command(label="Zoom in", command=increasefont)
    view_menu.add_command(label="Zoom out", command=lesssfont)

    # Help menu
    help_Menu = Menu(basicMenu, tearoff=0, activebackground='lightblue', activeforeground='black')
    basicMenu.add_cascade(label="Help", menu=help_Menu)
    help_Menu.add_command(label="About", command=lambda:messagebox.showinfo("About", 'Basic text - Version 1.0\nIncluded with workspace\nMade by IPP'))
    help_Menu.add_command(label="Contact developer", command=contanct)

    # Body
    body = Frame(ROOT, bg='white', bd=0)
    body.pack(expand=1, fill='both', side='top')

    # Config
    details = Label(ROOT, bd=0, bg='lightgrey', fg='black', font=("ubuntu", 11), text='New file')
    details.pack(side='left', ipady=3, ipadx=3, fill='x')

    # Text input box
    Textbox = Text(body, bd=0, bg='white', fg='black', font=("ubuntu", font_size), selectbackground='lightgrey', selectforeground='black', wrap=WORD, undo=True)
    Textbox.pack(expand=1, fill='both', pady=7, padx=7)

    # Get content
    content_str = Textbox.get("1.0", "end")

# Define toolbar menu
toolbar_menu = Menu(root, tearoff=0, activebackground='lightblue', activeforeground='black')
toolbar_menu.add_command(label="Close window", command=openfile)

# Bind rightclick menu to <toolbar>
def toolbar_bind(event):
    try: toolbar_menu.tk_popup(event.x_root, event.y_root)
    finally: toolbar_menu.grab_release()

# Set icons
chrome_icon = Image.open(r"Icons\chrome.png")
chrome_icon = chrome_icon.resize((35, 35))
chrome_icon = ImageTk.PhotoImage(chrome_icon)

# Python icon
py_icon = Image.open(r"Icons\python.png")
py_icon = py_icon.resize((35, 35))
py_icon = ImageTk.PhotoImage(py_icon)

# Explorer icon
explorer_icon = Image.open(r"Icons\explorer.png")
explorer_icon = explorer_icon.resize((35, 35))
explorer_icon = ImageTk.PhotoImage(explorer_icon)

# Atom icon
atom_icon = Image.open(r"Icons\atom.png")
atom_icon = atom_icon.resize((35, 35))
atom_icon = ImageTk.PhotoImage(atom_icon)

# Terminal icon
terminal_icon = Image.open(r"Icons\terminal.png")
terminal_icon = terminal_icon.resize((35, 35))
terminal_icon = ImageTk.PhotoImage(terminal_icon)

# Text editor icon
text_icon = Image.open(r"Icons\texteditor.png")
text_icon = text_icon.resize((35, 35))
text_icon = ImageTk.PhotoImage(text_icon)

# Settings icon
gear_icon = Image.open(r"Icons\gear.png")
gear_icon = gear_icon.resize((35, 35))
gear_icon = ImageTk.PhotoImage(gear_icon)

# Taskbar
Taskbar = Frame(root, bg='lightgrey', bd=0)
Taskbar.pack(side='bottom')

# Add area
fnx = Label(Taskbar, bg='lightgrey', font=('ubuntu', 17), text=' ')
fnx.grid(row=0, column=0, pady=7)

# Chrome button
chrome_btn = Button(Taskbar, bg='lightgrey', fg='black', activebackground='lightgrey', activeforeground='black', font=('ubuntu', 17), image=chrome_icon, bd=0, command=lambda:os.popen("start chrome"))
chrome_btn.grid(row=0, column=1, pady=7, padx=7)

# File explorer button
explorer_btn = Button(Taskbar, bg='lightgrey', fg='black', activebackground='lightgrey', activeforeground='black', font=('ubuntu', 17), image=explorer_icon, bd=0, command=lambda:os.popen("start explorer.exe"))
explorer_btn.grid(row=0, column=2, pady=7, padx=7)

# Atom button
atom_btn = Button(Taskbar, bg='lightgrey', fg='black', activebackground='lightgrey', activeforeground='black', font=('ubuntu', 17), image=atom_icon, bd=0, command=lambda:os.popen("start atom.exe"))
atom_btn.grid(row=0, column=3, pady=7, padx=7)

# Settings button
setting_btn = Button(Taskbar, bg='lightgrey', fg='black', activebackground='lightgrey', activeforeground='black', font=('ubuntu', 17), image=gear_icon, bd=0, command=lambda:os.popen("start ms-settings:"))
setting_btn.grid(row=0, column=4, pady=7, padx=7)

# Windows terminal
terminal_btn = Button(Taskbar, bg='lightgrey', fg='black', activebackground='lightgrey', activeforeground='black', font=('ubuntu', 17), image=terminal_icon, bd=0, command=lambda:os.popen("start wt.exe"))
terminal_btn.grid(row=0, column=5, pady=7, padx=7)

# Basic text button
text_btn = Button(Taskbar, bg='lightgrey', fg='black', activebackground='lightgrey', activeforeground='black', font=('ubuntu', 17), image=text_icon, bd=0, command=lambda:Text_editor())
text_btn.grid(row=0, column=6, pady=7, padx=7)

# Python button
py_btn = Button(Taskbar, bg='lightgrey', fg='black', activebackground='lightgrey', activeforeground='black', font=('ubuntu', 17), image=py_icon, bd=0, command=lambda:os.popen("start py"))
py_btn.grid(row=0, column=7, pady=7, padx=7)

twd = Label(Taskbar, bg='lightgrey', font=('ubuntu', 17), text=' ')
twd.grid(row=0, column=8, pady=7)

# Bind <rightclickmenu>
def do_popup(event):
    try: main_menu.tk_popup(event.x_root, event.y_root)
    finally: main_menu.grab_release()

if __name__ == '__main__':
    # Commandline arguments
    try:
        argskw = sys.argv
        argskw.pop(0)

        print(argskw)

        # Fullscreen
        if ("-f" in argskw): root.attributes('-fullscreen', True)

        # About
        if ("-a" in argskw): about_cmd()

        # Source code
        if ("-s" in argskw): view_source_code()

    except IndexError: pass

    # On exit
    def exit_app():
        # App exec
        soundActive = open(f"Config\soundName.cnf")
        soundActive = soundActive.read()

        if soundActive == "TRUE":
            try:
                sound_name = open(f"Config\Sounds\logoffSound.cnf")
                sound_name = sound_name.read()

                pygame.mixer.init()
                pygame.mixer.music.load(f'Sounds\{sound_name}')
                pygame.mixer.music.play(loops=0)
                root.after(3000, root.quit)

            except Exception:
                messagebox.showerror('Error', f"The file {sound_name} does not exist.")
                root.quit()

        else: root.quit()

root.protocol("WM_DELETE_WINDOW", exit_app)

# Bind keys
root.bind("<Button-3>", do_popup)
try: toolbar.bind("<Button-3>", toolbar_bind)
except: pass

normal_menu()
root.mainloop()
