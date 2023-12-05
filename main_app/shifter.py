import time
from app_interface.app_ui import LoginApp
from app_run.app_handler import start_app

# Función para realizar una operación en la calculadora una sola vez
def open_app():
    driver = start_app()  # Iniciar la aplicación

    #try:
    time.sleep(8)
    #driver.find_element("id", value="com.doordash.driverapp:id/sign_in").click()
    driver.find_element('xpath', value='//android.widget.TextView[@resource-id=\"com.doordash.driverapp:id/textView_prism_button_title\" and @text=\"Iniciar sesión\"]').click()
    #except Exception as e:
        # Si ocurre algún error, captura la excepción e imprime un mensaje
        #print(f"Ocurrió un error: {e}")

# Función que se ejecuta al hacer clic en el botón de iniciar
def log_in():
    open_app()

interface = LoginApp(log_in, lambda: None)
interface.start()