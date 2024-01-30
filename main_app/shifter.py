from time import sleep
from app_interface.app_ui import LoginApp
from app_run.app_handler import start_app
from appium.webdriver.common.touch_action import TouchAction

def datos():
    interfaz_instancia = LoginApp(None)

    email, password = interfaz_instancia.get_credentials()

    return email, password

# Ejecucion principal del codigo
def open_app():
    # Abrir la aplicación
    driver = start_app()

    # Pulsar boton de iniciar sesion
    sleep(15)
    try: 
        driver.find_element("xpath", value='//android.widget.TextView[@resource-id="com.doordash.driverapp:id/textView_prism_button_title" and @text="Iniciar sesión"]').click()
    except Exception as e:
        print(f"Ocurrió un error: {e}")

    # Pulsar iniciar sesion con correo y contraseña
    actions = TouchAction(driver)
    sleep(15)
    #actions.tap(x=471, y=897).wait(15000).tap(x=285, y=577).perform()
    try:
        actions.tap(x=471, y=897).perform()
    except Exception as e:
        print(f"Ocurrió un error: {e}")    

    # Escribir el correo
    sleep(15)
    try:
        correo = driver.find_element("xpath", value='//android.widget.EditText[@resource-id="FieldWrapper-2"]')
        correo.send_keys("jeffreyospina17@gmail.com")
    except Exception as e:
        print(f"Ocurrió un error: {e}")         

    # Escribir la clave
    sleep(7)
    try:
        clave = driver.find_element("xpath", value='//android.widget.EditText[@resource-id="FieldWrapper-3"]')
        #sleep(5)
        clave.send_keys("holamundo123")
    except Exception as e:
        print(f"Ocurrió un error: {e}")

    # Iniciar sesion
    sleep(7)
    try:
        driver.find_element("xpath", value='//android.widget.Button[@resource-id="login-submit-button"]').click()
    except Exception as e:
        print(f"Ocurrió un error: {e}")        

# Función para la ejecucion del codigo
def log_in():
    open_app()

interface = LoginApp(log_in, lambda: None)
interface.start()