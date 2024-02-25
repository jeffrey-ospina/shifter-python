import tkinter as tk
from tkinter import ttk
from tkinter import *
from tkcalendar import DateEntry
from babel.numbers import *

class LoginApp:
        def __init__(self, log_in, log_out):
                # Instancia principal de la ventana
                self.app = tk.Tk()

                # Se declara el tamaño de la ventana
                height = 270
                width = 270
                x = (self.app.winfo_screenwidth()//2)-(width//2)
                y = (self.app.winfo_screenheight()//2)-(height//2)
                self.app.geometry('{}x{}+{}+{}'.format(width, height, x, y))
                self.app.resizable(False, False)

                self.app.columnconfigure(0, weight=2)
                self.app.columnconfigure(1, weight=1)

                # Nombre de ventana
                self.app.wm_title("Shifter App")  # Modificación aquí

                # Icono de ventana
                self.app.iconbitmap('C:\\Users\\user\\Documents\\shifter-python\\assets\\smartphone.ico')

                # Correo
                self.email_label = tk.Label(self.app, text= "Correo:", font=("Calibri", 10)).grid(column=0, row=0, sticky="W", padx=20, pady=5)
                self.email_entry = tk.Entry(self.app, font= ("Calibri", 10)).grid(column=1, row=0, sticky="E", padx=20, pady=5)

                # Clave
                self.password_label = tk.Label(self.app, text= "Clave:", font=("Calibri", 10)).grid(column=0, row=1, sticky="W", padx=20, pady=5)
                self.password_entry = tk.Entry(self.app, font= ("Calibri", 10)).grid(column=1, row=1, sticky="E", padx=20, pady=5)

                # Lista despegable
                self.menu = ttk.Combobox(self.app, values=["Seleccione país", "Estados Unidos"], state="readonly", font=("Calibri", 10))
                self.menu.current(0)
                self.menu.grid(row=2, columnspan=3, sticky="EW", padx= 20, pady=5)

                # Fecha
                cal = DateEntry(self.app, locale="es_US", date_pattern="dd-mm-yy", width= 10, background= "darkblue", foreground= "white", borderwidth=2, showweeknumbers=False, firstweekday="monday")
                cal.grid(column= 0, columnspan=3, row=3, sticky="EW", padx=20, pady=5)

                # Ingreso de hora
                self.hora_label = tk.Label(self.app, text="Hora: (H:M)", font=("Calibri", 10)).grid(column=0, row=4, sticky="W", padx=15, ipadx=20, pady=5)
                self.hora_entry = tk.Entry(self.app, width=15, font= ("Calibri", 10)).grid(column=1, row=4, sticky="NS", padx=20, pady=5)

                # Caja de texto
                text = Text(self.app, height=3)
                text.grid(column=0, columnspan=3, row=6, sticky="EW", padx=20, pady=5)

                # Boton de ingreso
                login_button = tk.Button(self.app, 
                        text="Ingresar",
                        font=("Calibri", 10),
                        fg='white', 
                        bg='green',
                        command=log_in 
                        ).grid(column=0, columnspan=3, row=7, sticky="NS", pady=10)

        def start(self):
                self.app.mainloop()