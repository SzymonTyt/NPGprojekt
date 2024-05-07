import tkinter as tk


def button_clicked():
    print("Button clicked!")

root = tk.Tk()


button = tk.Button(root,
                   text="Press to start",
                   command=button_clicked,
                   activebackground="pink",
                   activeforeground="black",
                   anchor="center",
                   bd=3,
                   bg="lightblue",
                   cursor="hand2",
                   disabledforeground="gray",
                   fg="black",
                   font=("Arial", 12),
                   height=2,
                   highlightbackground="black",
                   highlightcolor="green",
                   highlightthickness=2,
                   justify="center",
                   overrelief="raised",
                   padx=10,
                   pady=5,
                   width=15,
                   wraplength=100)

button.pack(padx=20, pady=20)

root.mainloop()
