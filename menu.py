from customtkinter import CTk, CTkButton, CTkSlider, CTkFrame, set_appearance_mode, CTkComboBox, CTkToplevel, CTkLabel


def start_game():
    print("Game started")


def quit_game():
    app.destroy()

def open_settings():
    print("Settings opened")

app = CTk()
app.title("Menu Gry")
app.geometry("500x400")
set_appearance_mode("dark")
app.resizable(False, False)

frame = CTkFrame(app)
frame.pack(pady=60)

start_button = CTkButton(frame, text="Start", corner_radius=32, fg_color="#4158D0", hover_color="#C850C0", command=start_game)
start_button.grid(row=0, column=0, padx=50, pady=30)

settings_button = CTkButton(frame, text="Ustawienia", corner_radius=32, fg_color="#4158D0", hover_color="#C850C0", command=open_settings)
settings_button.grid(row=1, column=0, padx=50, pady=30)

quit_button = CTkButton(frame, text="Wyjście", corner_radius=32, fg_color="#4158D0", hover_color="#C850C0",
                        command=quit_game)
quit_button.grid(row=2, column=0, padx=50, pady=30)

app.mainloop()
