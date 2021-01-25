# http://192.168.0.12/admin/
import allure


class TestAdmin:

    @allure.title('Заголовок = Orders')
    def test_total_orders(self,admin):
        """Проверка, что заголовок = 'Orders'"""
        assert admin.get_heading() != -1

    @allure.title('Переход Systems -> Settings')
    def test_settings(self, admin):
        """Проверка, перехода Systems -> Settings"""
        assert admin.settings() > -1

    @allure.title('Таблица с товарами')
    def test_table(self, admin):
        """Проверка перехода к разделу с товарами, что появляется таблица с товарами """
        assert admin.product_table() > -1

    @allure.title('Авторизация')
    def test_login(self, admin):
        """Проверка логина"""
        assert admin.admin_authorization() != -1

    @allure.title('Выход из учетки')
    def test_logout(self, admin):
        """Проверка разлогина"""
        assert admin.admin_logout() > -1

