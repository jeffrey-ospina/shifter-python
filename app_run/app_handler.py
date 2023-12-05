from appium import webdriver
from appium.options.android import UiAutomator2Options


def start_app():
    driver_config = {
        "platformName": "Android",
        "appium:platformVersion": "13.0",
        "appium:deviceName": "emu64x",
        "appium:automationName": "UiAutomator2",
        "appium:appPackage": "com.doordash.driverapp",
        "appium:appActivity": "com.doordash.driverapp.ui.login.LauncherActivity"
    }
        
    options = UiAutomator2Options().load_capabilities(driver_config)
    driver = webdriver.Remote('http://localhost:4723/wd/hub', options=options)
    return driver