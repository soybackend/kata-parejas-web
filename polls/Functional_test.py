from selenium.webdriver.common.by import By

__autor__ = 'Jose Alvarez - Fernando Arruza'

from unittest import TestCase
from selenium import webdriver


class FuncionalTest(TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_1title(self):
        self.browser.get('http://localhost:8000')
        self.assertIn('Busco Ayuda', self.browser.title)

    def test_2register(self):
        self.browser.get('http://localhost:8000')
        link = self.browser.find_element_by_id('id_register')
        link.click()

        self.browser.implicitly_wait(1)

        nombre = self.browser.find_element_by_id('id_nombre')
        nombre.send_keys('Juan Daniel')

        apellidos = self.browser.find_element_by_id('id_apellidos')
        apellidos.send_keys('Arevalo')

        experiencia = self.browser.find_element_by_id('id_aniosExperiencia')
        experiencia.send_keys('5')

        self.browser.find_element_by_xpath("//select[@id='id_tiposDeServicio']/option[text()='Desarrollador Web']").click()

        telefono = self.browser.find_element_by_id('id_telefono')
        telefono.send_keys('3113344555')

        correo = self.browser.find_element_by_id('id_correo')
        correo.send_keys('jdpatino1@uniandes.edu.co')

        imagen = self.browser.find_element_by_id('id_imagen')
        imagen.send_keys('/Users/jose/Downloads/123.jpg')

        nombre_usuario = self.browser.find_element_by_id('id_username')
        nombre_usuario.send_keys('juan645')

        clave = self.browser.find_element_by_id('id_password')
        clave.send_keys('clave123')

        botonGrabar = self.browser.find_element_by_id('id_grabar')
        botonGrabar.click()
        self.browser.implicitly_wait(3)

        span = self.browser.find_element(By.XPATH, '//span[text()="Juan Daniel Arevalo"]')

        self.assertIn('Juan Daniel Arevalo', span.text)


    def test_3verDetalle(self):
        self.browser.get('http://localhost:8000')
        span = self.browser.find_element(By.XPATH, '//span[text()="Juan Daniel Arevalo"]')
        span.click()

        h2 = self.browser.find_element(By.XPATH, '//h2[text()="Juan Daniel Arevalo"]')

        self.assertIn('Juan Daniel Arevalo', h2.text)


    def test_4login(self):
        self.browser.get('http://localhost:8000/login/')

        nombre_usuario = self.browser.find_element_by_id('id_username')
        nombre_usuario.send_keys('juan645')

        clave = self.browser.find_element_by_id('id_password')
        clave.send_keys('clave123')

        botonLogin = self.browser.find_element_by_id('id_botonLogin')
        botonLogin.click()

        self.browser.implicitly_wait(3)

        botonLogout = self.browser.find_element_by_id('id_botonLogout')
        botonLogout.click()


    # def test_editar(self):
    #
    #     self.browser.get('http://localhost:8000/login/')
    #
    #     nombre_usuario = self.browser.find_element_by_id('id_username')
    #     nombre_usuario.send_keys('juan645')
    #
    #     clave = self.browser.find_element_by_id('id_password')
    #     clave.send_keys('clave123')
    #
    #     botonLogin = self.browser.find_element_by_id('id_botonLogin')
    #     botonLogin.click()
    #
    #     botonEditar = self.browser.find_element_by_id('id_editar')
    #     botonEditar.click()
    #
    #     nombre = self.browser.find_element_by_id('id_nombre')
    #     nombre.send_keys('Juan Carlos')
    #
    #     botonEditarGuardar = self.browser.find_element_by_id('id_botonEditar')
    #     botonEditarGuardar.click()
    #
    #     self.browser.implicitly_wait(3)
    #
    #     botonLogout = self.browser.find_element_by_id('id_botonLogout')
    #     botonLogout.click()
    #
    #     self.browser.implicitly_wait(3)
    #
    #     span = self.browser.find_element(By.XPATH, '//span[text()="Juan Carlos"]')
    #     self.assertIn('Juan Carlos', span.text)




