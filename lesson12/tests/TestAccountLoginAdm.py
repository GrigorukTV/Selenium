# http://localhost/admin/
class TestAccountLoginAdm:

    """
    Проверка, что при отправке пустой формы, появляется предупреждающее собщение
    """
    def test_login_null(self, account_login_adm):
        assert account_login_adm.get_message_danger() > -1

    """
    Проверка, что при вводе в форме только логина, появляется предупреждающее собщение
    """
    def test_user_login(self, account_login_adm):
        assert account_login_adm.get_message_danger_not_pass() > -1

    """
    Проверка, что при вводе в форме только пароля, появляется предупреждающее собщение
    """
    def test_user_pass(self, account_login_adm):
        assert account_login_adm.get_message_danger_not_login() > -1

    """
    Проверка, что при ошибке в логине, нажав на крестик сообщения, оно закрывается
    """
    def test_message_close(self, account_login_adm):
        assert account_login_adm.check_login_error_close() == 0

    """
    Проверка, что пользователь авторизован
    """

    def test_authorization(self, account_login_adm):
        assert account_login_adm.check_authorization_user() is True
