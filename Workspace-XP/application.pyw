# -*- coding: utf-8 -*-
from pickle import POP
from tkinter import *
import tkinter as tk
from tkinter import ttk
from subprocess import *
from tkcalendar import *
import tkinter.ttk as ttk
from random import randint
from functools import partial
from PIL import ImageTk, Image
from tkinter import filedialog, messagebox, colorchooser
import os, center_tk_window, sys, webbrowser, time, psutil, pyttsx3, random
from tools_xp import cwindow, dwindow, messagebox_info, messagebox_error, messagebox_warning
from subprocess import Popen, run, STDOUT, PIPE
from tkcode import CodeEditor
from customtkinter import CTkFrame

# Main Window
root = Tk()
root.title("Workspace XP")
root.geometry("1020x500")
root.config(bg='lightblue')
root.iconbitmap("logo.ico")

# Ex full screen
def exit_view(viewbtn):
	root.attributes('-fullscreen', False)	
	viewbtn.config(command=lambda:full_view(viewbtn), text='FullScreen')

# Full screen
def full_view(viewbtn):
	root.attributes('-fullscreen', True)
	viewbtn.config(command=lambda:exit_view(viewbtn), text='Exit FullScreen')

# Exit program
def workspace_exit():
	root.destroy()

# Exit start menu
def startoof(start_frame):
	start_frame.pack_forget()
	start.config(comman=startmenu)

# About text
about_txt = """\nIPP Workspace XP

	Version XP DAP (Build XP-DEV-112721D)
	IPP Workspace ® Codename ® eXPerience

	2021/2022 Izkaan Python Productions. 
	Please give me credit. Else i will get sad, and email you a virus

	# -- NEW FEATURES -- #
	- Re-written kernal
	- New GUI (hope you all xp fans are happy)
	- Text Editor XP
	- Calculator
	- Rock Paper Scissors (With AI)
	
	# -- VERSION TWO (DAP: Da App Update) -- #
	- MaterialCode
	- Place2D
	- More bugs

	If this gets traction, i will allow 3rd party softwares easy developement :)
"""

# Exit about_workspace
def about_exit():
	about_win.pack_forget()

def tedit_exit():
	tedit_win.pack_forget()

# eee
def tmrf():
	# Return a frame window
	tmrw = Frame(bd=0, bg='#0C0C0C')
	tmrw.pack(padx=50, pady=37)

	# Toolbar
	toolbar = Frame(tmrw, bg='#2259E1', bd=0)
	toolbar.pack(side='top', fill='x')

	# Exit button
	exit_btn = Button(toolbar, bd=0, text=' ✕ ', fg='white', bg='#FF4900', font=("ubuntu", 10), activebackground='#FF4900', activeforeground='white', command=lambda:tmrw.pack_forget())
	exit_btn.pack(side='right')

	# Toolbar text
	toolbartext = Label(toolbar, bd=0, text='Rock Paper Scissors', font=('ubuntu', 12), bg='#2259E1', fg='white')
	toolbartext.pack(ipady=1)

	# Sidebar one
	cframe = Frame(tmrw, bg='#323232')
	cframe.pack(side='top', fill='x')

	rock_ =1
	paper_ = 2
	scissor_ = 3

	def rpc(opt):
		print(opt)
		# THIS IS THE AI LOL
		AI = random.randint(1, 3)

		if opt == 1 and AI == 1: iid.config(text='Rock + Rock = TIE', bg='lightgrey')
		elif opt == 1 and AI == 2: iid.config(text='Rock + Paper = You Win', bg='green')
		elif opt == 1 and AI == 3: iid.config(text='Rock + Scissor = You Win', bg='green')

		if opt == 2 and AI == 1: iid.config(text='Paper + Rock = AI Wins', bg='red')
		elif opt == 2 and AI == 2: iid.config(text='Paper + Paper = TIE', bg='lightgrey')
		elif opt == 3 and AI == 3: iid.config(text='Paper + Scissor = AI Wins', bg='red')

		if opt == 3 and AI == 1: iid.config(text='Scissor + Rock = AI Wins', bg='red')
		elif opt == 3 and AI == 2: iid.config(text='Scissor + Paper = You Win', bg='green')
		elif opt == 3 and AI == 3: iid.config(text='Scissor + Scissor = TIE', bg='lightgrey')

	rock = Button(cframe, bg='#323232', text='  ROCK  ', activeforeground='lightgrey', bd=0, font=('ubuntu', 14), fg='white', activebackground='#323232', command=lambda: rpc(rock_))
	rock.grid(row=0, column=0)

	paper = Button(cframe, bg='#323232', text='  PAPER  ', activeforeground='lightgrey', bd=0, font=('ubuntu', 14), fg='white', activebackground='#323232', command=lambda: rpc(paper_))
	paper.grid(row=0, column=1)

	scissor = Button(cframe, bg='#323232', text='  SCISSOR  ', activeforeground='lightgrey', bd=0, font=('ubuntu', 14), fg='white', activebackground='#323232', command=lambda: rpc(scissor_))
	scissor.grid(row=0, column=2)

	iid = Label(tmrw, bg='#323232', fg='white', text='', font=('ubuntu', 14))
	iid.pack(fill='x')

