from app_interface.app_ui import LoginApp
from app_run.app_handler import start_app
from appium.webdriver.common.touch_action import TouchAction
from time import sleep


def open_app():

    # Abrir la aplicación
    driver = start_app()

    # Ejecucion para el inicio de sesion del usuario
    sleep(15)
    try:
        driver.find_element(
            "xpath",
            value='//android.widget.TextView[@resource-id="com.doordash.driverapp:id/textView_prism_button_title" and @text="Log in"]',
        ).click()
    except Exception as e:
        print(f"Ocurrió un error: {e}")

    # Iniciar sesion con correo electronico
    actions = TouchAction(driver)
    sleep(21)
    try:
        actions.tap(x=471, y=897).perform()
        # driver.find_element("xpath", value='//android.widget.Button[@text="Log in with email and password"]',).click()
    except Exception as e:
        print(f"Ocurrió un error: {e}")

    # Ingreso de correo electronico
    sleep(15)
    try:
        correo = driver.find_element(
            "xpath", value='//android.widget.EditText[@resource-id="FieldWrapper-2"]'
        )
        correo.send_keys("email@example.com")
    except Exception as e:
        print(f"Ocurrió un error: {e}")

    # Ingreso de clave
    sleep(12)
    try:
        clave = driver.find_element(
            "xpath", value='//android.widget.EditText[@resource-id="FieldWrapper-3"]'
        )
        clave.send_keys("password123")
    except Exception as e:
        print(f"Ocurrió un error: {e}")

    # Iniciar sesion
    sleep(12)
    try:
        driver.find_element(
            "xpath", value='//android.widget.Button[@resource-id="login-submit-button"]'
        ).click()
    except Exception as e:
        print(f"Ocurrió un error: {e}")


# def log_in():
# Función para iniciar sesión, se llama al hacer clic en el botón
# open_app()

LoginApp(open_app)
