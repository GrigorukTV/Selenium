# http://localhost/index.php?route=product/category&path=20
class TestCatalog:


    '''
    Проверка, что при отображении карточек на странице списком или в гриде, колличество элементов на странице равно
    '''
    def test_count_elements(self, catalog):
        dict = catalog.get_count_elements()
        assert dict["1"] == dict["2"]

    '''
    Проверка, что при отображении карточек на странице списком или в гриде, колличество элементов на странице равно
    '''

    def test_sorted(self, catalog):
        catalog = catalog.get_attribute_first_letter()
        assert catalog[0] == 'S'

    '''
    Проверка, что при нажатии на баннер открывается другая страница
    '''

    def test_banner(self, catalog):
        assert catalog.get_clicked_url() != 'http://localhost/index.php?route=product/category&path=20'

    '''
    Проверка, что при нажатии в боковом меню Tablets открывается страница Tablets и на ней есть товар
    '''

    def test_menu(self, catalog):
        assert catalog.get_name_product() == 'Samsung Galaxy Tab 10.1'

    '''
    Проверка, что при выборе товара в избранное, в сплывающем сообщении присутствует название товара
    '''

    def test_message(self, catalog):
        assert catalog.get_text_message() == 'Apple Cinema 30"'

