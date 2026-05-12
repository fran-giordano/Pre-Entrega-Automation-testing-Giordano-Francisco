"""
Suite de pruebas automatizadas para saucedemo.com
Cubre: Login, Catálogo e interacción con carrito
"""

import pytest
from selenium.webdriver.common.by import By
from utils.helpers import crear_driver, hacer_login, esperar_elemento, BASE_URL

class TestLogin:
    """ Caso de prueba: Automatización de Login."""
    
    def setup_method(self):
        """ Configuración previa a cada prueba: Crear WebDriver y realizar login. """
        self.driver = crear_driver()

    def teardown_method(self):
        """ Limpieza posterior a cada prueba: Cerrar el WebDriver. """
        self.driver.quit()

    def test_login_exitoso(self):
        """" Valida que el loigin con credenciales válidas redirija al inventario """
        hacer_login(self.driver)

        esperar_elemento(self.driver, By.CLASS_NAME, "inventory_list")

        assert "/inventory.html" in self.driver.current_url, \
        f"URL esperadod con /inventory.html, pero se obtuvo {self.driver.current_url}"

        assert "Swag Labs" in self.driver.title, \
        f"El título de la página no es 'Swag Labs', se obtuvo {self.driver.title}"


class TestCatalogo:
    """ Caso de prueba: Navegación y Verificacion del Catálogo """

    def setup_method(self):
        self.driver = crear_driver()
        hacer_login(self.driver)

    def teardown_method(self):
        self.driver.quit() 

    def test_catalogo_inventario(self):
        """ Valida titulo, presenciua del producto y datos del primero. """

        titulo = esperar_elemento(self.driver, By.CLASS_NAME, "title").text
        assert titulo == "Products", \
            f"El título esperado es 'Products', pero se obtuvo '{titulo}'"
        
        productos = self.driver.find_elements(By.CLASS_NAME, "inventory_item")
        assert len(productos) > 0, "No se encontraron productos en el catálogo."

        primer_nombre = productos[0].find_element(By.CLASS_NAME, "inventory_item_name").text
        primer_precio = productos[0].find_element(By.CLASS_NAME, "inventory_item_price").text

        assert primer_nombre, "El nombre del primer producto esta vacío"
        assert primer_precio.startswith("$"), \
            f"Precio ineseperado: '{primer_precio}'" 

        self.driver.find_element(By.ID, "react-burger-menu-btn")
        self.driver.find_element(By.CLASS_NAME, "product_sort_container")

class TestCarrito:
    """ Caso de prueba: Interacción con Productos y Carrito. """

    def setup_method(self):
        self.driver = crear_driver()
        hacer_login(self.driver)

    def teardown_method(self):
        self.driver.quit() 

    def test_agregar_al_carrito(self):
        """ Valida que se pueda agregar un producto al carrito y verificar su presencia. """

        primer_producto = esperar_elemento(self.driver, By.CLASS_NAME, "inventory_item")
        nombre_producto = primer_producto.find_element(By.CLASS_NAME, "inventory_item_name").text

        # Agregar el primer producto al carrito
        primer_producto.find_element(By.CLASS_NAME, "btn_inventory").click()

        # Verificar que el contador del carrito se actualice
        contador = self.driver.find_element(By.CLASS_NAME, "shopping_cart_badge")
        assert contador.text == "1", \
            f"Se esperaba un contador de '1', pero se obtuvo '{contador.text}'"
        
        # Navegar al carrito y verificar el producto agregado
        self.driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()

        # Verifica que el producto aparece en el carrito
        items_carrito = esperar_elemento(self.driver, By.CLASS_NAME, "cart_item")
        nombre_carrito = items_carrito.find_element(By.CLASS_NAME, "inventory_item_name").text

        assert nombre_carrito == nombre_producto, \
            f"El nombre del producto en el carrito no coincide. Se esperaba '{nombre_producto}', pero se obtuvo '{nombre_carrito}'"
        

        