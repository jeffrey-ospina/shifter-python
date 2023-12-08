from time import sleep
from app_interface.app_ui import LoginApp
from app_run.app_handler import start_app

# Ejecucion principal del codigo
def open_app():
    # Iniciar la aplicación
    driver = start_app()  

    #try:
    sleep(8)

    omitir_1 = driver.find_element('xpath', value='//android.widget.TextView[@resource-id="com.mercadolibre:id/andes_button_text" and @text="Omitir"]')
    if omitir_1:
        print("Omitiendo pantalla")
        omitir_1.click()
    else:
        print("No se ha podido encontrar el boton de omitir")


    sleep(8)
    menu = driver.find_element("xpath", value='//android.widget.ImageButton[@content-desc="Menú"]')
    if menu:
        print("Se ha encontrado el menú")
        menu.click()
    else:
        print("No se ha podido encontrar el menú")

    sleep(6)
    ingresar = driver.find_element("id", value="com.mercadolibre:id/profile_drawer_action_btn")
    if ingresar:
        print("Se ha encontrado el botón de ingreso a mi perfil")
        ingresar.click()
    else:
        print("No se ha podido encontrar el botón de ingreso a mi perfil")

    sleep(6)
    omitir_2 = driver.find_element("id", value="com.google.android.gms:id/cancel")
    if omitir_2:
        print("Se ha encontrado el botón de omitir")
        omitir_2.click()
    else:
        print("No se ha podido encontrar el botón de omitir")

    sleep(6)
    correo = driver.find_element('xpath', value='//android.widget.EditText[@resource-id="com.mercadolibre:id/andes_textfield_edittext"]')
    if correo:
        print("Ingresando correo")
        correo.send_keys('jeffreyospina16@gmail.com')
    else:
        print("No se ha podido encontrar el campo para ingresar el correo")

    sleep(6)
    continuar = driver.find_element('xpath', value='//android.widget.TextView[@resource-id="com.mercadolibre:id/andes_button_text" and @text="Continuar"]')
    if continuar: 
        print("Continuando con el proceso")
        continuar.click()
    else:
        print("No se ha podido encontrar el botón de continuar")
    #except Exception as e:
        # Si ocurre algún error, captura la excepción e imprime un mensaje
        #print(f"Ocurrió un error: {e}")

# Función para la ejecucion del codigo
def log_in():
    open_app()

interface = LoginApp(log_in, lambda: None)
interface.start()