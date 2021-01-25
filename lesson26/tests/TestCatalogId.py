# http://192.168.0.12/index.php?route=product/product&path=57&product_id=49
import allure


class TestCatalogId:

    @allure.title('Наличие превьюшек')
    def test_img(self, catalog_id):
        """На странице есть превьюшки"""
        assert catalog_id.get_len_elements() > 0

    @allure.title('Стоимость товара')
    def test_price(self, catalog_id):
        """Проверка, что цена товара > 0"""
        assert catalog_id.get_price() > 0

    @allure.title('Счетчик корзины')
    def test_count(self, catalog_id):
        """Проверка, что при добавлении товара в корзину, счетчик корзины изменился с 0 на 1"""
        assert catalog_id.get_number_product != -1

    @allure.title('Совпадение url картинок')
    def test_gallery(self, catalog_id):
        """Проверка, что url превью совпадает с url открытой картинкой в галерее"""
        dict = catalog_id.get_url_gallery()
        assert dict["1"] == dict["2"]

    @allure.title('Отправка отзыва')
    def test_reviews(self, catalog_id):
        """Проверка, что при отправке отзыва появляется сообщение"""
        assert catalog_id.get_review_result() > -1


