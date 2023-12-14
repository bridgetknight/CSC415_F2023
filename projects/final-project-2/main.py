import tkinter as tk
import tkinter.ttk as ttk
from tkinter import *
import runpy
import io
from timeit import default_timer as timer
import sys

examples = {"Hello World": "examples/hello.py",
            "Selection Sort": "examples/selection_sort.py",
            "Insertion Sort": "examples/insertion_sort.py",
            "Bubble Sort": "examples/bubble_sort.py"}

def run_code():
    # This function will be called when the run button is clicked.
    code = textbox.get("1.0", tk.END)
    print(f">>> {code}")

    # Save code input to temporary file
    with open("tmp/input_code.py", "w") as f:
        f.write(code);

    # Execution
    output_text.configure(state='normal')
    try:
        # Capture output from code
        tmp = sys.stdout
        captured_output = io.StringIO()
        sys.stdout = captured_output

        # Run code using runpy
        start = timer()
        result = runpy.run_path("tmp/input_code.py", init_globals={}, run_name="__main__")
        end = timer()
        elapsedTime = end-start
        elapsedTime = str(elapsedTime)[:7]

        sys.stdout = tmp
        print(captured_output.getvalue())

        # Clean and append to output
        output_text.delete("1.0", tk.END)
        output_text.insert(tk.END, captured_output.getvalue())
        output_text.insert(tk.END, 
        f'''Elapsed time: {elapsedTime}''')
        print(f"Output: {captured_output.getvalue()}")

    except Exception as e:
        output_text.delete("1.0", tk.END)
        output_text.insert(tk.END, f"Error: {e}")
    output_text.configure(state='disabled')

def example_algorithm(*args):
    # Function to change input text based on selected example algorithm
    print(tkvar)
    chosen_option = examples[tkvar.get()]
    print(chosen_option)

    with open(chosen_option, "r") as file:
        data =  file.read()
    textbox.delete("1.0", tk.END)
    textbox.insert(tk.END, data)

if __name__ == "__main__":

    # Set up tkinter GUI
    root = tk.Tk()
    root.geometry("700x600")
    root.title("Benchmarker")
    root.config(background='#34435E', padx=10, pady=10)
   # root.grid_rowconfigure(1, weight=1)
   # root.grid_columnconfigure(0, weight=2)

    # Default input code
    tkvar = tk.StringVar(root)
    tkvar.set("Hello World")

    # Create the options menu for examples
    dropdown_frame = tk.Frame(root, width=450, height=10, pady=10, padx=2,bd=0, highlightthickness=0, relief='ridge')
    dropdown_frame.grid(row=0, sticky="w",)
    dropdown_menu = tk.OptionMenu(dropdown_frame, tkvar, *examples.keys())
    dropdown_menu.config(width=20)
    dropdown_menu.grid(row=1, column=1)

    dd_label = Label(dropdown_frame, text="Select an example algorithm:", font='Arial 10 bold',bd=0, highlightthickness=0, relief='ridge')
    dd_label.grid(row=0, column=1, pady=(5,0), sticky="W")
    
    tkvar.trace("w", example_algorithm)

    # Create text input box
    input_frame = tk.Frame(root, width=10, height=10,bd=0, highlightthickness=0, relief='ridge')
    
    # Horizontal (x) Scroll bar
    xscrollbar = Scrollbar(input_frame, orient=HORIZONTAL)

    # Vertical (y) Scroll Bar
    yscrollbar = Scrollbar(input_frame)
    
    input_frame.grid(row=1, sticky="ew")
    twidth = 84
    theight = 10
    textbox = tk.Text(input_frame, width=twidth, height=theight,
                xscrollcommand=xscrollbar.set,
                yscrollcommand=yscrollbar.set,
                wrap=WORD,bd=0, highlightthickness=0, relief='ridge')
    textbox.grid(row=3, column=0)

    in_label = Label(input_frame, text="Input", font='Arial 10 bold',bd=0, highlightthickness=0, relief='ridge')
    in_label.grid(row=2, column=0, sticky="W", pady=(5,2))

    run_button = tk.Button(input_frame, width=3, height=1, text="Run", command=run_code, padx=4, pady=3, bg="#87c98f",bd=0, highlightthickness=0, relief='ridge')
    run_button.grid(row=2, column=0, sticky="E")

    # Load default code
    with open("examples/hello.py", "r") as file:
        data =  file.read()
    textbox.delete("1.0", tk.END)
    textbox.insert(tk.END, data)

    # Create output box
    output_text = tk.Text(input_frame, width=84, height=10, wrap=WORD,bd=0, highlightthickness=0, relief='ridge')
    output_text.grid(row=5, column=0)
    output_text.config(state="disabled")
    out_label = Label(input_frame, text="Output", font="Arial 10 bold",bd=0, highlightthickness=0, relief='ridge')
    out_label.grid(row=4, column=0, sticky="W", pady=(10,2))

    # Start the main loop
    root.mainloop()
