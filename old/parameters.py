#!/usr/bin/python3
from subprocess import call
from tkinter import *
from tkinter import ttk

def direction_write(*args):
	try:
		#ex_var=dir_var;
		direction_label_var.set(dir_set.get());
	except ValueError:
		pass	

def steps_write(*args):
	try:
		steps_label_var.set(steps_var.get());
		pic_file=open("pic_file", 'w');
		if (dir_set.get()=="Right"):
			pic_file.write("%s 10 500" % steps_var.get());
		else:
			pic_file.write("-%s 10 500" % steps_var.get());
		pic_file.close;
		direction_label_var.set(dir_set.get());
	except ValueError:
		pass

def time_write(*args):
	try:
		time_label_var.set(time_var.get());
		num_file=open("num_file", 'w');
		num_file.write("12 %s" % time_var.get());
		num_file.close;
	except ValueError:
		pass
		
def start_sm(*args):
	try:
		call(["/home/pi/mixed_proj/sm/sm6"])
	except ValueError:
		pass
		
def close_prog(*args):
	try:
		root.destroy();
	except ValueError:
		pass			

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
##################################

mainframe = ttk.Frame(root, padding="5 5 5 5");
mainframe.grid(column=0, row=0, sticky=(N, W, E, S));
mainframe.grid_columnconfigure(0, weight=1);
mainframe.grid_rowconfigure(0, weight=1);

direction_var = StringVar();
direction_label_var = StringVar();
steps_var = StringVar();
steps_label_var = StringVar();
time_var = StringVar();
time_label_var = StringVar();

ttk.Label(mainframe, textvariable=steps_label_var).grid(column=3, row=1, sticky=(N, S, E, W));
ttk.Button(mainframe, text="Set number of steps", command=steps_write).grid(column=2, row=1, rowspan=2, sticky=(N, S, E, W));
steps_entry=ttk.Entry(mainframe, textvariable=steps_var);
steps_entry.grid(column=1, row=1, sticky=(N, S, E, W));
steps_entry.focus();
steps_entry.bind('<Return>', steps_write);


#ttk.Button(mainframe, text="Set direction", command=direction_write).grid(column=2, row=2, sticky=(N, S, E, W));
dir_set = ttk.Combobox(mainframe, textvariable=direction_var);
dir_set.grid(column=1, row=2, sticky=(W));
dir_set['values']=('Right','Left');
ttk.Label(mainframe, textvariable=direction_label_var).grid(column=3, row=2, sticky=(N, S, E, W));
dir_set.bind('<Return>', steps_write);
dir_set.bind('<<ComboboxSelected>>', steps_write);
#dir_set.bind('<<ComboboxSelected>>', ex_func);

ttk.Label(mainframe, textvariable=time_label_var).grid(column=3, row=3, sticky=(N, S, E, W));
ttk.Button(mainframe, text="Set time", command=time_write).grid(column=2, row=3, sticky=(N, S, E, W));
time_entry=ttk.Entry(mainframe, textvariable=time_var);
time_entry.grid(column=1, row=3, sticky=(N, S, E, W));
time_entry.bind('<Return>', time_write);

ttk.Button(mainframe, text="Start", command=start_sm).grid(column=0, columnspan=2, row=4, rowspan=2, sticky=(N, S, E, W));

ttk.Button(mainframe, text="Quit", command=close_prog).grid(column=2, columnspan=2, row=4, rowspan=2, sticky=(N, S, E, W));

for child in mainframe.winfo_children(): child.grid_configure(padx=5, pady=5);
root.mainloop()	
