#!/usr/bin/python3
from subprocess import call
from tkinter import *
from tkinter import ttk

class Point:
	def __init__(self, x_coord, y_coord, p_delay):
		self.x=x_coord;
		self.y=y_coord;
		self.delay=p_delay;
		
def parameters_write(*args):
	try:
		pic_file=open("pic_file", 'w');
		pic_file.write("{0} {1} {2}".format(x_var.get(), y_var.get(), time_var.get()));
		pic_file.close;
		#num_file=open("num_file", 'w');
		#num_file.write("12 %s" % time_var.get());
		#num_file.close;
		main_label_var.set("Point X:{0}; Y:{1} with delay of {2}ms was added".format(x_var.get(), y_var.get(), time_var.get()));
		start_button.focus();
	except ValueError:
		pass
		
def period_write(*args):
	try:
		num_file=open("num_file", 'w');
		num_file.write("12 {0}".format(period_var.get()));
		num_file.close;
	except ValueError:
		pass

def start_sm(*args):
	try:
		call(["/home/pi/mixed_proj/sm/sm6"]);
		set_button.focus();
	except ValueError:
		pass
		
def close_prog(*args):
	try:
		root.destroy();
	except ValueError:
		pass			
		
def entry_return_key(*args):
	if steps_var.get()=="":
		steps_entry.focus();
	elif dir_entry.get()=="":
		dir_entry.focus();
	elif time_var.get()=="":
		time_entry.focus();
	else:
		set_button.focus();

root = Tk();

#############Position#############
#w = 1000;
#h = 750;
#ws = root.winfo_screenwidth();
#hs = root.winfo_screenheight();
#x = (ws/2) - (w/2);
#y = (hs/2) - (h/2);
#root.geometry("%dx%d+%d+%d" % (w, h, x, y));
root.geometry("+700+370");
#root.geometry("+{0}+{1}".format(root.winfo_screenwidth(), root.winfo_screenheight()));
##################################

mainframe = ttk.Frame(root, padding="5 5 5 5");
mainframe.grid(column=0, row=0, sticky=(N, W, E, S));
mainframe.grid_columnconfigure(0, weight=1);
mainframe.grid_rowconfigure(0, weight=1);

points = [];
main_label_var      =StringVar();
period_var          =StringVar();
period_label_var    =StringVar();
direction_var       =StringVar();
direction_label_var =StringVar();
x_var               =StringVar();
x_label_var         =StringVar();
y_var               =StringVar();
y_label_var         =StringVar();
time_var            =StringVar();
time_label_var      =StringVar();

main_label    =ttk.Label(mainframe, textvariable=main_label_var);
period_label  =ttk.Label(mainframe, text="Period");
period_entry  =ttk.Entry(mainframe, textvariable=period_var);
period_button =ttk.Button(mainframe, text="Set period", command=period_write);
x_label       =ttk.Label(mainframe, text="X coord");
x_entry       =ttk.Entry(mainframe, textvariable=x_var);
y_label       =ttk.Label(mainframe, text="Y coord");
y_entry       =ttk.Entry(mainframe, textvariable=y_var);
time_label    =ttk.Label(mainframe, text="Time");
time_entry    =ttk.Entry(mainframe, textvariable=time_var);
set_button    =ttk.Button(mainframe, text="Set parameters", command=parameters_write);
start_button  =ttk.Button(mainframe, text="Start", command=start_sm);
quit_button   =ttk.Button(mainframe, text="Quit", command=close_prog);

main_label    .grid(column=1, columnspan=3, row=1,            sticky=(N, S)      );
period_label  .grid(column=1,               row=2,            sticky=(N, S, E)   );
period_entry  .grid(column=2,               row=2,            sticky=(N, S, E, W));
period_button .grid(column=3,  				row=2,            sticky=(N, S, E, W));
x_label       .grid(column=1,               row=3,            sticky=(N, S, E)   );
x_entry       .grid(column=2,               row=3,            sticky=(N, S, E, W));
y_label       .grid(column=1,               row=4,            sticky=(N, S, E)   );
y_entry       .grid(column=2,               row=4,            sticky=(N, S, E, W));
time_label    .grid(column=1,               row=5,            sticky=(N, S, E)   );
time_entry    .grid(column=2,               row=5,            sticky=(N, S, E, W));
set_button    .grid(column=3, 				row=3, rowspan=3, sticky=(N, S, E, W));
start_button  .grid(column=2, columnspan=2, row=6,            sticky=(N, S, E, W));
quit_button   .grid(column=1, 		        row=6,            sticky=(N, S, E, W));

period_entry  .bind('<Return>', entry_return_key);
period_button .bind('<Return>', period_write    );
x_entry       .bind('<Return>', entry_return_key);
y_entry       .bind('<Return>', entry_return_key);
time_entry    .bind('<Return>', entry_return_key);
set_button    .bind('<Return>', parameters_write); 
start_button  .bind('<Return>', start_sm        );

x_entry.focus();
main_label_var.set("Set parameters");




#ttk.Button(mainframe, text="Set time", command=time_write).grid(column=2, row=3, sticky=(N, S, E, W));




for child in mainframe.winfo_children(): child.grid_configure(padx=5, pady=5);
root.mainloop()	
