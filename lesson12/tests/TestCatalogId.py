# http://localhost/index.php?route=product/product&path=57&product_id=49
class TestCatalogId:

    '''
    На странице есть превьюшки
    '''
    def test_img(self, catalog_id):
        assert catalog_id.get_len_elements() > 0

    '''
    Проверка, что цена товара > 0
    '''
    def test_price(self, catalog_id):
        assert catalog_id.get_price() > 0

    '''
    Проверка, что при добавлении товара в корзину, счетчик корзины изменился с 0 на 1
    '''
    def test_count(self, catalog_id):
        assert catalog_id.get_number_product != -1

    '''
    Проверка, что url превью совпадает с url открытой картинкой в галерее
    '''
    def test_gallery(self, catalog_id):
        dict = catalog_id.get_url_gallery()
        assert dict["1"] == dict["2"]
    '''
    Проверка, что при отправке отзыва появляется сообщение
    '''
    def test_reviews(self, catalog_id):
        assert catalog_id.get_review_result() > -1