# Tic tac toe (....)
def ttc():
	global clicked, count
	mwind = Frame(bd=0)
	window = Frame(mwind, bd=0)

	# X starts so true
	clicked = True
	count = 0

	def Reset():
		global b1, b2, b3, b4, b5, b6, b7, b8, b9
		global clicked, count
		clicked = True
		count = 0

		#confuring a bg
		b1.configure(text=" ", bg="#4EC050", borderwidth=0, state="normal")
		b2.configure(text=" ", bg="#4EC050", borderwidth=0, state="normal")
		b3.configure(text=" ", bg="#4EC050", borderwidth=0, state="normal")
		b4.configure(text=" ", bg="#4EC050", borderwidth=0, state="normal")
		b5.configure(text=" ", bg="#4EC050", borderwidth=0, state="normal")
		b6.configure(text=" ", bg="#4EC050", borderwidth=0, state="normal")
		b7.configure(text=" ", bg="#4EC050", borderwidth=0, state="normal")
		b8.configure(text=" ", bg="#4EC050", borderwidth=0, state="normal")
		b9.configure(text=" ", bg="#4EC050", borderwidth=0, state="normal")


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
			b1.config(bg="#87A96B")
			b4.config(bg="#87A96B")
			b7.config(bg="#87A96B")
			winner = True
			messagebox_info("Winner", "	CONGRATULATIONS!, X WINS   ", root)
			disable_all_buttons()

		elif b2['text'] == "X" and b5['text'] == 'X' and b8 ['text'] == 'X':
			b2.config(bg="#87A96B")
			b5.config(bg="#87A96B")
			b8.config(bg="#87A96B")
			winner = True
			messagebox_info("Winner", "	CONGRATULATIONS!, X WINS   ", root)
			disable_all_buttons()

		elif b3['text'] == "X" and b6['text'] == 'X' and b9 ['text'] == 'X':
			b3.config(bg="#87A96B")
			b6.config(bg="#87A96B")
			b9.config(bg="#87A96B")
			winner = True
			messagebox_info("Winner", "	CONGRATULATIONS!, X WINS   ", root)
			disable_all_buttons()

		elif b1['text'] == "X" and b5['text'] == 'X' and b9 ['text'] == 'X':
			b1.config(bg="#87A96B")
			b5.config(bg="#87A96B")
			b9.config(bg="#87A96B")
			winner = True
			messagebox_info("Winner", "	CONGRATULATIONS!, X WINS   ", root)
			disable_all_buttons()

		elif b3['text'] == "X" and b5['text'] == 'X' and b7 ['text'] == 'X':
			b3.config(bg="#87A96B")
			b5.config(bg="#87A96B")
			b7.config(bg="#87A96B")
			winner = True
			messagebox_info("Winner", "	CONGRATULATIONS!, X WINS   ", root)
			disable_all_buttons()

		elif b1['text'] == "X" and b2['text'] == 'X' and b3 ['text'] == 'X':
			b1.config(bg="#87A96B")
			b2.config(bg="#87A96B")
			b3.config(bg="#87A96B")
			winner = True
			messagebox_info("Winner", "	CONGRATULATIONS!, X WINS   ", root)
			disable_all_buttons()

		elif b4['text'] == "X" and b5['text'] == 'X' and b6['text'] == 'X':
			b4.config(bg="#87A96B")
			b5.config(bg="#87A96B")
			b6.config(bg="#87A96B")
			winner = True
			messagebox_info("Winner", "	CONGRATULATIONS!, X WINS   ", root)
			disable_all_buttons()

		elif b7['text'] == "X" and b8['text'] == 'X' and b9['text'] == 'X':
			b7.config(bg="#87A96B")
			b8.config(bg="#87A96B")
			b9.config(bg="#87A96B")
			winner = True
			messagebox_info("Winner", "	CONGRATULATIONS!, X WINS   ", root)
			disable_all_buttons()

		elif b1['text'] == "O" and b4['text'] == 'O' and b7 ['text'] == 'O':
			b1.config(bg="#87A96B")
			b4.config(bg="#87A96B")
			b7.config(bg="#87A96B")
			winner = True
			messagebox_info("Winner", "	CONGRATULATIONS!, O WINS   ", root)
			disable_all_buttons()

		elif b2['text'] == "O" and b5['text'] == 'O' and b8 ['text'] == 'O':
			b2.config(bg="#87A96B")
			b5.config(bg="#87A96B")
			b8.config(bg="#87A96B")
			winner = True
			messagebox_info("Winner", "	CONGRATULATIONS!, O WINS   ", root)
			disable_all_buttons()

		elif b3['text'] == "O" and b6['text'] == 'O' and b9 ['text'] == 'O':
			b3.config(bg="#87A96B")
			b6.config(bg="#87A96B")
			b9.config(bg="#87A96B")
			winner = True
			messagebox_info("Winner", "	CONGRATULATIONS!, O WINS   ", root)
			disable_all_buttons()

		elif b1['text'] == "O" and b5['text'] == 'O' and b9 ['text'] == 'O':
			b1.config(bg="#87A96B")
			b5.config(bg="#87A96B")
			b9.config(bg="#87A96B")
			winner = True
			messagebox_info("Winner", "	CONGRATULATIONS!, O WINS   ", root)
			disable_all_buttons()

		elif b3['text'] == "O" and b5['text'] == 'O' and b7 ['text'] == 'O':
			b3.config(bg="#87A96B")
			b5.config(bg="#87A96B")
			b7.config(bg="#87A96B")
			winner = True
			messagebox_info("Winner", "	CONGRATULATIONS!, O WINS   ", root)
			disable_all_buttons()

		elif b1['text'] == "O" and b2['text'] == 'O' and b3 ['text'] == 'O':
			b1.config(bg="#87A96B")
			b2.config(bg="#87A96B")
			b3.config(bg="#87A96B")
			winner = True
			messagebox_info("Winner", "	CONGRATULATIONS!, O WINS   ", root)
			disable_all_buttons()

		elif b4['text'] == "O" and b5['text'] == 'O' and b6['text'] == 'O':
			b4.config(bg="#87A96B")
			b5.config(bg="#87A96B")
			b6.config(bg="#87A96B")
			winner = True
			messagebox_info("Winner", "	CONGRATULATIONS!, O WINS   ", root)
			disable_all_buttons()

		elif b7['text'] == "O" and b8['text'] == 'O' and b9['text'] == 'O`':
			b7.config(bg="#87A96B")
			b8.config(bg="#87A96B")
			b9.config(bg="#87A96B")
			winner = True
			messagebox_info("Winner", "	CONGRATULATIONS!, O WINS   ", root)
			disable_all_buttons()

		elif count == 9 and winner == False:
				messagebox_info("Winner", "It is a tie!\nno one wins, try starting a new match", root)
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
			messagebox_error("Error", "That box has already been used. Use another box", root)

	#buttons
	b1= Button(window, text=" ", borderwidth=0, font=("Arial", 20), height=3, width=6, bg="#4EC050",command= lambda: b_click(b1))
	b2= Button(window, text=" ", borderwidth=0, font=("Arial", 20), height=3, width=6, bg="#4EC050",command= lambda: b_click(b2))
	b3= Button(window, text=" ", borderwidth=0, font=("Arial", 20), height=3, width=6, bg="#4EC050",command= lambda: b_click(b3))

	b4= Button(window, text=" ", borderwidth=0, font=("Arial", 20), height=3, width=6, bg="#4EC050",command= lambda: b_click(b4))
	b5= Button(window, text=" ", borderwidth=0, font=("Arial", 20), height=3, width=6, bg="#4EC050",command= lambda: b_click(b5))
	b6= Button(window, text=" ", borderwidth=0, font=("Arial", 20), height=3, width=6, bg="#4EC050",command= lambda: b_click(b6))

	b7= Button(window, text=" ", borderwidth=0, font=("Arial", 20), height=3, width=6, bg="#4EC050",command= lambda: b_click(b7))
	b8= Button(window, text=" ", borderwidth=0, font=("Arial", 20), height=3, width=6, bg="#4EC050",command= lambda: b_click(b8))
	b9= Button(window, text=" ", borderwidth=0, font=("Arial", 20), height=3, width=6, bg="#4EC050",command= lambda: b_click(b9))

	def about_command():
		messagebox_info("About", 'tic tac toe is a simple tic tac toe game made by izkaan and dad python productions®', root)

	def show_help_command():
		messagebox_info('Help', "Mail izooizkaan@gmail.com for help", root)

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
	b1.configure(bg="#4EC050", fg='white', borderwidth=0, activebackground='#4EC050', activeforeground='red')
	b2.configure(bg="#4EC050", fg='white', borderwidth=0, activebackground='#4EC050', activeforeground='red')
	b3.configure(bg="#4EC050", fg='white', borderwidth=0, activebackground='#4EC050', activeforeground='red')
	b4.configure(bg="#4EC050", fg='white', borderwidth=0, activebackground='#4EC050', activeforeground='red')
	b5.configure(bg="#4EC050", fg='white', borderwidth=0, activebackground='#4EC050', activeforeground='red')
	b6.configure(bg="#4EC050", fg='white', borderwidth=0, activebackground='#4EC050', activeforeground='red')
	b7.configure(bg="#4EC050", fg='white', borderwidth=0, activebackground='#4EC050', activeforeground='red')
	b8.configure(bg="#4EC050", fg='white', borderwidth=0, activebackground='#4EC050', activeforeground='red')
	b9.configure(bg="#4EC050", fg='white', borderwidth=0, activebackground='#4EC050', activeforeground='red')

	dwindow("Tic Tac Toe", window, mwind)
	"""
	"""
	
