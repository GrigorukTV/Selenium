# http://localhost/
class TestHomePage:

    '''
    Проверка того, что мы на главной по title страницы
    '''
    def test_title(self, home_page):
        assert home_page.get_title() == 'Your Store'

    '''
    Проверка номера телефона
    '''
    def test_phone(self, home_page):
        assert home_page.search_phone() == '123456789'

    '''
    Проверка на то, что в Рекомендуемых товарах 4 карточки
    '''
    def test_cards(self, home_page):
        assert home_page.get_length_product_layouts() == 4

    '''
    Проверка, что ссылка Yor Store переходит на домашнюю страницу
    '''
    def test_href(self, home_page):
        assert home_page.get_clicked_url().find('?route=common/home') > -1

    '''
    Проверка, что ссылка Поиска переходит на страницу поиска
    '''
    def test_search(self, home_page):
        assert home_page.get_url_search() is True

    '''
    Проверка, что вторая карточка iphone переходит на страницу товара
    '''
    def test_iphone(self, home_page):
        assert home_page.get_url_search_iphone() is True


    # Новые тесты

    '''
    Проверка, что осуществляется переход на другую страницу с заголовком Product Comparison
    '''
    def test_product_comparison(self, home_page):
        assert home_page.get_url_product_comparison() == 'Product Comparison'

    '''
    Проверка, что при клике на номер телефона, открывается другая страница
    '''
    def test_contact_us(self, home_page):
        assert home_page.get_contact_us() is True

    '''
    Проверка поисковой строки
    '''
    def test_search(self, home_page):
        assert home_page.get_search() is True

    '''
    Проверка перехода на страницу Shopping Cart
    '''
    def test_checkout(self,home_page):
        assert home_page.get_shopping_cart() == 'Shopping Cart'

    '''
    Проверка перехода по ссылке из футера
    '''
    def test_footer_link(self, home_page):
        assert home_page.get_footer_link() is True









