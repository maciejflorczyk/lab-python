import customtkinter as ctk
from tkinter import filedialog

def wybierz_plik():
    path = filedialog.askopenfilename()
    if path:
        label.configure(text=path)

app = ctk.CTk()
app.title("Moje GUI")
app.geometry("600x400")

label = ctk.CTkLabel(app, text="Wybierz plik")
label.pack(pady=20)

button = ctk.CTkButton(app, text="Dodaj plik", command=wybierz_plik)
button.pack()

app.mainloop()
