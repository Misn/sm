#!/usr/bin/python3
from subprocess import call
from tkinter import *
from tkinter import ttk

class Point:
	def __init__(self, x_coord, y_coord, p_delay):
		self.x=x_coord;
		self.y=y_coord;
		self.delay=p_delay;

		
#def parameters_write(*args):
	#try:
		#pic_file=open("pic_file", 'w');
		#pic_file.write("{0} {1} {2}".format(x_var.get(), y_var.get(), delay_var.get()));
		#pic_file.close;
		##num_file=open("num_file", 'w');
		##num_file.write("12 %s" % time_var.get());
		##num_file.close;
		#main_label_var.set("Point X:{0}; Y:{1} with delay of {2}ms was added".format(x_var.get(), y_var.get(), delay_var.get()));
		#start_button.focus();
	#except ValueError:
		#pass
		
#def period_write(*args):
	#try:
		#num_file=open("num_file", 'w');
		##num_file.write("12 {0}".format(time_var.get()));
		#num_file.close;
	#except ValueError:
		#pass

#def start_sm(*args):
	#try:
		#call(["/home/pi/mixed_proj/sm/sm6"]);
		#set_button.focus();
	#except ValueError:
		#pass
		
def close_prog(*args):
	try:
		root.destroy();
	except ValueError:
		pass			
		
def fields_check(*args):
	if x_var.get()=="":
		main_label_var.set("Set X coord");
		x_entry.focus();
		return 0;
	elif y_var.get()=="":
		main_label_var.set("Set Y coord");
		y_entry.focus();
		return 0;
	elif delay_var.get()=="":
		main_label_var.set("Set Delay");
		delay_entry.focus();
		return 0;
	else:
		return 1;

def add_point(*args):
	try:
		#p=Point(x_var.get(),y_var.get(),delay_var.get());
		#points.append(p);
		#tree.insert("", "end", values=(points[len(points)-1].x, points[len(points)-1].y, points[len(points)-1].delay));
		if (fields_check()):
			tree.insert("", "end", values=(x_var.get(), y_var.get(), delay_var.get()));
	except ValueError:
		pass 
		
def swap_up(*args):
	try:
		a=1
	except ValueError:
		pass 
def swap_down(*args):
	try:
		a=1
	except ValueError:
		pass 
def point_del(*args):
	try:
		a=1;
		#tree.insert(tree.selection, "end", values=("x", "x", "x"));
	except ValueError:
		pass 
	
		
def entry_return_key(*args):
	if x_var.get()=="":
		x_entry.focus();
	elif y_var.get()=="":
		y_entry.focus();
	elif delay_var.get()=="":
		delay_entry.focus();
	else:
		add_button.focus();

root = Tk();


root.geometry("+700+370");


mainframe = ttk.Frame(root, padding="5 5 5 5");
mainframe.grid(column=0, row=0, sticky=(N, W, E, S));
mainframe.grid_columnconfigure(0, weight=1);
mainframe.grid_rowconfigure(0, weight=1);

points = [];
main_label_var      =StringVar();
#period_var          =StringVar();
#period_label_var    =StringVar();
#direction_var       =StringVar();
#direction_label_var =StringVar();
x_var               =StringVar();
#x_label_var         =StringVar();
y_var               =StringVar();
#y_label_var         =StringVar();
delay_var            =StringVar();
#delay_label_var      =StringVar();

main_label    =ttk.Label(mainframe, textvariable=main_label_var);
#period_label  =ttk.Label(mainframe, text="Period");
#period_entry  =ttk.Entry(mainframe, textvariable=period_var);
#period_button =ttk.Button(mainframe, text="Set period", command=period_write);
x_label       =ttk.Label(mainframe, text="X coord");
x_entry       =ttk.Entry(mainframe, textvariable=x_var);
y_label       =ttk.Label(mainframe, text="Y coord");
y_entry       =ttk.Entry(mainframe, textvariable=y_var);
delay_label   =ttk.Label(mainframe, text="Delay");
delay_entry   =ttk.Entry(mainframe, textvariable=delay_var);
#set_button    =ttk.Button(mainframe, text="Set parameters")#, command=parameters_write);
add_button    =ttk.Button(mainframe, text="Add point", command=add_point);
#start_button  =ttk.Button(mainframe, text="Start", command=start_sm);
quit_button   =ttk.Button(mainframe, text="Quit",   command=close_prog);
up_button     =ttk.Button(mainframe, text="UP",     command=swap_up);
down_button   =ttk.Button(mainframe, text="DOWN",   command=swap_down);
del_button    =ttk.Button(mainframe, text="Delete", command=point_del);

main_label    .grid(column=1, columnspan=3, row=1,            sticky=(N, S)      );
#period_label  .grid(column=1,               row=2,            sticky=(N, S, E)   );
#period_entry  .grid(column=2,               row=2,            sticky=(N, S, E, W));
#period_button .grid(column=3,               row=2,            sticky=(N, S, E, W));
x_label       .grid(column=1,               row=2,            sticky=(N, S, E)   );
x_entry       .grid(column=2,               row=2,            sticky=(N, S, E, W));
y_label       .grid(column=1,               row=3,            sticky=(N, S, E)   );
y_entry       .grid(column=2,               row=3,            sticky=(N, S, E, W));
delay_label   .grid(column=1,               row=4,            sticky=(N, S, E)   );
delay_entry   .grid(column=2,               row=4,            sticky=(N, S, E, W));
#set_button    .grid(column=2,               row=1, rowspan=3, sticky=(N, S, E, W));
add_button    .grid(column=3,               row=2, rowspan=3, sticky=(N, S, E, W));
#start_button  .grid(column=2, columnspan=2, row=6,            sticky=(N, S, E, W));
quit_button   .grid(column=1, columnspan=3, row=8,            sticky=(N, S, E, W));
up_button     .grid(column=3,               row=5,            sticky=(N, S, E, W));
down_button   .grid(column=3,               row=6,            sticky=(N, S, E, W));
del_button    .grid(column=3,               row=7,            sticky=(N, S, E, W));

#period_entry  .bind('<Return>', entry_return_key);
#period_button .bind('<Return>', period_write    );
x_entry       .bind('<Return>', entry_return_key);
y_entry       .bind('<Return>', entry_return_key);
delay_entry   .bind('<Return>', entry_return_key);
#set_button    .bind('<Return>', parameters_write); 
add_button    .bind('<Return>', add_point); 
#start_button  .bind('<Return>', start_sm        );

x_entry.focus();
main_label_var.set("Set parameters");


tree = ttk.Treeview(mainframe, selectmode="browse");

tree["columns"]=("x", "y", "delay");
tree.column("x", width=50);
tree.column("y", width=50);
tree.column("delay", width=100);
tree.heading("x", text="X");
tree.heading("y", text="Y");
tree.heading("delay", text="Delay");
tree.grid(column=1, columnspan=2, row=5, rowspan=3);
tree['show']='headings';

tree.insert("", 0, values=("100", "100", "500"));
#tree.pack;

for child in mainframe.winfo_children(): child.grid_configure(padx=5, pady=5);
root.mainloop()	
