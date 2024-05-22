import tkinter as tk
from jnius import autoclass
from sudoku import solve

root = tk.Tk()
root.columnconfigure(0, weight=1)

frame = tk.Frame(root)
frame.grid(row=1, column=0)

title = tk.Label(root, text="Sudoku Solver", font=("calibre", 15, "bold"))
title.grid(row=0, column=0)

num_elements = 9
global_index = 0
entry_list = []
var_list = []

for x in range(num_elements):
		for y in range(num_elements):
			var = tk.StringVar()
			var_list.append(var)
			ent = tk.Entry(frame, width=2, justify="center", textvariable=var_list[global_index], font=("calibre", 10, "normal"))
			ent.grid(row=x, column=y)
			if (y+1) % 3 == 0:
				ent.grid(padx=(0,10))
			if (x+1) % 3 == 0:
				ent.grid(pady=(0,10))
			entry_list.append(ent)
			global_index += 1

def reset():
	for i in range(len(var_list)):
		var_list[i].set("")


def submit():
	global_index = 0
	board = [[0 for i in range(num_elements)] for j in range(num_elements)]
	for row in range(num_elements):
		for col in range(num_elements):
			if var_list[global_index].get() == "":
				board[row][col] = 0
			else:
				board[row][col] = int(var_list[global_index].get())
			global_index += 1
	solve(board)
	global_index = 0
	for row in range(num_elements):
		for col in range(num_elements):
			var_list[global_index].set(str(board[row][col]))
			global_index += 1
			
			
def keyboard():
    InputMethodManager = autoclass("android.view.inputmethod.InputMethodManager")
    PythonActivity = autoclass("org.kivy.android.PythonActivity")
    Context = autoclass("android.content.Context")
    activity = PythonActivity.mActivity
    service = activity.getSystemService(Context.INPUT_METHOD_SERVICE)
    service.toggleSoftInput(InputMethodManager.SHOW_FORCED, 0)
			

solve_btn = tk.Button(root, text="Solve", command=submit)
solve_btn.grid(row=2, column=0)
reset_btn = tk.Button(root, text="Reset", command=reset)
reset_btn.grid(row=3, column=0)
keyboard_btn = tk.Button(root, text="Keyboard", command=keyboard)
keyboard_btn.grid(row=4, column=0)

root.mainloop()