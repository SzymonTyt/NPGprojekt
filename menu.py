from customtkinter import CTk, CTkButton, CTkSlider, CTkFrame, set_appearance_mode, CTkComboBox, CTkToplevel, CTkLabel


def start_game(): #funkcja po naciśnięcia przycisku "start"
    print("Game started")

def quit_game(): #funkcja po naciśnięcia przycisku "wyjście"
    app.destroy()

def open_settings(): #funkcja po naciśnięcia przycisku "ustawienia"
    def sliding(value):
        volume_label.configure(text=int(value))

#ustawienia okna ustawień
    settings_window = CTkToplevel()
    settings_window.title("Ustawienia")
    settings_window.geometry("500x400")
    settings_window.title("Settings")
    settings_window.resizable(False, False)

    frame2 = CTkFrame(settings_window)
    frame2.pack(pady=40)
    frame2.configure(width=500, height=600)

#ustawienia paska głośności
    volume_label = CTkLabel(frame2, text="Głośność", font=("", 14,))
    volume_label.grid(row=0, column=1, padx=0, pady=8)
    volume = CTkSlider(frame2, from_=0, to=100, orientation="horizontal", fg_color="#4158D0",
                       command=sliding)
    volume.grid(row=1, column=1, padx=0, pady=16)
    volume.set(50)

#ustawienia wyboru poziomu trudności    
    difficulty_label = CTkLabel(frame2, text="Poziom trudności", font=("", 14))
    difficulty_label.grid(row=2, column=1, padx=0, pady=8)
    difficulty = CTkComboBox(frame2, corner_radius=32, values=["Łatwy", "Średni", "Trudny"])
    difficulty.grid(row=3, column=1, padx=0, pady=16)

#ustawienia przycisku powrotu do menu
    back_button_label = CTkLabel(frame2, text="Głośność", font=("", 14))
    back_button_label.grid(row=4, column=1, padx=0, pady=8)
    back_button = CTkButton(frame2, text="Powrót Do Menu", corner_radius=32, fg_color="#4158D0", hover_color="#C850C0",
                            command=settings_window.destroy)
    back_button.grid(row=5, column=1, columnspan=2, pady=16)
    settings_window.mainloop()

#ustawienia okna menu
app = CTk()
app.title("Menu Gry")
app.geometry("500x400")
set_appearance_mode("dark")
app.resizable(False, False)

frame = CTkFrame(app)
frame.pack(pady=60)

#przycisk start
start_button = CTkButton(frame, text="Start", corner_radius=32, fg_color="#4158D0", hover_color="#C850C0", command=start_game)
start_button.grid(row=0, column=0, padx=50, pady=30)

#przycisk ustawień
settings_button = CTkButton(frame, text="Ustawienia", corner_radius=32, fg_color="#4158D0", hover_color="#C850C0", command=open_settings)
settings_button.grid(row=1, column=0, padx=50, pady=30)

#przycisk wyjścia
quit_button = CTkButton(frame, text="Wyjście", corner_radius=32, fg_color="#4158D0", hover_color="#C850C0",
                        command=quit_game)
quit_button.grid(row=2, column=0, padx=50, pady=30)


app.mainloop()