# Calculator
def calcs():
	global num
	ws = Frame(bd=0, bg='#585953')
	dowin = Frame(ws, bd=0, bg='#585953')
	
	dwindow(" Calculator (3rd party software) ", dowin, ws)

	# global variables
	num = ''

	# functions
	def display(number):
		global num 
		num = num + str(number)
		scr_lbl['text'] = num
		

	def clear_scr():
		global num
		num = ''
		scr_lbl['text'] = num


	def equal_btn():
		global num
		add=str(eval(num))
		scr_lbl['text'] = add
		num=''
	def equal_btn():
		global num
		sub=str(eval(num))
		scr_lbl['text'] = sub
		num=''	 
	def equal_btn():
		global num
		mul=str(eval(num))
		scr_lbl['text'] = mul
		num=''
	def equal_btn():
		global num
		div=str(eval(num))
		scr_lbl['text'] = div
		num=''	

	var = StringVar()

	# frames 
	frame_1 = Frame(ws) 
	frame_1.pack(expand=True, fill=BOTH)

	frame_2 = Frame(ws)
	frame_2.pack(expand=True, fill=BOTH)

	frame_3 = Frame(ws)
	frame_3.pack(expand=True, fill=BOTH)

	frame_4 = Frame(ws)
	frame_4.pack(expand=True, fill=BOTH)

	# label
	scr_lbl = Label(
		frame_1,
		textvariable='',
		font=('Arial', 20),
		anchor = SE,
		bg = '#595954',
		fg = 'white' 
		)

	scr_lbl.pack(expand=True, fill=BOTH)

	# buttons
	key_1 = Button(
		frame_1,
		text='1',
		font=('Arial', 22),
		border = 0,
		relief = GROOVE,
		bg = '#2E2E2B',
		fg = 'white',
		command = lambda: display(1)
		)

	key_1.pack(expand=True, fill=BOTH, side=LEFT)

	key_2 = Button(
		frame_1,
		text='2',
		font=('Arial', 22),
		border = 0,
		relief = GROOVE,
		bg = '#2E2E2B',
		fg = 'white',
		command = lambda: display(2)
		)

	key_2.pack(expand=True, fill=BOTH, side=LEFT)

	key_3 = Button(
		frame_1,
		text='3',
		font=('Arial', 22),
		border = 0,
		relief = GROOVE,
		bg = '#2E2E2B',
		fg = 'white',
		command = lambda: display(3)
		)

	key_3.pack(expand=True, fill=BOTH, side=LEFT)

	key_add = Button(
		frame_1,
		text='+',
		font=('Arial', 22),
		border = 0,
		relief = GROOVE,
		bg = '#2E2E2B',
		fg = 'white',
		command = lambda: display('+')
		)

	key_add.pack(expand=True, fill=BOTH, side=LEFT)

	key_4 = Button(
		frame_2,
		text='4',
		font=('Arial', 22),
		border = 0,
		relief = GROOVE,
		bg = '#2E2E2B',
		fg = 'white',
		command = lambda: display(4)
		)

	key_4.pack(expand=True, fill=BOTH, side=LEFT)

	key_5 = Button(
		frame_2,
		text='5',
		font=('Arial', 22),
		border = 0,
		relief = GROOVE,
		bg = '#2E2E2B',
		fg = 'white',
		command = lambda: display(5)
		)

	key_5.pack(expand=True, fill=BOTH, side=LEFT)

	key_6 = Button(
		frame_2,
		text='6',
		font=('Arial', 22),
		border = 0,
		relief = GROOVE,
		bg = '#2E2E2B',
		fg = 'white',
		command = lambda: display(6)
		)

	key_6.pack(expand=True, fill=BOTH, side=LEFT)

	key_sub = Button(
		frame_2,
		text='-',
		font=('Arial', 22),
		border = 0,
		relief = GROOVE,
		bg = '#2E2E2B',
		fg = 'white',
		command = lambda: display('-')
		)

	key_sub.pack(expand=True, fill=BOTH, side=LEFT)

	key_7 = Button(
		frame_3,
		text='7',
		font=('Arial', 22),
		border = 0,
		relief = GROOVE,
		bg = '#2E2E2B',
		fg = 'white',
		command = lambda: display(7)
		)

	key_7.pack(expand=True, fill=BOTH, side=LEFT)

	key_8 = Button(
		frame_3,
		text='8',
		font=('Arial', 22),
		border = 0,
		relief = GROOVE,
		bg = '#2E2E2B',
		fg = 'white',
		command = lambda: display(8)
		)

	key_8.pack(expand=True, fill=BOTH, side=LEFT)

	key_9 = Button(
		frame_3,
		text='9',
		font=('Arial', 22),
		border = 0,
		relief = GROOVE,
		bg = '#2E2E2B',
		fg = 'white',
		command = lambda: display(9)
		)

	key_9.pack(expand=True, fill=BOTH, side=LEFT)

	key_mul = Button(
		frame_3,
		text='*',
		font=('Arial', 22),
		border = 0,
		relief = GROOVE,
		bg = '#2E2E2B',
		fg = 'white',
		command = lambda: display('*')
		)

	key_mul.pack(expand=True, fill=BOTH, side=LEFT)


	key_clr = Button(
		frame_4,
		text='C',
		font=('Arial', 22),
		border = 0,
		relief = GROOVE,
		bg = '#2E2E2B',
		fg = 'white',
		command = clear_scr 
		)

	key_clr.pack(expand=True, fill=BOTH, side=LEFT)

	key_0 = Button(
		frame_4,
		text='0',
		font=('Arial', 22),
		border = 0,
		relief = GROOVE,
		bg = '#2E2E2B',
		fg = 'white',
		command = lambda: display(0)
		)

	key_0.pack(expand=True, fill=BOTH, side=LEFT)

	key_res = Button(
		frame_4,
		text='=',
		font=('Arial', 22),
		border = 0,
		relief = GROOVE,
		bg = '#2E2E2B',
		fg = 'white',
		command = equal_btn
		)

	key_res.pack(expand=True, fill=BOTH, side=LEFT)

	key_div = Button(
		frame_4,
		text='/',
		font=('Arial', 22),
		border = 0,
		relief = GROOVE,
		bg = '#2E2E2B',
		fg = 'white',
		command = lambda: display('/')
		)

	key_div.pack(expand=True, fill=BOTH, side=LEFT)

