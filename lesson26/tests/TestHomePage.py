# http://192.168.0.12/
import logging
import allure



class TestHomePage:

    @allure.title('Заголовок на главной странице')
    @allure.link('https://demo.opencart.com/', name='Ссылка на главную страницу')
    def test_title(self, home_page):
        """Проверка того, что мы на главной по title страницы"""
        assert home_page.get_title() == 'Your Store'

    @allure.title('Номер телефона')
    def test_phone(self, home_page):
        """Проверка номера телефона"""
        assert home_page.search_phone() == '123456789'

    @allure.title('Количество карточек в Рекомендуемых товарах')
    def test_cards(self, home_page):
        """Проверка на то, что в Рекомендуемых товарах 4 карточки"""
        assert home_page.get_length_product_layouts() == 4

    @allure.title('Переход на домашнюю страницу')
    def test_href(self, home_page):
        """Проверка, что ссылка Yor Store переходит на домашнюю страницу"""
        assert home_page.get_clicked_url().find('?route=common/home') > -1

    @allure.title('Переход на страницу поиска')
    def test_search(self, home_page):
        """Проверка, что ссылка Поиска переходит на страницу поиска"""
        assert home_page.get_url_search() is True

    @allure.title('Переход на страницу товара iphone')
    def test_iphone(self, home_page):
        """Проверка, что вторая карточка iphone переходит на страницу товара"""
        assert home_page.get_url_search_iphone() is True

    # Новые тесты
    @allure.title('Переход на страницу Product Comparison')
    def test_product_comparison(self, home_page):
        """Проверка, что осуществляется переход на другую страницу с заголовком Product Comparison"""
        assert home_page.get_url_product_comparison() == 'Product Comparison'

    @allure.title('Переход на другую страницу при клике на номер телефона')
    def test_contact_us(self, home_page):
        """Проверка, что при клике на номер телефона, открывается другая страница"""
        assert home_page.get_contact_us() is True

    @allure.title('Поисковая строка')
    def test_search(self, home_page):
        """Проверка поисковой строки"""
        assert home_page.get_search() is True

    @allure.title('Переход на страницу Shopping Cart')
    def test_checkout(self, home_page):
        """Проверка перехода на страницу Shopping Cart"""
        assert home_page.get_shopping_cart() == 'Shopping Cart'

    @allure.title('Переход по ссылке из футера')
    def test_footer_link(self, home_page):
        """Проверка перехода по ссылке из футера"""
        # assert home_page.get_footer_link() is True
        assert home_page.get_footer_link() is True
