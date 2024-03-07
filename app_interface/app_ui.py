from tkcalendar import DateEntry
from tkinter import Tk, Label, Entry, OptionMenu, StringVar, Text, Button
from babel.numbers import *


class LoginApp:
    def __init__(self, log_in):

        # Inicialización de la ventana principal de la aplicación
        app = Tk()

        # Configuración de la geometría de la ventana
        height = 270
        width = 270
        x = (app.winfo_screenwidth() // 2) - (width // 2)
        y = (app.winfo_screenheight() // 2) - (height // 2)
        app.geometry("{}x{}+{}+{}".format(width, height, x, y))
        app.resizable(False, False)

        # Configuración de columnas de la ventana
        app.columnconfigure(0, weight=2)
        app.columnconfigure(1, weight=1)

        # Título de la ventana
        app.title("Shifter App")

        # Etiqueta y entrada para el correo electrónico
        self.email_label = Label(app, text="Correo:", font=("Calibri", 10))
        self.email_label.grid(column=0, row=0, sticky="W", padx=20, pady=5)
        self.email_entry = Entry(app, font=("Calibri", 10))
        self.email_entry.grid(column=1, row=0, sticky="E", padx=20, pady=5)

        # Etiqueta y entrada para la contraseña
        self.password_label = Label(app, text="Clave:", font=("Calibri", 10))
        self.password_label.grid(column=0, row=1, sticky="W", padx=20, pady=5)
        self.password_entry = Entry(app, font=("Calibri", 10))
        self.password_entry.grid(column=1, row=1, sticky="E", padx=20, pady=5)

        # Lista desplegable para el país
        choices = ["Estados Unidos"]
        value_selected = StringVar(app)
        value_selected.set("Seleccione país")
        self.menu = OptionMenu(
            app,
            value_selected,
            *choices,
        )
        self.menu.grid(column=0, row=2, columnspan=3, sticky="EW", padx=20, pady=5)

        # Calendario
        self.calendar = DateEntry(
            app,
            locale="es_US",
            date_pattern="mm-dd-yy",
            width=10,
            background="darkblue",
            foreground="white",
            borderwidth=2,
            showweeknumbers=False,
            firstweekday="monday",
        )
        self.calendar.grid(column=0, columnspan=3, row=3, sticky="EW", padx=20, pady=5)

        # Entrada para la hora
        self.hora_label = Label(app, text="Hora: (H:M)", font=("Calibri", 10))
        self.hora_label.grid(column=0, row=4, sticky="W", padx=15, ipadx=20, pady=5)
        self.hora_entry = Entry(app, width=15, font=("Calibri", 10))
        self.hora_entry.grid(column=1, row=4, sticky="NS", padx=20, pady=5)

        # Caja de texto
        text = Text(app, height=3)
        text.grid(column=0, columnspan=3, row=6, sticky="EW", padx=20, pady=5)

        # Botón de ingreso
        self.login_button = Button(
            app,
            text="Ingresar",
            font=("Calibri", 10),
            fg="white",
            bg="green",
            command=log_in,  # Asignamos la función de inicio de sesión al botón
        )
        self.login_button.grid(column=0, columnspan=3, row=7, sticky="NS", pady=10)

        # Método para iniciar el bucle principal de la aplicación
        app.mainloop()

    # def get_data(self):
    ## Extrae los datos introducidos por el usuario y devuelve una tupla con ellos
    # fecha_str = self.calendar.get()
    # hora_str = self.hora_entry.get().replace(":", "")
    # return fecha_str + " " + hora_str

    def on_login_button_click(correito):
        # Obtener los datos ingresados por el usuario
        # self.email = self.email_entry.get()
        # self.password = self.password_entry.get()

        print(correito)

    def get_email(self):
        # Método para obtener el correo electrónico ingresado
        return self.email

    def get_password(self):
        # Método para obtener la contraseña ingresada
        return self.password