# tedit app
def tedit_app():
	global tedit_win, toolbar, toolbartext

	# Return a frame window
	tedit_win = Frame(bd=0, bg='white')
	tedit_win.pack(padx=37, pady=37, fill='both', expand=1)

	# Toolbar
	toolbar = Frame(tedit_win, bg='#2259E1', bd=0)
	toolbar.pack(side='top', fill='x')

	# Exit button
	exit_btn = Button(toolbar, bd=0, text=' ✕ ', fg='white', bg='#FF4900', font=("ubuntu", 10), activebackground='#FF4900', activeforeground='white', command=tedit_exit)
	exit_btn.pack(side='right')

	# Toolbar text
	toolbartext = Label(toolbar, bd=0, text='TextEditor XP', font=('ubuntu', 12), bg='#2259E1', fg='white')
	toolbartext.pack(ipady=1)

	# TLFrm
	TLB = Frame(tedit_win, bg='#2259E1', bd=0)
	TLB.pack(side='top', fill='x')

	# New file
	def newfile():
		my_text.delete("1.0", END)

	# TLB BTN NEW
	newbtn = Button(TLB, bd=0, text='New File', bg='#2259E1', font=('ubuntu', 13), activebackground='#2259E2', fg='white', activeforeground='lightgrey', command=newfile)
	newbtn.pack(fill='x', side='left', ipadx=5)

	# Open file
	def open_file():
		global text_file, trext_file
		my_text.delete("1.0", END)
		trext_file = filedialog.askopenfilename(title="Open file", filetypes=(("Text Files", "*txt"), ("HTML Files", "*.html"), ("Python Files", "*.py"), ("All Files", "*.*")))
		text_file = open(trext_file, 'r')
		stuff = text_file.read()
		my_text.insert(END, stuff)
		text_file.close()
		
		toolbartext.config(text=f'TextEditor XP - Opened file')

	# TLB BTN
	openbtn = Button(TLB, bd=0, text='Open File', bg='#2259E1', font=('ubuntu', 13), activebackground='#2259E2', fg='white', activeforeground='lightgrey', command=open_file)
	openbtn.pack(fill='x', side='left', ipadx=5)

	def save_file():
		try:
			# Get text and filename
			global content_str
			content_str = my_text.get(1.0, END)

			# Write to filename
			open_filename = open(trext_file, mode='w', encoding='utf8')
			open_filename.write(content_str)
			open_filename.close()

			messagebox_info('Saved file', 'We sucsessfully saved your file, or atleast we think we did?', root)

		except NameError as errraa:
			messagebox_error('Error', 'Please open a file before saving it', root)
		except Exception as exceptiontk:
			messagebox_error('Error', f"We ran into the following error:\n{exceptiontk}", root)

	# TLB BTN SAVE
	save_btn = Button(TLB, bd=0, text='Save File', bg='#2259E1', font=('ubuntu', 13), activebackground='#2259E2', fg='white', activeforeground='lightgrey', command=save_file)
	save_btn.pack(fill='x', side='left', ipadx=5)

	def save_as_file():
		# Get file name, directory
		savefilemsg = filedialog.asksaveasfilename(title='What should we save as?')
		savefilemsg = ''.join(savefilemsg)

		# Make file
		try:
			if (savefilemsg != ""):
				os.system(f'touch "{savefilemsg}"')

				with open(savefilemsg, 'w') as file:
					# Write to file
					file.write(my_text.get(1.0, END))
					file.close()

		except Exception as err__:
			print(err__)
			messagebox_error("Error", f'The following error occoured in PROCESS_SAVE_AS:\n{err__}', root)

	# tTLB SAVE BUTTON AS button
	save_as_btn = Button(TLB, bd=0, text='Save As', bg='#2259E1', font=('ubuntu', 13), activebackground='#2259E2', fg='white', activeforeground='lightgrey', command=save_as_file)
	save_as_btn.pack(fill='x', side='left', ipadx=5)

	tedit_frame = Frame(tedit_win, bg='white')
	tedit_frame.pack(fill='both', expand=1)

	"""
	what is carnival?
	what is the meaninig of life.
	KEEPIN FODDERS FAART WITH PRDIE
	AAAAA--A-A-A-A--A 
	kippiwww wowaa..

	"""

	# Main textbox
	my_text = Text(tedit_win, font=("Arial", 16), selectbackground="Lightgrey", selectforeground="Black", undo=True, bd=0)
	my_text.pack(expand=1, fill='both')

	def readtexts():
		engine = pyttsx3.init()
		engine.say(my_text.get(1.0, END))

		engine.runAndWait()
		return

	# A read file
	read_btn = Button(TLB, bd=0, text='Read Text', bg='#2259E1', font=('ubuntu', 13), activebackground='#2259E2', fg='white', activeforeground='lightgrey', command=readtexts)
	read_btn.pack(fill='x', side='left', ipadx=5)

	# Context menu
	tedit_root = Menu(root)

	tedit_root = Menu(tedit_root, tearoff=0, activebackground='lightblue', activeforeground='black')
	tedit_root.add_command(label="Clear text", command=newfile)
	tedit_root.add_command(label="Open file", command=open_file)
	tedit_root.add_command(label="Save file", command=save_file)
	tedit_root.add_command(label="Save as file", command=save_as_file)
	tedit_root.add_command(label="Read Text", command=readtexts)

	def do_pap(event):
		try: tedit_root.tk_popup(event.x_root, event.y_root)
		finally: tedit_root.grab_release()

	my_text.bind("<Button-3>", do_pap)

