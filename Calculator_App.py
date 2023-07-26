import tkinter as tk

def on_click(event):
    text = event.widget.cget("text")
    if text == "=":
        try:
            result = eval(display.get())
            display.set(result)
        except Exception as e:
            display.set("Error")
    elif text == "C":
        display.set("")
    else:
        display.set(display.get() + text)

root = tk.Tk()

root.title("Calculator App")
root.geometry("400x500")
root.configure(bg="#f0f0f0")

display = tk.StringVar()
entry = tk.Entry(root, textvar=display, font=("Helvetica", 20), bd=10, relief=tk.RIDGE, justify=tk.RIGHT)
entry.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

button_list = [
    
    ("C", "(", ")", "/"),
    ("7", "8", "9", "*"),
    ("4", "5", "6", "-"),
    ("1", "2", "3", "+"),
    ("0", ".", "=")
    
]

for row in button_list:
    frame = tk.Frame(root, bg="#f0f0f0")
    frame.pack(fill=tk.BOTH, expand=True)
    for button_text in row:
        button = tk.Button(frame, text=button_text, font=("Helvetica", 20), relief=tk.GROOVE, bd=3)
        button.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        button.bind("<Button-1>", on_click)

root.mainloop()