from app_interface.app_ui import LoginApp
from app_run.app_handler import start_app
from time import sleep


def open_app():
    # email = app.get_email()
    # password = app.get_password()

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
    sleep(21)
    try:
        driver.find_element(
            "xpath",
            value='//android.widget.Button[@text="Log in with email and password"]',
        ).click()
    except Exception as e:
        print(f"Ocurrió un error: {e}")

    # Ingreso de correo electronico
    sleep(15)
    try:
        correo = driver.find_element(
            "xpath", value='//android.widget.EditText[@resource-id="FieldWrapper-2"]'
        )
        correo.send_keys()  # Utilizamos el método para obtener el correo electrónico
    except Exception as e:
        print(f"Ocurrió un error: {e}")

    # Ingreso de clave
    sleep(12)
    try:
        clave = driver.find_element(
            "xpath", value='//android.widget.EditText[@resource-id="FieldWrapper-3"]'
        )
        clave.send_keys()  # Utilizamos el método para obtener la contraseña
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
