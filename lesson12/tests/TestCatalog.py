# http://192.168.0.12/index.php?route=product/category&path=20
import allure


class TestCatalog:

    @allure.title('Сортировка карточек')
    def test_count_elements(self, catalog):
        """
        Проверка, что при отображении карточек на странице списком или в гриде, колличество элементов на странице равно
        """
        dict = catalog.get_count_elements()
        assert dict["1"] == dict["2"]

    @allure.title('Сортировка от A-Z')
    def test_sorted(self, catalog):
        """Сортировка от A-Z"""
        catalog = catalog.get_attribute_first_letter()
        assert catalog[0] == 'S'

    @allure.title('Нажатие на баннер')
    def test_banner(self, catalog):
        """Проверка, что при нажатии на баннер открывается другая страница"""
        assert catalog.get_clicked_url() != 'http://192.168.0.12/index.php?route=product/category&path=20'

    @allure.title('Открытие страница Tablets')
    def test_menu(self, catalog):
        """Проверка, что при нажатии в боковом меню Tablets открывается страница Tablets и на ней есть товар"""
        assert catalog.get_name_product() == 'Samsung Galaxy Tab 10.1'

    @allure.title('Выбор товара в избранное')
    def test_message(self, catalog):
        """Проверка, что при выборе товара в избранное, в сплывающем сообщении присутствует название товара"""
        assert catalog.get_text_message() == 'Apple Cinema 30"'

