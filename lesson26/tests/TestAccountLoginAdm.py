# http://192.168.0.12/admin/
import allure


class TestAccountLoginAdm:

    @allure.title('Отправка пустой формы')
    def test_login_null(self, account_login_adm):
        """Проверка, что при отправке пустой формы, появляется предупреждающее собщение"""
        assert account_login_adm.get_message_danger() > -1

    @allure.title('Отправка в форме только логина')
    def test_user_login(self, account_login_adm):
        """Проверка, что при вводе в форме только логина, появляется предупреждающее собщение"""
        assert account_login_adm.get_message_danger_not_pass() > -1

    @allure.title('Отправка в форме только пароля')
    def test_user_pass(self, account_login_adm):
        """Проверка, что при вводе в форме только пароля, появляется предупреждающее собщение"""
        assert account_login_adm.get_message_danger_not_login() > -1

    @allure.title('Закрытие предупреждающего сообщения')
    def test_message_close(self, account_login_adm):
        """Проверка, что при ошибке в логине, нажав на крестик сообщения, оно закрывается"""
        assert account_login_adm.check_login_error_close() == 0

    @allure.title('Пользователь авторизован')
    def test_authorization(self, account_login_adm):
        """Проверка, что пользователь авторизован"""
        assert account_login_adm.check_authorization_user() is True
