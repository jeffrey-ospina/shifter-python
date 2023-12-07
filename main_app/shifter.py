from time import sleep
from app_interface.app_ui import LoginApp
from app_run.app_handler import start_app

# Ejecucion principal del codigo
def open_app():
    # Iniciar la aplicación
    driver = start_app()  

    #try:
    sleep(8)
    inciar = driver.find_element("id", value="com.doordash.driverapp:id/sign_in")
    if inciar:
        print('Se ha iniciado correctamente')
        inciar.click()
    else:
        print('No se pudo iniciar la sesión')
    
    sleep(14)
    login = driver.find_element("xpath", value='//android.view.View[contains(@text, "Iniciar sesión con correo electrónico y contraseña")]')
    if login:
        print('Se ha encontrado el elemento de logueo')
        login.click()
    else:
        print('El elemento no existe')

    #login = driver.find_element("xpath", "//*[@resource-id='login']")

    #driver.find_element('xpath', value='//android.widget.TextView[@resource-id=\"com.doordash.driverapp:id/textView_prism_button_title\" and @text=\"Iniciar sesión\"]').click()
    #driver.find_element('xpath', value='//android.view.View[@resource-id=\"com.doordash.driverapp:id/guided-phone-form\"]/android.view.View[2]').click()
    #driver.find_element('xpath', value='//android.view.View[@resource-id=\"guided-phone-form\"]/android.view.View[2]').click()
    #driver.find_element('xpath', value='//android.widget.EditText[@resource-id="FieldWrapper-1"]').click()
    #driver.find_element("xpath", value='//android.widget.ImageButton[@content-desc="Navegar hacia arriba"]').click()
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