#!/usr/bin/python3
from subprocess import Popen
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
import RPi.GPIO as GPIO

class Point:
	def __init__(self, x_coord, y_coord, p_delay):
		self.x=x_coord;
		self.y=y_coord;
		self.delay=p_delay;

class list:
	def last(self):
			return self[len(self)-1];
		
#def parameters_write(*args):
	#try:
		#pic_file=open("pic_file", 'w');
		#pic_file.write("{0} {1} {2}".format(x_var.get(), y_var.get(), time_var.get()));
		#pic_file.close;
		##num_file=open("num_file", 'w');
		##num_file.write("12 %s" % time_var.get());
		##num_file.close;
		#main_label_var.set("Point X:{0}; Y:{1} with delay of {2}ms was added".format(x_var.get(), y_var.get(), time_var.get()));
		#start_button.focus();
	#except ValueError:
		#pass
		
#def period_write(*args):
	#try:
		#num_file=open("num_file", 'w');
		#num_file.write("12 {0}".format(time_var.get()));
		#num_file.close;
	#except ValueError:
		#pass

def start_sm(*args):
	try:
		#call(["/home/pi/mixed_proj/sm/sm6"]);
		#set_button.focus();
		global sm_proc;
		sm_proc=Popen("/home/pi/mixed_proj/sm/sm6");
		#sm_proc.wait();
		#stop_button.enable();
	except ValueError:
		pass
		
def stop_sm(*args):
	try:
		sm_proc.terminate();
		GPIO.setmode(GPIO.BOARD);
		GPIO.setwarnings(False);
		for i in (11, 12, 13, 15, 16, 18):
			GPIO.setup(i,GPIO.OUT, initial=GPIO.LOW);
		#set_button.focus();
	except ValueError:
		pass
		
def close_prog(*args):
	try:
		root.destroy();
	except ValueError:
		pass			
		
def add_point(*args):
	try:
		p=Point(x_var.get(),y_var.get(),time_var.get());
		points.append(p);
		tree.insert("", "end", values=(points[len(points)-1].x, points[len(points)-1].y, points[len(points)-1].delay));
	except ValueError:
		pass 

def open_file(*args):
	filename = filedialog.askopenfilename();
	return filename;		
		
#def entry_return_key(*args):
	#if steps_var.get()=="":
		#steps_entry.focus();
	#elif dir_entry.get()=="":
		#dir_entry.focus();
	#elif time_var.get()=="":
		#time_entry.focus();
	#else:
		#set_button.focus();

root = Tk();

root.geometry("+700+370");


mainframe = ttk.Frame(root, padding="5 5 5 5");
mainframe.grid(column=0, row=0, sticky=(N, W, E, S));
mainframe.grid_columnconfigure(0, weight=1);
mainframe.grid_rowconfigure(0, weight=1);

points = [];
main_label_var      =StringVar();
quit_button   =ttk.Button(mainframe, text="Quit",   command=close_prog);
main_label    =ttk.Label(mainframe, textvariable=main_label_var);
start_button  =ttk.Button(mainframe, text="Start", command=start_sm);
x_right_button=ttk.Button(mainframe, text="Right");
y_right_button=ttk.Button(mainframe, text="Left");
x_left_button =ttk.Button(mainframe, text="Up");
y_left_button =ttk.Button(mainframe, text="Down");
stop_button   =ttk.Button(mainframe, text="STOP", command=stop_sm);

#open_button=ttk.Button(mainframe, text="open", command=open_file);
main_label    .grid(column=1, row=1,            sticky=(N, S)      );
start_button  .grid(column=1, row=2,            sticky=(N, S, E, W));
quit_button   .grid(column=1, row=3,            sticky=(N, S, E, W));
#open_button   .grid(column=1, row=2,            sticky=(N, S, E, W));
x_right_button.grid(column=4, row=2,            sticky=(N, S, E, W));
y_right_button.grid(column=3, row=1,            sticky=(N, S, E, W));
x_left_button .grid(column=2, row=2,            sticky=(N, S, E, W));
y_left_button .grid(column=3, row=3,            sticky=(N, S, E, W));
stop_button   .grid(column=3, row=2,            sticky=(N, S, E, W));
#main_label_var=open_file();
	
#start_button  .bind('<Return>', start_sm        );

#main_label_var.set("Set parameters");

for child in mainframe.winfo_children(): child.grid_configure(padx=5, pady=5);
root.mainloop()	
