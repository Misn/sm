#!/usr/bin/python3
from subprocess import call
from tkinter import *
from tkinter import ttk

def parameters_write(*args):
	try:
		pic_file=open("pic_file", 'w');
		if (dir_entry.get()=="Right"):
			pic_file.write("%s 10 500" % steps_var.get());
		else:
			pic_file.write("-%s 10 500" % steps_var.get());
		pic_file.close;
		num_file=open("num_file", 'w');
		num_file.write("12 %s" % time_var.get());
		num_file.close;
		main_label_var.set("SM will make {0} steps in {1} direction with {2}ms delay on step".format(steps_var.get(), dir_entry.get(), time_var.get()));
		start_button.focus();
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
##################################

mainframe = ttk.Frame(root, padding="5 5 5 5");
mainframe.grid(column=0, row=0, sticky=(N, W, E, S));
mainframe.grid_columnconfigure(0, weight=1);
mainframe.grid_rowconfigure(0, weight=1);

main_label_var = StringVar();
ttk.Label(mainframe, textvariable=main_label_var).grid(column=1, columnspan=3, row=1, sticky=(N, S));
main_label_var.set("Set parameters");

direction_var = StringVar();
direction_label_var = StringVar();
steps_var = StringVar();
steps_label_var = StringVar();
time_var = StringVar();
time_label_var = StringVar();

ttk.Label(mainframe, text="N steps").grid(column=1, row=2, sticky=(N, S, E));
ttk.Label(mainframe, text="Direction").grid(column=1, row=3, sticky=(N, S, E));
ttk.Label(mainframe, text="Delay").grid(column=1, row=4, sticky=(N, S, E));

steps_entry=ttk.Entry(mainframe, textvariable=steps_var);
steps_entry.grid(column=2, row=2, sticky=(N, S, E, W));
steps_entry.focus();
steps_entry.bind('<Return>', entry_return_key);

dir_entry = ttk.Combobox(mainframe, textvariable=direction_var, state="readonly");
dir_entry.grid(column=2, row=3, sticky=(N, S, E, W));
dir_entry['values']=('Right','Left');
dir_entry.bind('<Return>', entry_return_key);
#dir_entry.bind('<<ComboboxSelected>>', steps_write);

time_entry=ttk.Entry(mainframe, textvariable=time_var);
time_entry.grid(column=2, row=4, sticky=(N, S, E, W));
time_entry.bind('<Return>', entry_return_key);

#ttk.Button(mainframe, text="Set time", command=time_write).grid(column=2, row=3, sticky=(N, S, E, W));

set_button=ttk.Button(mainframe, text="Set parameters", command=parameters_write);
set_button.grid(column=3, row=2, rowspan=2, sticky=(N, S, E, W));
set_button.bind('<Return>', parameters_write);

start_button=ttk.Button(mainframe, text="Start", command=start_sm);
start_button.grid(column=3, row=4, sticky=(N, S, E, W));
start_button.bind('<Return>', start_sm);

ttk.Button(mainframe, text="Quit", command=close_prog).grid(column=1, columnspan=3, row=5, sticky=(N, S, E, W));

for child in mainframe.winfo_children(): child.grid_configure(padx=5, pady=5);
root.mainloop()	
