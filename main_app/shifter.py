from time import sleep
from app_interface.app_ui import LoginApp
from app_run.app_handler import start_app
from appium.webdriver.common.touch_action import TouchAction

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
    sleep(15)
    actions = TouchAction(driver)
    #actions.tap(x=471, y=897).wait(15000).tap(x=285, y=577).perform()
    actions.tap(x=471, y=897).perform()

    sleep(15)
    # Escribir el correo
    correo = driver.find_element("xpath", value='//android.widget.EditText[@resource-id="FieldWrapper-2"]')
    if correo:
        print('Se ingresa el correo')
        correo.send_keys("jeffreyospina17@gmail.com")
    else:
        print('El elemento no existe')

    sleep(7)
    # Escribir la clave
    clave = driver.find_element("xpath", value='//android.widget.EditText[@resource-id="FieldWrapper-3"]')
    if clave:
        print('Se ingresa la clave')
        clave.send_keys("holamundo123")
    else:
        print('El elemento no existe')
        
    sleep(7)
    # Iniciar sesion
    login = driver.find_element("xpath", value='//android.widget.Button[@resource-id="login-submit-button"]')
    if login:
        print('Se inicia sesion')
        login.click()
    else:
        print('El elemento no existe')

   

# Función para la ejecucion del codigo
def log_in():
    open_app()

interface = LoginApp(log_in, lambda: None)
interface.start()