# About workspace
def about_workspace():
	global about_win
	# Return a frame window
	about_win = Frame()
	about_win.pack(pady=(37, 37))

	# Toolbar
	toolbar = Frame(about_win, bg='#2259E1', bd=0)
	toolbar.pack(side='top', fill='x')

	# Exit button
	exit_btn = Button(toolbar, bd=0, text=' ✕ ', fg='white', bg='#FF4900', font=("ubuntu", 12), activebackground='#FF4900', activeforeground='white', command=about_exit)
	exit_btn.pack(side='right')

	# Toolbar text
	toolbartext = Label(toolbar, bd=0, text='About Workspace (Version Info)', font=('ubuntu', 12), bg='#2259E1', fg='white')
	toolbartext.pack(ipady=1)

	about_label = Text(about_win, font=('Monospace', 13), selectbackground='#f0f0f0', selectforeground='black', bd=0, wrap=WORD, bg='#f0f0f0')
	about_label.insert('1.0', about_txt)
	about_label.pack(expand=1, fill='both', pady=2, padx=2)
	about_label.config(state="disabled")

	# Tag
	about_label.tag_add("start", "2.0", "2.30")
	about_label.tag_config("start", font=('ubuntu', 20), justify='center', foreground='#0077c8')

# Place2D app
def pixel_painter():
	global colors, current_block

	pp = Frame()
	window = Frame(pp)

	colors = {
		"Brown": "#914710",
		"Red": "#e28383",
		"Red Orange": "#e29b83",
		"Orange": "#e2b383",
		"Yellow Orange": "#e2ca83",
		"Yellow": "#e2e283",
		"Lighter Green": "#cae283",
		"Light Green": "#b3e283",
		"Green": "#9be283",
		"Greener": "#83e283",
		"Turquoise": "#83e29b",
		"Turquoise-ish": "#83e2b3",
		"Light Blue": "#83e2ca",
		"Another Blue": "#83cae2",
		"Blue": "#83b3e2",
		"Purplish Blue": "#839be2",
		"Purple": "#8383e2",
		"Violet": "#9b83e2",
		"Mostly Pink": "#b383e2",
		"Saturated Pink": "#ca83e2",
		"Reddish Pink": "#e283b3",
		"Workspace Blue": "#2259E1",
		"Workspace Green": "#4EC050",
		"Black": 'black',
		"Grey": 'grey',
		"White": "White",
	}

	# Colors
	ROWS = 0
	ROW_2 = 0
	TAG = 0

	# Testing feature
	testing = True
	if testing == True:

		# Color row 
		color_row = Frame(window)
		color_row.pack(side=LEFT, fill='y')

		for color in colors:
			ROWS += 1

			batan = Button(
					color_row, bg=colors.get(color), height=2, width=4, activebackground=colors.get(color)
				)
			batan["command"] = lambda colorr=colors.get(color): set_block(colorr)

			if ROWS <= 13: batan.grid(row=ROWS, column=0)
			else:
				ROW_2 += 1
				batan.grid(row=ROW_2, column=1)

	# Create main frame
	root = Frame(window)
	root.pack(fill='both', expand=1)

	# Variables
	r,c = 0,0
	__width = 32
	current_block = colors["Green"]

	tags = []
	tag = 0

	"""cb = Frame(root, height=45, bg=current_block)
	cb.grid(row=11, columnspan=28, sticky="nsew")

	cc = Label(cb, text="Useless application", font=("Product Sans", 21), bg=current_block)
	cc.pack()"""

	def set_block(color):
		global current_block
		current_block = color
		root.config(bg=current_block)
		color_row.config(bg=current_block)

	def placeb(btn):
		global current_block
		btn["bg"] = current_block
		btn["activebackground"] = current_block

	# Itterate a bunch of tons
	for x in range(1,417):
		tag += 1
		tags.append(tag)
		b = Button(root, bg=colors["Another Blue"], width=4, height=2, highlightbackground='black', activebackground=colors["Another Blue"])
		b.grid(row=r, column=c, sticky=N+S+E+W)
		b["command"] = lambda b=b: placeb(b)
		c+=1

		if c==__width:
			r+=1
			c=0

	# Build some grass
	r_, c_ = 0, 0
	_width = 18,0
	fake_tags = 126

	"""for x in range(1, 29):
		fake_tags += 1
		tags.append(fake_tags)
		b = Button(root, bg=colors["Green"], width=4, height=2, highlightbackground='black', activebackground=colors["Green"])
		b.grid(row=10, column=c_, sticky=N+S+E+W)
		b["command"] = lambda b=b: placeb(b)
		c_+=1

		if c_==_width:
			r_+=1"""

	cwindow("Pixel Painter (Imported)", window, pp)

