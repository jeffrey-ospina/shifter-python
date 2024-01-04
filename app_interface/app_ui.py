import customtkinter as ctk

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

# Boton salir
        #self.stop_button = ctk.CTkButton(self.app,
                                        #text="Salir",
                                        #text_color="white",
                                        #hover_color="#ff6363",
                                        #fg_color="#ff0000",
                                        #width=50,
                                        #border_width=1,
                                        #command=log_out)
        #self.stop_button.grid(column=1,
                            #row=1,
                            #padx=15,
                            #pady=5,
                            #ipadx=10,)

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

    # Obtener valores ingresados
    def get_credentials(self):
        email = self.email_entry.get()
        password = self.password_entry.get()
        print("Correo", email)
        print("Clave", password)

    # Funcion para la apertura de la ventana
    def start(self):
        self.app.mainloop()
