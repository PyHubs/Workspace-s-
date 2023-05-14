# -*- coding: utf-8 -*-
from tkinter import *
from tkinter import ttk
from tkcalendar import *
from tkinter import filedialog
from tkinter import messagebox
from PIL import ImageTk, Image
import os, center_tk_window, sys, pygame, webbrowser

"""
This an legit program developed by IPP
Open source, free to fork
"""

# Window
root = Tk()
root.title("Workspace UX for windows")
root.geometry('')
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
- Ahmed shareef (Assistant, tester)
- Kayan (Adverisitng assistant)

All credits of the UI and application developemenent goes to izkaan while some suggestions and bugs were found by ahmed shareef, and kayan was the contributor of the advertisement video.

The contribution numbers will be Izkaan 65%, Shareef 30% and Kayan 5%.
Concept of workspace was also developed by izkaan, founder of IPP, And asic text lite was 95% izkaan and 5% shareef"

"""

if SPECM == "$SEE_PEOPLE_WHO_MADE_IT_GOOD.REAL":
    messagebox.showinfo(r"The people", people_str)

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
about_txt = """\n:-) Workspace UX for windows
    -------------------------------------------------------------------------------------------

    IPP Workspace
    Version UX (Build UX-DEV-7121Rm)
    Milestone 4.3x Build, offical milestone update
    IPP Workspace ® Codename ® Cornflakes

    © 2021 Izkaan Python Productions. All rights reserved

    The code for "Workspace" shall NOT be distributed illegally.
    This product is licensed under the MIT license OFFICALLY.
    This is also a developement build, not for public.
"""

about_config = """:-) Workpace UX Help - Config

    The "Config\\" directory is one of the key structers and requirements for IPP Workspace UX to work. To locate it go to the home (Workspace-UX folder) and cd to config.

    The "Config\\" directory inclues all the CONFIG files (.cnf files). Config files are files that allow you to change settings in workspace. For an example if you want to set moutain.png as your background, you will have to use config on a fresh install of Workspace UX (as deafult.png is the deafult background image). To change the background images, open "Config\\soundName.cnf" and type the image name.

* sidenote : The image HAS to be uploaded or in the "Images\\" directory, and NO EXTRA LINES after the filename should be added, or an error will occour.

    - Config filename and its action
    activeWidgets > Set widget state as active (TRUE) or disabled (FALSE)
    soundName > Set logon/logoff sounds to play (TRUE) or not to be played (FALSE)
    imageName > Type the image name to display as the deafult background
    logonSound > Set the custom logon sound file
    logoff sound > Set the custom logoff sound file