# Matterial app
def mtc_app():
	global main, code_font, fonts
	mtcc = Frame()
	main = Frame(mtcc)

	# APP STARTS HERE
	code_font = ("Jetbrains Mono", 14)

	# Colors (removed unsued)
	indigo_200 = "#9FA8DA"
	indigo_300 = "#7986CB"
	blue_grey_900 = "#263238"

	# Fonts
	fonts = ("Product Sans", 14)
	blue_grey = "#2259E1"

	# Open folder
	def open_folder():
		global text, tree

		path = filedialog.askdirectory()
		nodes = dict()

		text.destroy()

		style = ttk.Style(main)
		style.theme_use("clam")
		style.configure(
			"Treeview", background=deafult,  fieldbackground=deafult, foreground=blue_grey_900, activebackground=deafult,
			font=("Product Sans", 12), bd=0
		)

		style.configure("Treeview.Heading", background=deafult,  fieldbackground=deafult, foreground=blue_grey_900)

		tree.destroy()

		tree = ttk.Treeview(main, height=100)
		tree.heading('#0', text='Project tree', anchor='w')
		tree.pack(side=LEFT, fill='y')

		text = CodeEditor(main, bg=blue_grey, fg=blue_grey_900, font=code_font, wrap=WORD, insertbackground=deafult, undo=True, maxundo=100)
		text.pack(side=BOTTOM, fill=BOTH, expand=1)

		text.bind("<Control-n>", lambda event: text.delete(1.0, END))
		text.bind("<Control-o>", lambda event: open_file(main, text, open_button))
		text.bind("<Control-s>", lambda event: save_file(main, text, save_button, save_as))
		text.bind("<Control-Shift-s>", lambda event: save_as_function(main, text, save_as))
		text.bind("<Control-Shift-f>", lambda event: open_folder())

		def insert_node(parent, text, abspath):
			node = tree.insert(parent, 'end', text=text, open=False)
			if os.path.isdir(abspath):
				nodes[node] = abspath
				tree.insert(node, 'end')

		def open_node(event):
			node = tree.focus()
			abspath = nodes.pop(node, None)
			if abspath:
				tree.delete(tree.get_children(node))
				for p in os.listdir(abspath):
					insert_node(node, p, os.path.join(abspath, p))

		def open_file(text):
			global filename
			curItem = tree.focus()
			print(tree.item(curItem))
			eee = tree.item(curItem)
			eeee = eee["text"]

			filename = f"{path}\\{eeee}"

			if os.path.isdir(eeee) == False:
				try:
					if os.path.isfile(filename):
						if text.get(1.0, END) != open(filename, "r").read():
							#file_label.config(text=f"  {filename}")
							#titlechangerset(f'Material Code Editor - {filename}')
							text.delete(1.0, END)
							text.insert(1.0, open(filename, "r").read())
				except PermissionError: messagebox.showerror("Permission", "Permission denied")
		
				text.pack(fill='both', expand=1)

		abspath = os.path.abspath(path)
		insert_node('', abspath, abspath)
		tree.bind('<<TreeviewOpen>>', open_node)
		tree.bind("<ButtonRelease-1>", lambda event: open_file(text))

	# Open file
	def open_file(main, text, open_button):
		global filename
		open_button.config(bg=indigo_200)

		# Ask filename
		file = filedialog.askopenfilename(title="Open file")

		if file != '':
			try:
				text.delete(1.0, END)

				# Open file
				text_file = open(file, 'r')
				stuff = text_file.read() # Get text content

				text.insert(END, stuff)
				text_file.close()

				filename = file
				#file_label.config(text=f"  {filename}")
				#titlechangerset(f'Material Code Editor - {filename}')
			except Exception as err:
				messagebox.showerror("File Not Found", f"The file you tried to open does not exist??")

	# Save as file
	def save_as_function(main, text, save_as):
		global filename

		save_as.config(bg=indigo_200)
		global filename
		try:
			file = filedialog.asksaveasfilename(title="Save file")

			files = open(file, 'w')
			files.write(text.get(1.0, END))
			files.close()

			filename = file

			#file_label.config(text=f"  {filename}")
			#titlechangerset(f"Material Code Editor - Saved as {filename}")

		except Exception as urmom: print(urmom)

	# Save file
	def save_file(main, text, save_button, save_as):
		global filename
		try:
			save_button.config(bg=indigo_200)

			content = text.get(1.0, END)
			
			writes = open(filename, "w")
			writes.write(content)

			print(f"Saved: {filename}\nContent: {content}")

			writes.close()

			#file_label.config(text=f"  {filename}")
			#titlechangerset(f"Material Code Editor - Saved {filename}")

		except Exception as errors:
			save_as_function(main, text, save_as)

	# Variables (not material ones)
	filename = "Untitled File"
	deafult = "#2259E1"

	# Create a topbar
	topbar = Frame(main, bg=deafult)
	topbar.pack(side=TOP, fill=X) 

	# Save as
	save_as = Label(topbar, text="  Save As  ", bg=deafult, fg=blue_grey_900, font=fonts)
	save_as.grid(row=1, column=5)

	save_as.bind("<Enter>", lambda event: save_as.config(bg=indigo_300))
	save_as.bind("<Leave>", lambda event: save_as.config(bg=deafult))
	save_as.bind("<Button-1>", lambda event: save_as_function(main, text, save_as))

	# Save button
	save_button = Label(topbar, text="  Save  ", bg=deafult, fg=blue_grey_900, font=fonts)
	save_button.grid(row=1, column=4)

	save_button.bind("<Enter>", lambda event: save_button.config(bg=indigo_300))
	save_button.bind("<Leave>", lambda event: save_button.config(bg=deafult))
	save_button.bind("<Button-1>", lambda event: save_file(main, text, save_button, save_as))

	# New button
	new_button = Label(topbar, text="  Clear  ", bg=deafult, fg=blue_grey_900, font=fonts)
	new_button.grid(row=1, column=3)

	new_button.bind("<Enter>", lambda event: new_button.config(bg=indigo_300))
	new_button.bind("<Leave>", lambda event: new_button.config(bg=deafult))
	new_button.bind("<Button-1>", lambda event: text.delete(1.0, END))

	global tree
	tree = ttk.Treeview(main, height=100)
	tree.heading('#0', text='Project tree', anchor='w')

	# Open button
	folder_button = Label(topbar, text="  Folder  ", bg=deafult, fg=blue_grey_900, font=fonts)
	folder_button.grid(row=1, column=2)

	folder_button.bind("<Enter>", lambda event: folder_button.config(bg=indigo_300))
	folder_button.bind("<Leave>", lambda event: folder_button.config(bg=deafult))
	folder_button.bind("<Button-1>", lambda event: open_folder())

	# Open button
	open_button = Label(topbar, text="  Open  ", bg=deafult, fg=blue_grey_900, font=fonts)
	open_button.grid(row=1, column=1)

	open_button.bind("<Enter>", lambda event: open_button.config(bg=indigo_300))
	open_button.bind("<Leave>", lambda event: open_button.config(bg=deafult))
	open_button.bind("<Button-1>", lambda event: open_file(main, text, open_button))

	global text

	# Create a code editor
	text = CodeEditor(main, bg=blue_grey, fg=blue_grey_900, font=code_font, wrap=WORD, insertbackground=deafult, undo=True, maxundo=100)
	text.bind("<Control-n>", lambda event: text.delete(1.0, END))
	text.bind("<Control-o>", lambda event: open_file(main, text, open_button))
	text.bind("<Control-s>", lambda event: save_file(main, text, save_button, save_as))
	text.bind("<Control-Shift-s>", lambda event: save_as_function(main, text, save_as))
	text.bind("<Control-Shift-f>", lambda event: open_folder())

	text.insert(1.0, """# Welcome to Material Code Edittor
# An flat material inspired text editor by Me.

# This editor is the evolution and an arguably nicer version of the "Orcim" which was inspired by
# gedit and looked fine in a way. However it used customtkinter

# However, this version is an huge improvement, with new features, such as sidebars and a new UI
# and not as bugged, which took an painstaking amount of time which i will not share

## IMPORTANT
# - The files panel is ugly
# - Click the sidebar button and you can choose to show/hide FILES panel and SHORTCUT sidebar
# - You can also choose to show run button
	""")

	text.pack(side=BOTTOM, fill=BOTH, expand=1)

	cwindow("MaterialCode (WXP-VRS)", main, mtcc)

