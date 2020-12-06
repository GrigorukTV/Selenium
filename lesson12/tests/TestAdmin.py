# http://localhost/admin/
class TestAdmin:

    '''
    Проверка, что заголовок = 'Orders'
    '''
    def test_total_orders(self,admin):
        assert admin.get_heading() != -1

    '''
    Проверка, перехода Systems -> Settings
    '''
    def test_settings(self, admin):
        assert admin.settings() > -1

    '''
    Проверка перехода к разделу с товарами, что появляется таблица с товарами
    '''
    def test_table(self, admin):
        assert admin.product_table() > -1

    '''
    Проверка логина
    '''
    def test_login(self, admin):
        assert admin.admin_authorization() != -1

    '''
    Проверка разлогина
    '''
    def test_logout(self, admin):
        assert admin.admin_logout() > -1

