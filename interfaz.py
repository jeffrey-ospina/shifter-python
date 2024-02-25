from tkcalendar import DateEntry
import customtkinter as ctk
import tkinter as tk

# Escoger el color de la ventana para GUI - dark, light o system para color segun el SO
ctk.set_appearance_mode("light")

# Escoger el color del tema de la ventana
ctk.set_default_color_theme("blue")

# Crear ventana con botón para iniciar y detener la calculadora
class LoginApp:
    def __init__(self, log_in, log_out):
        self.app = ctk.CTk()
        self.app.title("Shifter App")
        self.app.resizable(False, False)
        self.app.iconbitmap('C:\\Users\\user\\Documents\\shifter-python\\assets\\smartphone.ico')

# Entry para ingresar el correo
        self.email_entry= ctk.CTkEntry(self.app, placeholder_text="Correo")
        self.email_entry.grid(column=0,
                            row=0,
                            padx=15,
                            pady=5,
                            ipadx=10)

# Entry para ingresar la clave
        self.password_entry= ctk.CTkEntry(self.app, placeholder_text="Clave")
        self.password_entry.grid(column=0,
                                row=1,
                                padx=15,
                                pady=5,
                                ipadx=10)

# Boton de ingresar
        self.start_button = ctk.CTkButton(self.app,
                                        text="Ingresar",
                                        text_color="white",
                                        hover_color="#45c451",
                                        fg_color="#2ea63a",
                                        width=50,
                                        border_width=1,
                                        command=log_in)
        self.start_button.grid(column=1,
                            row=3,
                            #sticky=ctk.E,
                            padx=15,
                            pady=5,
                            ipadx=10)
        
        # Boton de ingresar PRUEBA
        self.start_button = ctk.CTkButton(self.app,
                                        text="Imprimir",
                                        text_color="white",
                                        hover_color="#45c451",
                                        fg_color="#2ea63a",
                                        width=50,
                                        border_width=1,
                                        command=None)
        self.start_button.grid(column=1,
                            row=2,
                            #sticky=ctk.E,
                            padx=15,
                            pady=5,
                            ipadx=10)

# Menu desplegable
        self.option_menu = ctk.CTkOptionMenu(self.app,
                                    values=["Estados Unidos"])
        self.option_menu.grid(column=0,
                            row=2,
                            padx=15,
                            pady=5,
                            ipadx=10)
        self.option_menu.set("Seleccione pais")  # set initial value


# Caja de texto
        self.textbox = ctk.CTkTextbox(self.app,
                                    height=80,
                                    corner_radius=6,
                                    border_width=1)
        
        self.textbox.grid(column=0,
                        row=4,
                        columnspan=2,
                        padx=15,
                        pady=5,
                        ipadx=10)

# Selector de fecha 
        def select_date():
            cal = DateEntry(self.app, width=12, background='blue',
                    foreground='white', borderwidth=1, showweeknumbers=False, firstweekday='monday')
            cal.grid(padx=10, pady=10)

            select_date()

    # Obtener valores ingresados
    def credentials(self):
        self.email_value = self.email_entry.get()
        self.password_value = self.password_entry.get()

    # Funcion para la apertura de la ventana
    def start(self):
        self.app.mainloop()