# Start menus
def startmenu():
	global start_frame, viewbtn

	start_frame = Frame(bg='white')
	start_frame.pack(side='left', anchor='s', ipady=100)

	# Top bar
	textlbl = Label(start_frame, bg='#2E77C6', font=("ubuntu", 14), fg='white', text=' Workspace User			')
	textlbl.pack(side='top', ipady=2, fill='x')

	# Bottom bar
	bottombar = Frame(start_frame, bg='#2E77C6', bd=0, width=2)
	bottombar.pack(side='bottom', ipady=2, fill='x')

	# One side bar (#D0E6FD)
	one_sidebar = Frame(start_frame, bg='#D0E6FD')
	one_sidebar.pack(side='right', fill='y')

	# Sidebar text
	mydocs = Button(one_sidebar, bg='#D0E6FD', activebackground='#D0E6FD', text='Kontact Developer', font=("ubuntu", 12), fg='black', bd=0, command=lambda:webbrowser.open("mailto:pycodes.10@gmail.com"))
	mydocs.grid(row=0, column=0, ipadx=3)

	myhelp = Button(one_sidebar, bg='#D0E6FD', activebackground='#D0E6FD', text='About workspace', font=("ubuntu", 12), fg='black', bd=0, command=about_workspace)
	myhelp.grid(row=1, column=0, ipadx=3)


	# Left side bar
	left_sidebar = Frame(start_frame, bg='white')
	left_sidebar.pack(side='left', fill='y')

	ttcbtn = Button(left_sidebar, bg='white', activebackground='white', text='Pixel Painter ', font=("ubuntu", 12), fg='black', bd=0, command=pixel_painter)
	ttcbtn.grid(row=0, column=0, ipadx=0)

	mtc_btn = Button(left_sidebar, bg='white', activebackground='white', text='MaterialCode', font=("ubuntu", 12), fg='black', bd=0, command=mtc_app)
	mtc_btn.grid(row=1, column=0, ipadx=0)

	txp_btn = Button(left_sidebar, bg='white', activebackground='white', text='TextEditor   ', font=("ubuntu", 12), fg='black', bd=0, command=tedit_app, anchor='w')
	txp_btn.grid(row=2, column=0, ipadx=0)

	rpc_btn = Button(left_sidebar, bg='white', activebackground='white', text='RPCGame    ', font=("ubuntu", 12), fg='black', bd=0, command=tmrf)
	rpc_btn.grid(row=3, column=0, ipadx=0)

	clc_btn = Button(left_sidebar, bg='white', activebackground='white', text='Calculator   ', font=("ubuntu", 12), fg='black', bd=0, command=calcs)
	clc_btn.grid(row=4, column=0, ipadx=0)

	ttcbtn = Button(left_sidebar, bg='white', activebackground='white', text='Tic Tac Toe ', font=("ubuntu", 12), fg='black', bd=0, command=ttc)
	ttcbtn.grid(row=5, column=0, ipadx=0)

	viewbtn = Button(bottombar, bg='#E68E00', font=('Ubtunu', 10), fg='white', text='FullScreen', bd=0, command=lambda:full_view(viewbtn))
	viewbtn.config(activebackground='#E68E00', fg='white')
	viewbtn.pack(side='right', pady=3, padx=3)

	about_btn = Button(bottombar, bg='#E68E00', font=('Ubtunu', 10), fg='white', text='About WXP', bd=0, command=about_workspace)
	about_btn.config(activebackground='#E68E00', fg='white')
	about_btn.pack(side='right', pady=3, padx=3)

	# Logoff
	shutbtn = Button(bottombar, bg='#FF4D00', font=('Ubtunu', 10), fg='white', text='Shut down', bd=0, command=workspace_exit)
	shutbtn.config(activebackground='#FF4D00', fg='white')
	shutbtn.pack(side='right', pady=3, padx=3)

	start.config(comman=lambda:startoof(start_frame))