"""

# About workspace
def about_cmd():
    # About window
    about_win = Toplevel()
    about_win.title("About - Workspace UX for windows")
    about_win.geometry('600x350')
    about_win.config(bg='#f0f0f0')
    about_win.resizable(0, 0)
    center_tk_window.center_on_screen(about_win)

    # Display about text
    about_label = Text(about_win, font=('Helvetica', 13), selectbackground='#f0f0f0', selectforeground='black', bd=0, wrap=WORD, bg='#f0f0f0')
    about_label.insert('1.0', about_txt)
    about_label.pack(expand=1, fill='both', pady=2, padx=2)
    about_label.config(state="disabled")

    # Tag
    about_label.tag_add("start", "2.0", "2.30")
    about_label.tag_config("start", font=('Helvetica', 20), justify='center', foreground='#0077c8')

# Open file
def openfile():
    filename = filedialog.askopenfilename(initialdir='C:\\', title='Select file to open')
    filename = ''.join(filename)
    os.popen(filename)

# View source code
def view_source_code():
    # Source code window
    srcwin = Toplevel()
    srcwin.title("Workspace UX for windows - Source code (Application.py)")
    srcwin.geometry('500x265')
    srcwin.config(bg='white')
    center_tk_window.center_on_screen(srcwin)

    # Get source code
    src_code = open("Application.py", "r")
    src_code = src_code.read()

    # Define scrollbar
    scrollbar = Scrollbar(srcwin)
    scrollbar.pack(side=RIGHT, fill=Y)

    # Display source Recorder
    src_code_label = Text(srcwin, font=('Monospace', 12), selectbackground='lightblue', selectforeground='black', bd=0)
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
    tkcalander.pack(anchor='nw', pady=15, padx=15)
    sir_frame.pack(anchor='nw', pady=15, padx=15)
    tktext.pack()

# Disable widgets
def disl_widget():
    file = open(r"Config\activeWidgets.cnf", 'w')
    file.write("FALSE")
    tkcalander.pack_forget()
    sir_frame.pack_forget()
    tktext.pack_forget()

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
    main_menu.add_command(label="Exit workspace", command=exit_app)

    # Program
    program_menu = Menu(normalMenubar, tearoff=0, activebackground='lightblue', activeforeground='black')
    normalMenubar.add_cascade(label="Programs", menu=program_menu)
    program_menu.add_command(label="Microsoft edge", command=openfile)
    program_menu.add_command(label="Google chrome", command=lambda:os.popen("start chrome"))
    program_menu.add_command(label="Windows explorer", command=lambda:os.popen("start msedge"))
    program_menu.add_command(label="Github atom", command=lambda:os.popen("start atom"))
    program_menu.add_command(label="Windows terminal", command=lambda:os.popen("start wt"))
    program_menu.add_command(label="Basic text [LITE]", command=lambda:Text_editor())

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
    help_menu.add_command(label="Version info", command=lambda:messagebox.showinfo("Version info - Workspace", "IPP Workspace Codename Cornflakes\nBuild number 7121Rm\nPublic offical build"))
    help_menu.add_command(label="Report bug", command=lambda:webbrowser.open("mailto:izooizkaan@outlook.com", new=1))

# Widgets
activewidgets = open(r"Config\activeWidgets.cnf")
activewidgets = activewidgets.read()

# Calander
root.style = ttk.Style()
root.style.theme_use("clam")

tkcalander = Calendar(root, background="lightblue", disabledbackground="lightblue", bordercolor="lightblue", bd=0,
               headersbackground="lightblue", normalbackground="lightblue", foreground='Black',
               normalforeground='Black', headersforeground='Black')

#if (tkcalander.get_date())

# Text widget
sir_frame = Frame(bd=0, bg='#e4f9e0')
tktext = Text(sir_frame, height=10, width=29, bg='#e4f9e0', fg='black', font=("Arial", 11), selectbackground='lightgrey', selectforeground='black', wrap=WORD)

# Add scrollbar
sprint = Scrollbar(sir_frame)
sprint.pack(side=RIGHT, fill=Y)
tktext.config(yscrollcommand=sprint.set)
sprint.config(command=tktext.yview)

# Display if ALLOWED
if (activewidgets == "FALSE"):
    sir_frame.pack_forget()
    tktext.pack_forget()
    tkcalander.pack_forget()

if (activewidgets == "TRUE"):
    tkcalander.pack(anchor='nw', pady=15, padx=15)
    sir_frame.pack(anchor='nw', pady=15, padx=15)
    tktext.pack()

# Exit basic text application
def exits():
    ROOT.pack_forget()
    Taskbar.pack(side='bottom')
    text_btn.config(state='active')
    activ_widgets()
    normal_menu()

# Makesize basic text window
def mazow():
    ROOT.pack_forget()
    ROOT.pack(expand=1, fill='both', pady=0, padx=0)
    Taskbar.pack_forget()
    txtel.config(command=mixode)

# Size window
def mixode():
    ROOT.pack(fill='both', expand=1, padx=35, pady=35)
    Taskbar.pack(side='bottom')
    txtel.config(command=mazow)

# Basic Text new file
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

# basic text application
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
        Textbox.config(font=("Helvetica", font_size))

    # Less font Size
    def lesssfont():
        global font_size
        font_size -= 3
        Textbox.config(font=("Helvetica", font_size))

    # Contact developer
    def contanct(): webbrowser.open("mailto:izooizkaan@outlook.com")

    global ROOT, txtel, Textbox, details, content_str
    # Hide <widgets> and the <dock>
    tkcalander.pack_forget()
    sir_frame.pack_forget()
    tktext.pack_forget()

    # Disbale MORE window openings
    text_btn.config(state='disabled')

    # Main root
    ROOT = Frame(bg='white', bd=0)
    ROOT.pack(fill='both', expand=1, padx=35, pady=35)

    # Exit application
    toolbar = Frame(ROOT, bd=0, bg='#637980')
    toolbar.pack(fill='x', side='top')

    # Exit button
    exit_btn = Button(toolbar, text='  X  ', font=('Helvetica', 14), bg='#637980', fg='white', bd=0, activebackground='red', activeforeground='white', command=lambda:exits())
    exit_btn.grid(row=0, column=0)

    txtel = Button(toolbar, text='Basic text [LITE]', justify='center', fg='white', font=("Helvetica", 14), bg='#637980', bd=0, activebackground='#637980', activeforeground='white', command=lambda:mazow())
    txtel.grid(row=0, column=1)

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
    help_Menu.add_command(label="About", command=lambda:messagebox.showinfo("About", 'Basic Text Lite - Version 1.0\nIncluded with workspace\nMade by IPP'))
    help_Menu.add_command(label="Contact developer", command=contanct)

    # Body
    body = Frame(ROOT, bg='white', bd=0)
    body.pack(expand=1, fill='both', side='top')

    # Config
    details = Label(ROOT, bd=0, bg='lightgrey', fg='black', font=("Helvetica", 11), text='New file')
    details.pack(side='left', ipady=3, ipadx=3, fill='x')

    # Text input box
    Textbox = Text(body, bd=0, bg='white', fg='black', font=("Helvetica", font_size), selectbackground='lightgrey', selectforeground='black', wrap=WORD, undo=True)
    Textbox.pack(expand=1, fill='both', pady=5, padx=5)

    # Get content
    content_str = Textbox.get("1.0", "end")

# Taskbar
Taskbar = Frame(root, bg='lightgrey', bd=0)
Taskbar.pack(side='bottom')

# Key button
key_btn = Button(Taskbar, bg='lightgrey', fg='black', activebackground='lightgrey', activeforeground='black', font=('Helvetica', 17), text=' :-) ', bd=0)
key_btn.grid(row=0, column=0, pady=5)

# Edge button
edge_btn = Button(Taskbar, bg='lightgrey', fg='black', activebackground='lightgrey', activeforeground='black', font=('Helvetica', 17), text='Edge', bd=0, command=lambda:os.popen("start msedge"))
edge_btn.grid(row=0, column=1, pady=5)

# Chrome button
chrome_btn = Button(Taskbar, bg='lightgrey', fg='black', activebackground='lightgrey', activeforeground='black', font=('Helvetica', 17), text='Chrome', bd=0, command=lambda:os.popen("start chrome"))
chrome_btn.grid(row=0, column=2, pady=5)

# File explorer button
explorer_btn = Button(Taskbar, bg='lightgrey', fg='black', activebackground='lightgrey', activeforeground='black', font=('Helvetica', 17), text='Explorer', bd=0, command=lambda:os.popen("start explorer.exe"))
explorer_btn.grid(row=0, column=3, pady=5)

# Atom button
atom_btn = Button(Taskbar, bg='lightgrey', fg='black', activebackground='lightgrey', activeforeground='black', font=('Helvetica', 17), text='Atom', bd=0, command=lambda:os.popen("start atom.exe"))
atom_btn.grid(row=0, column=4, pady=5)

# Windows terminal
explorer_btn = Button(Taskbar, bg='lightgrey', fg='black', activebackground='lightgrey', activeforeground='black', font=('Helvetica', 17), text='Terminal', bd=0, command=lambda:os.popen("start wt.exe"))
explorer_btn.grid(row=0, column=5, pady=5)

# Basic text button
text_btn = Button(Taskbar, bg='lightgrey', fg='black', activebackground='lightgrey', activeforeground='black', font=('Helvetica', 17), text='Basic-Text', bd=0, command=lambda:Text_editor())
text_btn.grid(row=0, column=6, pady=5)

# Minimize taskbar button
mint_btn = Button(Taskbar, bg='lightgrey', fg='black', activebackground='lightgrey', activeforeground='black', font=('Helvetica', 17), text='- ', bd=0, command=lambda:Taskbar.pack_forget())
mint_btn.grid(row=0, column=7, pady=5)

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
root.bind("<Button-3>", do_popup)
normal_menu()
root.mainloop()
