from time import sleep
from app_interface.app_ui import LoginApp
from app_run.app_handler import start_app

# Ejecucion principal del codigo
def open_app():
    # Iniciar la aplicación
    driver = start_app()  

    #try:
    sleep(8)

    omitir = driver.find_element('xpath', value='//android.widget.TextView[@resource-id="com.mercadolibre:id/andes_button_text" and @text="Omitir"]')
    if omitir:
        print("Omitiendo pantalla")
        omitir.click()
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
    buscar = driver.find_element("xpath", value='//*[contains(@text, "Buscar")]')


    #driver.find_element('xpath', value='//android.view.View[@resource-id=\"guided-phone-form\"/android.widget.TextView/android.widget.Button and @text=\"Iniciar sesión con correo electrónico y contraseña\"]').click()
    #driver.find_element('xpath', value='//android.view.View[@resource-id=\"guided-phone-form\"]/android.widget.TextView/android.widget.Button and @text="Iniciar sesión con correo electrónico y contraseña').click()
    #driver.find_element('xpath', value='//android.view.View[@resource-id="guided-phone-form"]/android.widget.TextView/android.widget.Button and @text="Iniciar sesión con correo electrónico y contraseña').click()
    #driver.find_element("xpath", value='//android.view.View[@resource-id="guided-phone-form"]/android.widget.TextView/android.widget.Button and @text="Iniciar sesión con correo electrónico y contraseña').click()
    #driver.find_element('xpath', value='//android.widget.Button[@text="Continue"]').click()
    #driver.find_element('xpath', value='//android.view.View[@resource-id="guided-phone-form"]/android.view.View[3]').click()

    #except Exception as e:
        # Si ocurre algún error, captura la excepción e imprime un mensaje
        #print(f"Ocurrió un error: {e}")

# Función para la ejecucion del codigo
def log_in():
    open_app()

interface = LoginApp(log_in, lambda: None)
interface.start()