# Background image
SPECM = PhotoImage(file=r"windows_xp.png")

background_label = Label(root, image=SPECM)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

# TEditor icon
txp_icon = Image.open(r"texteditor.png")
txp_icon = txp_icon.resize((27, 27))
txp_icon = ImageTk.PhotoImage(txp_icon)

tict_icon = Image.open(r"tic-tac-toe.png")
tict_icon = tict_icon.resize((27, 27))
tict_icon = ImageTk.PhotoImage(tict_icon)

calc_icon = Image.open(r"calc.png")
calc_icon = calc_icon.resize((27, 27))
calc_icon = ImageTk.PhotoImage(calc_icon)

tmr_icn = Image.open(r"terminal.png")
tmr_icn = tmr_icn.resize((27, 27))
tmr_icn = ImageTk.PhotoImage(tmr_icn)

mtc_icn = Image.open(r"materialcode.png")
mtc_icn = mtc_icn.resize((27, 27))
mtc_icn = ImageTk.PhotoImage(mtc_icn)

# Taskbar
taskbar = Frame(root, bg='#2E77C6')
taskbar.pack(fill='x', side='bottom')

# Start menu
start = Button(taskbar, bg='#4EC050', text='Workspace', bd=0, font=("ubuntu", 14), fg='white', command=lambda:startmenu())
start.config(activebackground='#52d154', activeforeground='white')
start.pack(side='left', ipady=2, ipadx=2)

txp_btn = Button(taskbar, image=txp_icon, bd=0, activebackground='#2E77C6', bg='#2E77C6', command=tedit_app)
txp_btn.pack(side='left', ipady=5, ipadx=7)

tmr_btn = Button(taskbar, image=tmr_icn, bd=0, activebackground='#2E77C6', bg='#2E77C6', command=tmrf)
tmr_btn.pack(side='left', ipady=5, ipadx=7)

calcs_btn = Button(taskbar, image=calc_icon, bd=0, activebackground='#2E77C6', bg='#2E77C6', command=calcs)
calcs_btn.pack(side='left', ipady=5, ipadx=7)

tic_btn = Button(taskbar, image=tict_icon, bd=0, activebackground='#2E77C6', bg='#2E77C6', command=ttc)
tic_btn.pack(side='left', ipady=5, ipadx=7)

# Time
times = time.strftime("%H:%M:%S")

def timechan():
	global hms
	hms = time.strftime("%X")
	time_lbl.config(text=hms)
	root.after(500, timechan)


def batterchan():
	global percent
	battery = psutil.sensors_battery()
	plugged = battery.power_plugged
	percent = str(battery.percent)
	percent = f'{percent}%'

	battery_lbl.config(text=percent)

	root.after(1000, batterchan)

time_lbl = Label(taskbar, bg='#008EFF', text='', fg='white', font=('Ubuntu', 14))
time_lbl.pack(side='right', ipady=5, ipadx=1)

timechan()

# Battery
battery_lbl = Label(taskbar, bg='#008EFF', text='', fg='white', font=('Ubuntu', 14))
battery_lbl.pack(side='right', ipady=5, ipadx=3)
batterchan()

# Extra icon
extr_icon = Image.open(r"more.png")
extr_icon = extr_icon.resize((27, 27))
extr_icon = ImageTk.PhotoImage(extr_icon)

# Context menu
context_root = Menu(root)

context_menu = Menu(context_root, tearoff=0, activebackground='lightblue', activeforeground='black')
context_menu.add_command(label="Shut down", command=workspace_exit)
context_menu.add_command(label="Version info", command=about_workspace)
context_menu.add_separator()
context_menu.add_command(label="Full Screen", command=lambda:root.attributes('-fullscreen', True))
context_menu.add_command(label="Exit Full Screen", command=lambda:root.attributes('-fullscreen', False))

def do_popup(event):
	try: context_menu.tk_popup(event.x_root, event.y_root)
	finally: context_menu.grab_release()

# Extra button
extr_btn = Button(taskbar, image=extr_icon, bd=0, activebackground='#008EFF', bg='#008EFF')
extr_btn.bind("<Button-1>", do_popup)
extr_btn.pack(side='right', ipady=5, ipadx=3)

# Execute code
if __name__ == '__main__':

	# Context menu
	text_root = Menu(root)

	text_root = Menu(text_root, tearoff=0, activebackground='lightblue', activeforeground='black')
	text_root.add_command(label="Text Editor XP", command=tedit_app)
	text_root.add_command(label="Rock Paper Scissors", command=tmrf)
	text_root.add_separator()
	text_root.add_command(label="Shut down", command=workspace_exit)
	text_root.add_command(label="About Workspace", command=about_workspace)
	text_root.add_separator()
	text_root.add_command(label="Full Screen", command=lambda:root.attributes('-fullscreen', True))
	text_root.add_command(label="Exit Full Screen", command=lambda:root.attributes('-fullscreen', False))

	def do_poop(event):
		try: text_root.tk_popup(event.x_root, event.y_root)
		finally: text_root.grab_release()

	root.bind("<Button-3>", do_poop)

	# Plugged
	battery = psutil.sensors_battery()
	pluggede = battery.power_plugged

	if pluggede == 1:
		messagebox_info('Plugged in', '  You are plugged in to power  ', root)
	elif pluggede == 0:
		messagebox_warning("Not Plugged In", "  You are not plugged in  ", root)

	# Mainloop
	root.mainloop()
