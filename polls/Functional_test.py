__autor__ = 'Jose Alvarez - Fernando Arruza'

from unittest import TestCase
from selenium import webdriver


class FuncionalTest(TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_title(self):
        self.browser.get('http://localhost:8000')
        self.assertIn('Busco Ayuda', self.browser.title)
