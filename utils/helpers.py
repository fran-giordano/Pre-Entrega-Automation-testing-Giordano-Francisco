"""
Funcionalidades auxiliares para el proyecto.
Centraliza la configuración del WebDriver y otras las especifica
"""

from selenium import webdriver
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from webdriver_manager.firefox import GeckoDriverManager 
from selenium.webdriver.firefox.service import Service 

BASE_URL = "https://www.saucedemo.com"
TIMEOUT = 10

def crear_driver() -> webdriver.Firefox:
    """
    Crea y configura un WebDriver para Firefox.
    Devuelve una instancia del WebDriver configurado.
    """
    options = FirefoxOptions()

    options.add_argument("--width=1920")
    options.add_argument("--height=1080")
    
    driver = webdriver.Firefox(
        service=Service(GeckoDriverManager().install()),
        options=options
    )
    driver.implicitly_wait(TIMEOUT)  # Configurar tiempo de espera implícito
    return driver

def esperar_elemento(driver: webdriver.Firefox, by: By, value: str) -> object:
    """ espera explícitamente a que un elemento sea visible -> Lo retorna"""

    return WebDriverWait(driver, TIMEOUT).until(
        EC.visibility_of_element_located((by, value))
    )

def hacer_login(driver: webdriver.Firefox, username: str = "standard_user", password: str = "secret_sauce") -> None:
    """ Realiza el proceso de login en la aplicación """

    driver.get(BASE_URL)
    esperar_elemento(driver, By.ID, "user-name").send_keys(username)
    driver.find_element(By.ID, "password").send_keys(password)
    driver.find_element(By.ID, "login-button").click()

