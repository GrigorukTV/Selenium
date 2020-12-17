# http://192.168.0.12/index.php?route=account/login

import allure

class TestAccountLogin:

    @allure.title('Заголовок на главной странице')
    def test_new_customer(self, account_login):
        """New Customer при клике на Continue меняется ссылка"""
        assert account_login.get_clicked_url() is True

    @allure.title('Заголовок на главной странице')
    def test_returning_customer(self, account_login):
        """При отправке пустой формы в Returning Customer, появляется сообщение об ошибке"""
        assert account_login.get_message_danger() > -1

    @allure.title('Заголовок на главной странице')
    def test_forgotten_password(self, account_login):
        """Проверка, что при нажатии Forgotten Password меняется url"""
        assert account_login.get_url_forgotten() is True

    @allure.title('Заголовок на главной странице')
    def test_user_not_found(self, account_login):
        """Проверка, что при вводе не существующего email и пароля, появляется сообщение, что пользователь не найден"""
        assert account_login.get_message_not_login != -1

    @allure.title('Заголовок на главной странице')
    def test_account(self, account_login):
        """Проверка, что при вводе существующего email и пароля, пользователь авторизован"""
        assert account_login.get_heading_account != -1
